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
    'GetRegionsResult',
    'AwaitableGetRegionsResult',
    'get_regions',
    'get_regions_output',
]

@pulumi.output_type
class GetRegionsResult:
    """
    A collection of values returned by getRegions.
    """
    def __init__(__self__, filters=None, id=None, regions=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if regions and not isinstance(regions, list):
            raise TypeError("Expected argument 'regions' to be a list")
        pulumi.set(__self__, "regions", regions)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetRegionsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def regions(self) -> Optional[Sequence['outputs.GetRegionsRegionResult']]:
        return pulumi.get(self, "regions")


class AwaitableGetRegionsResult(GetRegionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegionsResult(
            filters=self.filters,
            id=self.id,
            regions=self.regions)


def get_regions(filters: Optional[Sequence[pulumi.InputType['GetRegionsFilterArgs']]] = None,
                regions: Optional[Sequence[pulumi.InputType['GetRegionsRegionArgs']]] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegionsResult:
    """
    Provides information about Linode regions that match a set of filters.

    ```python
    import pulumi
    import pulumi_linode as linode

    filtered_regions = linode.get_regions(filters=[
        linode.GetRegionsFilterArgs(
            name="status",
            values=["ok"],
        ),
        linode.GetRegionsFilterArgs(
            name="capabilities",
            values=["NodeBalancers"],
        ),
    ])
    pulumi.export("regions", filtered_regions.regions)
    ```

    ## Filterable Fields

    * `status`

    * `country`

    * `capabilities`
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['regions'] = regions
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('linode:index/getRegions:getRegions', __args__, opts=opts, typ=GetRegionsResult).value

    return AwaitableGetRegionsResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        regions=pulumi.get(__ret__, 'regions'))


@_utilities.lift_output_func(get_regions)
def get_regions_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetRegionsFilterArgs']]]]] = None,
                       regions: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetRegionsRegionArgs']]]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRegionsResult]:
    """
    Provides information about Linode regions that match a set of filters.

    ```python
    import pulumi
    import pulumi_linode as linode

    filtered_regions = linode.get_regions(filters=[
        linode.GetRegionsFilterArgs(
            name="status",
            values=["ok"],
        ),
        linode.GetRegionsFilterArgs(
            name="capabilities",
            values=["NodeBalancers"],
        ),
    ])
    pulumi.export("regions", filtered_regions.regions)
    ```

    ## Filterable Fields

    * `status`

    * `country`

    * `capabilities`
    """
    ...
