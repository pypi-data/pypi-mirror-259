# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetProjectResult',
    'AwaitableGetProjectResult',
    'get_project',
    'get_project_output',
]

@pulumi.output_type
class GetProjectResult:
    """
    A collection of values returned by getProject.
    """
    def __init__(__self__, description=None, features=None, id=None, name=None, process_template_id=None, project_id=None, version_control=None, visibility=None, work_item_template=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if features and not isinstance(features, dict):
            raise TypeError("Expected argument 'features' to be a dict")
        pulumi.set(__self__, "features", features)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if process_template_id and not isinstance(process_template_id, str):
            raise TypeError("Expected argument 'process_template_id' to be a str")
        pulumi.set(__self__, "process_template_id", process_template_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if version_control and not isinstance(version_control, str):
            raise TypeError("Expected argument 'version_control' to be a str")
        pulumi.set(__self__, "version_control", version_control)
        if visibility and not isinstance(visibility, str):
            raise TypeError("Expected argument 'visibility' to be a str")
        pulumi.set(__self__, "visibility", visibility)
        if work_item_template and not isinstance(work_item_template, str):
            raise TypeError("Expected argument 'work_item_template' to be a str")
        pulumi.set(__self__, "work_item_template", work_item_template)

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def features(self) -> Mapping[str, Any]:
        return pulumi.get(self, "features")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="processTemplateId")
    def process_template_id(self) -> str:
        return pulumi.get(self, "process_template_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[str]:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="versionControl")
    def version_control(self) -> str:
        return pulumi.get(self, "version_control")

    @property
    @pulumi.getter
    def visibility(self) -> str:
        return pulumi.get(self, "visibility")

    @property
    @pulumi.getter(name="workItemTemplate")
    def work_item_template(self) -> str:
        return pulumi.get(self, "work_item_template")


class AwaitableGetProjectResult(GetProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectResult(
            description=self.description,
            features=self.features,
            id=self.id,
            name=self.name,
            process_template_id=self.process_template_id,
            project_id=self.project_id,
            version_control=self.version_control,
            visibility=self.visibility,
            work_item_template=self.work_item_template)


def get_project(name: Optional[str] = None,
                project_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectResult:
    """
    Use this data source to access information about an existing Project within Azure DevOps.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azuredevops as azuredevops

    example = azuredevops.get_project(name="Example Project")
    pulumi.export("project", example)
    ```
    ## Relevant Links

    - [Azure DevOps Service REST API 7.0 - Projects - Get](https://docs.microsoft.com/en-us/rest/api/azure/devops/core/projects/get?view=azure-devops-rest-7.0)


    :param str name: Name of the Project.
    :param str project_id: ID of the Project.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['projectId'] = project_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azuredevops:index/getProject:getProject', __args__, opts=opts, typ=GetProjectResult).value

    return AwaitableGetProjectResult(
        description=pulumi.get(__ret__, 'description'),
        features=pulumi.get(__ret__, 'features'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        process_template_id=pulumi.get(__ret__, 'process_template_id'),
        project_id=pulumi.get(__ret__, 'project_id'),
        version_control=pulumi.get(__ret__, 'version_control'),
        visibility=pulumi.get(__ret__, 'visibility'),
        work_item_template=pulumi.get(__ret__, 'work_item_template'))


@_utilities.lift_output_func(get_project)
def get_project_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                       project_id: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectResult]:
    """
    Use this data source to access information about an existing Project within Azure DevOps.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azuredevops as azuredevops

    example = azuredevops.get_project(name="Example Project")
    pulumi.export("project", example)
    ```
    ## Relevant Links

    - [Azure DevOps Service REST API 7.0 - Projects - Get](https://docs.microsoft.com/en-us/rest/api/azure/devops/core/projects/get?view=azure-devops-rest-7.0)


    :param str name: Name of the Project.
    :param str project_id: ID of the Project.
    """
    ...
