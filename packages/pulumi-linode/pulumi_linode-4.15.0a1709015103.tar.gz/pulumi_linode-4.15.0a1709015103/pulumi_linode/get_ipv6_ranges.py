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
    'GetIpv6RangesResult',
    'AwaitableGetIpv6RangesResult',
    'get_ipv6_ranges',
    'get_ipv6_ranges_output',
]

@pulumi.output_type
class GetIpv6RangesResult:
    """
    A collection of values returned by getIpv6Ranges.
    """
    def __init__(__self__, filters=None, id=None, ranges=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ranges and not isinstance(ranges, list):
            raise TypeError("Expected argument 'ranges' to be a list")
        pulumi.set(__self__, "ranges", ranges)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetIpv6RangesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ranges(self) -> Optional[Sequence['outputs.GetIpv6RangesRangeResult']]:
        return pulumi.get(self, "ranges")


class AwaitableGetIpv6RangesResult(GetIpv6RangesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIpv6RangesResult(
            filters=self.filters,
            id=self.id,
            ranges=self.ranges)


def get_ipv6_ranges(filters: Optional[Sequence[pulumi.InputType['GetIpv6RangesFilterArgs']]] = None,
                    ranges: Optional[Sequence[pulumi.InputType['GetIpv6RangesRangeArgs']]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIpv6RangesResult:
    """
    Provides information about Linode IPv6 ranges that match a set of filters.

    > Some fields may not be accessible directly the results of this data source.
    For additional information about a specific IPv6 range consider using the Ipv6Range
    data source.

    ```python
    import pulumi
    import pulumi_linode as linode

    filtered_ranges = linode.get_ipv6_ranges(filters=[linode.GetIpv6RangesFilterArgs(
        name="region",
        values=["us-mia"],
    )])
    pulumi.export("ranges", data["linode_ipv4_ranges"]["filtered-ranges"]["ranges"])
    ```

    ## Filterable Fields

    * `range`

    * `route_target`

    * `prefix`

    * `region`
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['ranges'] = ranges
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('linode:index/getIpv6Ranges:getIpv6Ranges', __args__, opts=opts, typ=GetIpv6RangesResult).value

    return AwaitableGetIpv6RangesResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        ranges=pulumi.get(__ret__, 'ranges'))


@_utilities.lift_output_func(get_ipv6_ranges)
def get_ipv6_ranges_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetIpv6RangesFilterArgs']]]]] = None,
                           ranges: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetIpv6RangesRangeArgs']]]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIpv6RangesResult]:
    """
    Provides information about Linode IPv6 ranges that match a set of filters.

    > Some fields may not be accessible directly the results of this data source.
    For additional information about a specific IPv6 range consider using the Ipv6Range
    data source.

    ```python
    import pulumi
    import pulumi_linode as linode

    filtered_ranges = linode.get_ipv6_ranges(filters=[linode.GetIpv6RangesFilterArgs(
        name="region",
        values=["us-mia"],
    )])
    pulumi.export("ranges", data["linode_ipv4_ranges"]["filtered-ranges"]["ranges"])
    ```

    ## Filterable Fields

    * `range`

    * `route_target`

    * `prefix`

    * `region`
    """
    ...
