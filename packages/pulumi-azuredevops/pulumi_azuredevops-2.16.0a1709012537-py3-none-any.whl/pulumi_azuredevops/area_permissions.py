# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AreaPermissionsArgs', 'AreaPermissions']

@pulumi.input_type
class AreaPermissionsArgs:
    def __init__(__self__, *,
                 permissions: pulumi.Input[Mapping[str, pulumi.Input[str]]],
                 principal: pulumi.Input[str],
                 project_id: pulumi.Input[str],
                 path: Optional[pulumi.Input[str]] = None,
                 replace: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a AreaPermissions resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] permissions: the permissions to assign. The following permissions are available.
        :param pulumi.Input[str] principal: The **group** principal to assign the permissions.
        :param pulumi.Input[str] project_id: The ID of the project to assign the permissions.
        :param pulumi.Input[str] path: The name of the branch to assign the permissions.
        :param pulumi.Input[bool] replace: Replace (`true`) or merge (`false`) the permissions. Default: `true`.
               
               | Permission             | Description                          |
               |------------------------|--------------------------------------|
               | GENERIC_READ           | View permissions for this node       |
               | GENERIC_WRITE          | Edit this node                       |
               | CREATE_CHILDREN        | Create child nodes                   |
               | DELETE                 | Delete this node                     |
               | WORK_ITEM_READ         | View work items in this node         |
               | WORK_ITEM_WRITE        | Edit work items in this node         |
               | MANAGE_TEST_PLANS      | Manage test plans                    |
               | MANAGE_TEST_SUITES     | Manage test suites                   |
               | WORK_ITEM_SAVE_COMMENT | Edit work item comments in this node |
        """
        pulumi.set(__self__, "permissions", permissions)
        pulumi.set(__self__, "principal", principal)
        pulumi.set(__self__, "project_id", project_id)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if replace is not None:
            pulumi.set(__self__, "replace", replace)

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        the permissions to assign. The following permissions are available.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def principal(self) -> pulumi.Input[str]:
        """
        The **group** principal to assign the permissions.
        """
        return pulumi.get(self, "principal")

    @principal.setter
    def principal(self, value: pulumi.Input[str]):
        pulumi.set(self, "principal", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        The ID of the project to assign the permissions.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the branch to assign the permissions.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def replace(self) -> Optional[pulumi.Input[bool]]:
        """
        Replace (`true`) or merge (`false`) the permissions. Default: `true`.

        | Permission             | Description                          |
        |------------------------|--------------------------------------|
        | GENERIC_READ           | View permissions for this node       |
        | GENERIC_WRITE          | Edit this node                       |
        | CREATE_CHILDREN        | Create child nodes                   |
        | DELETE                 | Delete this node                     |
        | WORK_ITEM_READ         | View work items in this node         |
        | WORK_ITEM_WRITE        | Edit work items in this node         |
        | MANAGE_TEST_PLANS      | Manage test plans                    |
        | MANAGE_TEST_SUITES     | Manage test suites                   |
        | WORK_ITEM_SAVE_COMMENT | Edit work item comments in this node |
        """
        return pulumi.get(self, "replace")

    @replace.setter
    def replace(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "replace", value)


@pulumi.input_type
class _AreaPermissionsState:
    def __init__(__self__, *,
                 path: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 principal: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 replace: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering AreaPermissions resources.
        :param pulumi.Input[str] path: The name of the branch to assign the permissions.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] permissions: the permissions to assign. The following permissions are available.
        :param pulumi.Input[str] principal: The **group** principal to assign the permissions.
        :param pulumi.Input[str] project_id: The ID of the project to assign the permissions.
        :param pulumi.Input[bool] replace: Replace (`true`) or merge (`false`) the permissions. Default: `true`.
               
               | Permission             | Description                          |
               |------------------------|--------------------------------------|
               | GENERIC_READ           | View permissions for this node       |
               | GENERIC_WRITE          | Edit this node                       |
               | CREATE_CHILDREN        | Create child nodes                   |
               | DELETE                 | Delete this node                     |
               | WORK_ITEM_READ         | View work items in this node         |
               | WORK_ITEM_WRITE        | Edit work items in this node         |
               | MANAGE_TEST_PLANS      | Manage test plans                    |
               | MANAGE_TEST_SUITES     | Manage test suites                   |
               | WORK_ITEM_SAVE_COMMENT | Edit work item comments in this node |
        """
        if path is not None:
            pulumi.set(__self__, "path", path)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if principal is not None:
            pulumi.set(__self__, "principal", principal)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if replace is not None:
            pulumi.set(__self__, "replace", replace)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the branch to assign the permissions.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        the permissions to assign. The following permissions are available.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[str]]:
        """
        The **group** principal to assign the permissions.
        """
        return pulumi.get(self, "principal")

    @principal.setter
    def principal(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project to assign the permissions.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def replace(self) -> Optional[pulumi.Input[bool]]:
        """
        Replace (`true`) or merge (`false`) the permissions. Default: `true`.

        | Permission             | Description                          |
        |------------------------|--------------------------------------|
        | GENERIC_READ           | View permissions for this node       |
        | GENERIC_WRITE          | Edit this node                       |
        | CREATE_CHILDREN        | Create child nodes                   |
        | DELETE                 | Delete this node                     |
        | WORK_ITEM_READ         | View work items in this node         |
        | WORK_ITEM_WRITE        | Edit work items in this node         |
        | MANAGE_TEST_PLANS      | Manage test plans                    |
        | MANAGE_TEST_SUITES     | Manage test suites                   |
        | WORK_ITEM_SAVE_COMMENT | Edit work item comments in this node |
        """
        return pulumi.get(self, "replace")

    @replace.setter
    def replace(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "replace", value)


class AreaPermissions(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 principal: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 replace: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Manages permissions for an Area (Component)

        > **Note** Permissions can be assigned to group principals and not to single user principals.

        ## Permission levels

        Permission for Areas within Azure DevOps can be applied on two different levels.
        Those levels are reflected by specifying (or omitting) values for the arguments `project_id` and `path`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example = azuredevops.Project("example",
            work_item_template="Agile",
            version_control="Git",
            visibility="private",
            description="Managed by Terraform")
        example_project_readers = azuredevops.get_group_output(project_id=example.id,
            name="Readers")
        example_root_permissions = azuredevops.AreaPermissions("example-root-permissions",
            project_id=example.id,
            principal=example_project_readers.id,
            path="/",
            permissions={
                "CREATE_CHILDREN": "Deny",
                "GENERIC_READ": "Allow",
                "DELETE": "Deny",
                "WORK_ITEM_READ": "Allow",
            })
        ```
        ## Relevant Links

        * [Azure DevOps Service REST API 7.0 - Security](https://docs.microsoft.com/en-us/rest/api/azure/devops/security/?view=azure-devops-rest-7.0)

        ## PAT Permissions Required

        - **Project & Team**: vso.security_manage - Grants the ability to read, write, and manage security permissions.

        ## Import

        The resource does not support import.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] path: The name of the branch to assign the permissions.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] permissions: the permissions to assign. The following permissions are available.
        :param pulumi.Input[str] principal: The **group** principal to assign the permissions.
        :param pulumi.Input[str] project_id: The ID of the project to assign the permissions.
        :param pulumi.Input[bool] replace: Replace (`true`) or merge (`false`) the permissions. Default: `true`.
               
               | Permission             | Description                          |
               |------------------------|--------------------------------------|
               | GENERIC_READ           | View permissions for this node       |
               | GENERIC_WRITE          | Edit this node                       |
               | CREATE_CHILDREN        | Create child nodes                   |
               | DELETE                 | Delete this node                     |
               | WORK_ITEM_READ         | View work items in this node         |
               | WORK_ITEM_WRITE        | Edit work items in this node         |
               | MANAGE_TEST_PLANS      | Manage test plans                    |
               | MANAGE_TEST_SUITES     | Manage test suites                   |
               | WORK_ITEM_SAVE_COMMENT | Edit work item comments in this node |
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AreaPermissionsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages permissions for an Area (Component)

        > **Note** Permissions can be assigned to group principals and not to single user principals.

        ## Permission levels

        Permission for Areas within Azure DevOps can be applied on two different levels.
        Those levels are reflected by specifying (or omitting) values for the arguments `project_id` and `path`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example = azuredevops.Project("example",
            work_item_template="Agile",
            version_control="Git",
            visibility="private",
            description="Managed by Terraform")
        example_project_readers = azuredevops.get_group_output(project_id=example.id,
            name="Readers")
        example_root_permissions = azuredevops.AreaPermissions("example-root-permissions",
            project_id=example.id,
            principal=example_project_readers.id,
            path="/",
            permissions={
                "CREATE_CHILDREN": "Deny",
                "GENERIC_READ": "Allow",
                "DELETE": "Deny",
                "WORK_ITEM_READ": "Allow",
            })
        ```
        ## Relevant Links

        * [Azure DevOps Service REST API 7.0 - Security](https://docs.microsoft.com/en-us/rest/api/azure/devops/security/?view=azure-devops-rest-7.0)

        ## PAT Permissions Required

        - **Project & Team**: vso.security_manage - Grants the ability to read, write, and manage security permissions.

        ## Import

        The resource does not support import.

        :param str resource_name: The name of the resource.
        :param AreaPermissionsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AreaPermissionsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 principal: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 replace: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AreaPermissionsArgs.__new__(AreaPermissionsArgs)

            __props__.__dict__["path"] = path
            if permissions is None and not opts.urn:
                raise TypeError("Missing required property 'permissions'")
            __props__.__dict__["permissions"] = permissions
            if principal is None and not opts.urn:
                raise TypeError("Missing required property 'principal'")
            __props__.__dict__["principal"] = principal
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["replace"] = replace
        super(AreaPermissions, __self__).__init__(
            'azuredevops:index/areaPermissions:AreaPermissions',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            path: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            principal: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            replace: Optional[pulumi.Input[bool]] = None) -> 'AreaPermissions':
        """
        Get an existing AreaPermissions resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] path: The name of the branch to assign the permissions.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] permissions: the permissions to assign. The following permissions are available.
        :param pulumi.Input[str] principal: The **group** principal to assign the permissions.
        :param pulumi.Input[str] project_id: The ID of the project to assign the permissions.
        :param pulumi.Input[bool] replace: Replace (`true`) or merge (`false`) the permissions. Default: `true`.
               
               | Permission             | Description                          |
               |------------------------|--------------------------------------|
               | GENERIC_READ           | View permissions for this node       |
               | GENERIC_WRITE          | Edit this node                       |
               | CREATE_CHILDREN        | Create child nodes                   |
               | DELETE                 | Delete this node                     |
               | WORK_ITEM_READ         | View work items in this node         |
               | WORK_ITEM_WRITE        | Edit work items in this node         |
               | MANAGE_TEST_PLANS      | Manage test plans                    |
               | MANAGE_TEST_SUITES     | Manage test suites                   |
               | WORK_ITEM_SAVE_COMMENT | Edit work item comments in this node |
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AreaPermissionsState.__new__(_AreaPermissionsState)

        __props__.__dict__["path"] = path
        __props__.__dict__["permissions"] = permissions
        __props__.__dict__["principal"] = principal
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["replace"] = replace
        return AreaPermissions(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the branch to assign the permissions.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Mapping[str, str]]:
        """
        the permissions to assign. The following permissions are available.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def principal(self) -> pulumi.Output[str]:
        """
        The **group** principal to assign the permissions.
        """
        return pulumi.get(self, "principal")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The ID of the project to assign the permissions.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def replace(self) -> pulumi.Output[Optional[bool]]:
        """
        Replace (`true`) or merge (`false`) the permissions. Default: `true`.

        | Permission             | Description                          |
        |------------------------|--------------------------------------|
        | GENERIC_READ           | View permissions for this node       |
        | GENERIC_WRITE          | Edit this node                       |
        | CREATE_CHILDREN        | Create child nodes                   |
        | DELETE                 | Delete this node                     |
        | WORK_ITEM_READ         | View work items in this node         |
        | WORK_ITEM_WRITE        | Edit work items in this node         |
        | MANAGE_TEST_PLANS      | Manage test plans                    |
        | MANAGE_TEST_SUITES     | Manage test suites                   |
        | WORK_ITEM_SAVE_COMMENT | Edit work item comments in this node |
        """
        return pulumi.get(self, "replace")

