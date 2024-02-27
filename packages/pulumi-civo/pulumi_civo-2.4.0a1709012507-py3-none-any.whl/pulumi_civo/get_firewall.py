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
    'GetFirewallResult',
    'AwaitableGetFirewallResult',
    'get_firewall',
    'get_firewall_output',
]

@pulumi.output_type
class GetFirewallResult:
    """
    A collection of values returned by getFirewall.
    """
    def __init__(__self__, id=None, name=None, network_id=None, region=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the firewall
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> str:
        """
        The id of the associated network
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The region where the firewall is
        """
        return pulumi.get(self, "region")


class AwaitableGetFirewallResult(GetFirewallResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirewallResult(
            id=self.id,
            name=self.name,
            network_id=self.network_id,
            region=self.region)


def get_firewall(id: Optional[str] = None,
                 name: Optional[str] = None,
                 region: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirewallResult:
    """
    Retrieve information about a firewall for use in other resources.

    This data source provides all of the firewall's properties as configured on your Civo account.

    Firewalls may be looked up by id or name, and you can optionally pass region if you want to make a lookup for a specific firewall inside that region.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    test = civo.get_firewall(name="test-firewall",
        region="LON1")
    ```


    :param str id: The ID of this resource.
    :param str name: The name of the firewall
    :param str region: The region where the firewall is
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['region'] = region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('civo:index/getFirewall:getFirewall', __args__, opts=opts, typ=GetFirewallResult).value

    return AwaitableGetFirewallResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        network_id=pulumi.get(__ret__, 'network_id'),
        region=pulumi.get(__ret__, 'region'))


@_utilities.lift_output_func(get_firewall)
def get_firewall_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        region: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirewallResult]:
    """
    Retrieve information about a firewall for use in other resources.

    This data source provides all of the firewall's properties as configured on your Civo account.

    Firewalls may be looked up by id or name, and you can optionally pass region if you want to make a lookup for a specific firewall inside that region.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    test = civo.get_firewall(name="test-firewall",
        region="LON1")
    ```


    :param str id: The ID of this resource.
    :param str name: The name of the firewall
    :param str region: The region where the firewall is
    """
    ...
