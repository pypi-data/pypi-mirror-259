# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from pyavd.vendor.strip_empties import strip_empties_from_dict
from pyavd.vendor.utils import get

from .utils import UtilsMixin


class RouterPathSelectionMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_path_selection(self) -> dict | None:
        """
        Return structured config for router path-selection (DPS)
        """

        if not self.shared_utils.is_wan_router:
            return None

        router_path_selection = {
            "load_balance_policies": self._wan_load_balance_policies,
        }

        # When running CV Pathfinder, only load balance policies are configured
        # for AutoVPN, need also vrfs and policies.
        if self.shared_utils.wan_mode == "autovpn":
            vrfs = [{"name": vrf["name"], "path_selection_policy": vrf["policy"]} for vrf in self._filtered_wan_vrfs]

            router_path_selection.update(
                {
                    "policies": self._autovpn_policies,
                    "vrfs": vrfs,
                }
            )

        return strip_empties_from_dict(router_path_selection)

    @cached_property
    def _autovpn_policies(self) -> list:
        """
        Return a list of AutoVPN Policies.
        """
        autovpn_policies = []

        for policy in self._filtered_wan_policies:
            rule_id_offset = 0
            autovpn_policy = {
                "name": policy["name"],
            }

            if get(policy, "is_default", default=False):
                autovpn_policy.setdefault("rules", []).append(
                    {
                        "id": 10,
                        "application_profile": self._wan_control_plane_application_profile,
                        "load_balance": self.shared_utils.generate_lb_policy_name(self._wan_control_plane_profile),
                    }
                )
                rule_id_offset = 1

            for rule_id, application_virtual_topology in enumerate(get(policy, "application_virtual_topologies", []), start=1):
                name = get(
                    application_virtual_topology,
                    "name",
                    default=self._default_profile_name(policy["profile_prefix"], application_virtual_topology["application_profile"]),
                )
                application_profile = get(application_virtual_topology, "application_profile", required=True)
                autovpn_policy.setdefault("rules", []).append(
                    {
                        "id": 10 * (rule_id + rule_id_offset),
                        "application_profile": application_profile,
                        "load_balance": self.shared_utils.generate_lb_policy_name(name),
                    }
                )
            default_virtual_topology = get(policy, "default_virtual_topology", required=True)
            if not get(default_virtual_topology, "drop_unmatched", default=False):
                name = get(
                    default_virtual_topology,
                    "name",
                    default=self._default_profile_name(policy["profile_prefix"], "DEFAULT"),
                )
                autovpn_policy["default_match"] = {"load_balance": self.shared_utils.generate_lb_policy_name(name)}

            autovpn_policies.append(autovpn_policy)

        return autovpn_policies
