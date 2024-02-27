# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ImageArgs', 'Image']

@pulumi.input_type
class ImageArgs:
    def __init__(__self__, *,
                 label: pulumi.Input[str],
                 cloud_init: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk_id: Optional[pulumi.Input[int]] = None,
                 file_hash: Optional[pulumi.Input[str]] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 linode_id: Optional[pulumi.Input[int]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Image resource.
        :param pulumi.Input[str] label: A short description of the Image. Labels cannot contain special characters.
        :param pulumi.Input[bool] cloud_init: Whether this image supports cloud-init.
        :param pulumi.Input[str] description: A detailed description of this Image.
               
               - - -
               
               The following arguments apply to creating an image from an existing Linode Instance:
        :param pulumi.Input[int] disk_id: The ID of the Linode Disk that this Image will be created from.
        :param pulumi.Input[str] file_hash: The MD5 hash of the file to be uploaded. This is used to trigger file updates.
        :param pulumi.Input[str] file_path: The path of the image file to be uploaded.
        :param pulumi.Input[int] linode_id: The ID of the Linode that this Image will be created from.
               
               - - -
               
               > **NOTICE:** Uploading images is currently in beta. Ensure `LINODE_API_VERSION` is set to `v4beta` in order to use this functionality.
               
               The following arguments apply to uploading an image:
        :param pulumi.Input[str] region: The region of the image. See all regions [here](https://api.linode.com/v4/regions).
        """
        pulumi.set(__self__, "label", label)
        if cloud_init is not None:
            pulumi.set(__self__, "cloud_init", cloud_init)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if disk_id is not None:
            pulumi.set(__self__, "disk_id", disk_id)
        if file_hash is not None:
            pulumi.set(__self__, "file_hash", file_hash)
        if file_path is not None:
            pulumi.set(__self__, "file_path", file_path)
        if linode_id is not None:
            pulumi.set(__self__, "linode_id", linode_id)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def label(self) -> pulumi.Input[str]:
        """
        A short description of the Image. Labels cannot contain special characters.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: pulumi.Input[str]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="cloudInit")
    def cloud_init(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this image supports cloud-init.
        """
        return pulumi.get(self, "cloud_init")

    @cloud_init.setter
    def cloud_init(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cloud_init", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A detailed description of this Image.

        - - -

        The following arguments apply to creating an image from an existing Linode Instance:
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the Linode Disk that this Image will be created from.
        """
        return pulumi.get(self, "disk_id")

    @disk_id.setter
    def disk_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_id", value)

    @property
    @pulumi.getter(name="fileHash")
    def file_hash(self) -> Optional[pulumi.Input[str]]:
        """
        The MD5 hash of the file to be uploaded. This is used to trigger file updates.
        """
        return pulumi.get(self, "file_hash")

    @file_hash.setter
    def file_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_hash", value)

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[pulumi.Input[str]]:
        """
        The path of the image file to be uploaded.
        """
        return pulumi.get(self, "file_path")

    @file_path.setter
    def file_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_path", value)

    @property
    @pulumi.getter(name="linodeId")
    def linode_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the Linode that this Image will be created from.

        - - -

        > **NOTICE:** Uploading images is currently in beta. Ensure `LINODE_API_VERSION` is set to `v4beta` in order to use this functionality.

        The following arguments apply to uploading an image:
        """
        return pulumi.get(self, "linode_id")

    @linode_id.setter
    def linode_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "linode_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the image. See all regions [here](https://api.linode.com/v4/regions).
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _ImageState:
    def __init__(__self__, *,
                 capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cloud_init: Optional[pulumi.Input[bool]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 deprecated: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk_id: Optional[pulumi.Input[int]] = None,
                 expiry: Optional[pulumi.Input[str]] = None,
                 file_hash: Optional[pulumi.Input[str]] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 is_public: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 linode_id: Optional[pulumi.Input[int]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vendor: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Image resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] capabilities: The capabilities of this Image.
        :param pulumi.Input[bool] cloud_init: Whether this image supports cloud-init.
        :param pulumi.Input[str] created: When this Image was created.
        :param pulumi.Input[str] created_by: The name of the User who created this Image.
        :param pulumi.Input[bool] deprecated: Whether or not this Image is deprecated. Will only be True for deprecated public Images.
        :param pulumi.Input[str] description: A detailed description of this Image.
               
               - - -
               
               The following arguments apply to creating an image from an existing Linode Instance:
        :param pulumi.Input[int] disk_id: The ID of the Linode Disk that this Image will be created from.
        :param pulumi.Input[str] expiry: Only Images created automatically (from a deleted Linode; type=automatic) will expire.
        :param pulumi.Input[str] file_hash: The MD5 hash of the file to be uploaded. This is used to trigger file updates.
        :param pulumi.Input[str] file_path: The path of the image file to be uploaded.
        :param pulumi.Input[bool] is_public: True if the Image is public.
        :param pulumi.Input[str] label: A short description of the Image. Labels cannot contain special characters.
        :param pulumi.Input[int] linode_id: The ID of the Linode that this Image will be created from.
               
               - - -
               
               > **NOTICE:** Uploading images is currently in beta. Ensure `LINODE_API_VERSION` is set to `v4beta` in order to use this functionality.
               
               The following arguments apply to uploading an image:
        :param pulumi.Input[str] region: The region of the image. See all regions [here](https://api.linode.com/v4/regions).
        :param pulumi.Input[int] size: The minimum size this Image needs to deploy. Size is in MB.
        :param pulumi.Input[str] status: The current status of this Image.
        :param pulumi.Input[str] type: How the Image was created. 'Manual' Images can be created at any time. 'Automatic' images are created automatically from a deleted Linode.
        :param pulumi.Input[str] vendor: The upstream distribution vendor. Nil for private Images.
        """
        if capabilities is not None:
            pulumi.set(__self__, "capabilities", capabilities)
        if cloud_init is not None:
            pulumi.set(__self__, "cloud_init", cloud_init)
        if created is not None:
            pulumi.set(__self__, "created", created)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if deprecated is not None:
            pulumi.set(__self__, "deprecated", deprecated)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if disk_id is not None:
            pulumi.set(__self__, "disk_id", disk_id)
        if expiry is not None:
            pulumi.set(__self__, "expiry", expiry)
        if file_hash is not None:
            pulumi.set(__self__, "file_hash", file_hash)
        if file_path is not None:
            pulumi.set(__self__, "file_path", file_path)
        if is_public is not None:
            pulumi.set(__self__, "is_public", is_public)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if linode_id is not None:
            pulumi.set(__self__, "linode_id", linode_id)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if vendor is not None:
            pulumi.set(__self__, "vendor", vendor)

    @property
    @pulumi.getter
    def capabilities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The capabilities of this Image.
        """
        return pulumi.get(self, "capabilities")

    @capabilities.setter
    def capabilities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "capabilities", value)

    @property
    @pulumi.getter(name="cloudInit")
    def cloud_init(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this image supports cloud-init.
        """
        return pulumi.get(self, "cloud_init")

    @cloud_init.setter
    def cloud_init(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cloud_init", value)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[str]]:
        """
        When this Image was created.
        """
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the User who created this Image.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter
    def deprecated(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not this Image is deprecated. Will only be True for deprecated public Images.
        """
        return pulumi.get(self, "deprecated")

    @deprecated.setter
    def deprecated(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "deprecated", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A detailed description of this Image.

        - - -

        The following arguments apply to creating an image from an existing Linode Instance:
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the Linode Disk that this Image will be created from.
        """
        return pulumi.get(self, "disk_id")

    @disk_id.setter
    def disk_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_id", value)

    @property
    @pulumi.getter
    def expiry(self) -> Optional[pulumi.Input[str]]:
        """
        Only Images created automatically (from a deleted Linode; type=automatic) will expire.
        """
        return pulumi.get(self, "expiry")

    @expiry.setter
    def expiry(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiry", value)

    @property
    @pulumi.getter(name="fileHash")
    def file_hash(self) -> Optional[pulumi.Input[str]]:
        """
        The MD5 hash of the file to be uploaded. This is used to trigger file updates.
        """
        return pulumi.get(self, "file_hash")

    @file_hash.setter
    def file_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_hash", value)

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[pulumi.Input[str]]:
        """
        The path of the image file to be uploaded.
        """
        return pulumi.get(self, "file_path")

    @file_path.setter
    def file_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_path", value)

    @property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> Optional[pulumi.Input[bool]]:
        """
        True if the Image is public.
        """
        return pulumi.get(self, "is_public")

    @is_public.setter
    def is_public(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_public", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        A short description of the Image. Labels cannot contain special characters.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="linodeId")
    def linode_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the Linode that this Image will be created from.

        - - -

        > **NOTICE:** Uploading images is currently in beta. Ensure `LINODE_API_VERSION` is set to `v4beta` in order to use this functionality.

        The following arguments apply to uploading an image:
        """
        return pulumi.get(self, "linode_id")

    @linode_id.setter
    def linode_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "linode_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the image. See all regions [here](https://api.linode.com/v4/regions).
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        The minimum size this Image needs to deploy. Size is in MB.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The current status of this Image.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        How the Image was created. 'Manual' Images can be created at any time. 'Automatic' images are created automatically from a deleted Linode.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def vendor(self) -> Optional[pulumi.Input[str]]:
        """
        The upstream distribution vendor. Nil for private Images.
        """
        return pulumi.get(self, "vendor")

    @vendor.setter
    def vendor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vendor", value)


class Image(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_init: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk_id: Optional[pulumi.Input[int]] = None,
                 file_hash: Optional[pulumi.Input[str]] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 linode_id: Optional[pulumi.Input[int]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Linode Image resource.  This can be used to create, modify, and delete Linodes Images.  Linode Images are snapshots of a Linode Instance Disk which can then be used to provision more Linode Instances.  Images can be used across regions.

        For more information, see [Linode's documentation on Images](https://www.linode.com/docs/platform/disk-images/linode-images/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/createImage).

        ## Import

        Linodes Images can be imported using the Linode Image `id`, e.g.

        ```sh
        $ pulumi import linode:index/image:Image myimage 1234567
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] cloud_init: Whether this image supports cloud-init.
        :param pulumi.Input[str] description: A detailed description of this Image.
               
               - - -
               
               The following arguments apply to creating an image from an existing Linode Instance:
        :param pulumi.Input[int] disk_id: The ID of the Linode Disk that this Image will be created from.
        :param pulumi.Input[str] file_hash: The MD5 hash of the file to be uploaded. This is used to trigger file updates.
        :param pulumi.Input[str] file_path: The path of the image file to be uploaded.
        :param pulumi.Input[str] label: A short description of the Image. Labels cannot contain special characters.
        :param pulumi.Input[int] linode_id: The ID of the Linode that this Image will be created from.
               
               - - -
               
               > **NOTICE:** Uploading images is currently in beta. Ensure `LINODE_API_VERSION` is set to `v4beta` in order to use this functionality.
               
               The following arguments apply to uploading an image:
        :param pulumi.Input[str] region: The region of the image. See all regions [here](https://api.linode.com/v4/regions).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ImageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Linode Image resource.  This can be used to create, modify, and delete Linodes Images.  Linode Images are snapshots of a Linode Instance Disk which can then be used to provision more Linode Instances.  Images can be used across regions.

        For more information, see [Linode's documentation on Images](https://www.linode.com/docs/platform/disk-images/linode-images/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/createImage).

        ## Import

        Linodes Images can be imported using the Linode Image `id`, e.g.

        ```sh
        $ pulumi import linode:index/image:Image myimage 1234567
        ```

        :param str resource_name: The name of the resource.
        :param ImageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ImageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_init: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk_id: Optional[pulumi.Input[int]] = None,
                 file_hash: Optional[pulumi.Input[str]] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 linode_id: Optional[pulumi.Input[int]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ImageArgs.__new__(ImageArgs)

            __props__.__dict__["cloud_init"] = cloud_init
            __props__.__dict__["description"] = description
            __props__.__dict__["disk_id"] = disk_id
            __props__.__dict__["file_hash"] = file_hash
            __props__.__dict__["file_path"] = file_path
            if label is None and not opts.urn:
                raise TypeError("Missing required property 'label'")
            __props__.__dict__["label"] = label
            __props__.__dict__["linode_id"] = linode_id
            __props__.__dict__["region"] = region
            __props__.__dict__["capabilities"] = None
            __props__.__dict__["created"] = None
            __props__.__dict__["created_by"] = None
            __props__.__dict__["deprecated"] = None
            __props__.__dict__["expiry"] = None
            __props__.__dict__["is_public"] = None
            __props__.__dict__["size"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["vendor"] = None
        super(Image, __self__).__init__(
            'linode:index/image:Image',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            cloud_init: Optional[pulumi.Input[bool]] = None,
            created: Optional[pulumi.Input[str]] = None,
            created_by: Optional[pulumi.Input[str]] = None,
            deprecated: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            disk_id: Optional[pulumi.Input[int]] = None,
            expiry: Optional[pulumi.Input[str]] = None,
            file_hash: Optional[pulumi.Input[str]] = None,
            file_path: Optional[pulumi.Input[str]] = None,
            is_public: Optional[pulumi.Input[bool]] = None,
            label: Optional[pulumi.Input[str]] = None,
            linode_id: Optional[pulumi.Input[int]] = None,
            region: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            status: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            vendor: Optional[pulumi.Input[str]] = None) -> 'Image':
        """
        Get an existing Image resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] capabilities: The capabilities of this Image.
        :param pulumi.Input[bool] cloud_init: Whether this image supports cloud-init.
        :param pulumi.Input[str] created: When this Image was created.
        :param pulumi.Input[str] created_by: The name of the User who created this Image.
        :param pulumi.Input[bool] deprecated: Whether or not this Image is deprecated. Will only be True for deprecated public Images.
        :param pulumi.Input[str] description: A detailed description of this Image.
               
               - - -
               
               The following arguments apply to creating an image from an existing Linode Instance:
        :param pulumi.Input[int] disk_id: The ID of the Linode Disk that this Image will be created from.
        :param pulumi.Input[str] expiry: Only Images created automatically (from a deleted Linode; type=automatic) will expire.
        :param pulumi.Input[str] file_hash: The MD5 hash of the file to be uploaded. This is used to trigger file updates.
        :param pulumi.Input[str] file_path: The path of the image file to be uploaded.
        :param pulumi.Input[bool] is_public: True if the Image is public.
        :param pulumi.Input[str] label: A short description of the Image. Labels cannot contain special characters.
        :param pulumi.Input[int] linode_id: The ID of the Linode that this Image will be created from.
               
               - - -
               
               > **NOTICE:** Uploading images is currently in beta. Ensure `LINODE_API_VERSION` is set to `v4beta` in order to use this functionality.
               
               The following arguments apply to uploading an image:
        :param pulumi.Input[str] region: The region of the image. See all regions [here](https://api.linode.com/v4/regions).
        :param pulumi.Input[int] size: The minimum size this Image needs to deploy. Size is in MB.
        :param pulumi.Input[str] status: The current status of this Image.
        :param pulumi.Input[str] type: How the Image was created. 'Manual' Images can be created at any time. 'Automatic' images are created automatically from a deleted Linode.
        :param pulumi.Input[str] vendor: The upstream distribution vendor. Nil for private Images.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ImageState.__new__(_ImageState)

        __props__.__dict__["capabilities"] = capabilities
        __props__.__dict__["cloud_init"] = cloud_init
        __props__.__dict__["created"] = created
        __props__.__dict__["created_by"] = created_by
        __props__.__dict__["deprecated"] = deprecated
        __props__.__dict__["description"] = description
        __props__.__dict__["disk_id"] = disk_id
        __props__.__dict__["expiry"] = expiry
        __props__.__dict__["file_hash"] = file_hash
        __props__.__dict__["file_path"] = file_path
        __props__.__dict__["is_public"] = is_public
        __props__.__dict__["label"] = label
        __props__.__dict__["linode_id"] = linode_id
        __props__.__dict__["region"] = region
        __props__.__dict__["size"] = size
        __props__.__dict__["status"] = status
        __props__.__dict__["type"] = type
        __props__.__dict__["vendor"] = vendor
        return Image(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def capabilities(self) -> pulumi.Output[Sequence[str]]:
        """
        The capabilities of this Image.
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter(name="cloudInit")
    def cloud_init(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether this image supports cloud-init.
        """
        return pulumi.get(self, "cloud_init")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        When this Image was created.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        The name of the User who created this Image.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def deprecated(self) -> pulumi.Output[bool]:
        """
        Whether or not this Image is deprecated. Will only be True for deprecated public Images.
        """
        return pulumi.get(self, "deprecated")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A detailed description of this Image.

        - - -

        The following arguments apply to creating an image from an existing Linode Instance:
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Output[Optional[int]]:
        """
        The ID of the Linode Disk that this Image will be created from.
        """
        return pulumi.get(self, "disk_id")

    @property
    @pulumi.getter
    def expiry(self) -> pulumi.Output[str]:
        """
        Only Images created automatically (from a deleted Linode; type=automatic) will expire.
        """
        return pulumi.get(self, "expiry")

    @property
    @pulumi.getter(name="fileHash")
    def file_hash(self) -> pulumi.Output[str]:
        """
        The MD5 hash of the file to be uploaded. This is used to trigger file updates.
        """
        return pulumi.get(self, "file_hash")

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> pulumi.Output[Optional[str]]:
        """
        The path of the image file to be uploaded.
        """
        return pulumi.get(self, "file_path")

    @property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> pulumi.Output[bool]:
        """
        True if the Image is public.
        """
        return pulumi.get(self, "is_public")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[str]:
        """
        A short description of the Image. Labels cannot contain special characters.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="linodeId")
    def linode_id(self) -> pulumi.Output[Optional[int]]:
        """
        The ID of the Linode that this Image will be created from.

        - - -

        > **NOTICE:** Uploading images is currently in beta. Ensure `LINODE_API_VERSION` is set to `v4beta` in order to use this functionality.

        The following arguments apply to uploading an image:
        """
        return pulumi.get(self, "linode_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        The region of the image. See all regions [here](https://api.linode.com/v4/regions).
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        The minimum size this Image needs to deploy. Size is in MB.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The current status of this Image.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        How the Image was created. 'Manual' Images can be created at any time. 'Automatic' images are created automatically from a deleted Linode.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def vendor(self) -> pulumi.Output[str]:
        """
        The upstream distribution vendor. Nil for private Images.
        """
        return pulumi.get(self, "vendor")

