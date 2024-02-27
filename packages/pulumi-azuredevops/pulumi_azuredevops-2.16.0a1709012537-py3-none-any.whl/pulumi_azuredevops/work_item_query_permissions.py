# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['WorkItemQueryPermissionsArgs', 'WorkItemQueryPermissions']

@pulumi.input_type
class WorkItemQueryPermissionsArgs:
    def __init__(__self__, *,
                 permissions: pulumi.Input[Mapping[str, pulumi.Input[str]]],
                 principal: pulumi.Input[str],
                 project_id: pulumi.Input[str],
                 path: Optional[pulumi.Input[str]] = None,
                 replace: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a WorkItemQueryPermissions resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] permissions: the permissions to assign. The following permissions are available
               
               | Permissions              | Description                        |
               |--------------------------|------------------------------------|
               | Read                     | Read                               |
               | Contribute               | Contribute                         |
               | Delete                   | Delete                             |
               | ManagePermissions        | Manage Permissions                 |
        :param pulumi.Input[str] principal: The **group** principal to assign the permissions.
        :param pulumi.Input[str] project_id: The ID of the project to assign the permissions.
        :param pulumi.Input[str] path: Path to a query or folder beneath `Shared Queries`
        :param pulumi.Input[bool] replace: Replace (`true`) or merge (`false`) the permissions. Default: `true`
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
        the permissions to assign. The following permissions are available

        | Permissions              | Description                        |
        |--------------------------|------------------------------------|
        | Read                     | Read                               |
        | Contribute               | Contribute                         |
        | Delete                   | Delete                             |
        | ManagePermissions        | Manage Permissions                 |
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
        Path to a query or folder beneath `Shared Queries`
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def replace(self) -> Optional[pulumi.Input[bool]]:
        """
        Replace (`true`) or merge (`false`) the permissions. Default: `true`
        """
        return pulumi.get(self, "replace")

    @replace.setter
    def replace(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "replace", value)


