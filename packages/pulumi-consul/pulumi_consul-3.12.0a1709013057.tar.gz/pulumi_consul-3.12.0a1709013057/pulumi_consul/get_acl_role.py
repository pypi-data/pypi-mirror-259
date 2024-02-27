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
    'GetAclRoleResult',
    'AwaitableGetAclRoleResult',
    'get_acl_role',
    'get_acl_role_output',
]

@pulumi.output_type
class GetAclRoleResult:
    """
    A collection of values returned by getAclRole.
    """
    def __init__(__self__, description=None, id=None, name=None, namespace=None, node_identities=None, partition=None, policies=None, service_identities=None, templated_policies=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
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
        if service_identities and not isinstance(service_identities, list):
            raise TypeError("Expected argument 'service_identities' to be a list")
        pulumi.set(__self__, "service_identities", service_identities)
        if templated_policies and not isinstance(templated_policies, list):
            raise TypeError("Expected argument 'templated_policies' to be a list")
        pulumi.set(__self__, "templated_policies", templated_policies)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the ACL Role.
        """
        return pulumi.get(self, "description")

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
        """
        The name of the ACL Role.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        The namespace to lookup the role.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="nodeIdentities")
    def node_identities(self) -> Sequence['outputs.GetAclRoleNodeIdentityResult']:
        """
        The list of node identities associated with the ACL Role.
        """
        return pulumi.get(self, "node_identities")

    @property
    @pulumi.getter
    def partition(self) -> Optional[str]:
        """
        The partition to lookup the role.
        """
        return pulumi.get(self, "partition")

    @property
    @pulumi.getter
    def policies(self) -> Sequence['outputs.GetAclRolePolicyResult']:
        """
        The list of policies associated with the ACL Role.
        """
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter(name="serviceIdentities")
    def service_identities(self) -> Sequence['outputs.GetAclRoleServiceIdentityResult']:
        """
        The list of service identities associated with the ACL Role.
        """
        return pulumi.get(self, "service_identities")

    @property
    @pulumi.getter(name="templatedPolicies")
    def templated_policies(self) -> Sequence['outputs.GetAclRoleTemplatedPolicyResult']:
        """
        The list of templated policies that should be applied to the token.
        """
        return pulumi.get(self, "templated_policies")


class AwaitableGetAclRoleResult(GetAclRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAclRoleResult(
            description=self.description,
            id=self.id,
            name=self.name,
            namespace=self.namespace,
            node_identities=self.node_identities,
            partition=self.partition,
            policies=self.policies,
            service_identities=self.service_identities,
            templated_policies=self.templated_policies)


def get_acl_role(name: Optional[str] = None,
                 namespace: Optional[str] = None,
                 partition: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAclRoleResult:
    """
    The `AclRole` data source returns the information related to a [Consul ACL Role](https://www.consul.io/api/acl/roles.html).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_consul as consul

    test = consul.get_acl_role(name="example-role")
    pulumi.export("consulAclRole", test.id)
    ```


    :param str namespace: The namespace to lookup the role.
    :param str partition: The partition to lookup the role.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['namespace'] = namespace
    __args__['partition'] = partition
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('consul:index/getAclRole:getAclRole', __args__, opts=opts, typ=GetAclRoleResult).value

    return AwaitableGetAclRoleResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        namespace=pulumi.get(__ret__, 'namespace'),
        node_identities=pulumi.get(__ret__, 'node_identities'),
        partition=pulumi.get(__ret__, 'partition'),
        policies=pulumi.get(__ret__, 'policies'),
        service_identities=pulumi.get(__ret__, 'service_identities'),
        templated_policies=pulumi.get(__ret__, 'templated_policies'))


@_utilities.lift_output_func(get_acl_role)
def get_acl_role_output(name: Optional[pulumi.Input[str]] = None,
                        namespace: Optional[pulumi.Input[Optional[str]]] = None,
                        partition: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAclRoleResult]:
    """
    The `AclRole` data source returns the information related to a [Consul ACL Role](https://www.consul.io/api/acl/roles.html).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_consul as consul

    test = consul.get_acl_role(name="example-role")
    pulumi.export("consulAclRole", test.id)
    ```


    :param str namespace: The namespace to lookup the role.
    :param str partition: The partition to lookup the role.
    """
    ...
