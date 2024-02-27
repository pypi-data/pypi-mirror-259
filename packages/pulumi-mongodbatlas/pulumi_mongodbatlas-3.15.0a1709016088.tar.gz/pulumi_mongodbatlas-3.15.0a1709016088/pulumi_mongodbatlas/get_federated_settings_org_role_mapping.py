# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetFederatedSettingsOrgRoleMappingResult',
    'AwaitableGetFederatedSettingsOrgRoleMappingResult',
    'get_federated_settings_org_role_mapping',
    'get_federated_settings_org_role_mapping_output',
]

@pulumi.output_type
class GetFederatedSettingsOrgRoleMappingResult:
    """
    A collection of values returned by getFederatedSettingsOrgRoleMapping.
    """
    def __init__(__self__, external_group_name=None, federation_settings_id=None, id=None, org_id=None, role_assignments=None, role_mapping_id=None):
        if external_group_name and not isinstance(external_group_name, str):
            raise TypeError("Expected argument 'external_group_name' to be a str")
        pulumi.set(__self__, "external_group_name", external_group_name)
        if federation_settings_id and not isinstance(federation_settings_id, str):
            raise TypeError("Expected argument 'federation_settings_id' to be a str")
        pulumi.set(__self__, "federation_settings_id", federation_settings_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if org_id and not isinstance(org_id, str):
            raise TypeError("Expected argument 'org_id' to be a str")
        pulumi.set(__self__, "org_id", org_id)
        if role_assignments and not isinstance(role_assignments, list):
            raise TypeError("Expected argument 'role_assignments' to be a list")
        pulumi.set(__self__, "role_assignments", role_assignments)
        if role_mapping_id and not isinstance(role_mapping_id, str):
            raise TypeError("Expected argument 'role_mapping_id' to be a str")
        pulumi.set(__self__, "role_mapping_id", role_mapping_id)

    @property
    @pulumi.getter(name="externalGroupName")
    def external_group_name(self) -> str:
        """
        Unique human-readable label that identifies the identity provider group to which this role mapping applies.
        """
        return pulumi.get(self, "external_group_name")

    @property
    @pulumi.getter(name="federationSettingsId")
    def federation_settings_id(self) -> str:
        return pulumi.get(self, "federation_settings_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unique 24-hexadecimal digit string that identifies this role mapping.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> str:
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="roleAssignments")
    def role_assignments(self) -> Sequence['outputs.GetFederatedSettingsOrgRoleMappingRoleAssignmentResult']:
        """
        Atlas roles and the unique identifiers of the groups and organizations associated with each role.
        """
        return pulumi.get(self, "role_assignments")

    @property
    @pulumi.getter(name="roleMappingId")
    def role_mapping_id(self) -> str:
        return pulumi.get(self, "role_mapping_id")


class AwaitableGetFederatedSettingsOrgRoleMappingResult(GetFederatedSettingsOrgRoleMappingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFederatedSettingsOrgRoleMappingResult(
            external_group_name=self.external_group_name,
            federation_settings_id=self.federation_settings_id,
            id=self.id,
            org_id=self.org_id,
            role_assignments=self.role_assignments,
            role_mapping_id=self.role_mapping_id)


def get_federated_settings_org_role_mapping(federation_settings_id: Optional[str] = None,
                                            org_id: Optional[str] = None,
                                            role_mapping_id: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFederatedSettingsOrgRoleMappingResult:
    """
    `FederatedSettingsOrgRoleMapping` provides an Federated Settings Org Role Mapping datasource. Atlas Cloud Federated Settings Org Role Mapping provides federated settings outputs for the configured Org Role Mapping.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    org_group_role_mapping_import = mongodbatlas.FederatedSettingsOrgRoleMapping("orgGroupRoleMappingImport",
        federation_settings_id=data["mongodbatlas_federated_settings"]["federated_settings"]["id"],
        org_id="627a9683e7f7f7ff7fe306f14",
        external_group_name="myGrouptest",
        role_assignments=[
            mongodbatlas.FederatedSettingsOrgRoleMappingRoleAssignmentArgs(
                org_id="627a9683e7f7f7ff7fe306f14",
                roles=[
                    "ORG_MEMBER",
                    "ORG_GROUP_CREATOR",
                    "ORG_BILLING_ADMIN",
                ],
            ),
            mongodbatlas.FederatedSettingsOrgRoleMappingRoleAssignmentArgs(
                group_id="628aa20db7f7f7f98b81b8",
                roles=[
                    "GROUP_OWNER",
                    "GROUP_DATA_ACCESS_ADMIN",
                    "GROUP_SEARCH_INDEX_EDITOR",
                    "GROUP_DATA_ACCESS_READ_ONLY",
                ],
            ),
            mongodbatlas.FederatedSettingsOrgRoleMappingRoleAssignmentArgs(
                group_id="62b477f7f7f7f5e741489c",
                roles=[
                    "GROUP_OWNER",
                    "GROUP_DATA_ACCESS_ADMIN",
                    "GROUP_SEARCH_INDEX_EDITOR",
                    "GROUP_DATA_ACCESS_READ_ONLY",
                    "GROUP_DATA_ACCESS_READ_WRITE",
                ],
            ),
        ])
    role_mapping = mongodbatlas.get_federated_settings_org_role_mapping_output(federation_settings_id=org_group_role_mapping_import.id,
        org_id="627a9683e7f7f7ff7fe306f14",
        role_mapping_id="627a9673e7f7f7ff7fe306f14")
    ```


    :param str federation_settings_id: Unique 24-hexadecimal digit string that identifies the federated authentication configuration.
    :param str org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects.
    """
    __args__ = dict()
    __args__['federationSettingsId'] = federation_settings_id
    __args__['orgId'] = org_id
    __args__['roleMappingId'] = role_mapping_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getFederatedSettingsOrgRoleMapping:getFederatedSettingsOrgRoleMapping', __args__, opts=opts, typ=GetFederatedSettingsOrgRoleMappingResult).value

    return AwaitableGetFederatedSettingsOrgRoleMappingResult(
        external_group_name=pulumi.get(__ret__, 'external_group_name'),
        federation_settings_id=pulumi.get(__ret__, 'federation_settings_id'),
        id=pulumi.get(__ret__, 'id'),
        org_id=pulumi.get(__ret__, 'org_id'),
        role_assignments=pulumi.get(__ret__, 'role_assignments'),
        role_mapping_id=pulumi.get(__ret__, 'role_mapping_id'))


@_utilities.lift_output_func(get_federated_settings_org_role_mapping)
def get_federated_settings_org_role_mapping_output(federation_settings_id: Optional[pulumi.Input[str]] = None,
                                                   org_id: Optional[pulumi.Input[str]] = None,
                                                   role_mapping_id: Optional[pulumi.Input[str]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFederatedSettingsOrgRoleMappingResult]:
    """
    `FederatedSettingsOrgRoleMapping` provides an Federated Settings Org Role Mapping datasource. Atlas Cloud Federated Settings Org Role Mapping provides federated settings outputs for the configured Org Role Mapping.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    org_group_role_mapping_import = mongodbatlas.FederatedSettingsOrgRoleMapping("orgGroupRoleMappingImport",
        federation_settings_id=data["mongodbatlas_federated_settings"]["federated_settings"]["id"],
        org_id="627a9683e7f7f7ff7fe306f14",
        external_group_name="myGrouptest",
        role_assignments=[
            mongodbatlas.FederatedSettingsOrgRoleMappingRoleAssignmentArgs(
                org_id="627a9683e7f7f7ff7fe306f14",
                roles=[
                    "ORG_MEMBER",
                    "ORG_GROUP_CREATOR",
                    "ORG_BILLING_ADMIN",
                ],
            ),
            mongodbatlas.FederatedSettingsOrgRoleMappingRoleAssignmentArgs(
                group_id="628aa20db7f7f7f98b81b8",
                roles=[
                    "GROUP_OWNER",
                    "GROUP_DATA_ACCESS_ADMIN",
                    "GROUP_SEARCH_INDEX_EDITOR",
                    "GROUP_DATA_ACCESS_READ_ONLY",
                ],
            ),
            mongodbatlas.FederatedSettingsOrgRoleMappingRoleAssignmentArgs(
                group_id="62b477f7f7f7f5e741489c",
                roles=[
                    "GROUP_OWNER",
                    "GROUP_DATA_ACCESS_ADMIN",
                    "GROUP_SEARCH_INDEX_EDITOR",
                    "GROUP_DATA_ACCESS_READ_ONLY",
                    "GROUP_DATA_ACCESS_READ_WRITE",
                ],
            ),
        ])
    role_mapping = mongodbatlas.get_federated_settings_org_role_mapping_output(federation_settings_id=org_group_role_mapping_import.id,
        org_id="627a9683e7f7f7ff7fe306f14",
        role_mapping_id="627a9673e7f7f7ff7fe306f14")
    ```


    :param str federation_settings_id: Unique 24-hexadecimal digit string that identifies the federated authentication configuration.
    :param str org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects.
    """
    ...
