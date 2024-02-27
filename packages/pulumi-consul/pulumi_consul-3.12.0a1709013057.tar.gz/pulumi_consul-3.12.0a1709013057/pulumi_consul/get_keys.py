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
    'GetKeysResult',
    'AwaitableGetKeysResult',
    'get_keys',
    'get_keys_output',
]

@pulumi.output_type
class GetKeysResult:
    """
    A collection of values returned by getKeys.
    """
    def __init__(__self__, datacenter=None, error_on_missing_keys=None, id=None, keys=None, namespace=None, partition=None, token=None, var=None):
        if datacenter and not isinstance(datacenter, str):
            raise TypeError("Expected argument 'datacenter' to be a str")
        pulumi.set(__self__, "datacenter", datacenter)
        if error_on_missing_keys and not isinstance(error_on_missing_keys, bool):
            raise TypeError("Expected argument 'error_on_missing_keys' to be a bool")
        pulumi.set(__self__, "error_on_missing_keys", error_on_missing_keys)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if keys and not isinstance(keys, list):
            raise TypeError("Expected argument 'keys' to be a list")
        pulumi.set(__self__, "keys", keys)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if partition and not isinstance(partition, str):
            raise TypeError("Expected argument 'partition' to be a str")
        pulumi.set(__self__, "partition", partition)
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)
        if var and not isinstance(var, dict):
            raise TypeError("Expected argument 'var' to be a dict")
        pulumi.set(__self__, "var", var)

    @property
    @pulumi.getter
    def datacenter(self) -> str:
        """
        The datacenter to use. This overrides the agent's default datacenter and the datacenter in the provider setup.
        """
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter(name="errorOnMissingKeys")
    def error_on_missing_keys(self) -> Optional[bool]:
        """
        Whether to return an error when a key is absent from the KV store and no default is configured. This defaults to `false`.
        """
        return pulumi.get(self, "error_on_missing_keys")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def keys(self) -> Optional[Sequence['outputs.GetKeysKeyResult']]:
        """
        Specifies a key in Consul to be read. Supported values documented below. Multiple blocks supported.
        """
        return pulumi.get(self, "keys")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        The namespace to lookup the keys.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def partition(self) -> Optional[str]:
        """
        The partition to lookup the keys.
        """
        return pulumi.get(self, "partition")

    @property
    @pulumi.getter
    def token(self) -> Optional[str]:
        """
        The ACL token to use. This overrides the token that the agent provides by default.
        """
        warnings.warn("""The token argument has been deprecated and will be removed in a future release.
Please use the token argument in the provider configuration""", DeprecationWarning)
        pulumi.log.warn("""token is deprecated: The token argument has been deprecated and will be removed in a future release.
Please use the token argument in the provider configuration""")

        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def var(self) -> Mapping[str, str]:
        """
        For each name given, the corresponding attribute has the value of the key.
        """
        return pulumi.get(self, "var")


class AwaitableGetKeysResult(GetKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeysResult(
            datacenter=self.datacenter,
            error_on_missing_keys=self.error_on_missing_keys,
            id=self.id,
            keys=self.keys,
            namespace=self.namespace,
            partition=self.partition,
            token=self.token,
            var=self.var)


def get_keys(datacenter: Optional[str] = None,
             error_on_missing_keys: Optional[bool] = None,
             keys: Optional[Sequence[pulumi.InputType['GetKeysKeyArgs']]] = None,
             namespace: Optional[str] = None,
             partition: Optional[str] = None,
             token: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeysResult:
    """
    The `Keys` datasource reads values from the Consul key/value store. This is a powerful way to dynamically set values in templates.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws
    import pulumi_consul as consul

    app_keys = consul.get_keys(datacenter="nyc1",
        keys=[consul.GetKeysKeyArgs(
            name="ami",
            path="service/app/launch_ami",
            default="ami-1234",
        )])
    # Start our instance with the dynamic ami value
    app_instance = aws.ec2.Instance("appInstance", ami=app_keys.var["ami"])
    # ...
    ```


    :param str datacenter: The datacenter to use. This overrides the agent's default datacenter and the datacenter in the provider setup.
    :param bool error_on_missing_keys: Whether to return an error when a key is absent from the KV store and no default is configured. This defaults to `false`.
    :param Sequence[pulumi.InputType['GetKeysKeyArgs']] keys: Specifies a key in Consul to be read. Supported values documented below. Multiple blocks supported.
    :param str namespace: The namespace to lookup the keys.
    :param str partition: The partition to lookup the keys.
    :param str token: The ACL token to use. This overrides the token that the agent provides by default.
    """
    __args__ = dict()
    __args__['datacenter'] = datacenter
    __args__['errorOnMissingKeys'] = error_on_missing_keys
    __args__['keys'] = keys
    __args__['namespace'] = namespace
    __args__['partition'] = partition
    __args__['token'] = token
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('consul:index/getKeys:getKeys', __args__, opts=opts, typ=GetKeysResult).value

    return AwaitableGetKeysResult(
        datacenter=pulumi.get(__ret__, 'datacenter'),
        error_on_missing_keys=pulumi.get(__ret__, 'error_on_missing_keys'),
        id=pulumi.get(__ret__, 'id'),
        keys=pulumi.get(__ret__, 'keys'),
        namespace=pulumi.get(__ret__, 'namespace'),
        partition=pulumi.get(__ret__, 'partition'),
        token=pulumi.get(__ret__, 'token'),
        var=pulumi.get(__ret__, 'var'))


@_utilities.lift_output_func(get_keys)
def get_keys_output(datacenter: Optional[pulumi.Input[Optional[str]]] = None,
                    error_on_missing_keys: Optional[pulumi.Input[Optional[bool]]] = None,
                    keys: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetKeysKeyArgs']]]]] = None,
                    namespace: Optional[pulumi.Input[Optional[str]]] = None,
                    partition: Optional[pulumi.Input[Optional[str]]] = None,
                    token: Optional[pulumi.Input[Optional[str]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKeysResult]:
    """
    The `Keys` datasource reads values from the Consul key/value store. This is a powerful way to dynamically set values in templates.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws
    import pulumi_consul as consul

    app_keys = consul.get_keys(datacenter="nyc1",
        keys=[consul.GetKeysKeyArgs(
            name="ami",
            path="service/app/launch_ami",
            default="ami-1234",
        )])
    # Start our instance with the dynamic ami value
    app_instance = aws.ec2.Instance("appInstance", ami=app_keys.var["ami"])
    # ...
    ```


    :param str datacenter: The datacenter to use. This overrides the agent's default datacenter and the datacenter in the provider setup.
    :param bool error_on_missing_keys: Whether to return an error when a key is absent from the KV store and no default is configured. This defaults to `false`.
    :param Sequence[pulumi.InputType['GetKeysKeyArgs']] keys: Specifies a key in Consul to be read. Supported values documented below. Multiple blocks supported.
    :param str namespace: The namespace to lookup the keys.
    :param str partition: The partition to lookup the keys.
    :param str token: The ACL token to use. This overrides the token that the agent provides by default.
    """
    ...
