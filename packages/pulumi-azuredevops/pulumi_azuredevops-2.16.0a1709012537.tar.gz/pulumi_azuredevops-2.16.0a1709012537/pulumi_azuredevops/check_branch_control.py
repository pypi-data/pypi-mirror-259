# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CheckBranchControlArgs', 'CheckBranchControl']

@pulumi.input_type
class CheckBranchControlArgs:
    def __init__(__self__, *,
                 project_id: pulumi.Input[str],
                 target_resource_id: pulumi.Input[str],
                 target_resource_type: pulumi.Input[str],
                 allowed_branches: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 ignore_unknown_protection_status: Optional[pulumi.Input[bool]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 verify_branch_protection: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a CheckBranchControl resource.
        :param pulumi.Input[str] project_id: The project ID.
        :param pulumi.Input[str] target_resource_id: The ID of the resource being protected by the check.
        :param pulumi.Input[str] target_resource_type: The type of resource being protected by the check. Valid values: `endpoint`, `environment`, `queue`, `repository`, `securefile`, `variablegroup`.
        :param pulumi.Input[str] allowed_branches: The branches allowed to use the resource. Specify a comma separated list of allowed branches in `refs/heads/branch_name` format. To allow deployments from all branches, specify ` * ` . `refs/heads/features/* , refs/heads/releases/*` restricts deployments to all branches under features/ or releases/ . Defaults to `*`.
        :param pulumi.Input[str] display_name: The name of the branch control check displayed in the web UI.
        :param pulumi.Input[bool] ignore_unknown_protection_status: Allow deployment from branches for which protection status could not be obtained. Only relevant when verify_branch_protection is `true`. Defaults to `false`.
        :param pulumi.Input[int] timeout: The timeout in minutes for the branch control check. Defaults to `1440`.
        :param pulumi.Input[bool] verify_branch_protection: Validate the branches being deployed are protected. Defaults to `false`.
        """
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "target_resource_id", target_resource_id)
        pulumi.set(__self__, "target_resource_type", target_resource_type)
        if allowed_branches is not None:
            pulumi.set(__self__, "allowed_branches", allowed_branches)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if ignore_unknown_protection_status is not None:
            pulumi.set(__self__, "ignore_unknown_protection_status", ignore_unknown_protection_status)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)
        if verify_branch_protection is not None:
            pulumi.set(__self__, "verify_branch_protection", verify_branch_protection)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        The project ID.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Input[str]:
        """
        The ID of the resource being protected by the check.
        """
        return pulumi.get(self, "target_resource_id")

    @target_resource_id.setter
    def target_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_resource_id", value)

    @property
    @pulumi.getter(name="targetResourceType")
    def target_resource_type(self) -> pulumi.Input[str]:
        """
        The type of resource being protected by the check. Valid values: `endpoint`, `environment`, `queue`, `repository`, `securefile`, `variablegroup`.
        """
        return pulumi.get(self, "target_resource_type")

    @target_resource_type.setter
    def target_resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_resource_type", value)

    @property
    @pulumi.getter(name="allowedBranches")
    def allowed_branches(self) -> Optional[pulumi.Input[str]]:
        """
        The branches allowed to use the resource. Specify a comma separated list of allowed branches in `refs/heads/branch_name` format. To allow deployments from all branches, specify ` * ` . `refs/heads/features/* , refs/heads/releases/*` restricts deployments to all branches under features/ or releases/ . Defaults to `*`.
        """
        return pulumi.get(self, "allowed_branches")

    @allowed_branches.setter
    def allowed_branches(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allowed_branches", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the branch control check displayed in the web UI.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="ignoreUnknownProtectionStatus")
    def ignore_unknown_protection_status(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow deployment from branches for which protection status could not be obtained. Only relevant when verify_branch_protection is `true`. Defaults to `false`.
        """
        return pulumi.get(self, "ignore_unknown_protection_status")

    @ignore_unknown_protection_status.setter
    def ignore_unknown_protection_status(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_unknown_protection_status", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        """
        The timeout in minutes for the branch control check. Defaults to `1440`.
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)

    @property
    @pulumi.getter(name="verifyBranchProtection")
    def verify_branch_protection(self) -> Optional[pulumi.Input[bool]]:
        """
        Validate the branches being deployed are protected. Defaults to `false`.
        """
        return pulumi.get(self, "verify_branch_protection")

    @verify_branch_protection.setter
    def verify_branch_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "verify_branch_protection", value)


@pulumi.input_type
class _CheckBranchControlState:
    def __init__(__self__, *,
                 allowed_branches: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 ignore_unknown_protection_status: Optional[pulumi.Input[bool]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 target_resource_type: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 verify_branch_protection: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering CheckBranchControl resources.
        :param pulumi.Input[str] allowed_branches: The branches allowed to use the resource. Specify a comma separated list of allowed branches in `refs/heads/branch_name` format. To allow deployments from all branches, specify ` * ` . `refs/heads/features/* , refs/heads/releases/*` restricts deployments to all branches under features/ or releases/ . Defaults to `*`.
        :param pulumi.Input[str] display_name: The name of the branch control check displayed in the web UI.
        :param pulumi.Input[bool] ignore_unknown_protection_status: Allow deployment from branches for which protection status could not be obtained. Only relevant when verify_branch_protection is `true`. Defaults to `false`.
        :param pulumi.Input[str] project_id: The project ID.
        :param pulumi.Input[str] target_resource_id: The ID of the resource being protected by the check.
        :param pulumi.Input[str] target_resource_type: The type of resource being protected by the check. Valid values: `endpoint`, `environment`, `queue`, `repository`, `securefile`, `variablegroup`.
        :param pulumi.Input[int] timeout: The timeout in minutes for the branch control check. Defaults to `1440`.
        :param pulumi.Input[bool] verify_branch_protection: Validate the branches being deployed are protected. Defaults to `false`.
        """
        if allowed_branches is not None:
            pulumi.set(__self__, "allowed_branches", allowed_branches)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if ignore_unknown_protection_status is not None:
            pulumi.set(__self__, "ignore_unknown_protection_status", ignore_unknown_protection_status)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if target_resource_id is not None:
            pulumi.set(__self__, "target_resource_id", target_resource_id)
        if target_resource_type is not None:
            pulumi.set(__self__, "target_resource_type", target_resource_type)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)
        if verify_branch_protection is not None:
            pulumi.set(__self__, "verify_branch_protection", verify_branch_protection)

    @property
    @pulumi.getter(name="allowedBranches")
    def allowed_branches(self) -> Optional[pulumi.Input[str]]:
        """
        The branches allowed to use the resource. Specify a comma separated list of allowed branches in `refs/heads/branch_name` format. To allow deployments from all branches, specify ` * ` . `refs/heads/features/* , refs/heads/releases/*` restricts deployments to all branches under features/ or releases/ . Defaults to `*`.
        """
        return pulumi.get(self, "allowed_branches")

    @allowed_branches.setter
    def allowed_branches(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allowed_branches", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the branch control check displayed in the web UI.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="ignoreUnknownProtectionStatus")
    def ignore_unknown_protection_status(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow deployment from branches for which protection status could not be obtained. Only relevant when verify_branch_protection is `true`. Defaults to `false`.
        """
        return pulumi.get(self, "ignore_unknown_protection_status")

    @ignore_unknown_protection_status.setter
    def ignore_unknown_protection_status(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_unknown_protection_status", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The project ID.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the resource being protected by the check.
        """
        return pulumi.get(self, "target_resource_id")

    @target_resource_id.setter
    def target_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_resource_id", value)

    @property
    @pulumi.getter(name="targetResourceType")
    def target_resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of resource being protected by the check. Valid values: `endpoint`, `environment`, `queue`, `repository`, `securefile`, `variablegroup`.
        """
        return pulumi.get(self, "target_resource_type")

    @target_resource_type.setter
    def target_resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_resource_type", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        """
        The timeout in minutes for the branch control check. Defaults to `1440`.
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)

    @property
    @pulumi.getter(name="verifyBranchProtection")
    def verify_branch_protection(self) -> Optional[pulumi.Input[bool]]:
        """
        Validate the branches being deployed are protected. Defaults to `false`.
        """
        return pulumi.get(self, "verify_branch_protection")

    @verify_branch_protection.setter
    def verify_branch_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "verify_branch_protection", value)


class CheckBranchControl(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_branches: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 ignore_unknown_protection_status: Optional[pulumi.Input[bool]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 target_resource_type: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 verify_branch_protection: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Manages a branch control check on a resource within Azure DevOps.

        ## Example Usage
        ### Protect a service connection

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example_project = azuredevops.Project("exampleProject")
        example_service_endpoint_generic = azuredevops.ServiceEndpointGeneric("exampleServiceEndpointGeneric",
            project_id=example_project.id,
            server_url="https://some-server.example.com",
            username="username",
            password="password",
            service_endpoint_name="Example Generic",
            description="Managed by Terraform")
        example_check_branch_control = azuredevops.CheckBranchControl("exampleCheckBranchControl",
            project_id=example_project.id,
            display_name="Managed by Terraform",
            target_resource_id=example_service_endpoint_generic.id,
            target_resource_type="endpoint",
            allowed_branches="refs/heads/main, refs/heads/features/*",
            timeout=1440)
        ```
        ### Protect an environment

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example_project = azuredevops.Project("exampleProject")
        example_environment = azuredevops.Environment("exampleEnvironment", project_id=example_project.id)
        example_check_branch_control = azuredevops.CheckBranchControl("exampleCheckBranchControl",
            project_id=example_project.id,
            display_name="Managed by Terraform",
            target_resource_id=example_environment.id,
            target_resource_type="environment",
            allowed_branches="refs/heads/main, refs/heads/features/*")
        ```
        ### Protect an agent queue

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example_project = azuredevops.Project("exampleProject")
        example_pool = azuredevops.Pool("examplePool")
        example_queue = azuredevops.Queue("exampleQueue",
            project_id=example_project.id,
            agent_pool_id=example_pool.id)
        example_check_branch_control = azuredevops.CheckBranchControl("exampleCheckBranchControl",
            project_id=example_project.id,
            display_name="Managed by Terraform",
            target_resource_id=example_queue.id,
            target_resource_type="queue",
            allowed_branches="refs/heads/main, refs/heads/features/*")
        ```
        ### Protect a repository

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example_project = azuredevops.Project("exampleProject")
        example_git = azuredevops.Git("exampleGit",
            project_id=example_project.id,
            initialization=azuredevops.GitInitializationArgs(
                init_type="Clean",
            ))
        example_check_branch_control = azuredevops.CheckBranchControl("exampleCheckBranchControl",
            project_id=example_project.id,
            display_name="Managed by Terraform",
            target_resource_id=pulumi.Output.all(example_project.id, example_git.id).apply(lambda exampleProjectId, exampleGitId: f"{example_project_id}.{example_git_id}"),
            target_resource_type="repository",
            allowed_branches="refs/heads/main, refs/heads/features/*")
        ```
        ### Protect a variable group

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example_project = azuredevops.Project("exampleProject")
        example_variable_group = azuredevops.VariableGroup("exampleVariableGroup",
            project_id=example_project.id,
            description="Example Variable Group Description",
            allow_access=True,
            variables=[
                azuredevops.VariableGroupVariableArgs(
                    name="key1",
                    value="val1",
                ),
                azuredevops.VariableGroupVariableArgs(
                    name="key2",
                    secret_value="val2",
                    is_secret=True,
                ),
            ])
        example_check_branch_control = azuredevops.CheckBranchControl("exampleCheckBranchControl",
            project_id=example_project.id,
            display_name="Managed by Terraform",
            target_resource_id=example_variable_group.id,
            target_resource_type="variablegroup",
            allowed_branches="refs/heads/main, refs/heads/features/*")
        ```
        ## Relevant Links

        - [Define approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops&tabs=check-pass)

        ## Import

        Importing this resource is not supported.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] allowed_branches: The branches allowed to use the resource. Specify a comma separated list of allowed branches in `refs/heads/branch_name` format. To allow deployments from all branches, specify ` * ` . `refs/heads/features/* , refs/heads/releases/*` restricts deployments to all branches under features/ or releases/ . Defaults to `*`.
        :param pulumi.Input[str] display_name: The name of the branch control check displayed in the web UI.
        :param pulumi.Input[bool] ignore_unknown_protection_status: Allow deployment from branches for which protection status could not be obtained. Only relevant when verify_branch_protection is `true`. Defaults to `false`.
        :param pulumi.Input[str] project_id: The project ID.
        :param pulumi.Input[str] target_resource_id: The ID of the resource being protected by the check.
        :param pulumi.Input[str] target_resource_type: The type of resource being protected by the check. Valid values: `endpoint`, `environment`, `queue`, `repository`, `securefile`, `variablegroup`.
        :param pulumi.Input[int] timeout: The timeout in minutes for the branch control check. Defaults to `1440`.
        :param pulumi.Input[bool] verify_branch_protection: Validate the branches being deployed are protected. Defaults to `false`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CheckBranchControlArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a branch control check on a resource within Azure DevOps.

        ## Example Usage
        ### Protect a service connection

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example_project = azuredevops.Project("exampleProject")
        example_service_endpoint_generic = azuredevops.ServiceEndpointGeneric("exampleServiceEndpointGeneric",
            project_id=example_project.id,
            server_url="https://some-server.example.com",
            username="username",
            password="password",
            service_endpoint_name="Example Generic",
            description="Managed by Terraform")
        example_check_branch_control = azuredevops.CheckBranchControl("exampleCheckBranchControl",
            project_id=example_project.id,
            display_name="Managed by Terraform",
            target_resource_id=example_service_endpoint_generic.id,
            target_resource_type="endpoint",
            allowed_branches="refs/heads/main, refs/heads/features/*",
            timeout=1440)
        ```
        ### Protect an environment

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example_project = azuredevops.Project("exampleProject")
        example_environment = azuredevops.Environment("exampleEnvironment", project_id=example_project.id)
        example_check_branch_control = azuredevops.CheckBranchControl("exampleCheckBranchControl",
            project_id=example_project.id,
            display_name="Managed by Terraform",
            target_resource_id=example_environment.id,
            target_resource_type="environment",
            allowed_branches="refs/heads/main, refs/heads/features/*")
        ```
        ### Protect an agent queue

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example_project = azuredevops.Project("exampleProject")
        example_pool = azuredevops.Pool("examplePool")
        example_queue = azuredevops.Queue("exampleQueue",
            project_id=example_project.id,
            agent_pool_id=example_pool.id)
        example_check_branch_control = azuredevops.CheckBranchControl("exampleCheckBranchControl",
            project_id=example_project.id,
            display_name="Managed by Terraform",
            target_resource_id=example_queue.id,
            target_resource_type="queue",
            allowed_branches="refs/heads/main, refs/heads/features/*")
        ```
        ### Protect a repository

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example_project = azuredevops.Project("exampleProject")
        example_git = azuredevops.Git("exampleGit",
            project_id=example_project.id,
            initialization=azuredevops.GitInitializationArgs(
                init_type="Clean",
            ))
        example_check_branch_control = azuredevops.CheckBranchControl("exampleCheckBranchControl",
            project_id=example_project.id,
            display_name="Managed by Terraform",
            target_resource_id=pulumi.Output.all(example_project.id, example_git.id).apply(lambda exampleProjectId, exampleGitId: f"{example_project_id}.{example_git_id}"),
            target_resource_type="repository",
            allowed_branches="refs/heads/main, refs/heads/features/*")
        ```
        ### Protect a variable group

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        example_project = azuredevops.Project("exampleProject")
        example_variable_group = azuredevops.VariableGroup("exampleVariableGroup",
            project_id=example_project.id,
            description="Example Variable Group Description",
            allow_access=True,
            variables=[
                azuredevops.VariableGroupVariableArgs(
                    name="key1",
                    value="val1",
                ),
                azuredevops.VariableGroupVariableArgs(
                    name="key2",
                    secret_value="val2",
                    is_secret=True,
                ),
            ])
        example_check_branch_control = azuredevops.CheckBranchControl("exampleCheckBranchControl",
            project_id=example_project.id,
            display_name="Managed by Terraform",
            target_resource_id=example_variable_group.id,
            target_resource_type="variablegroup",
            allowed_branches="refs/heads/main, refs/heads/features/*")
        ```
        ## Relevant Links

        - [Define approvals and checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops&tabs=check-pass)

        ## Import

        Importing this resource is not supported.

        :param str resource_name: The name of the resource.
        :param CheckBranchControlArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CheckBranchControlArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_branches: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 ignore_unknown_protection_status: Optional[pulumi.Input[bool]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 target_resource_type: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 verify_branch_protection: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CheckBranchControlArgs.__new__(CheckBranchControlArgs)

            __props__.__dict__["allowed_branches"] = allowed_branches
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["ignore_unknown_protection_status"] = ignore_unknown_protection_status
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            if target_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_resource_id'")
            __props__.__dict__["target_resource_id"] = target_resource_id
            if target_resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'target_resource_type'")
            __props__.__dict__["target_resource_type"] = target_resource_type
            __props__.__dict__["timeout"] = timeout
            __props__.__dict__["verify_branch_protection"] = verify_branch_protection
        super(CheckBranchControl, __self__).__init__(
            'azuredevops:index/checkBranchControl:CheckBranchControl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allowed_branches: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            ignore_unknown_protection_status: Optional[pulumi.Input[bool]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            target_resource_id: Optional[pulumi.Input[str]] = None,
            target_resource_type: Optional[pulumi.Input[str]] = None,
            timeout: Optional[pulumi.Input[int]] = None,
            verify_branch_protection: Optional[pulumi.Input[bool]] = None) -> 'CheckBranchControl':
        """
        Get an existing CheckBranchControl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] allowed_branches: The branches allowed to use the resource. Specify a comma separated list of allowed branches in `refs/heads/branch_name` format. To allow deployments from all branches, specify ` * ` . `refs/heads/features/* , refs/heads/releases/*` restricts deployments to all branches under features/ or releases/ . Defaults to `*`.
        :param pulumi.Input[str] display_name: The name of the branch control check displayed in the web UI.
        :param pulumi.Input[bool] ignore_unknown_protection_status: Allow deployment from branches for which protection status could not be obtained. Only relevant when verify_branch_protection is `true`. Defaults to `false`.
        :param pulumi.Input[str] project_id: The project ID.
        :param pulumi.Input[str] target_resource_id: The ID of the resource being protected by the check.
        :param pulumi.Input[str] target_resource_type: The type of resource being protected by the check. Valid values: `endpoint`, `environment`, `queue`, `repository`, `securefile`, `variablegroup`.
        :param pulumi.Input[int] timeout: The timeout in minutes for the branch control check. Defaults to `1440`.
        :param pulumi.Input[bool] verify_branch_protection: Validate the branches being deployed are protected. Defaults to `false`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CheckBranchControlState.__new__(_CheckBranchControlState)

        __props__.__dict__["allowed_branches"] = allowed_branches
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["ignore_unknown_protection_status"] = ignore_unknown_protection_status
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["target_resource_id"] = target_resource_id
        __props__.__dict__["target_resource_type"] = target_resource_type
        __props__.__dict__["timeout"] = timeout
        __props__.__dict__["verify_branch_protection"] = verify_branch_protection
        return CheckBranchControl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedBranches")
    def allowed_branches(self) -> pulumi.Output[Optional[str]]:
        """
        The branches allowed to use the resource. Specify a comma separated list of allowed branches in `refs/heads/branch_name` format. To allow deployments from all branches, specify ` * ` . `refs/heads/features/* , refs/heads/releases/*` restricts deployments to all branches under features/ or releases/ . Defaults to `*`.
        """
        return pulumi.get(self, "allowed_branches")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the branch control check displayed in the web UI.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="ignoreUnknownProtectionStatus")
    def ignore_unknown_protection_status(self) -> pulumi.Output[Optional[bool]]:
        """
        Allow deployment from branches for which protection status could not be obtained. Only relevant when verify_branch_protection is `true`. Defaults to `false`.
        """
        return pulumi.get(self, "ignore_unknown_protection_status")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The project ID.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Output[str]:
        """
        The ID of the resource being protected by the check.
        """
        return pulumi.get(self, "target_resource_id")

    @property
    @pulumi.getter(name="targetResourceType")
    def target_resource_type(self) -> pulumi.Output[str]:
        """
        The type of resource being protected by the check. Valid values: `endpoint`, `environment`, `queue`, `repository`, `securefile`, `variablegroup`.
        """
        return pulumi.get(self, "target_resource_type")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[int]]:
        """
        The timeout in minutes for the branch control check. Defaults to `1440`.
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter(name="verifyBranchProtection")
    def verify_branch_protection(self) -> pulumi.Output[Optional[bool]]:
        """
        Validate the branches being deployed are protected. Defaults to `false`.
        """
        return pulumi.get(self, "verify_branch_protection")

