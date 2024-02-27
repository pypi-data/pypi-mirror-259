'''
# `google_network_connectivity_spoke`

Refer to the Terraform Registry for docs: [`google_network_connectivity_spoke`](https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class GoogleNetworkConnectivitySpoke(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpoke",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke google_network_connectivity_spoke}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        hub: builtins.str,
        location: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        linked_interconnect_attachments: typing.Optional[typing.Union["GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments", typing.Dict[builtins.str, typing.Any]]] = None,
        linked_router_appliance_instances: typing.Optional[typing.Union["GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances", typing.Dict[builtins.str, typing.Any]]] = None,
        linked_vpc_network: typing.Optional[typing.Union["GoogleNetworkConnectivitySpokeLinkedVpcNetwork", typing.Dict[builtins.str, typing.Any]]] = None,
        linked_vpn_tunnels: typing.Optional[typing.Union["GoogleNetworkConnectivitySpokeLinkedVpnTunnels", typing.Dict[builtins.str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleNetworkConnectivitySpokeTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke google_network_connectivity_spoke} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param hub: Immutable. The URI of the hub that this spoke is attached to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#hub GoogleNetworkConnectivitySpoke#hub}
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#location GoogleNetworkConnectivitySpoke#location}
        :param name: Immutable. The name of the spoke. Spoke names must be unique. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#name GoogleNetworkConnectivitySpoke#name}
        :param description: An optional description of the spoke. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#description GoogleNetworkConnectivitySpoke#description}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#id GoogleNetworkConnectivitySpoke#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Optional labels in key:value format. For more information about labels, see `Requirements for labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements>`_. **Note**: This field is non-authoritative, and will only manage the labels present in your configuration. Please refer to the field ``effective_labels`` for all of the labels present on the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#labels GoogleNetworkConnectivitySpoke#labels}
        :param linked_interconnect_attachments: linked_interconnect_attachments block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#linked_interconnect_attachments GoogleNetworkConnectivitySpoke#linked_interconnect_attachments}
        :param linked_router_appliance_instances: linked_router_appliance_instances block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#linked_router_appliance_instances GoogleNetworkConnectivitySpoke#linked_router_appliance_instances}
        :param linked_vpc_network: linked_vpc_network block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#linked_vpc_network GoogleNetworkConnectivitySpoke#linked_vpc_network}
        :param linked_vpn_tunnels: linked_vpn_tunnels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#linked_vpn_tunnels GoogleNetworkConnectivitySpoke#linked_vpn_tunnels}
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#project GoogleNetworkConnectivitySpoke#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#timeouts GoogleNetworkConnectivitySpoke#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1d765c83109722e07e0f12f2e13b814f5c3737f3196a19ee81de1ea742c92da)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleNetworkConnectivitySpokeConfig(
            hub=hub,
            location=location,
            name=name,
            description=description,
            id=id,
            labels=labels,
            linked_interconnect_attachments=linked_interconnect_attachments,
            linked_router_appliance_instances=linked_router_appliance_instances,
            linked_vpc_network=linked_vpc_network,
            linked_vpn_tunnels=linked_vpn_tunnels,
            project=project,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a GoogleNetworkConnectivitySpoke resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the GoogleNetworkConnectivitySpoke to import.
        :param import_from_id: The id of the existing GoogleNetworkConnectivitySpoke that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the GoogleNetworkConnectivitySpoke to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd6f2cec2033b842676b3cf7aaa8ecc73abd348b59021bcbcb54c14beb92eae1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putLinkedInterconnectAttachments")
    def put_linked_interconnect_attachments(
        self,
        *,
        site_to_site_data_transfer: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        uris: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#site_to_site_data_transfer GoogleNetworkConnectivitySpoke#site_to_site_data_transfer}
        :param uris: The URIs of linked interconnect attachment resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#uris GoogleNetworkConnectivitySpoke#uris}
        '''
        value = GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments(
            site_to_site_data_transfer=site_to_site_data_transfer, uris=uris
        )

        return typing.cast(None, jsii.invoke(self, "putLinkedInterconnectAttachments", [value]))

    @jsii.member(jsii_name="putLinkedRouterApplianceInstances")
    def put_linked_router_appliance_instances(
        self,
        *,
        instances: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances", typing.Dict[builtins.str, typing.Any]]]],
        site_to_site_data_transfer: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param instances: instances block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#instances GoogleNetworkConnectivitySpoke#instances}
        :param site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#site_to_site_data_transfer GoogleNetworkConnectivitySpoke#site_to_site_data_transfer}
        '''
        value = GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances(
            instances=instances, site_to_site_data_transfer=site_to_site_data_transfer
        )

        return typing.cast(None, jsii.invoke(self, "putLinkedRouterApplianceInstances", [value]))

    @jsii.member(jsii_name="putLinkedVpcNetwork")
    def put_linked_vpc_network(
        self,
        *,
        uri: builtins.str,
        exclude_export_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param uri: The URI of the VPC network resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#uri GoogleNetworkConnectivitySpoke#uri}
        :param exclude_export_ranges: IP ranges encompassing the subnets to be excluded from peering. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#exclude_export_ranges GoogleNetworkConnectivitySpoke#exclude_export_ranges}
        '''
        value = GoogleNetworkConnectivitySpokeLinkedVpcNetwork(
            uri=uri, exclude_export_ranges=exclude_export_ranges
        )

        return typing.cast(None, jsii.invoke(self, "putLinkedVpcNetwork", [value]))

    @jsii.member(jsii_name="putLinkedVpnTunnels")
    def put_linked_vpn_tunnels(
        self,
        *,
        site_to_site_data_transfer: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        uris: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#site_to_site_data_transfer GoogleNetworkConnectivitySpoke#site_to_site_data_transfer}
        :param uris: The URIs of linked VPN tunnel resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#uris GoogleNetworkConnectivitySpoke#uris}
        '''
        value = GoogleNetworkConnectivitySpokeLinkedVpnTunnels(
            site_to_site_data_transfer=site_to_site_data_transfer, uris=uris
        )

        return typing.cast(None, jsii.invoke(self, "putLinkedVpnTunnels", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#create GoogleNetworkConnectivitySpoke#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#delete GoogleNetworkConnectivitySpoke#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#update GoogleNetworkConnectivitySpoke#update}.
        '''
        value = GoogleNetworkConnectivitySpokeTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLinkedInterconnectAttachments")
    def reset_linked_interconnect_attachments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedInterconnectAttachments", []))

    @jsii.member(jsii_name="resetLinkedRouterApplianceInstances")
    def reset_linked_router_appliance_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedRouterApplianceInstances", []))

    @jsii.member(jsii_name="resetLinkedVpcNetwork")
    def reset_linked_vpc_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedVpcNetwork", []))

    @jsii.member(jsii_name="resetLinkedVpnTunnels")
    def reset_linked_vpn_tunnels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedVpnTunnels", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="effectiveLabels")
    def effective_labels(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "effectiveLabels"))

    @builtins.property
    @jsii.member(jsii_name="linkedInterconnectAttachments")
    def linked_interconnect_attachments(
        self,
    ) -> "GoogleNetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference":
        return typing.cast("GoogleNetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference", jsii.get(self, "linkedInterconnectAttachments"))

    @builtins.property
    @jsii.member(jsii_name="linkedRouterApplianceInstances")
    def linked_router_appliance_instances(
        self,
    ) -> "GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference":
        return typing.cast("GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference", jsii.get(self, "linkedRouterApplianceInstances"))

    @builtins.property
    @jsii.member(jsii_name="linkedVpcNetwork")
    def linked_vpc_network(
        self,
    ) -> "GoogleNetworkConnectivitySpokeLinkedVpcNetworkOutputReference":
        return typing.cast("GoogleNetworkConnectivitySpokeLinkedVpcNetworkOutputReference", jsii.get(self, "linkedVpcNetwork"))

    @builtins.property
    @jsii.member(jsii_name="linkedVpnTunnels")
    def linked_vpn_tunnels(
        self,
    ) -> "GoogleNetworkConnectivitySpokeLinkedVpnTunnelsOutputReference":
        return typing.cast("GoogleNetworkConnectivitySpokeLinkedVpnTunnelsOutputReference", jsii.get(self, "linkedVpnTunnels"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="terraformLabels")
    def terraform_labels(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "terraformLabels"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleNetworkConnectivitySpokeTimeoutsOutputReference":
        return typing.cast("GoogleNetworkConnectivitySpokeTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uniqueId")
    def unique_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uniqueId"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hubInput")
    def hub_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hubInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedInterconnectAttachmentsInput")
    def linked_interconnect_attachments_input(
        self,
    ) -> typing.Optional["GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments"]:
        return typing.cast(typing.Optional["GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments"], jsii.get(self, "linkedInterconnectAttachmentsInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedRouterApplianceInstancesInput")
    def linked_router_appliance_instances_input(
        self,
    ) -> typing.Optional["GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances"]:
        return typing.cast(typing.Optional["GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances"], jsii.get(self, "linkedRouterApplianceInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedVpcNetworkInput")
    def linked_vpc_network_input(
        self,
    ) -> typing.Optional["GoogleNetworkConnectivitySpokeLinkedVpcNetwork"]:
        return typing.cast(typing.Optional["GoogleNetworkConnectivitySpokeLinkedVpcNetwork"], jsii.get(self, "linkedVpcNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedVpnTunnelsInput")
    def linked_vpn_tunnels_input(
        self,
    ) -> typing.Optional["GoogleNetworkConnectivitySpokeLinkedVpnTunnels"]:
        return typing.cast(typing.Optional["GoogleNetworkConnectivitySpokeLinkedVpnTunnels"], jsii.get(self, "linkedVpnTunnelsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "GoogleNetworkConnectivitySpokeTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "GoogleNetworkConnectivitySpokeTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7507719d0eb3a6eca77f236db6a53ada158f2125de9396848ff15c01617f045e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="hub")
    def hub(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hub"))

    @hub.setter
    def hub(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1656b3d1cc9625eff6869dc3e0ad6450d917c6feac56f2ecec0f357869ad5f8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hub", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f07aa5efb59ac8a34f56035cd2e04188349eaf2a379910b7a68b7f3da1987b8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e981d97825d3a0524733853b74e7055570ac5f73e332ff41e9894c8ffcdb695)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa696cf8ebdb45a433ba752003d8e8c0895922df5de5a39980d34dbfc567832e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70c03fbe245c20d14ec398f7fa8c833da22825908b7239359e4c0f54e16a2471)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__657129d20c34a3938839ca8ea30d41013839ee5d2b42e707b77666ba6b841211)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "hub": "hub",
        "location": "location",
        "name": "name",
        "description": "description",
        "id": "id",
        "labels": "labels",
        "linked_interconnect_attachments": "linkedInterconnectAttachments",
        "linked_router_appliance_instances": "linkedRouterApplianceInstances",
        "linked_vpc_network": "linkedVpcNetwork",
        "linked_vpn_tunnels": "linkedVpnTunnels",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleNetworkConnectivitySpokeConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        hub: builtins.str,
        location: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        linked_interconnect_attachments: typing.Optional[typing.Union["GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments", typing.Dict[builtins.str, typing.Any]]] = None,
        linked_router_appliance_instances: typing.Optional[typing.Union["GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances", typing.Dict[builtins.str, typing.Any]]] = None,
        linked_vpc_network: typing.Optional[typing.Union["GoogleNetworkConnectivitySpokeLinkedVpcNetwork", typing.Dict[builtins.str, typing.Any]]] = None,
        linked_vpn_tunnels: typing.Optional[typing.Union["GoogleNetworkConnectivitySpokeLinkedVpnTunnels", typing.Dict[builtins.str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleNetworkConnectivitySpokeTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param hub: Immutable. The URI of the hub that this spoke is attached to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#hub GoogleNetworkConnectivitySpoke#hub}
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#location GoogleNetworkConnectivitySpoke#location}
        :param name: Immutable. The name of the spoke. Spoke names must be unique. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#name GoogleNetworkConnectivitySpoke#name}
        :param description: An optional description of the spoke. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#description GoogleNetworkConnectivitySpoke#description}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#id GoogleNetworkConnectivitySpoke#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Optional labels in key:value format. For more information about labels, see `Requirements for labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements>`_. **Note**: This field is non-authoritative, and will only manage the labels present in your configuration. Please refer to the field ``effective_labels`` for all of the labels present on the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#labels GoogleNetworkConnectivitySpoke#labels}
        :param linked_interconnect_attachments: linked_interconnect_attachments block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#linked_interconnect_attachments GoogleNetworkConnectivitySpoke#linked_interconnect_attachments}
        :param linked_router_appliance_instances: linked_router_appliance_instances block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#linked_router_appliance_instances GoogleNetworkConnectivitySpoke#linked_router_appliance_instances}
        :param linked_vpc_network: linked_vpc_network block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#linked_vpc_network GoogleNetworkConnectivitySpoke#linked_vpc_network}
        :param linked_vpn_tunnels: linked_vpn_tunnels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#linked_vpn_tunnels GoogleNetworkConnectivitySpoke#linked_vpn_tunnels}
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#project GoogleNetworkConnectivitySpoke#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#timeouts GoogleNetworkConnectivitySpoke#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(linked_interconnect_attachments, dict):
            linked_interconnect_attachments = GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments(**linked_interconnect_attachments)
        if isinstance(linked_router_appliance_instances, dict):
            linked_router_appliance_instances = GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances(**linked_router_appliance_instances)
        if isinstance(linked_vpc_network, dict):
            linked_vpc_network = GoogleNetworkConnectivitySpokeLinkedVpcNetwork(**linked_vpc_network)
        if isinstance(linked_vpn_tunnels, dict):
            linked_vpn_tunnels = GoogleNetworkConnectivitySpokeLinkedVpnTunnels(**linked_vpn_tunnels)
        if isinstance(timeouts, dict):
            timeouts = GoogleNetworkConnectivitySpokeTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb03f121aaadb4d699bca0a4d893ea2ce660da50f878340b0aad22da142939a5)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument hub", value=hub, expected_type=type_hints["hub"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument linked_interconnect_attachments", value=linked_interconnect_attachments, expected_type=type_hints["linked_interconnect_attachments"])
            check_type(argname="argument linked_router_appliance_instances", value=linked_router_appliance_instances, expected_type=type_hints["linked_router_appliance_instances"])
            check_type(argname="argument linked_vpc_network", value=linked_vpc_network, expected_type=type_hints["linked_vpc_network"])
            check_type(argname="argument linked_vpn_tunnels", value=linked_vpn_tunnels, expected_type=type_hints["linked_vpn_tunnels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hub": hub,
            "location": location,
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if linked_interconnect_attachments is not None:
            self._values["linked_interconnect_attachments"] = linked_interconnect_attachments
        if linked_router_appliance_instances is not None:
            self._values["linked_router_appliance_instances"] = linked_router_appliance_instances
        if linked_vpc_network is not None:
            self._values["linked_vpc_network"] = linked_vpc_network
        if linked_vpn_tunnels is not None:
            self._values["linked_vpn_tunnels"] = linked_vpn_tunnels
        if project is not None:
            self._values["project"] = project
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def hub(self) -> builtins.str:
        '''Immutable. The URI of the hub that this spoke is attached to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#hub GoogleNetworkConnectivitySpoke#hub}
        '''
        result = self._values.get("hub")
        assert result is not None, "Required property 'hub' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The location for the resource.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#location GoogleNetworkConnectivitySpoke#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Immutable. The name of the spoke. Spoke names must be unique.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#name GoogleNetworkConnectivitySpoke#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the spoke.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#description GoogleNetworkConnectivitySpoke#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#id GoogleNetworkConnectivitySpoke#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional labels in key:value format. For more information about labels, see `Requirements for labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements>`_.

        **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
        Please refer to the field ``effective_labels`` for all of the labels present on the resource.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#labels GoogleNetworkConnectivitySpoke#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def linked_interconnect_attachments(
        self,
    ) -> typing.Optional["GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments"]:
        '''linked_interconnect_attachments block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#linked_interconnect_attachments GoogleNetworkConnectivitySpoke#linked_interconnect_attachments}
        '''
        result = self._values.get("linked_interconnect_attachments")
        return typing.cast(typing.Optional["GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments"], result)

    @builtins.property
    def linked_router_appliance_instances(
        self,
    ) -> typing.Optional["GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances"]:
        '''linked_router_appliance_instances block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#linked_router_appliance_instances GoogleNetworkConnectivitySpoke#linked_router_appliance_instances}
        '''
        result = self._values.get("linked_router_appliance_instances")
        return typing.cast(typing.Optional["GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances"], result)

    @builtins.property
    def linked_vpc_network(
        self,
    ) -> typing.Optional["GoogleNetworkConnectivitySpokeLinkedVpcNetwork"]:
        '''linked_vpc_network block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#linked_vpc_network GoogleNetworkConnectivitySpoke#linked_vpc_network}
        '''
        result = self._values.get("linked_vpc_network")
        return typing.cast(typing.Optional["GoogleNetworkConnectivitySpokeLinkedVpcNetwork"], result)

    @builtins.property
    def linked_vpn_tunnels(
        self,
    ) -> typing.Optional["GoogleNetworkConnectivitySpokeLinkedVpnTunnels"]:
        '''linked_vpn_tunnels block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#linked_vpn_tunnels GoogleNetworkConnectivitySpoke#linked_vpn_tunnels}
        '''
        result = self._values.get("linked_vpn_tunnels")
        return typing.cast(typing.Optional["GoogleNetworkConnectivitySpokeLinkedVpnTunnels"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project for the resource.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#project GoogleNetworkConnectivitySpoke#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleNetworkConnectivitySpokeTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#timeouts GoogleNetworkConnectivitySpoke#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleNetworkConnectivitySpokeTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNetworkConnectivitySpokeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments",
    jsii_struct_bases=[],
    name_mapping={
        "site_to_site_data_transfer": "siteToSiteDataTransfer",
        "uris": "uris",
    },
)
class GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments:
    def __init__(
        self,
        *,
        site_to_site_data_transfer: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        uris: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#site_to_site_data_transfer GoogleNetworkConnectivitySpoke#site_to_site_data_transfer}
        :param uris: The URIs of linked interconnect attachment resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#uris GoogleNetworkConnectivitySpoke#uris}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d09ed0cb325f7833c5c08ee531410e1f41854289ca60665f726edddecd3cebd)
            check_type(argname="argument site_to_site_data_transfer", value=site_to_site_data_transfer, expected_type=type_hints["site_to_site_data_transfer"])
            check_type(argname="argument uris", value=uris, expected_type=type_hints["uris"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "site_to_site_data_transfer": site_to_site_data_transfer,
            "uris": uris,
        }

    @builtins.property
    def site_to_site_data_transfer(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''A value that controls whether site-to-site data transfer is enabled for these resources.

        Note that data transfer is available only in supported locations.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#site_to_site_data_transfer GoogleNetworkConnectivitySpoke#site_to_site_data_transfer}
        '''
        result = self._values.get("site_to_site_data_transfer")
        assert result is not None, "Required property 'site_to_site_data_transfer' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def uris(self) -> typing.List[builtins.str]:
        '''The URIs of linked interconnect attachment resources.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#uris GoogleNetworkConnectivitySpoke#uris}
        '''
        result = self._values.get("uris")
        assert result is not None, "Required property 'uris' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b888f62db622fcee1ede9b3d89c4229328953f63cbd48182e09794e762d66dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="siteToSiteDataTransferInput")
    def site_to_site_data_transfer_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "siteToSiteDataTransferInput"))

    @builtins.property
    @jsii.member(jsii_name="urisInput")
    def uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "urisInput"))

    @builtins.property
    @jsii.member(jsii_name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "siteToSiteDataTransfer"))

    @site_to_site_data_transfer.setter
    def site_to_site_data_transfer(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c6e01d5f14b62e6325721791e4b551453ee413c1cba7a3aacf582dcb0cb739d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteToSiteDataTransfer", value)

    @builtins.property
    @jsii.member(jsii_name="uris")
    def uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "uris"))

    @uris.setter
    def uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f051558cc551a20dde0deeebe385b2d2129ea6137c3ca6a45bbb2890109ae35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uris", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments]:
        return typing.cast(typing.Optional[GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12377a6fe46e9cf592efbf33fa55c738d03492692f19219f6b393aa460cb6865)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances",
    jsii_struct_bases=[],
    name_mapping={
        "instances": "instances",
        "site_to_site_data_transfer": "siteToSiteDataTransfer",
    },
)
class GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances:
    def __init__(
        self,
        *,
        instances: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances", typing.Dict[builtins.str, typing.Any]]]],
        site_to_site_data_transfer: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param instances: instances block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#instances GoogleNetworkConnectivitySpoke#instances}
        :param site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#site_to_site_data_transfer GoogleNetworkConnectivitySpoke#site_to_site_data_transfer}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__924d9868829041834999bff7546712b74713ea2cc4d8ea871f460df5908337a4)
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument site_to_site_data_transfer", value=site_to_site_data_transfer, expected_type=type_hints["site_to_site_data_transfer"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instances": instances,
            "site_to_site_data_transfer": site_to_site_data_transfer,
        }

    @builtins.property
    def instances(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances"]]:
        '''instances block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#instances GoogleNetworkConnectivitySpoke#instances}
        '''
        result = self._values.get("instances")
        assert result is not None, "Required property 'instances' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances"]], result)

    @builtins.property
    def site_to_site_data_transfer(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''A value that controls whether site-to-site data transfer is enabled for these resources.

        Note that data transfer is available only in supported locations.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#site_to_site_data_transfer GoogleNetworkConnectivitySpoke#site_to_site_data_transfer}
        '''
        result = self._values.get("site_to_site_data_transfer")
        assert result is not None, "Required property 'site_to_site_data_transfer' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances",
    jsii_struct_bases=[],
    name_mapping={"ip_address": "ipAddress", "virtual_machine": "virtualMachine"},
)
class GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances:
    def __init__(
        self,
        *,
        ip_address: typing.Optional[builtins.str] = None,
        virtual_machine: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ip_address: The IP address on the VM to use for peering. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#ip_address GoogleNetworkConnectivitySpoke#ip_address}
        :param virtual_machine: The URI of the virtual machine resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#virtual_machine GoogleNetworkConnectivitySpoke#virtual_machine}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30f0730970e86a29f673da11c057278a717667775f661875938812d0797869db)
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument virtual_machine", value=virtual_machine, expected_type=type_hints["virtual_machine"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if virtual_machine is not None:
            self._values["virtual_machine"] = virtual_machine

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''The IP address on the VM to use for peering.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#ip_address GoogleNetworkConnectivitySpoke#ip_address}
        '''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_machine(self) -> typing.Optional[builtins.str]:
        '''The URI of the virtual machine resource.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#virtual_machine GoogleNetworkConnectivitySpoke#virtual_machine}
        '''
        result = self._values.get("virtual_machine")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__089054c026513ef193cea9cfbc6d89bf489b6a88dc4703d40b9b19a39d9bc787)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c65ececce95fddcba78ed939b7cf340181a0e5060e397f0ddadcf3eef4b08f0d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48c66623fed153b40d60d86e5c3095887b9a2215d62985cd59e23e186a7346c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b90b453ad7a1603065fd0a4ec11916e2e9a16afc0c2089905839d153b400baf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fc9d26fefd746ea3ca8133de1c8f2681ed0ef3b3826efa1fe1f4c48a2e6fc6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c6c096d4116e255f79cc80d97b4d88841150b2bbd5a75268a00e190ee290738)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e76d6b3825ca12d7548d986557d15c8393892a2380f5ab57224b79f5a85a09e6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIpAddress")
    def reset_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddress", []))

    @jsii.member(jsii_name="resetVirtualMachine")
    def reset_virtual_machine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualMachine", []))

    @builtins.property
    @jsii.member(jsii_name="ipAddressInput")
    def ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineInput")
    def virtual_machine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualMachineInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e982ac8c771afd32806061f4415974408419b04bc3877e8d247f364ed983d31c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="virtualMachine")
    def virtual_machine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachine"))

    @virtual_machine.setter
    def virtual_machine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7439774d9467087ae321bd5a38bd699d02b8f9f642fef2da1009f9d257cf24aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualMachine", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1656ccad117e0a78a0b9083f94325849bbe192b23785cc111154acf20bcd6ea0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd3a622b9322b6685e05fb2c589b17b803fc32eb29fa0a0a4050605ded7e811a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInstances")
    def put_instances(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15e0cde88878856d61a92e273a4f727af5531d0514dfb27ccb20389aaafbffc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInstances", [value]))

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(
        self,
    ) -> GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList:
        return typing.cast(GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList, jsii.get(self, "instances"))

    @builtins.property
    @jsii.member(jsii_name="instancesInput")
    def instances_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]]], jsii.get(self, "instancesInput"))

    @builtins.property
    @jsii.member(jsii_name="siteToSiteDataTransferInput")
    def site_to_site_data_transfer_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "siteToSiteDataTransferInput"))

    @builtins.property
    @jsii.member(jsii_name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "siteToSiteDataTransfer"))

    @site_to_site_data_transfer.setter
    def site_to_site_data_transfer(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d339ff4868ff26f86d998d4b0471928e51ab3d9985932fa22bc2e286a668e60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteToSiteDataTransfer", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances]:
        return typing.cast(typing.Optional[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd9a960a30827f2c204ba40815380ea9e051153a715cc2278a808373a63d9ab9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeLinkedVpcNetwork",
    jsii_struct_bases=[],
    name_mapping={"uri": "uri", "exclude_export_ranges": "excludeExportRanges"},
)
class GoogleNetworkConnectivitySpokeLinkedVpcNetwork:
    def __init__(
        self,
        *,
        uri: builtins.str,
        exclude_export_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param uri: The URI of the VPC network resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#uri GoogleNetworkConnectivitySpoke#uri}
        :param exclude_export_ranges: IP ranges encompassing the subnets to be excluded from peering. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#exclude_export_ranges GoogleNetworkConnectivitySpoke#exclude_export_ranges}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bda1eb075c06e45f85c6f4bac9678acb44008ade15be6b0a1a49a6b2ce0e3e83)
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument exclude_export_ranges", value=exclude_export_ranges, expected_type=type_hints["exclude_export_ranges"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "uri": uri,
        }
        if exclude_export_ranges is not None:
            self._values["exclude_export_ranges"] = exclude_export_ranges

    @builtins.property
    def uri(self) -> builtins.str:
        '''The URI of the VPC network resource.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#uri GoogleNetworkConnectivitySpoke#uri}
        '''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclude_export_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''IP ranges encompassing the subnets to be excluded from peering.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#exclude_export_ranges GoogleNetworkConnectivitySpoke#exclude_export_ranges}
        '''
        result = self._values.get("exclude_export_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNetworkConnectivitySpokeLinkedVpcNetwork(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNetworkConnectivitySpokeLinkedVpcNetworkOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeLinkedVpcNetworkOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bd974df66db67219287e70bc966d6de8a4666f335a51e4ad86b0be94f72719f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExcludeExportRanges")
    def reset_exclude_export_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeExportRanges", []))

    @builtins.property
    @jsii.member(jsii_name="excludeExportRangesInput")
    def exclude_export_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludeExportRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeExportRanges")
    def exclude_export_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludeExportRanges"))

    @exclude_export_ranges.setter
    def exclude_export_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__256846fb6d2c7120144fc1065b9edf834aeaa32f67da96068692bc2d0da31873)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeExportRanges", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff60a9ff95389d6f149315a86fd599553ed3b757a61ed06fbcc05ee372e8bd6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleNetworkConnectivitySpokeLinkedVpcNetwork]:
        return typing.cast(typing.Optional[GoogleNetworkConnectivitySpokeLinkedVpcNetwork], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNetworkConnectivitySpokeLinkedVpcNetwork],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__121d0b8f2e7c5e17ff21bce318ad5cc05dbf3338f86a33300f4409746d0fbfa6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeLinkedVpnTunnels",
    jsii_struct_bases=[],
    name_mapping={
        "site_to_site_data_transfer": "siteToSiteDataTransfer",
        "uris": "uris",
    },
)
class GoogleNetworkConnectivitySpokeLinkedVpnTunnels:
    def __init__(
        self,
        *,
        site_to_site_data_transfer: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        uris: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param site_to_site_data_transfer: A value that controls whether site-to-site data transfer is enabled for these resources. Note that data transfer is available only in supported locations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#site_to_site_data_transfer GoogleNetworkConnectivitySpoke#site_to_site_data_transfer}
        :param uris: The URIs of linked VPN tunnel resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#uris GoogleNetworkConnectivitySpoke#uris}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2074bb640101f62effba86b083efbbdfc5bf13bcf2764377035867e05cff5803)
            check_type(argname="argument site_to_site_data_transfer", value=site_to_site_data_transfer, expected_type=type_hints["site_to_site_data_transfer"])
            check_type(argname="argument uris", value=uris, expected_type=type_hints["uris"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "site_to_site_data_transfer": site_to_site_data_transfer,
            "uris": uris,
        }

    @builtins.property
    def site_to_site_data_transfer(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''A value that controls whether site-to-site data transfer is enabled for these resources.

        Note that data transfer is available only in supported locations.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#site_to_site_data_transfer GoogleNetworkConnectivitySpoke#site_to_site_data_transfer}
        '''
        result = self._values.get("site_to_site_data_transfer")
        assert result is not None, "Required property 'site_to_site_data_transfer' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def uris(self) -> typing.List[builtins.str]:
        '''The URIs of linked VPN tunnel resources.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#uris GoogleNetworkConnectivitySpoke#uris}
        '''
        result = self._values.get("uris")
        assert result is not None, "Required property 'uris' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNetworkConnectivitySpokeLinkedVpnTunnels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNetworkConnectivitySpokeLinkedVpnTunnelsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeLinkedVpnTunnelsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5e03b458ef16e509159c5721e328907129cac779dac33fbda3a62eb96582b34)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="siteToSiteDataTransferInput")
    def site_to_site_data_transfer_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "siteToSiteDataTransferInput"))

    @builtins.property
    @jsii.member(jsii_name="urisInput")
    def uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "urisInput"))

    @builtins.property
    @jsii.member(jsii_name="siteToSiteDataTransfer")
    def site_to_site_data_transfer(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "siteToSiteDataTransfer"))

    @site_to_site_data_transfer.setter
    def site_to_site_data_transfer(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd653bc7c6aa63fd89148e208f05a354f3855a9df8c2bf2ffe71569e75513bd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteToSiteDataTransfer", value)

    @builtins.property
    @jsii.member(jsii_name="uris")
    def uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "uris"))

    @uris.setter
    def uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbcc5bbe4edb2c49dfcee8b393b006ed469f85fdb058195a5eec2c54cd463b24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uris", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleNetworkConnectivitySpokeLinkedVpnTunnels]:
        return typing.cast(typing.Optional[GoogleNetworkConnectivitySpokeLinkedVpnTunnels], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleNetworkConnectivitySpokeLinkedVpnTunnels],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f92dbd44688915939db21a72a35b439d8787dabe457d450c8516b11015a37431)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleNetworkConnectivitySpokeTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#create GoogleNetworkConnectivitySpoke#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#delete GoogleNetworkConnectivitySpoke#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#update GoogleNetworkConnectivitySpoke#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c1d634f27c18788e87a2d8dd228806e9c7f4edbd081b96036317446c27828e1)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#create GoogleNetworkConnectivitySpoke#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#delete GoogleNetworkConnectivitySpoke#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_network_connectivity_spoke#update GoogleNetworkConnectivitySpoke#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleNetworkConnectivitySpokeTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleNetworkConnectivitySpokeTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleNetworkConnectivitySpoke.GoogleNetworkConnectivitySpokeTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9497a8eadc2ce1373c1d5885ea54eb9cd27753560397bf1ee43276c87932ab2d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1754f7b134f5132f1627a43efd9395aeb3656fa6891b86036dd18e320e7eda12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9d93b29b2d3504df5cda0256a55c15853c57237d9a074bee1a5a5e120187bda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c494bbb4056f4fc21acb71fef3062d07fe4fec5a3122d07611de9f47d60032e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleNetworkConnectivitySpokeTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleNetworkConnectivitySpokeTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleNetworkConnectivitySpokeTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f334c61ca5877e3c8f55ddaa283b84c90e2272730285acadbe9599bd7ab423ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleNetworkConnectivitySpoke",
    "GoogleNetworkConnectivitySpokeConfig",
    "GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments",
    "GoogleNetworkConnectivitySpokeLinkedInterconnectAttachmentsOutputReference",
    "GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances",
    "GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances",
    "GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesList",
    "GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstancesOutputReference",
    "GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesOutputReference",
    "GoogleNetworkConnectivitySpokeLinkedVpcNetwork",
    "GoogleNetworkConnectivitySpokeLinkedVpcNetworkOutputReference",
    "GoogleNetworkConnectivitySpokeLinkedVpnTunnels",
    "GoogleNetworkConnectivitySpokeLinkedVpnTunnelsOutputReference",
    "GoogleNetworkConnectivitySpokeTimeouts",
    "GoogleNetworkConnectivitySpokeTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__b1d765c83109722e07e0f12f2e13b814f5c3737f3196a19ee81de1ea742c92da(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    hub: builtins.str,
    location: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    linked_interconnect_attachments: typing.Optional[typing.Union[GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments, typing.Dict[builtins.str, typing.Any]]] = None,
    linked_router_appliance_instances: typing.Optional[typing.Union[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances, typing.Dict[builtins.str, typing.Any]]] = None,
    linked_vpc_network: typing.Optional[typing.Union[GoogleNetworkConnectivitySpokeLinkedVpcNetwork, typing.Dict[builtins.str, typing.Any]]] = None,
    linked_vpn_tunnels: typing.Optional[typing.Union[GoogleNetworkConnectivitySpokeLinkedVpnTunnels, typing.Dict[builtins.str, typing.Any]]] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleNetworkConnectivitySpokeTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd6f2cec2033b842676b3cf7aaa8ecc73abd348b59021bcbcb54c14beb92eae1(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7507719d0eb3a6eca77f236db6a53ada158f2125de9396848ff15c01617f045e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1656b3d1cc9625eff6869dc3e0ad6450d917c6feac56f2ecec0f357869ad5f8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f07aa5efb59ac8a34f56035cd2e04188349eaf2a379910b7a68b7f3da1987b8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e981d97825d3a0524733853b74e7055570ac5f73e332ff41e9894c8ffcdb695(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa696cf8ebdb45a433ba752003d8e8c0895922df5de5a39980d34dbfc567832e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70c03fbe245c20d14ec398f7fa8c833da22825908b7239359e4c0f54e16a2471(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__657129d20c34a3938839ca8ea30d41013839ee5d2b42e707b77666ba6b841211(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb03f121aaadb4d699bca0a4d893ea2ce660da50f878340b0aad22da142939a5(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    hub: builtins.str,
    location: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    linked_interconnect_attachments: typing.Optional[typing.Union[GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments, typing.Dict[builtins.str, typing.Any]]] = None,
    linked_router_appliance_instances: typing.Optional[typing.Union[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances, typing.Dict[builtins.str, typing.Any]]] = None,
    linked_vpc_network: typing.Optional[typing.Union[GoogleNetworkConnectivitySpokeLinkedVpcNetwork, typing.Dict[builtins.str, typing.Any]]] = None,
    linked_vpn_tunnels: typing.Optional[typing.Union[GoogleNetworkConnectivitySpokeLinkedVpnTunnels, typing.Dict[builtins.str, typing.Any]]] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleNetworkConnectivitySpokeTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d09ed0cb325f7833c5c08ee531410e1f41854289ca60665f726edddecd3cebd(
    *,
    site_to_site_data_transfer: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    uris: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b888f62db622fcee1ede9b3d89c4229328953f63cbd48182e09794e762d66dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c6e01d5f14b62e6325721791e4b551453ee413c1cba7a3aacf582dcb0cb739d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f051558cc551a20dde0deeebe385b2d2129ea6137c3ca6a45bbb2890109ae35(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12377a6fe46e9cf592efbf33fa55c738d03492692f19219f6b393aa460cb6865(
    value: typing.Optional[GoogleNetworkConnectivitySpokeLinkedInterconnectAttachments],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__924d9868829041834999bff7546712b74713ea2cc4d8ea871f460df5908337a4(
    *,
    instances: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances, typing.Dict[builtins.str, typing.Any]]]],
    site_to_site_data_transfer: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30f0730970e86a29f673da11c057278a717667775f661875938812d0797869db(
    *,
    ip_address: typing.Optional[builtins.str] = None,
    virtual_machine: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__089054c026513ef193cea9cfbc6d89bf489b6a88dc4703d40b9b19a39d9bc787(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c65ececce95fddcba78ed939b7cf340181a0e5060e397f0ddadcf3eef4b08f0d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48c66623fed153b40d60d86e5c3095887b9a2215d62985cd59e23e186a7346c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b90b453ad7a1603065fd0a4ec11916e2e9a16afc0c2089905839d153b400baf0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fc9d26fefd746ea3ca8133de1c8f2681ed0ef3b3826efa1fe1f4c48a2e6fc6c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c6c096d4116e255f79cc80d97b4d88841150b2bbd5a75268a00e190ee290738(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e76d6b3825ca12d7548d986557d15c8393892a2380f5ab57224b79f5a85a09e6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e982ac8c771afd32806061f4415974408419b04bc3877e8d247f364ed983d31c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7439774d9467087ae321bd5a38bd699d02b8f9f642fef2da1009f9d257cf24aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1656ccad117e0a78a0b9083f94325849bbe192b23785cc111154acf20bcd6ea0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd3a622b9322b6685e05fb2c589b17b803fc32eb29fa0a0a4050605ded7e811a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15e0cde88878856d61a92e273a4f727af5531d0514dfb27ccb20389aaafbffc2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstancesInstances, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d339ff4868ff26f86d998d4b0471928e51ab3d9985932fa22bc2e286a668e60(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd9a960a30827f2c204ba40815380ea9e051153a715cc2278a808373a63d9ab9(
    value: typing.Optional[GoogleNetworkConnectivitySpokeLinkedRouterApplianceInstances],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bda1eb075c06e45f85c6f4bac9678acb44008ade15be6b0a1a49a6b2ce0e3e83(
    *,
    uri: builtins.str,
    exclude_export_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bd974df66db67219287e70bc966d6de8a4666f335a51e4ad86b0be94f72719f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__256846fb6d2c7120144fc1065b9edf834aeaa32f67da96068692bc2d0da31873(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff60a9ff95389d6f149315a86fd599553ed3b757a61ed06fbcc05ee372e8bd6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__121d0b8f2e7c5e17ff21bce318ad5cc05dbf3338f86a33300f4409746d0fbfa6(
    value: typing.Optional[GoogleNetworkConnectivitySpokeLinkedVpcNetwork],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2074bb640101f62effba86b083efbbdfc5bf13bcf2764377035867e05cff5803(
    *,
    site_to_site_data_transfer: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    uris: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5e03b458ef16e509159c5721e328907129cac779dac33fbda3a62eb96582b34(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd653bc7c6aa63fd89148e208f05a354f3855a9df8c2bf2ffe71569e75513bd7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbcc5bbe4edb2c49dfcee8b393b006ed469f85fdb058195a5eec2c54cd463b24(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f92dbd44688915939db21a72a35b439d8787dabe457d450c8516b11015a37431(
    value: typing.Optional[GoogleNetworkConnectivitySpokeLinkedVpnTunnels],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c1d634f27c18788e87a2d8dd228806e9c7f4edbd081b96036317446c27828e1(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9497a8eadc2ce1373c1d5885ea54eb9cd27753560397bf1ee43276c87932ab2d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1754f7b134f5132f1627a43efd9395aeb3656fa6891b86036dd18e320e7eda12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9d93b29b2d3504df5cda0256a55c15853c57237d9a074bee1a5a5e120187bda(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c494bbb4056f4fc21acb71fef3062d07fe4fec5a3122d07611de9f47d60032e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f334c61ca5877e3c8f55ddaa283b84c90e2272730285acadbe9599bd7ab423ed(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleNetworkConnectivitySpokeTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
