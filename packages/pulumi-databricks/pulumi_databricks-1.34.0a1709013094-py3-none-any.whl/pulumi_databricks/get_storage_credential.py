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
from ._inputs import *

__all__ = [
    'GetStorageCredentialResult',
    'AwaitableGetStorageCredentialResult',
    'get_storage_credential',
    'get_storage_credential_output',
]

@pulumi.output_type
class GetStorageCredentialResult:
    """
    A collection of values returned by getStorageCredential.
    """
    def __init__(__self__, id=None, name=None, storage_credential_info=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if storage_credential_info and not isinstance(storage_credential_info, dict):
            raise TypeError("Expected argument 'storage_credential_info' to be a dict")
        pulumi.set(__self__, "storage_credential_info", storage_credential_info)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageCredentialInfo")
    def storage_credential_info(self) -> 'outputs.GetStorageCredentialStorageCredentialInfoResult':
        return pulumi.get(self, "storage_credential_info")


class AwaitableGetStorageCredentialResult(GetStorageCredentialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStorageCredentialResult(
            id=self.id,
            name=self.name,
            storage_credential_info=self.storage_credential_info)


def get_storage_credential(name: Optional[str] = None,
                           storage_credential_info: Optional[pulumi.InputType['GetStorageCredentialStorageCredentialInfoArgs']] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStorageCredentialResult:
    """
    ## Related Resources

    The following resources are used in the same context:

    * get_storage_credentials to get names of all credentials
    * StorageCredential to manage Storage Credentials within Unity Catalog.


    :param str name: The name of the storage credential
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['storageCredentialInfo'] = storage_credential_info
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('databricks:index/getStorageCredential:getStorageCredential', __args__, opts=opts, typ=GetStorageCredentialResult).value

    return AwaitableGetStorageCredentialResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        storage_credential_info=pulumi.get(__ret__, 'storage_credential_info'))


@_utilities.lift_output_func(get_storage_credential)
def get_storage_credential_output(name: Optional[pulumi.Input[str]] = None,
                                  storage_credential_info: Optional[pulumi.Input[Optional[pulumi.InputType['GetStorageCredentialStorageCredentialInfoArgs']]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStorageCredentialResult]:
    """
    ## Related Resources

    The following resources are used in the same context:

    * get_storage_credentials to get names of all credentials
    * StorageCredential to manage Storage Credentials within Unity Catalog.


    :param str name: The name of the storage credential
    """
    ...