@pulumi.input_type
class _WorkItemQueryPermissionsState:
    def __init__(__self__, *,
                 path: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 principal: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 replace: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering WorkItemQueryPermissions resources.
        :param pulumi.Input[str] path: Path to a query or folder beneath `Shared Queries`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] permissions: the permissions to assign. The following permissions are available
               
               | Permissions              | Description                        |
               |--------------------------|------------------------------------|
               | Read                     | Read                               |
               | Contribute               | Contribute                         |
               | Delete                   | Delete                             |
               | ManagePermissions        | Manage Permissions                 |
        :param pulumi.Input[str] principal: The **group** principal to assign the permissions.
        :param pulumi.Input[str] project_id: The ID of the project to assign the permissions.
        :param pulumi.Input[bool] replace: Replace (`true`) or merge (`false`) the permissions. Default: `true`
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
        Path to a query or folder beneath `Shared Queries`
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        the permissions to assign. The following permissions are available

        | Permissions              | Description                        |
        |--------------------------|------------------------------------|
        | Read                     | Read                               |
        | Contribute               | Contribute                         |
        | Delete                   | Delete                             |
        | ManagePermissions        | Manage Permissions                 |
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
        Replace (`true`) or merge (`false`) the permissions. Default: `true`
        """
        return pulumi.get(self, "replace")

    @replace.setter
    def replace(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "replace", value)


class WorkItemQueryPermissions(pulumi.CustomResource):
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
        Manages permissions for Work Item Queries.

        > **Note** Permissions can be assigned to group principals and not to single user principals.

        ## Permission levels

        Permission for Work Item Queries within Azure DevOps can be applied on two different levels.
        Those levels are reflected by specifying (or omitting) values for the arguments `project_id` and `path`.

        ### Project level

        Permissions for all Work Item Queries inside a project (existing or newly created ones) are specified, if only the argument `project_id` has a value.

        #### Example usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example = azuredevops.Project("example",
            work_item_template="Agile",
            version_control="Git",
            visibility="private",
            description="Managed by Terraform")
        example_readers = azuredevops.get_group_output(project_id=example.id,
            name="Readers")
        project_wiq_root_permissions = azuredevops.WorkItemQueryPermissions("project-wiq-root-permissions",
            project_id=example.id,
            principal=example_readers.id,
            permissions={
                "CreateRepository": "Deny",
                "DeleteRepository": "Deny",
                "RenameRepository": "NotSet",
            })
        ```

        ### Shared Queries folder level

        Permissions for a specific folder inside Shared Queries are specified if the arguments `project_id` and `path` are set.

        > **Note** To set permissions for the Shared Queries folder itself use `/` as path value

        #### Example usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example = azuredevops.Project("example",
            work_item_template="Agile",
            version_control="Git",
            visibility="private",
            description="Managed by Terraform")
        example_readers = azuredevops.get_group_output(project_id=example.id,
            name="Readers")
        example_permissions = azuredevops.WorkItemQueryPermissions("example-permissions",
            project_id=example.id,
            path="/Team",
            principal=example_readers.id,
            permissions={
                "Contribute": "Allow",
                "Delete": "Deny",
                "Read": "NotSet",
            })
        ```

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example = azuredevops.Project("example",
            work_item_template="Agile",
            version_control="Git",
            visibility="private",
            description="Managed by Terraform")
        example_readers = azuredevops.get_group_output(project_id=example.id,
            name="Readers")
        example_contributors = azuredevops.get_group_output(project_id=example.id,
            name="Contributors")
        example_project_permissions = azuredevops.WorkItemQueryPermissions("example-project-permissions",
            project_id=example.id,
            principal=example_readers.id,
            permissions={
                "Read": "Allow",
                "Delete": "Deny",
                "Contribute": "Deny",
                "ManagePermissions": "Deny",
            })
        example_sharedqueries_permissions = azuredevops.WorkItemQueryPermissions("example-sharedqueries-permissions",
            project_id=example.id,
            path="/",
            principal=example_contributors.id,
            permissions={
                "Read": "Allow",
                "Delete": "Deny",
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
        :param pulumi.Input[str] path: Path to a query or folder beneath `Shared Queries`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] permissions: the permissions to assign. The following permissions are available
               
               | Permissions              | Description                        |
               |--------------------------|------------------------------------|
               | Read                     | Read                               |
               | Contribute               | Contribute                         |
               | Delete                   | Delete                             |
               | ManagePermissions        | Manage Permissions                 |
        :param pulumi.Input[str] principal: The **group** principal to assign the permissions.
        :param pulumi.Input[str] project_id: The ID of the project to assign the permissions.
        :param pulumi.Input[bool] replace: Replace (`true`) or merge (`false`) the permissions. Default: `true`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkItemQueryPermissionsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages permissions for Work Item Queries.

        > **Note** Permissions can be assigned to group principals and not to single user principals.

        ## Permission levels

        Permission for Work Item Queries within Azure DevOps can be applied on two different levels.
        Those levels are reflected by specifying (or omitting) values for the arguments `project_id` and `path`.

        ### Project level

        Permissions for all Work Item Queries inside a project (existing or newly created ones) are specified, if only the argument `project_id` has a value.

        #### Example usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example = azuredevops.Project("example",
            work_item_template="Agile",
            version_control="Git",
            visibility="private",
            description="Managed by Terraform")
        example_readers = azuredevops.get_group_output(project_id=example.id,
            name="Readers")
        project_wiq_root_permissions = azuredevops.WorkItemQueryPermissions("project-wiq-root-permissions",
            project_id=example.id,
            principal=example_readers.id,
            permissions={
                "CreateRepository": "Deny",
                "DeleteRepository": "Deny",
                "RenameRepository": "NotSet",
            })
        ```

        ### Shared Queries folder level

        Permissions for a specific folder inside Shared Queries are specified if the arguments `project_id` and `path` are set.

        > **Note** To set permissions for the Shared Queries folder itself use `/` as path value

        #### Example usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example = azuredevops.Project("example",
            work_item_template="Agile",
            version_control="Git",
            visibility="private",
            description="Managed by Terraform")
        example_readers = azuredevops.get_group_output(project_id=example.id,
            name="Readers")
        example_permissions = azuredevops.WorkItemQueryPermissions("example-permissions",
            project_id=example.id,
            path="/Team",
            principal=example_readers.id,
            permissions={
                "Contribute": "Allow",
                "Delete": "Deny",
                "Read": "NotSet",
            })
        ```

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example = azuredevops.Project("example",
            work_item_template="Agile",
            version_control="Git",
            visibility="private",
            description="Managed by Terraform")
        example_readers = azuredevops.get_group_output(project_id=example.id,
            name="Readers")
        example_contributors = azuredevops.get_group_output(project_id=example.id,
            name="Contributors")
        example_project_permissions = azuredevops.WorkItemQueryPermissions("example-project-permissions",
            project_id=example.id,
            principal=example_readers.id,
            permissions={
                "Read": "Allow",
                "Delete": "Deny",
                "Contribute": "Deny",
                "ManagePermissions": "Deny",
            })
        example_sharedqueries_permissions = azuredevops.WorkItemQueryPermissions("example-sharedqueries-permissions",
            project_id=example.id,
            path="/",
            principal=example_contributors.id,
            permissions={
                "Read": "Allow",
                "Delete": "Deny",
            })
        ```
        ## Relevant Links

        * [Azure DevOps Service REST API 7.0 - Security](https://docs.microsoft.com/en-us/rest/api/azure/devops/security/?view=azure-devops-rest-7.0)

        ## PAT Permissions Required

        - **Project & Team**: vso.security_manage - Grants the ability to read, write, and manage security permissions.

        ## Import

        The resource does not support import.

        :param str resource_name: The name of the resource.
        :param WorkItemQueryPermissionsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkItemQueryPermissionsArgs, pulumi.ResourceOptions, *args, **kwargs)
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
            __props__ = WorkItemQueryPermissionsArgs.__new__(WorkItemQueryPermissionsArgs)

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
        super(WorkItemQueryPermissions, __self__).__init__(
            'azuredevops:index/workItemQueryPermissions:WorkItemQueryPermissions',
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
            replace: Optional[pulumi.Input[bool]] = None) -> 'WorkItemQueryPermissions':
        """
        Get an existing WorkItemQueryPermissions resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] path: Path to a query or folder beneath `Shared Queries`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] permissions: the permissions to assign. The following permissions are available
               
               | Permissions              | Description                        |
               |--------------------------|------------------------------------|
               | Read                     | Read                               |
               | Contribute               | Contribute                         |
               | Delete                   | Delete                             |
               | ManagePermissions        | Manage Permissions                 |
        :param pulumi.Input[str] principal: The **group** principal to assign the permissions.
        :param pulumi.Input[str] project_id: The ID of the project to assign the permissions.
        :param pulumi.Input[bool] replace: Replace (`true`) or merge (`false`) the permissions. Default: `true`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkItemQueryPermissionsState.__new__(_WorkItemQueryPermissionsState)

        __props__.__dict__["path"] = path
        __props__.__dict__["permissions"] = permissions
        __props__.__dict__["principal"] = principal
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["replace"] = replace
        return WorkItemQueryPermissions(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[Optional[str]]:
        """
        Path to a query or folder beneath `Shared Queries`
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Mapping[str, str]]:
        """
        the permissions to assign. The following permissions are available

        | Permissions              | Description                        |
        |--------------------------|------------------------------------|
        | Read                     | Read                               |
        | Contribute               | Contribute                         |
        | Delete                   | Delete                             |
        | ManagePermissions        | Manage Permissions                 |
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
        Replace (`true`) or merge (`false`) the permissions. Default: `true`
        """
        return pulumi.get(self, "replace")

