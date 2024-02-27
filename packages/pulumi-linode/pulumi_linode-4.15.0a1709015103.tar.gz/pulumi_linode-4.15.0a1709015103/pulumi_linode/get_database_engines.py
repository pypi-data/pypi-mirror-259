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
    'GetDatabaseEnginesResult',
    'AwaitableGetDatabaseEnginesResult',
    'get_database_engines',
    'get_database_engines_output',
]

@pulumi.output_type
class GetDatabaseEnginesResult:
    """
    A collection of values returned by getDatabaseEngines.
    """
    def __init__(__self__, engines=None, filters=None, id=None, latest=None, order=None, order_by=None):
        if engines and not isinstance(engines, list):
            raise TypeError("Expected argument 'engines' to be a list")
        pulumi.set(__self__, "engines", engines)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if latest and not isinstance(latest, bool):
            raise TypeError("Expected argument 'latest' to be a bool")
        pulumi.set(__self__, "latest", latest)
        if order and not isinstance(order, str):
            raise TypeError("Expected argument 'order' to be a str")
        pulumi.set(__self__, "order", order)
        if order_by and not isinstance(order_by, str):
            raise TypeError("Expected argument 'order_by' to be a str")
        pulumi.set(__self__, "order_by", order_by)

    @property
    @pulumi.getter
    def engines(self) -> Optional[Sequence['outputs.GetDatabaseEnginesEngineResult']]:
        return pulumi.get(self, "engines")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDatabaseEnginesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The Managed Database engine ID in engine/version format.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def latest(self) -> Optional[bool]:
        return pulumi.get(self, "latest")

    @property
    @pulumi.getter
    def order(self) -> Optional[str]:
        return pulumi.get(self, "order")

    @property
    @pulumi.getter(name="orderBy")
    def order_by(self) -> Optional[str]:
        return pulumi.get(self, "order_by")


class AwaitableGetDatabaseEnginesResult(GetDatabaseEnginesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseEnginesResult(
            engines=self.engines,
            filters=self.filters,
            id=self.id,
            latest=self.latest,
            order=self.order,
            order_by=self.order_by)


def get_database_engines(engines: Optional[Sequence[pulumi.InputType['GetDatabaseEnginesEngineArgs']]] = None,
                         filters: Optional[Sequence[pulumi.InputType['GetDatabaseEnginesFilterArgs']]] = None,
                         latest: Optional[bool] = None,
                         order: Optional[str] = None,
                         order_by: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseEnginesResult:
    """
    Provides information about Linode Managed Database engines that match a set of filters.

    ## Example Usage

    Get information about all Linode Managed Database engines:

    ```python
    import pulumi
    import pulumi_linode as linode

    all = linode.get_database_engines()
    pulumi.export("engineIds", [__item.id for __item in all.engines])
    ```

    Get information about all Linode MySQL Database engines:

    ```python
    import pulumi
    import pulumi_linode as linode

    mysql = linode.get_database_engines(filters=[linode.GetDatabaseEnginesFilterArgs(
        name="engine",
        values=["mysql"],
    )])
    pulumi.export("engineIds", [__item.id for __item in mysql.engines])
    ```

    Create a Linode MySQL Database using the latest support MySQL version:

    ```python
    import pulumi
    import pulumi_linode as linode

    mysql = linode.get_database_engines(latest=True,
        filters=[linode.GetDatabaseEnginesFilterArgs(
            name="engine",
            values=["mysql"],
        )])
    my_db = linode.DatabaseMysql("myDb",
        label="mydb",
        engine_id=mysql.engines[0].id,
        region="us-southeast",
        type="g6-nanode-1")
    ```


    :param bool latest: If true, only the latest engine version will be returned.
           
           * `filter` - (Optional) A set of filters used to select engines that meet certain requirements.
    :param str order: The order in which results should be returned. (`asc`, `desc`; default `asc`)
    :param str order_by: The attribute to order the results by. (`version`)
    """
    __args__ = dict()
    __args__['engines'] = engines
    __args__['filters'] = filters
    __args__['latest'] = latest
    __args__['order'] = order
    __args__['orderBy'] = order_by
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('linode:index/getDatabaseEngines:getDatabaseEngines', __args__, opts=opts, typ=GetDatabaseEnginesResult).value

    return AwaitableGetDatabaseEnginesResult(
        engines=pulumi.get(__ret__, 'engines'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        latest=pulumi.get(__ret__, 'latest'),
        order=pulumi.get(__ret__, 'order'),
        order_by=pulumi.get(__ret__, 'order_by'))


@_utilities.lift_output_func(get_database_engines)
def get_database_engines_output(engines: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDatabaseEnginesEngineArgs']]]]] = None,
                                filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDatabaseEnginesFilterArgs']]]]] = None,
                                latest: Optional[pulumi.Input[Optional[bool]]] = None,
                                order: Optional[pulumi.Input[Optional[str]]] = None,
                                order_by: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseEnginesResult]:
    """
    Provides information about Linode Managed Database engines that match a set of filters.

    ## Example Usage

    Get information about all Linode Managed Database engines:

    ```python
    import pulumi
    import pulumi_linode as linode

    all = linode.get_database_engines()
    pulumi.export("engineIds", [__item.id for __item in all.engines])
    ```

    Get information about all Linode MySQL Database engines:

    ```python
    import pulumi
    import pulumi_linode as linode

    mysql = linode.get_database_engines(filters=[linode.GetDatabaseEnginesFilterArgs(
        name="engine",
        values=["mysql"],
    )])
    pulumi.export("engineIds", [__item.id for __item in mysql.engines])
    ```

    Create a Linode MySQL Database using the latest support MySQL version:

    ```python
    import pulumi
    import pulumi_linode as linode

    mysql = linode.get_database_engines(latest=True,
        filters=[linode.GetDatabaseEnginesFilterArgs(
            name="engine",
            values=["mysql"],
        )])
    my_db = linode.DatabaseMysql("myDb",
        label="mydb",
        engine_id=mysql.engines[0].id,
        region="us-southeast",
        type="g6-nanode-1")
    ```


    :param bool latest: If true, only the latest engine version will be returned.
           
           * `filter` - (Optional) A set of filters used to select engines that meet certain requirements.
    :param str order: The order in which results should be returned. (`asc`, `desc`; default `asc`)
    :param str order_by: The attribute to order the results by. (`version`)
    """
    ...
