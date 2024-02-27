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
    'GetObjectStoreCredentialResult',
    'AwaitableGetObjectStoreCredentialResult',
    'get_object_store_credential',
    'get_object_store_credential_output',
]

@pulumi.output_type
class GetObjectStoreCredentialResult:
    """
    A collection of values returned by getObjectStoreCredential.
    """
    def __init__(__self__, access_key_id=None, id=None, name=None, region=None, secret_access_key=None, status=None):
        if access_key_id and not isinstance(access_key_id, str):
            raise TypeError("Expected argument 'access_key_id' to be a str")
        pulumi.set(__self__, "access_key_id", access_key_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if secret_access_key and not isinstance(secret_access_key, str):
            raise TypeError("Expected argument 'secret_access_key' to be a str")
        pulumi.set(__self__, "secret_access_key", secret_access_key)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> str:
        """
        The access key id of the Object Store Credential
        """
        return pulumi.get(self, "access_key_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of the Object Store Credential
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the Object Store Credential
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The region of an existing Object Store
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> str:
        """
        The secret access key of the Object Store Credential
        """
        return pulumi.get(self, "secret_access_key")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the Object Store Credential
        """
        return pulumi.get(self, "status")


class AwaitableGetObjectStoreCredentialResult(GetObjectStoreCredentialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetObjectStoreCredentialResult(
            access_key_id=self.access_key_id,
            id=self.id,
            name=self.name,
            region=self.region,
            secret_access_key=self.secret_access_key,
            status=self.status)


def get_object_store_credential(id: Optional[str] = None,
                                name: Optional[str] = None,
                                region: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetObjectStoreCredentialResult:
    """
    Get information of an Object Store Credential for use in other resources. This data source provides all of the Object Store Credential's properties as configured on your Civo account.

    Note: This data source returns a single Object Store Credential. When specifying a name, an error will be raised if more than one Object Store Credentials with the same name found.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    backup_object_store_credential = civo.get_object_store_credential(name="backup-server")
    # Use the credential to create a bucket
    backup_object_store = civo.ObjectStore("backupObjectStore",
        max_size_gb=500,
        region="LON1",
        access_key_id=backup_object_store_credential.access_key_id)
    ```


    :param str id: The ID of the Object Store Credential
    :param str name: The name of the Object Store Credential
    :param str region: The region of an existing Object Store
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['region'] = region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('civo:index/getObjectStoreCredential:getObjectStoreCredential', __args__, opts=opts, typ=GetObjectStoreCredentialResult).value

    return AwaitableGetObjectStoreCredentialResult(
        access_key_id=pulumi.get(__ret__, 'access_key_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        region=pulumi.get(__ret__, 'region'),
        secret_access_key=pulumi.get(__ret__, 'secret_access_key'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_object_store_credential)
def get_object_store_credential_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                       name: Optional[pulumi.Input[Optional[str]]] = None,
                                       region: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetObjectStoreCredentialResult]:
    """
    Get information of an Object Store Credential for use in other resources. This data source provides all of the Object Store Credential's properties as configured on your Civo account.

    Note: This data source returns a single Object Store Credential. When specifying a name, an error will be raised if more than one Object Store Credentials with the same name found.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    backup_object_store_credential = civo.get_object_store_credential(name="backup-server")
    # Use the credential to create a bucket
    backup_object_store = civo.ObjectStore("backupObjectStore",
        max_size_gb=500,
        region="LON1",
        access_key_id=backup_object_store_credential.access_key_id)
    ```


    :param str id: The ID of the Object Store Credential
    :param str name: The name of the Object Store Credential
    :param str region: The region of an existing Object Store
    """
    ...
