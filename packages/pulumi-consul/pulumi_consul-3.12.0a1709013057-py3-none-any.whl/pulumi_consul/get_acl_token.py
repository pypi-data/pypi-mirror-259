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
    'GetAclTokenResult',
    'AwaitableGetAclTokenResult',
    'get_acl_token',
    'get_acl_token_output',
]

@pulumi.output_type
class GetAclTokenResult:
    """
    A collection of values returned by getAclToken.
    """
    def __init__(__self__, accessor_id=None, description=None, expiration_time=None, id=None, local=None, namespace=None, node_identities=None, partition=None, policies=None, roles=None, service_identities=None, templated_policies=None):
        if accessor_id and not isinstance(accessor_id, str):
            raise TypeError("Expected argument 'accessor_id' to be a str")
        pulumi.set(__self__, "accessor_id", accessor_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if expiration_time and not isinstance(expiration_time, str):
            raise TypeError("Expected argument 'expiration_time' to be a str")
        pulumi.set(__self__, "expiration_time", expiration_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if local and not isinstance(local, bool):
            raise TypeError("Expected argument 'local' to be a bool")
        pulumi.set(__self__, "local", local)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if node_identities and not isinstance(node_identities, list):
            raise TypeError("Expected argument 'node_identities' to be a list")
        pulumi.set(__self__, "node_identities", node_identities)
        if partition and not isinstance(partition, str):
            raise TypeError("Expected argument 'partition' to be a str")
        pulumi.set(__self__, "partition", partition)
        if policies and not isinstance(policies, list):
            raise TypeError("Expected argument 'policies' to be a list")
        pulumi.set(__self__, "policies", policies)
        if roles and not isinstance(roles, list):
            raise TypeError("Expected argument 'roles' to be a list")
        pulumi.set(__self__, "roles", roles)
        if service_identities and not isinstance(service_identities, list):
            raise TypeError("Expected argument 'service_identities' to be a list")
        pulumi.set(__self__, "service_identities", service_identities)
        if templated_policies and not isinstance(templated_policies, list):
            raise TypeError("Expected argument 'templated_policies' to be a list")
        pulumi.set(__self__, "templated_policies", templated_policies)

    @property
    @pulumi.getter(name="accessorId")
    def accessor_id(self) -> str:
        """
        The accessor ID of the ACL token.
        """
        return pulumi.get(self, "accessor_id")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the ACL token.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> str:
        """
        If set this represents the point after which a token should be considered revoked and is eligible for destruction.
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def local(self) -> bool:
        """
        Whether the ACL token is local to the datacenter it was created within.
        """
        return pulumi.get(self, "local")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        The namespace to lookup the ACL token.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="nodeIdentities")
    def node_identities(self) -> Sequence['outputs.GetAclTokenNodeIdentityResult']:
        """
        The list of node identities attached to the token.
        """
        return pulumi.get(self, "node_identities")

    @property
    @pulumi.getter
    def partition(self) -> Optional[str]:
        """
        The partition to lookup the ACL token.
        """
        return pulumi.get(self, "partition")

    @property
    @pulumi.getter
    def policies(self) -> Sequence['outputs.GetAclTokenPolicyResult']:
        """
        A list of policies associated with the ACL token.
        """
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter
    def roles(self) -> Sequence['outputs.GetAclTokenRoleResult']:
        """
        List of roles linked to the token
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter(name="serviceIdentities")
    def service_identities(self) -> Sequence['outputs.GetAclTokenServiceIdentityResult']:
        """
        The list of service identities attached to the token.
        """
        return pulumi.get(self, "service_identities")

    @property
    @pulumi.getter(name="templatedPolicies")
    def templated_policies(self) -> Sequence['outputs.GetAclTokenTemplatedPolicyResult']:
        """
        The list of templated policies that should be applied to the token.
        """
        return pulumi.get(self, "templated_policies")


class AwaitableGetAclTokenResult(GetAclTokenResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAclTokenResult(
            accessor_id=self.accessor_id,
            description=self.description,
            expiration_time=self.expiration_time,
            id=self.id,
            local=self.local,
            namespace=self.namespace,
            node_identities=self.node_identities,
            partition=self.partition,
            policies=self.policies,
            roles=self.roles,
            service_identities=self.service_identities,
            templated_policies=self.templated_policies)


def get_acl_token(accessor_id: Optional[str] = None,
                  namespace: Optional[str] = None,
                  partition: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAclTokenResult:
    """
    The `AclToken` data source returns the information related to the `AclToken` resource with the exception of its secret ID.

    If you want to get the secret ID associated with a token, use the [`get_acl_token_secret_id` data source](https://www.terraform.io/docs/providers/consul/d/acl_token_secret_id.html).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_consul as consul

    test = consul.get_acl_token(accessor_id="00000000-0000-0000-0000-000000000002")
    pulumi.export("consulAclPolicies", test.policies)
    ```


    :param str accessor_id: The accessor ID of the ACL token.
    :param str namespace: The namespace to lookup the ACL token.
    :param str partition: The partition to lookup the ACL token.
    """
    __args__ = dict()
    __args__['accessorId'] = accessor_id
    __args__['namespace'] = namespace
    __args__['partition'] = partition
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('consul:index/getAclToken:getAclToken', __args__, opts=opts, typ=GetAclTokenResult).value

    return AwaitableGetAclTokenResult(
        accessor_id=pulumi.get(__ret__, 'accessor_id'),
        description=pulumi.get(__ret__, 'description'),
        expiration_time=pulumi.get(__ret__, 'expiration_time'),
        id=pulumi.get(__ret__, 'id'),
        local=pulumi.get(__ret__, 'local'),
        namespace=pulumi.get(__ret__, 'namespace'),
        node_identities=pulumi.get(__ret__, 'node_identities'),
        partition=pulumi.get(__ret__, 'partition'),
        policies=pulumi.get(__ret__, 'policies'),
        roles=pulumi.get(__ret__, 'roles'),
        service_identities=pulumi.get(__ret__, 'service_identities'),
        templated_policies=pulumi.get(__ret__, 'templated_policies'))


@_utilities.lift_output_func(get_acl_token)
def get_acl_token_output(accessor_id: Optional[pulumi.Input[str]] = None,
                         namespace: Optional[pulumi.Input[Optional[str]]] = None,
                         partition: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAclTokenResult]:
    """
    The `AclToken` data source returns the information related to the `AclToken` resource with the exception of its secret ID.

    If you want to get the secret ID associated with a token, use the [`get_acl_token_secret_id` data source](https://www.terraform.io/docs/providers/consul/d/acl_token_secret_id.html).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_consul as consul

    test = consul.get_acl_token(accessor_id="00000000-0000-0000-0000-000000000002")
    pulumi.export("consulAclPolicies", test.policies)
    ```


    :param str accessor_id: The accessor ID of the ACL token.
    :param str namespace: The namespace to lookup the ACL token.
    :param str partition: The partition to lookup the ACL token.
    """
    ...
