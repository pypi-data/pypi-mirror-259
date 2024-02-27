# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GitInitializationArgs',
]

@pulumi.input_type
class GitInitializationArgs:
    def __init__(__self__, *,
                 init_type: pulumi.Input[str],
                 service_connection_id: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 source_url: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] init_type: The type of repository to create. Valid values: `Uninitialized`, `Clean` or `Import`.
        :param pulumi.Input[str] service_connection_id: The id of service connection used to authenticate to a private repository for import initialization.
        :param pulumi.Input[str] source_type: Type of the source repository. Used if the `init_type` is `Import`. Valid values: `Git`.
        :param pulumi.Input[str] source_url: The URL of the source repository. Used if the `init_type` is `Import`.
        """
        pulumi.set(__self__, "init_type", init_type)
        if service_connection_id is not None:
            pulumi.set(__self__, "service_connection_id", service_connection_id)
        if source_type is not None:
            pulumi.set(__self__, "source_type", source_type)
        if source_url is not None:
            pulumi.set(__self__, "source_url", source_url)

    @property
    @pulumi.getter(name="initType")
    def init_type(self) -> pulumi.Input[str]:
        """
        The type of repository to create. Valid values: `Uninitialized`, `Clean` or `Import`.
        """
        return pulumi.get(self, "init_type")

    @init_type.setter
    def init_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "init_type", value)

    @property
    @pulumi.getter(name="serviceConnectionId")
    def service_connection_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of service connection used to authenticate to a private repository for import initialization.
        """
        return pulumi.get(self, "service_connection_id")

    @service_connection_id.setter
    def service_connection_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_connection_id", value)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the source repository. Used if the `init_type` is `Import`. Valid values: `Git`.
        """
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_type", value)

    @property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the source repository. Used if the `init_type` is `Import`.
        """
        return pulumi.get(self, "source_url")

    @source_url.setter
    def source_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_url", value)


