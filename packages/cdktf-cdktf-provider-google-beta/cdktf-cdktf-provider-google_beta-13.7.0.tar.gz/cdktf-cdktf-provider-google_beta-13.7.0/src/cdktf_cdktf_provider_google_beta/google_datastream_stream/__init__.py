'''
# `google_datastream_stream`

Refer to the Terraform Registry for docs: [`google_datastream_stream`](https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream).
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


class GoogleDatastreamStream(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStream",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream google_datastream_stream}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        destination_config: typing.Union["GoogleDatastreamStreamDestinationConfig", typing.Dict[builtins.str, typing.Any]],
        display_name: builtins.str,
        location: builtins.str,
        source_config: typing.Union["GoogleDatastreamStreamSourceConfig", typing.Dict[builtins.str, typing.Any]],
        stream_id: builtins.str,
        backfill_all: typing.Optional[typing.Union["GoogleDatastreamStreamBackfillAll", typing.Dict[builtins.str, typing.Any]]] = None,
        backfill_none: typing.Optional[typing.Union["GoogleDatastreamStreamBackfillNone", typing.Dict[builtins.str, typing.Any]]] = None,
        customer_managed_encryption_key: typing.Optional[builtins.str] = None,
        desired_state: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDatastreamStreamTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream google_datastream_stream} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination_config: destination_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#destination_config GoogleDatastreamStream#destination_config}
        :param display_name: Display name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#display_name GoogleDatastreamStream#display_name}
        :param location: The name of the location this stream is located in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#location GoogleDatastreamStream#location}
        :param source_config: source_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#source_config GoogleDatastreamStream#source_config}
        :param stream_id: The stream identifier. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#stream_id GoogleDatastreamStream#stream_id}
        :param backfill_all: backfill_all block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#backfill_all GoogleDatastreamStream#backfill_all}
        :param backfill_none: backfill_none block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#backfill_none GoogleDatastreamStream#backfill_none}
        :param customer_managed_encryption_key: A reference to a KMS encryption key. If provided, it will be used to encrypt the data. If left blank, data will be encrypted using an internal Stream-specific encryption key provisioned through KMS. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#customer_managed_encryption_key GoogleDatastreamStream#customer_managed_encryption_key}
        :param desired_state: Desired state of the Stream. Set this field to 'RUNNING' to start the stream, and 'PAUSED' to pause the stream. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#desired_state GoogleDatastreamStream#desired_state}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#id GoogleDatastreamStream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels. **Note**: This field is non-authoritative, and will only manage the labels present in your configuration. Please refer to the field 'effective_labels' for all of the labels present on the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#labels GoogleDatastreamStream#labels}
        :param project: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#project GoogleDatastreamStream#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#timeouts GoogleDatastreamStream#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6cfa931a0c0c189dada75078e20e325e1684379e1ca40acf3c5e5b9c924ed26)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDatastreamStreamConfig(
            destination_config=destination_config,
            display_name=display_name,
            location=location,
            source_config=source_config,
            stream_id=stream_id,
            backfill_all=backfill_all,
            backfill_none=backfill_none,
            customer_managed_encryption_key=customer_managed_encryption_key,
            desired_state=desired_state,
            id=id,
            labels=labels,
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
        '''Generates CDKTF code for importing a GoogleDatastreamStream resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the GoogleDatastreamStream to import.
        :param import_from_id: The id of the existing GoogleDatastreamStream that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the GoogleDatastreamStream to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__649154746d40cf79873b5aae4fd16769e00b6f7d4efd62ad25a2ff95a0cd5f33)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putBackfillAll")
    def put_backfill_all(
        self,
        *,
        mysql_excluded_objects: typing.Optional[typing.Union["GoogleDatastreamStreamBackfillAllMysqlExcludedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        oracle_excluded_objects: typing.Optional[typing.Union["GoogleDatastreamStreamBackfillAllOracleExcludedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        postgresql_excluded_objects: typing.Optional[typing.Union["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mysql_excluded_objects: mysql_excluded_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_excluded_objects GoogleDatastreamStream#mysql_excluded_objects}
        :param oracle_excluded_objects: oracle_excluded_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_excluded_objects GoogleDatastreamStream#oracle_excluded_objects}
        :param postgresql_excluded_objects: postgresql_excluded_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_excluded_objects GoogleDatastreamStream#postgresql_excluded_objects}
        '''
        value = GoogleDatastreamStreamBackfillAll(
            mysql_excluded_objects=mysql_excluded_objects,
            oracle_excluded_objects=oracle_excluded_objects,
            postgresql_excluded_objects=postgresql_excluded_objects,
        )

        return typing.cast(None, jsii.invoke(self, "putBackfillAll", [value]))

    @jsii.member(jsii_name="putBackfillNone")
    def put_backfill_none(self) -> None:
        value = GoogleDatastreamStreamBackfillNone()

        return typing.cast(None, jsii.invoke(self, "putBackfillNone", [value]))

    @jsii.member(jsii_name="putDestinationConfig")
    def put_destination_config(
        self,
        *,
        destination_connection_profile: builtins.str,
        bigquery_destination_config: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        gcs_destination_config: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigGcsDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param destination_connection_profile: Destination connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#destination_connection_profile GoogleDatastreamStream#destination_connection_profile}
        :param bigquery_destination_config: bigquery_destination_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#bigquery_destination_config GoogleDatastreamStream#bigquery_destination_config}
        :param gcs_destination_config: gcs_destination_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#gcs_destination_config GoogleDatastreamStream#gcs_destination_config}
        '''
        value = GoogleDatastreamStreamDestinationConfig(
            destination_connection_profile=destination_connection_profile,
            bigquery_destination_config=bigquery_destination_config,
            gcs_destination_config=gcs_destination_config,
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationConfig", [value]))

    @jsii.member(jsii_name="putSourceConfig")
    def put_source_config(
        self,
        *,
        source_connection_profile: builtins.str,
        mysql_source_config: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        oracle_source_config: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigOracleSourceConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        postgresql_source_config: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param source_connection_profile: Source connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#source_connection_profile GoogleDatastreamStream#source_connection_profile}
        :param mysql_source_config: mysql_source_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_source_config GoogleDatastreamStream#mysql_source_config}
        :param oracle_source_config: oracle_source_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_source_config GoogleDatastreamStream#oracle_source_config}
        :param postgresql_source_config: postgresql_source_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_source_config GoogleDatastreamStream#postgresql_source_config}
        '''
        value = GoogleDatastreamStreamSourceConfig(
            source_connection_profile=source_connection_profile,
            mysql_source_config=mysql_source_config,
            oracle_source_config=oracle_source_config,
            postgresql_source_config=postgresql_source_config,
        )

        return typing.cast(None, jsii.invoke(self, "putSourceConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#create GoogleDatastreamStream#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#delete GoogleDatastreamStream#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#update GoogleDatastreamStream#update}.
        '''
        value = GoogleDatastreamStreamTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBackfillAll")
    def reset_backfill_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackfillAll", []))

    @jsii.member(jsii_name="resetBackfillNone")
    def reset_backfill_none(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackfillNone", []))

    @jsii.member(jsii_name="resetCustomerManagedEncryptionKey")
    def reset_customer_managed_encryption_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerManagedEncryptionKey", []))

    @jsii.member(jsii_name="resetDesiredState")
    def reset_desired_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredState", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

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
    @jsii.member(jsii_name="backfillAll")
    def backfill_all(self) -> "GoogleDatastreamStreamBackfillAllOutputReference":
        return typing.cast("GoogleDatastreamStreamBackfillAllOutputReference", jsii.get(self, "backfillAll"))

    @builtins.property
    @jsii.member(jsii_name="backfillNone")
    def backfill_none(self) -> "GoogleDatastreamStreamBackfillNoneOutputReference":
        return typing.cast("GoogleDatastreamStreamBackfillNoneOutputReference", jsii.get(self, "backfillNone"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfig")
    def destination_config(
        self,
    ) -> "GoogleDatastreamStreamDestinationConfigOutputReference":
        return typing.cast("GoogleDatastreamStreamDestinationConfigOutputReference", jsii.get(self, "destinationConfig"))

    @builtins.property
    @jsii.member(jsii_name="effectiveLabels")
    def effective_labels(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "effectiveLabels"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="sourceConfig")
    def source_config(self) -> "GoogleDatastreamStreamSourceConfigOutputReference":
        return typing.cast("GoogleDatastreamStreamSourceConfigOutputReference", jsii.get(self, "sourceConfig"))

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
    def timeouts(self) -> "GoogleDatastreamStreamTimeoutsOutputReference":
        return typing.cast("GoogleDatastreamStreamTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="backfillAllInput")
    def backfill_all_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamBackfillAll"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamBackfillAll"], jsii.get(self, "backfillAllInput"))

    @builtins.property
    @jsii.member(jsii_name="backfillNoneInput")
    def backfill_none_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamBackfillNone"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamBackfillNone"], jsii.get(self, "backfillNoneInput"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedEncryptionKeyInput")
    def customer_managed_encryption_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerManagedEncryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredStateInput")
    def desired_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredStateInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfigInput")
    def destination_config_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfig"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfig"], jsii.get(self, "destinationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

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
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceConfigInput")
    def source_config_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfig"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfig"], jsii.get(self, "sourceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="streamIdInput")
    def stream_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "GoogleDatastreamStreamTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "GoogleDatastreamStreamTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedEncryptionKey")
    def customer_managed_encryption_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerManagedEncryptionKey"))

    @customer_managed_encryption_key.setter
    def customer_managed_encryption_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74f7b558fd7d27092d7ff81ee82d13e54010ef0007382db2c763be48aea337d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerManagedEncryptionKey", value)

    @builtins.property
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @desired_state.setter
    def desired_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f02e6d6086a6388386fbb0384210f4e368b675aedef36739e15a9b27dc467a86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ece6a77832fb6e89cc0916a10ebc588b04c7d7e93bf43677ad16f9563954cdc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f14ff4627f324370937935159e22c59189775d0e3b599757fff0ae7935aca61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6f63ddf26cb02e92cafbfd7bc5446de232f6b8cb951cc5271c9cd8ef7edbd70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08807dc9fe2f3212f60603e2be9674d576d9b9ebb97552f37256b43f078e57e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c2f2d9b51d02843746ef23bac88dfc96d8afb17d58d75cfc3fd4c132223b5fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="streamId")
    def stream_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamId"))

    @stream_id.setter
    def stream_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83b1410afdedd1ac85863a7d2b94759e47bfea699a0ad11b60e2b915ef038f04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAll",
    jsii_struct_bases=[],
    name_mapping={
        "mysql_excluded_objects": "mysqlExcludedObjects",
        "oracle_excluded_objects": "oracleExcludedObjects",
        "postgresql_excluded_objects": "postgresqlExcludedObjects",
    },
)
class GoogleDatastreamStreamBackfillAll:
    def __init__(
        self,
        *,
        mysql_excluded_objects: typing.Optional[typing.Union["GoogleDatastreamStreamBackfillAllMysqlExcludedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        oracle_excluded_objects: typing.Optional[typing.Union["GoogleDatastreamStreamBackfillAllOracleExcludedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        postgresql_excluded_objects: typing.Optional[typing.Union["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mysql_excluded_objects: mysql_excluded_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_excluded_objects GoogleDatastreamStream#mysql_excluded_objects}
        :param oracle_excluded_objects: oracle_excluded_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_excluded_objects GoogleDatastreamStream#oracle_excluded_objects}
        :param postgresql_excluded_objects: postgresql_excluded_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_excluded_objects GoogleDatastreamStream#postgresql_excluded_objects}
        '''
        if isinstance(mysql_excluded_objects, dict):
            mysql_excluded_objects = GoogleDatastreamStreamBackfillAllMysqlExcludedObjects(**mysql_excluded_objects)
        if isinstance(oracle_excluded_objects, dict):
            oracle_excluded_objects = GoogleDatastreamStreamBackfillAllOracleExcludedObjects(**oracle_excluded_objects)
        if isinstance(postgresql_excluded_objects, dict):
            postgresql_excluded_objects = GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects(**postgresql_excluded_objects)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e29d6dac06c9011c575a9755f405c8c91c314097f849d543ea610c2ae0604ac9)
            check_type(argname="argument mysql_excluded_objects", value=mysql_excluded_objects, expected_type=type_hints["mysql_excluded_objects"])
            check_type(argname="argument oracle_excluded_objects", value=oracle_excluded_objects, expected_type=type_hints["oracle_excluded_objects"])
            check_type(argname="argument postgresql_excluded_objects", value=postgresql_excluded_objects, expected_type=type_hints["postgresql_excluded_objects"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if mysql_excluded_objects is not None:
            self._values["mysql_excluded_objects"] = mysql_excluded_objects
        if oracle_excluded_objects is not None:
            self._values["oracle_excluded_objects"] = oracle_excluded_objects
        if postgresql_excluded_objects is not None:
            self._values["postgresql_excluded_objects"] = postgresql_excluded_objects

    @builtins.property
    def mysql_excluded_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamBackfillAllMysqlExcludedObjects"]:
        '''mysql_excluded_objects block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_excluded_objects GoogleDatastreamStream#mysql_excluded_objects}
        '''
        result = self._values.get("mysql_excluded_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamBackfillAllMysqlExcludedObjects"], result)

    @builtins.property
    def oracle_excluded_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamBackfillAllOracleExcludedObjects"]:
        '''oracle_excluded_objects block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_excluded_objects GoogleDatastreamStream#oracle_excluded_objects}
        '''
        result = self._values.get("oracle_excluded_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamBackfillAllOracleExcludedObjects"], result)

    @builtins.property
    def postgresql_excluded_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects"]:
        '''postgresql_excluded_objects block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_excluded_objects GoogleDatastreamStream#postgresql_excluded_objects}
        '''
        result = self._values.get("postgresql_excluded_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjects",
    jsii_struct_bases=[],
    name_mapping={"mysql_databases": "mysqlDatabases"},
)
class GoogleDatastreamStreamBackfillAllMysqlExcludedObjects:
    def __init__(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d07bf1e73cbfa0c9924cbdd112f8758d8c5843cb05b182d0821feebbecf1bbfe)
            check_type(argname="argument mysql_databases", value=mysql_databases, expected_type=type_hints["mysql_databases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mysql_databases": mysql_databases,
        }

    @builtins.property
    def mysql_databases(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases"]]:
        '''mysql_databases block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        result = self._values.get("mysql_databases")
        assert result is not None, "Required property 'mysql_databases' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllMysqlExcludedObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "mysql_tables": "mysqlTables"},
)
class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases:
    def __init__(
        self,
        *,
        database: builtins.str,
        mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param database: Database name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#database GoogleDatastreamStream#database}
        :param mysql_tables: mysql_tables block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_tables GoogleDatastreamStream#mysql_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__520481cec23840384472636822f5e61482b5d1f652a122cd771b9d999695e41c)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument mysql_tables", value=mysql_tables, expected_type=type_hints["mysql_tables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
        }
        if mysql_tables is not None:
            self._values["mysql_tables"] = mysql_tables

    @builtins.property
    def database(self) -> builtins.str:
        '''Database name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#database GoogleDatastreamStream#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables"]]]:
        '''mysql_tables block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_tables GoogleDatastreamStream#mysql_tables}
        '''
        result = self._values.get("mysql_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__42870644565e23d6a0facda4476561b2c813f8b187a9bef2d4b42bd3b22f4ad7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c27e6265ec073c6cb9d937296a3009c85694518ceb542eb262dc396c0fa0643)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b9f5caf8e7a7472f002063d637ce85c365c019c129961190ee0484f83cb0204)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df989554faa58557b3cee076a0334b3352d497fa9a172a9bc1154b271b849c0d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ff79f76bcf20116f1f916672658b25c9c6061a155abec3dc69a9fe18fcebc28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef052bf283a0faa4298ce68f02ad4567fa25c2230ddec569bcbb3eee18d62299)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "mysql_columns": "mysqlColumns"},
)
class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        :param mysql_columns: mysql_columns block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_columns GoogleDatastreamStream#mysql_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3636dc049bfc21560723eff546dfc6111fc1c67103fa20091fcb54e69eb14642)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument mysql_columns", value=mysql_columns, expected_type=type_hints["mysql_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table": table,
        }
        if mysql_columns is not None:
            self._values["mysql_columns"] = mysql_columns

    @builtins.property
    def table(self) -> builtins.str:
        '''Table name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]]:
        '''mysql_columns block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_columns GoogleDatastreamStream#mysql_columns}
        '''
        result = self._values.get("mysql_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb36c3ec485d5aa4159c543dbc6060937941194b2d7d16197d5fb5b186c37df9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ea3aa0c93b140d0d206e8e869f0817da6984fb7a0b1aff3d6241d5e683dbbe6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ad0c9c602594fd4c30646475e0cb03862cdafe47fef23ee13c7b73b8b81d3bf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4e409c71a7a46ac3ff0a29f111eb9a54fb36f9b824b997eebe0be60e76c7c343)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0be506fa80b767248dcaa2cb7ed0462bf54b31e761efd4e0fa33f50b4cc6fe9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd33626f965d1fd3a29041aa974d9db1d19cf1b45b7027bfc2e9bd65550d21d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    jsii_struct_bases=[],
    name_mapping={
        "collation": "collation",
        "column": "column",
        "data_type": "dataType",
        "nullable": "nullable",
        "ordinal_position": "ordinalPosition",
        "primary_key": "primaryKey",
    },
)
class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns:
    def __init__(
        self,
        *,
        collation: typing.Optional[builtins.str] = None,
        column: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ordinal_position: typing.Optional[jsii.Number] = None,
        primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param collation: Column collation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#collation GoogleDatastreamStream#collation}
        :param column: Column name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        :param data_type: The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        :param nullable: Whether or not the column can accept a null value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        :param ordinal_position: The ordinal position of the column in the table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        :param primary_key: Whether or not the column represents a primary key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23a54185e20f6073f2e24e14685a1bb95703a2f3f4ab9e6eea9d3117b60799c9)
            check_type(argname="argument collation", value=collation, expected_type=type_hints["collation"])
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
            check_type(argname="argument ordinal_position", value=ordinal_position, expected_type=type_hints["ordinal_position"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if collation is not None:
            self._values["collation"] = collation
        if column is not None:
            self._values["column"] = column
        if data_type is not None:
            self._values["data_type"] = data_type
        if nullable is not None:
            self._values["nullable"] = nullable
        if ordinal_position is not None:
            self._values["ordinal_position"] = ordinal_position
        if primary_key is not None:
            self._values["primary_key"] = primary_key

    @builtins.property
    def collation(self) -> typing.Optional[builtins.str]:
        '''Column collation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#collation GoogleDatastreamStream#collation}
        '''
        result = self._values.get("collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column can accept a null value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ordinal_position(self) -> typing.Optional[jsii.Number]:
        '''The ordinal position of the column in the table.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        '''
        result = self._values.get("ordinal_position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column represents a primary key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e6d7e7079d2c891205e2b32b0cf2ceba725f724854f198bf8512979a5696ce8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84e67f89a6476bdc5c731333cf2029e4a5c782f368d3d69f03978d2ce9dcd94b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa3cdc2a83c6840973d4070e34bf50a07ee5f2c7d1f3c68e499ac847bfa79317)
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
            type_hints = typing.get_type_hints(_typecheckingstub__22b091b27124f81de04d4b89dc1049358fc60349f3193740d406a0ce1c9e7eeb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88ef5e48f6385d0236f06a58e25f81251bbc3e6f2240cd75930e6be6beaec4de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f64de49e3b7a392b9d7c9e39a5e5b791d02929fb6fb384bc5ded7da1c10e90da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7292c72a6c771de19158c3d655adc2ba6b3d55d617a83d86255518effa23ba98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCollation")
    def reset_collation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollation", []))

    @jsii.member(jsii_name="resetColumn")
    def reset_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumn", []))

    @jsii.member(jsii_name="resetDataType")
    def reset_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataType", []))

    @jsii.member(jsii_name="resetNullable")
    def reset_nullable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNullable", []))

    @jsii.member(jsii_name="resetOrdinalPosition")
    def reset_ordinal_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrdinalPosition", []))

    @jsii.member(jsii_name="resetPrimaryKey")
    def reset_primary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryKey", []))

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property
    @jsii.member(jsii_name="collationInput")
    def collation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "collationInput"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTypeInput")
    def data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nullableInput")
    def nullable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "nullableInput"))

    @builtins.property
    @jsii.member(jsii_name="ordinalPositionInput")
    def ordinal_position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ordinalPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="collation")
    def collation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "collation"))

    @collation.setter
    def collation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbe8e9c9cb2a678b797af0d6f265ede6140c005c291f7a871610e2b0c46c1239)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collation", value)

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5e78f3a0e42427fb9fe7d3218cf22fcd63107183474d933dbe292a0f22ada60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__801b81a5be1dff9dc10685707b5806e4749464fea9dee3509b069be09a39915d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "nullable"))

    @nullable.setter
    def nullable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a4491c86d6cbca170107672efa5ae073217977e38d890ee684dfabffcdc9bbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @ordinal_position.setter
    def ordinal_position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8adf2449960f783a3598bbe1db28d2f83ca4c95a6ca774684164731a9ca4603)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ordinalPosition", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "primaryKey"))

    @primary_key.setter
    def primary_key(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3cfd6c4c2f5f53f106b06e68701b9e7338a0198f1de4971a3980cb71319134f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4e5c86192b35d7aa9f1c9ff0b2312d4c56114766b1948aeaa6cdb4a187c7447)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5510498980068046efbd3bccc489edaa11d41baf610cf3c6d8b04640da29f441)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlColumns")
    def put_mysql_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1393719f87438cd6e681938c318697c567154ef4d21de037b9794b496d5c053)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlColumns", [value]))

    @jsii.member(jsii_name="resetMysqlColumns")
    def reset_mysql_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlColumns", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList:
        return typing.cast(GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList, jsii.get(self, "mysqlColumns"))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumnsInput")
    def mysql_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "mysqlColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5cdd451c93c14f8bf1348dbc84d1613ee34bee075f1a7ef30641b00e9cc6ddf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40a46438b33027c86396b4bad6c02ccc4329f55d360d33ee604e8932c6d1d25f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9bb2b89ed5c7ab305b2df59f9f1fcae91cadc3414f28c3659364e57a3e1b6dbe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlTables")
    def put_mysql_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6be4542a5978109673a55f553153be687fb0155ae52e28084709f661e644b3d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlTables", [value]))

    @jsii.member(jsii_name="resetMysqlTables")
    def reset_mysql_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlTables", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlTables")
    def mysql_tables(
        self,
    ) -> GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList:
        return typing.cast(GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList, jsii.get(self, "mysqlTables"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlTablesInput")
    def mysql_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "mysqlTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a8764873fb24dfdd954a5d2dbc34cad2573c675bedecb4826b1febb63d5437b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed873de9162601787f1de0b1f1d7bbc82ff2ff4f4f29dcdd5060713a530c99bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b17ebe8e257a4918dda760ce5f15ec271e6f36463b2e0b3b2102f151e7afa5a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlDatabases")
    def put_mysql_databases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72168f0c6c5360f01d1caa68b898ee8a3874c0c09c031475e80aefbaf55f483b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlDatabases", [value]))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList:
        return typing.cast(GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList, jsii.get(self, "mysqlDatabases"))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabasesInput")
    def mysql_databases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]], jsii.get(self, "mysqlDatabasesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49719e784f731e00fa4b5f129ee237712081738ae7d610fb8420b43adc072ede)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllOracleExcludedObjects",
    jsii_struct_bases=[],
    name_mapping={"oracle_schemas": "oracleSchemas"},
)
class GoogleDatastreamStreamBackfillAllOracleExcludedObjects:
    def __init__(
        self,
        *,
        oracle_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param oracle_schemas: oracle_schemas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_schemas GoogleDatastreamStream#oracle_schemas}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91d62ed480f3fa3b3b42fa502a9ed016297cfd3f897f0d05c49b43aae31ddb03)
            check_type(argname="argument oracle_schemas", value=oracle_schemas, expected_type=type_hints["oracle_schemas"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "oracle_schemas": oracle_schemas,
        }

    @builtins.property
    def oracle_schemas(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas"]]:
        '''oracle_schemas block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_schemas GoogleDatastreamStream#oracle_schemas}
        '''
        result = self._values.get("oracle_schemas")
        assert result is not None, "Required property 'oracle_schemas' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllOracleExcludedObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas",
    jsii_struct_bases=[],
    name_mapping={"schema": "schema", "oracle_tables": "oracleTables"},
)
class GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas:
    def __init__(
        self,
        *,
        schema: builtins.str,
        oracle_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param schema: Schema name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema GoogleDatastreamStream#schema}
        :param oracle_tables: oracle_tables block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_tables GoogleDatastreamStream#oracle_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cde81619ce4f9773e3bcac1d1eac26e1b80fef0034c22df9c39c4e57b6311b4c)
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument oracle_tables", value=oracle_tables, expected_type=type_hints["oracle_tables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema": schema,
        }
        if oracle_tables is not None:
            self._values["oracle_tables"] = oracle_tables

    @builtins.property
    def schema(self) -> builtins.str:
        '''Schema name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema GoogleDatastreamStream#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oracle_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables"]]]:
        '''oracle_tables block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_tables GoogleDatastreamStream#oracle_tables}
        '''
        result = self._values.get("oracle_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__efd3094acab0bcbe30a0b24b7dad2112c364cfae80d2a80c6697772945bf2553)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__928c0c3beaf230a91a1648e8095c38efa703030d4607ea7fef17a1623a7d98dd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b57c8885adaf03769ebcea16cb4e45db9aa7f7de2bbd42b9b8c8d738b560f82)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ddb5bb1ba02934848b7dece18ad408f2efb82b210e3637cc254096f2d0814a51)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d3399ec8a222bb8a85a44b0854195351843bd4a4bb6613e6006fd9f37045295)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f267140b0f46f87b73bb114fa99a63577637d4a8dee15b398cca4b60ccbed71c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "oracle_columns": "oracleColumns"},
)
class GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        oracle_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        :param oracle_columns: oracle_columns block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_columns GoogleDatastreamStream#oracle_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51232ab056e0830dca1741ae338bc8911ef6316f203b0c9de5aabfd3cb9b2cfd)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument oracle_columns", value=oracle_columns, expected_type=type_hints["oracle_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table": table,
        }
        if oracle_columns is not None:
            self._values["oracle_columns"] = oracle_columns

    @builtins.property
    def table(self) -> builtins.str:
        '''Table name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oracle_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns"]]]:
        '''oracle_columns block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_columns GoogleDatastreamStream#oracle_columns}
        '''
        result = self._values.get("oracle_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ac0558b1c2ece320fa4dd8665aa9be2324747ec194a0ee4842c9109d5ac45e8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c75cfd5dc4c03ddaf75df1d7d5a2db884121a8f1502de1723dfc2495d0bd21d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26a166dd5d37dc758abf6b4d97af1cf1665a16821eb73be6a3e752eeaa123335)
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
            type_hints = typing.get_type_hints(_typecheckingstub__53ff14e96c500d547e3d544e1a0083ef9b73685b45888cb81fc03f912bdf93b4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca136cff12962de157b6784784f22f0c600e4e270e32ad220c5e85e0957cd868)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c19f83c7d83548c4ba9ca4024d69087f17cfa338fa7dcd1e98228c5218f442a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns",
    jsii_struct_bases=[],
    name_mapping={"column": "column", "data_type": "dataType"},
)
class GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns:
    def __init__(
        self,
        *,
        column: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param column: Column name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        :param data_type: The Oracle data type. Full data types list can be found here: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Data-Types.html. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6355fb3a37c3f3b9017f417fa31d41e8a5e56b36ea746998b568fb7cc67e6588)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if column is not None:
            self._values["column"] = column
        if data_type is not None:
            self._values["data_type"] = data_type

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The Oracle data type. Full data types list can be found here: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Data-Types.html.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2c030ca32bf48f1135773c6c03c88149b97649d699cbaaf236e8eae9a3a6686)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f56c77e1951d088194c6ea4562e0f3ef439f4c6c1a1ef5c74627a0cee838ad3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__749a511324ac27fc60717fbc9ce9066c2dab773aab0878f7a0152671e39504e2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4813c8156e1fdf7dd18e62a46dccc5f9bf4402e149c5f11a04cd2c70b38f083c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ace209faaa8a99572f83638be39226ba65475edc2ce0e6657afa9476701eaf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fd0e3f4fe524540ed70bf1b235bf4cd87cb21e5055ddfdd90d12c9e5f0b5f68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e060e394a8ce41c77c28adbb65536007b66f35a08382b6a21c86bbd4839c1b0a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetColumn")
    def reset_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumn", []))

    @jsii.member(jsii_name="resetDataType")
    def reset_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataType", []))

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "nullable"))

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @builtins.property
    @jsii.member(jsii_name="precision")
    def precision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "precision"))

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "primaryKey"))

    @builtins.property
    @jsii.member(jsii_name="scale")
    def scale(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scale"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTypeInput")
    def data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d72ec20fa92d21619bfacfd46de060e09f08a3b95cfee84482c86ebaa856875a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__499a2274d77bc70280b900bdc07a22cfcf1b3f5138fcc8bd791fb02f5a772779)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c535116d5034ab37245aff3b1c42e402a0532da5c60a9b029e68a9ab047b084c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d02a3641f2ca7316c945da61c399ff690cacb68085cb3dba58aca46b209a39e3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putOracleColumns")
    def put_oracle_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb210e0fee35ea40f225c994acfe3f4bf9a9f56055b4aa0c64aa1fdca4bd4c6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOracleColumns", [value]))

    @jsii.member(jsii_name="resetOracleColumns")
    def reset_oracle_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOracleColumns", []))

    @builtins.property
    @jsii.member(jsii_name="oracleColumns")
    def oracle_columns(
        self,
    ) -> GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumnsList:
        return typing.cast(GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumnsList, jsii.get(self, "oracleColumns"))

    @builtins.property
    @jsii.member(jsii_name="oracleColumnsInput")
    def oracle_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns]]], jsii.get(self, "oracleColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01e7e8a63e4307997ac247f2dfeba2479e317c223d082c798e9e777556014ce1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f26d13db4081a2a4b32bbc3da771f78c6f7105dceeb3be840e605fe30edd7593)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9e126b93e12b18d38500307735ddc6ed1fc3cda056ef9e6e21d7812fd71e1cd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putOracleTables")
    def put_oracle_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__520f00bd2dcf608c4814507927cf9024a65f669914e7f2cf3c4c9ec5f9ce676c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOracleTables", [value]))

    @jsii.member(jsii_name="resetOracleTables")
    def reset_oracle_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOracleTables", []))

    @builtins.property
    @jsii.member(jsii_name="oracleTables")
    def oracle_tables(
        self,
    ) -> GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesList:
        return typing.cast(GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesList, jsii.get(self, "oracleTables"))

    @builtins.property
    @jsii.member(jsii_name="oracleTablesInput")
    def oracle_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables]]], jsii.get(self, "oracleTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e4ef90208ebedc1c370f7d08defb352230959ad705bc14c6bed5b2469b301c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9a12920a531b030c68168a271c0023b324bca863476d97d397ed66b25f724c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__abf152989bccdbf713d22bf06bdbfe4777e9fd9b4b03d02d9e1e63abc37ae21d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOracleSchemas")
    def put_oracle_schemas(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b40950d0c225b2691d41a692c78d5b61b54fd9f92fc7642d3bfb6bdc468aa8d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOracleSchemas", [value]))

    @builtins.property
    @jsii.member(jsii_name="oracleSchemas")
    def oracle_schemas(
        self,
    ) -> GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasList:
        return typing.cast(GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasList, jsii.get(self, "oracleSchemas"))

    @builtins.property
    @jsii.member(jsii_name="oracleSchemasInput")
    def oracle_schemas_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas]]], jsii.get(self, "oracleSchemasInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamBackfillAllOracleExcludedObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillAllOracleExcludedObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamBackfillAllOracleExcludedObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfa0f6695759b22c658d74737ec0b2786a3083ffb1c2bbd240901cf4df8b607e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e274f1c79b478e8a9935941ed6e1cae337452327e7e0df1b2e287933f42cb449)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlExcludedObjects")
    def put_mysql_excluded_objects(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        value = GoogleDatastreamStreamBackfillAllMysqlExcludedObjects(
            mysql_databases=mysql_databases
        )

        return typing.cast(None, jsii.invoke(self, "putMysqlExcludedObjects", [value]))

    @jsii.member(jsii_name="putOracleExcludedObjects")
    def put_oracle_excluded_objects(
        self,
        *,
        oracle_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param oracle_schemas: oracle_schemas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_schemas GoogleDatastreamStream#oracle_schemas}
        '''
        value = GoogleDatastreamStreamBackfillAllOracleExcludedObjects(
            oracle_schemas=oracle_schemas
        )

        return typing.cast(None, jsii.invoke(self, "putOracleExcludedObjects", [value]))

    @jsii.member(jsii_name="putPostgresqlExcludedObjects")
    def put_postgresql_excluded_objects(
        self,
        *,
        postgresql_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param postgresql_schemas: postgresql_schemas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_schemas GoogleDatastreamStream#postgresql_schemas}
        '''
        value = GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects(
            postgresql_schemas=postgresql_schemas
        )

        return typing.cast(None, jsii.invoke(self, "putPostgresqlExcludedObjects", [value]))

    @jsii.member(jsii_name="resetMysqlExcludedObjects")
    def reset_mysql_excluded_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlExcludedObjects", []))

    @jsii.member(jsii_name="resetOracleExcludedObjects")
    def reset_oracle_excluded_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOracleExcludedObjects", []))

    @jsii.member(jsii_name="resetPostgresqlExcludedObjects")
    def reset_postgresql_excluded_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostgresqlExcludedObjects", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlExcludedObjects")
    def mysql_excluded_objects(
        self,
    ) -> GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference:
        return typing.cast(GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference, jsii.get(self, "mysqlExcludedObjects"))

    @builtins.property
    @jsii.member(jsii_name="oracleExcludedObjects")
    def oracle_excluded_objects(
        self,
    ) -> GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOutputReference:
        return typing.cast(GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOutputReference, jsii.get(self, "oracleExcludedObjects"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlExcludedObjects")
    def postgresql_excluded_objects(
        self,
    ) -> "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsOutputReference":
        return typing.cast("GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsOutputReference", jsii.get(self, "postgresqlExcludedObjects"))

    @builtins.property
    @jsii.member(jsii_name="mysqlExcludedObjectsInput")
    def mysql_excluded_objects_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects], jsii.get(self, "mysqlExcludedObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="oracleExcludedObjectsInput")
    def oracle_excluded_objects_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamBackfillAllOracleExcludedObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillAllOracleExcludedObjects], jsii.get(self, "oracleExcludedObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlExcludedObjectsInput")
    def postgresql_excluded_objects_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects"], jsii.get(self, "postgresqlExcludedObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDatastreamStreamBackfillAll]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamBackfillAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e18596f2739b568b00dc8878957e1a0ae36c322e4460e1efcc618a1fbd80dfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects",
    jsii_struct_bases=[],
    name_mapping={"postgresql_schemas": "postgresqlSchemas"},
)
class GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects:
    def __init__(
        self,
        *,
        postgresql_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param postgresql_schemas: postgresql_schemas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_schemas GoogleDatastreamStream#postgresql_schemas}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6934e68e3ff15aace86a557b5fcdef40790b7d1dcfeba766a0482fa1b38802a)
            check_type(argname="argument postgresql_schemas", value=postgresql_schemas, expected_type=type_hints["postgresql_schemas"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "postgresql_schemas": postgresql_schemas,
        }

    @builtins.property
    def postgresql_schemas(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas"]]:
        '''postgresql_schemas block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_schemas GoogleDatastreamStream#postgresql_schemas}
        '''
        result = self._values.get("postgresql_schemas")
        assert result is not None, "Required property 'postgresql_schemas' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef0e1e63c4b7a5a04debeff85c97f3fd7bd6c6cb80d20711b3ba3278d80ec353)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPostgresqlSchemas")
    def put_postgresql_schemas(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d91185c63066f069f351201e0ff47747a96ec09dd3d9962a3f4b1ecffa3cc223)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPostgresqlSchemas", [value]))

    @builtins.property
    @jsii.member(jsii_name="postgresqlSchemas")
    def postgresql_schemas(
        self,
    ) -> "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasList":
        return typing.cast("GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasList", jsii.get(self, "postgresqlSchemas"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlSchemasInput")
    def postgresql_schemas_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas"]]], jsii.get(self, "postgresqlSchemasInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99032ce0897661a0f857e5fdc2766dd3f40641553834bb1514286172ba319d20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas",
    jsii_struct_bases=[],
    name_mapping={"schema": "schema", "postgresql_tables": "postgresqlTables"},
)
class GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas:
    def __init__(
        self,
        *,
        schema: builtins.str,
        postgresql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param schema: Database name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema GoogleDatastreamStream#schema}
        :param postgresql_tables: postgresql_tables block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_tables GoogleDatastreamStream#postgresql_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05a169c1d9312cae3424b4cf7316597bc578cadf1937be01bf6b4ef31ff318b0)
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument postgresql_tables", value=postgresql_tables, expected_type=type_hints["postgresql_tables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema": schema,
        }
        if postgresql_tables is not None:
            self._values["postgresql_tables"] = postgresql_tables

    @builtins.property
    def schema(self) -> builtins.str:
        '''Database name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema GoogleDatastreamStream#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postgresql_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables"]]]:
        '''postgresql_tables block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_tables GoogleDatastreamStream#postgresql_tables}
        '''
        result = self._values.get("postgresql_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ba383460f26f69ba509fb5e772f486a53c196fbdc4e4109ae394c6bda7d76e4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c89c447c39c8b15f01815481c20a0fa4bc29a528957254b6fed496cdfa521837)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52e5ea0a86139b5c5893e6e74f4e56228601a4e9fdec1fb5cb8bc6efbdaf6c38)
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
            type_hints = typing.get_type_hints(_typecheckingstub__025e75d4d4563f72d050a070442264c7450e2755ae7b3f1c8dbaf058003dcb8b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c24b1a64202a816b124f72f8206772a1574306d6747149d57b1abeeef5e0d253)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52aba87205fd056dc50e1d9ab17060ed7bcd93865687544a06530b6752afc77a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__36573c962ad63512915d06f83c5854c269c638dbe7c38cb58a8d1fab15819375)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPostgresqlTables")
    def put_postgresql_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6831d7f7a468c6c62d6d3d695ca30ce45020caa7ead3c11a5a706b09a168e598)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPostgresqlTables", [value]))

    @jsii.member(jsii_name="resetPostgresqlTables")
    def reset_postgresql_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostgresqlTables", []))

    @builtins.property
    @jsii.member(jsii_name="postgresqlTables")
    def postgresql_tables(
        self,
    ) -> "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesList":
        return typing.cast("GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesList", jsii.get(self, "postgresqlTables"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlTablesInput")
    def postgresql_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables"]]], jsii.get(self, "postgresqlTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00de054fb9da01b6f9d9713f3b8c7fc4cb3590238f567337fbd0c7dcaa42c50c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__699a4a9e23e2db77d0b2d6fe84ec37ae780ddbfc518797cb891ca259d802c120)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "postgresql_columns": "postgresqlColumns"},
)
class GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        postgresql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        :param postgresql_columns: postgresql_columns block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_columns GoogleDatastreamStream#postgresql_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b66fc593b40d3a7b31ee6b94969b31d2e732a6d05aa0e9b4c3c7737cfdef21dd)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument postgresql_columns", value=postgresql_columns, expected_type=type_hints["postgresql_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table": table,
        }
        if postgresql_columns is not None:
            self._values["postgresql_columns"] = postgresql_columns

    @builtins.property
    def table(self) -> builtins.str:
        '''Table name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postgresql_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns"]]]:
        '''postgresql_columns block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_columns GoogleDatastreamStream#postgresql_columns}
        '''
        result = self._values.get("postgresql_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a24790b4632522537214a52da553dea21b2a740d5afcccf1e1b47fc04956b675)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b435f756e86cd7415b5bbb8004f2b3f6773179250ea89211b7aaa6f7d2421e0f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c52d8fdd0c3efc72761bf6ac3bf80e9b006889cf2bf36643054e3142c3ed34c3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__61b548f4d3f09166d5113b36c98d7908a6e5bf45402f26282847cc2dab9d224d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ce19649192b891826321da0402e0912b85150724012173ebb6747ac34670bf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c44dd15e41e4216e2593b6cd4e5be954f6c1ffb2443e9a05cba66f99a6f104a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1c79a43e282268cfc73a2de510a4c49ef4819bcd34be3c28678519795254fb6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPostgresqlColumns")
    def put_postgresql_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60e5f7a8b9b86c0b9277ddebbb62854902117db8943f26ca12e6196c73668035)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPostgresqlColumns", [value]))

    @jsii.member(jsii_name="resetPostgresqlColumns")
    def reset_postgresql_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostgresqlColumns", []))

    @builtins.property
    @jsii.member(jsii_name="postgresqlColumns")
    def postgresql_columns(
        self,
    ) -> "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList":
        return typing.cast("GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList", jsii.get(self, "postgresqlColumns"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlColumnsInput")
    def postgresql_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns"]]], jsii.get(self, "postgresqlColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dd4177e6b293e2281bec0b4667e1fcdcad37080a4f087467b0afc9ddb621c3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30e613c4dbcf9c96bda77a7ac2c0671acf5b6b35d9b3d82274aebeff963dae25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "data_type": "dataType",
        "nullable": "nullable",
        "ordinal_position": "ordinalPosition",
        "primary_key": "primaryKey",
    },
)
class GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns:
    def __init__(
        self,
        *,
        column: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ordinal_position: typing.Optional[jsii.Number] = None,
        primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param column: Column name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        :param data_type: The PostgreSQL data type. Full data types list can be found here: https://www.postgresql.org/docs/current/datatype.html. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        :param nullable: Whether or not the column can accept a null value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        :param ordinal_position: The ordinal position of the column in the table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        :param primary_key: Whether or not the column represents a primary key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__011222891dbbe92444a6ae0e8752cd8607a8cdec716b117cfcee323e5e366464)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
            check_type(argname="argument ordinal_position", value=ordinal_position, expected_type=type_hints["ordinal_position"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if column is not None:
            self._values["column"] = column
        if data_type is not None:
            self._values["data_type"] = data_type
        if nullable is not None:
            self._values["nullable"] = nullable
        if ordinal_position is not None:
            self._values["ordinal_position"] = ordinal_position
        if primary_key is not None:
            self._values["primary_key"] = primary_key

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The PostgreSQL data type. Full data types list can be found here: https://www.postgresql.org/docs/current/datatype.html.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column can accept a null value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ordinal_position(self) -> typing.Optional[jsii.Number]:
        '''The ordinal position of the column in the table.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        '''
        result = self._values.get("ordinal_position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column represents a primary key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2492c75d0ab44294e30a17a291ba51204e50947e1bbf9288f00559561142edad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__601b097b3324b6691855ef65c2e51f0a8abc01adfc4f0ec18e55971bbb6d7d56)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4ee78b7df0d1bb3aa0efb76e5a9799adbfac935152947349902a90da95d4ccc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a173d2f2f24ab7b5e141d45d3b19cc57f72b9fc2d78f1aca0a4f1c769482300e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4e67d04b5a0d51d107a8fbd1a497417942c8e8069e0df9c1731d8534753b21de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9d933cf1d30658c9a9f7a46ac398cc952069a345aa2b6b31c8ce27f4e6fdcad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f37c7b49c96139951341e37959e5380814a66382aa5fff66f9883a88c641b23)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetColumn")
    def reset_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumn", []))

    @jsii.member(jsii_name="resetDataType")
    def reset_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataType", []))

    @jsii.member(jsii_name="resetNullable")
    def reset_nullable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNullable", []))

    @jsii.member(jsii_name="resetOrdinalPosition")
    def reset_ordinal_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrdinalPosition", []))

    @jsii.member(jsii_name="resetPrimaryKey")
    def reset_primary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryKey", []))

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property
    @jsii.member(jsii_name="precision")
    def precision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "precision"))

    @builtins.property
    @jsii.member(jsii_name="scale")
    def scale(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scale"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTypeInput")
    def data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nullableInput")
    def nullable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "nullableInput"))

    @builtins.property
    @jsii.member(jsii_name="ordinalPositionInput")
    def ordinal_position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ordinalPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d27d25ec834ff7241cf86e0235c339433b7fa6db163ae3862f8b73a25ffe6bbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd0c5fac24dec8a1750574e186d9ca3341b636104bc89b79c04f6b7cc590f7d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "nullable"))

    @nullable.setter
    def nullable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ae84dc4aedb19866d3c92c409974db9a499f250d06e5cd318eaa311a3ec2c49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @ordinal_position.setter
    def ordinal_position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bf1287f27d9d8d62e80f8bcf3f03d5efc1a9bb0b5db2dda9a5a55ade660f0f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ordinalPosition", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "primaryKey"))

    @primary_key.setter
    def primary_key(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4a5eb9e007468dac28d2d6c7c80ea552e014a3c9ed3825c336e28b548e08d09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aacc1fba903eb1404c6a096687be6ef2b6887a9d9da5d17d7eabe3833f94cc71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillNone",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleDatastreamStreamBackfillNone:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillNone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillNoneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillNoneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7d92abc899aebc8d6d75893b1acd1ccfce0f432db79b875d3d4e45b3724468b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDatastreamStreamBackfillNone]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillNone], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamBackfillNone],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfa1cb735e7372c389d187e9df62ce48602d5e810e1d37efcc2c795f44eae0eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "destination_config": "destinationConfig",
        "display_name": "displayName",
        "location": "location",
        "source_config": "sourceConfig",
        "stream_id": "streamId",
        "backfill_all": "backfillAll",
        "backfill_none": "backfillNone",
        "customer_managed_encryption_key": "customerManagedEncryptionKey",
        "desired_state": "desiredState",
        "id": "id",
        "labels": "labels",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleDatastreamStreamConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        destination_config: typing.Union["GoogleDatastreamStreamDestinationConfig", typing.Dict[builtins.str, typing.Any]],
        display_name: builtins.str,
        location: builtins.str,
        source_config: typing.Union["GoogleDatastreamStreamSourceConfig", typing.Dict[builtins.str, typing.Any]],
        stream_id: builtins.str,
        backfill_all: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAll, typing.Dict[builtins.str, typing.Any]]] = None,
        backfill_none: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillNone, typing.Dict[builtins.str, typing.Any]]] = None,
        customer_managed_encryption_key: typing.Optional[builtins.str] = None,
        desired_state: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDatastreamStreamTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param destination_config: destination_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#destination_config GoogleDatastreamStream#destination_config}
        :param display_name: Display name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#display_name GoogleDatastreamStream#display_name}
        :param location: The name of the location this stream is located in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#location GoogleDatastreamStream#location}
        :param source_config: source_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#source_config GoogleDatastreamStream#source_config}
        :param stream_id: The stream identifier. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#stream_id GoogleDatastreamStream#stream_id}
        :param backfill_all: backfill_all block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#backfill_all GoogleDatastreamStream#backfill_all}
        :param backfill_none: backfill_none block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#backfill_none GoogleDatastreamStream#backfill_none}
        :param customer_managed_encryption_key: A reference to a KMS encryption key. If provided, it will be used to encrypt the data. If left blank, data will be encrypted using an internal Stream-specific encryption key provisioned through KMS. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#customer_managed_encryption_key GoogleDatastreamStream#customer_managed_encryption_key}
        :param desired_state: Desired state of the Stream. Set this field to 'RUNNING' to start the stream, and 'PAUSED' to pause the stream. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#desired_state GoogleDatastreamStream#desired_state}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#id GoogleDatastreamStream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels. **Note**: This field is non-authoritative, and will only manage the labels present in your configuration. Please refer to the field 'effective_labels' for all of the labels present on the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#labels GoogleDatastreamStream#labels}
        :param project: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#project GoogleDatastreamStream#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#timeouts GoogleDatastreamStream#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(destination_config, dict):
            destination_config = GoogleDatastreamStreamDestinationConfig(**destination_config)
        if isinstance(source_config, dict):
            source_config = GoogleDatastreamStreamSourceConfig(**source_config)
        if isinstance(backfill_all, dict):
            backfill_all = GoogleDatastreamStreamBackfillAll(**backfill_all)
        if isinstance(backfill_none, dict):
            backfill_none = GoogleDatastreamStreamBackfillNone(**backfill_none)
        if isinstance(timeouts, dict):
            timeouts = GoogleDatastreamStreamTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8212616678ebc8f5f13dc67f8ecb8284c7ae5d6006e98280adbb52774b08f47)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument destination_config", value=destination_config, expected_type=type_hints["destination_config"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument source_config", value=source_config, expected_type=type_hints["source_config"])
            check_type(argname="argument stream_id", value=stream_id, expected_type=type_hints["stream_id"])
            check_type(argname="argument backfill_all", value=backfill_all, expected_type=type_hints["backfill_all"])
            check_type(argname="argument backfill_none", value=backfill_none, expected_type=type_hints["backfill_none"])
            check_type(argname="argument customer_managed_encryption_key", value=customer_managed_encryption_key, expected_type=type_hints["customer_managed_encryption_key"])
            check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_config": destination_config,
            "display_name": display_name,
            "location": location,
            "source_config": source_config,
            "stream_id": stream_id,
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
        if backfill_all is not None:
            self._values["backfill_all"] = backfill_all
        if backfill_none is not None:
            self._values["backfill_none"] = backfill_none
        if customer_managed_encryption_key is not None:
            self._values["customer_managed_encryption_key"] = customer_managed_encryption_key
        if desired_state is not None:
            self._values["desired_state"] = desired_state
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
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
    def destination_config(self) -> "GoogleDatastreamStreamDestinationConfig":
        '''destination_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#destination_config GoogleDatastreamStream#destination_config}
        '''
        result = self._values.get("destination_config")
        assert result is not None, "Required property 'destination_config' is missing"
        return typing.cast("GoogleDatastreamStreamDestinationConfig", result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''Display name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#display_name GoogleDatastreamStream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The name of the location this stream is located in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#location GoogleDatastreamStream#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_config(self) -> "GoogleDatastreamStreamSourceConfig":
        '''source_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#source_config GoogleDatastreamStream#source_config}
        '''
        result = self._values.get("source_config")
        assert result is not None, "Required property 'source_config' is missing"
        return typing.cast("GoogleDatastreamStreamSourceConfig", result)

    @builtins.property
    def stream_id(self) -> builtins.str:
        '''The stream identifier.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#stream_id GoogleDatastreamStream#stream_id}
        '''
        result = self._values.get("stream_id")
        assert result is not None, "Required property 'stream_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backfill_all(self) -> typing.Optional[GoogleDatastreamStreamBackfillAll]:
        '''backfill_all block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#backfill_all GoogleDatastreamStream#backfill_all}
        '''
        result = self._values.get("backfill_all")
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillAll], result)

    @builtins.property
    def backfill_none(self) -> typing.Optional[GoogleDatastreamStreamBackfillNone]:
        '''backfill_none block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#backfill_none GoogleDatastreamStream#backfill_none}
        '''
        result = self._values.get("backfill_none")
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillNone], result)

    @builtins.property
    def customer_managed_encryption_key(self) -> typing.Optional[builtins.str]:
        '''A reference to a KMS encryption key.

        If provided, it will be used to encrypt the data. If left blank, data
        will be encrypted using an internal Stream-specific encryption key provisioned through KMS.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#customer_managed_encryption_key GoogleDatastreamStream#customer_managed_encryption_key}
        '''
        result = self._values.get("customer_managed_encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def desired_state(self) -> typing.Optional[builtins.str]:
        '''Desired state of the Stream.

        Set this field to 'RUNNING' to start the stream, and 'PAUSED' to pause the stream.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#desired_state GoogleDatastreamStream#desired_state}
        '''
        result = self._values.get("desired_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#id GoogleDatastreamStream#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels.

        **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
        Please refer to the field 'effective_labels' for all of the labels present on the resource.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#labels GoogleDatastreamStream#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#project GoogleDatastreamStream#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDatastreamStreamTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#timeouts GoogleDatastreamStream#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDatastreamStreamTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "destination_connection_profile": "destinationConnectionProfile",
        "bigquery_destination_config": "bigqueryDestinationConfig",
        "gcs_destination_config": "gcsDestinationConfig",
    },
)
class GoogleDatastreamStreamDestinationConfig:
    def __init__(
        self,
        *,
        destination_connection_profile: builtins.str,
        bigquery_destination_config: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        gcs_destination_config: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigGcsDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param destination_connection_profile: Destination connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#destination_connection_profile GoogleDatastreamStream#destination_connection_profile}
        :param bigquery_destination_config: bigquery_destination_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#bigquery_destination_config GoogleDatastreamStream#bigquery_destination_config}
        :param gcs_destination_config: gcs_destination_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#gcs_destination_config GoogleDatastreamStream#gcs_destination_config}
        '''
        if isinstance(bigquery_destination_config, dict):
            bigquery_destination_config = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig(**bigquery_destination_config)
        if isinstance(gcs_destination_config, dict):
            gcs_destination_config = GoogleDatastreamStreamDestinationConfigGcsDestinationConfig(**gcs_destination_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a082f18c6634f77c5c989c278a91ddf6916c61c1c1c1ecaeb403873feb786f6f)
            check_type(argname="argument destination_connection_profile", value=destination_connection_profile, expected_type=type_hints["destination_connection_profile"])
            check_type(argname="argument bigquery_destination_config", value=bigquery_destination_config, expected_type=type_hints["bigquery_destination_config"])
            check_type(argname="argument gcs_destination_config", value=gcs_destination_config, expected_type=type_hints["gcs_destination_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_connection_profile": destination_connection_profile,
        }
        if bigquery_destination_config is not None:
            self._values["bigquery_destination_config"] = bigquery_destination_config
        if gcs_destination_config is not None:
            self._values["gcs_destination_config"] = gcs_destination_config

    @builtins.property
    def destination_connection_profile(self) -> builtins.str:
        '''Destination connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#destination_connection_profile GoogleDatastreamStream#destination_connection_profile}
        '''
        result = self._values.get("destination_connection_profile")
        assert result is not None, "Required property 'destination_connection_profile' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bigquery_destination_config(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig"]:
        '''bigquery_destination_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#bigquery_destination_config GoogleDatastreamStream#bigquery_destination_config}
        '''
        result = self._values.get("bigquery_destination_config")
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig"], result)

    @builtins.property
    def gcs_destination_config(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigGcsDestinationConfig"]:
        '''gcs_destination_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#gcs_destination_config GoogleDatastreamStream#gcs_destination_config}
        '''
        result = self._values.get("gcs_destination_config")
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigGcsDestinationConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "data_freshness": "dataFreshness",
        "single_target_dataset": "singleTargetDataset",
        "source_hierarchy_datasets": "sourceHierarchyDatasets",
    },
)
class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig:
    def __init__(
        self,
        *,
        data_freshness: typing.Optional[builtins.str] = None,
        single_target_dataset: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset", typing.Dict[builtins.str, typing.Any]]] = None,
        source_hierarchy_datasets: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param data_freshness: The guaranteed data freshness (in seconds) when querying tables created by the stream. Editing this field will only affect new tables created in the future, but existing tables will not be impacted. Lower values mean that queries will return fresher data, but may result in higher cost. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_freshness GoogleDatastreamStream#data_freshness}
        :param single_target_dataset: single_target_dataset block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#single_target_dataset GoogleDatastreamStream#single_target_dataset}
        :param source_hierarchy_datasets: source_hierarchy_datasets block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#source_hierarchy_datasets GoogleDatastreamStream#source_hierarchy_datasets}
        '''
        if isinstance(single_target_dataset, dict):
            single_target_dataset = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset(**single_target_dataset)
        if isinstance(source_hierarchy_datasets, dict):
            source_hierarchy_datasets = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets(**source_hierarchy_datasets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a49c814b4f2ebe3deb762ed064f6ce81ac50435614e1bd2718d7e8651def96)
            check_type(argname="argument data_freshness", value=data_freshness, expected_type=type_hints["data_freshness"])
            check_type(argname="argument single_target_dataset", value=single_target_dataset, expected_type=type_hints["single_target_dataset"])
            check_type(argname="argument source_hierarchy_datasets", value=source_hierarchy_datasets, expected_type=type_hints["source_hierarchy_datasets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if data_freshness is not None:
            self._values["data_freshness"] = data_freshness
        if single_target_dataset is not None:
            self._values["single_target_dataset"] = single_target_dataset
        if source_hierarchy_datasets is not None:
            self._values["source_hierarchy_datasets"] = source_hierarchy_datasets

    @builtins.property
    def data_freshness(self) -> typing.Optional[builtins.str]:
        '''The guaranteed data freshness (in seconds) when querying tables created by the stream.

        Editing this field will only affect new tables created in the future, but existing tables
        will not be impacted. Lower values mean that queries will return fresher data, but may result in higher cost.
        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_freshness GoogleDatastreamStream#data_freshness}
        '''
        result = self._values.get("data_freshness")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_target_dataset(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset"]:
        '''single_target_dataset block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#single_target_dataset GoogleDatastreamStream#single_target_dataset}
        '''
        result = self._values.get("single_target_dataset")
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset"], result)

    @builtins.property
    def source_hierarchy_datasets(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets"]:
        '''source_hierarchy_datasets block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#source_hierarchy_datasets GoogleDatastreamStream#source_hierarchy_datasets}
        '''
        result = self._values.get("source_hierarchy_datasets")
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3391270fd72825792750d900baabf072a22d3aa8bfdf9b72803fa90f89feb99)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSingleTargetDataset")
    def put_single_target_dataset(self, *, dataset_id: builtins.str) -> None:
        '''
        :param dataset_id: Dataset ID in the format projects/{project}/datasets/{dataset_id} or {project}:{dataset_id}. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#dataset_id GoogleDatastreamStream#dataset_id}
        '''
        value = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset(
            dataset_id=dataset_id
        )

        return typing.cast(None, jsii.invoke(self, "putSingleTargetDataset", [value]))

    @jsii.member(jsii_name="putSourceHierarchyDatasets")
    def put_source_hierarchy_datasets(
        self,
        *,
        dataset_template: typing.Union["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param dataset_template: dataset_template block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#dataset_template GoogleDatastreamStream#dataset_template}
        '''
        value = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets(
            dataset_template=dataset_template
        )

        return typing.cast(None, jsii.invoke(self, "putSourceHierarchyDatasets", [value]))

    @jsii.member(jsii_name="resetDataFreshness")
    def reset_data_freshness(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataFreshness", []))

    @jsii.member(jsii_name="resetSingleTargetDataset")
    def reset_single_target_dataset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleTargetDataset", []))

    @jsii.member(jsii_name="resetSourceHierarchyDatasets")
    def reset_source_hierarchy_datasets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceHierarchyDatasets", []))

    @builtins.property
    @jsii.member(jsii_name="singleTargetDataset")
    def single_target_dataset(
        self,
    ) -> "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference":
        return typing.cast("GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference", jsii.get(self, "singleTargetDataset"))

    @builtins.property
    @jsii.member(jsii_name="sourceHierarchyDatasets")
    def source_hierarchy_datasets(
        self,
    ) -> "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference":
        return typing.cast("GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference", jsii.get(self, "sourceHierarchyDatasets"))

    @builtins.property
    @jsii.member(jsii_name="dataFreshnessInput")
    def data_freshness_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataFreshnessInput"))

    @builtins.property
    @jsii.member(jsii_name="singleTargetDatasetInput")
    def single_target_dataset_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset"], jsii.get(self, "singleTargetDatasetInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceHierarchyDatasetsInput")
    def source_hierarchy_datasets_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets"], jsii.get(self, "sourceHierarchyDatasetsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFreshness")
    def data_freshness(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFreshness"))

    @data_freshness.setter
    def data_freshness(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc227360efefd83c13161506d90374637c3c2dba1821899cf3a429435283aaa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFreshness", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1e71cd219e14ea812cecfdb4e16eae14cb53d03b3d7baea51323b1fb77a39c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset",
    jsii_struct_bases=[],
    name_mapping={"dataset_id": "datasetId"},
)
class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset:
    def __init__(self, *, dataset_id: builtins.str) -> None:
        '''
        :param dataset_id: Dataset ID in the format projects/{project}/datasets/{dataset_id} or {project}:{dataset_id}. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#dataset_id GoogleDatastreamStream#dataset_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8fb9ad9224f683a8eb1f9139234f286bd44fddeece5772c9709e709e591a645)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_id": dataset_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''Dataset ID in the format projects/{project}/datasets/{dataset_id} or {project}:{dataset_id}.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#dataset_id GoogleDatastreamStream#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a3d055ab4e6752ba6dfdb4394295e7f7318d4a3b762834c187cc27231d4ca7a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4c9b188fd123021caa994f45cf0394e7b3f43765b979d928e6f4d9f0621a963)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04350676f2a57de4c6c34fd5c31fe09fe4989c93a30002c55349461fcd324dd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets",
    jsii_struct_bases=[],
    name_mapping={"dataset_template": "datasetTemplate"},
)
class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets:
    def __init__(
        self,
        *,
        dataset_template: typing.Union["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param dataset_template: dataset_template block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#dataset_template GoogleDatastreamStream#dataset_template}
        '''
        if isinstance(dataset_template, dict):
            dataset_template = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate(**dataset_template)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe99655d10da1ece8d92b4b95410a92466fc73978fb56cabdd00ce4872af7f30)
            check_type(argname="argument dataset_template", value=dataset_template, expected_type=type_hints["dataset_template"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_template": dataset_template,
        }

    @builtins.property
    def dataset_template(
        self,
    ) -> "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate":
        '''dataset_template block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#dataset_template GoogleDatastreamStream#dataset_template}
        '''
        result = self._values.get("dataset_template")
        assert result is not None, "Required property 'dataset_template' is missing"
        return typing.cast("GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate",
    jsii_struct_bases=[],
    name_mapping={
        "location": "location",
        "dataset_id_prefix": "datasetIdPrefix",
        "kms_key_name": "kmsKeyName",
    },
)
class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate:
    def __init__(
        self,
        *,
        location: builtins.str,
        dataset_id_prefix: typing.Optional[builtins.str] = None,
        kms_key_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param location: The geographic location where the dataset should reside. See https://cloud.google.com/bigquery/docs/locations for supported locations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#location GoogleDatastreamStream#location}
        :param dataset_id_prefix: If supplied, every created dataset will have its name prefixed by the provided value. The prefix and name will be separated by an underscore. i.e. _. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#dataset_id_prefix GoogleDatastreamStream#dataset_id_prefix}
        :param kms_key_name: Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key. i.e. projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{cryptoKey}. See https://cloud.google.com/bigquery/docs/customer-managed-encryption for more information. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#kms_key_name GoogleDatastreamStream#kms_key_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10bc9309ea21fa94f6d71ec05001d53825566fb8b23e70b72f26ff70b216afbf)
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument dataset_id_prefix", value=dataset_id_prefix, expected_type=type_hints["dataset_id_prefix"])
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location": location,
        }
        if dataset_id_prefix is not None:
            self._values["dataset_id_prefix"] = dataset_id_prefix
        if kms_key_name is not None:
            self._values["kms_key_name"] = kms_key_name

    @builtins.property
    def location(self) -> builtins.str:
        '''The geographic location where the dataset should reside. See https://cloud.google.com/bigquery/docs/locations for supported locations.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#location GoogleDatastreamStream#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_id_prefix(self) -> typing.Optional[builtins.str]:
        '''If supplied, every created dataset will have its name prefixed by the provided value.

        The prefix and name will be separated by an underscore. i.e. _.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#dataset_id_prefix GoogleDatastreamStream#dataset_id_prefix}
        '''
        result = self._values.get("dataset_id_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_name(self) -> typing.Optional[builtins.str]:
        '''Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.

        The BigQuery Service Account associated with your project requires access to this
        encryption key. i.e. projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{cryptoKey}.
        See https://cloud.google.com/bigquery/docs/customer-managed-encryption for more information.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#kms_key_name GoogleDatastreamStream#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__589f4d7cacffa3fe9eaf1ee753fd3bb86c046e23b7c2e374b0f0fe1f59848e72)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatasetIdPrefix")
    def reset_dataset_id_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetIdPrefix", []))

    @jsii.member(jsii_name="resetKmsKeyName")
    def reset_kms_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyName", []))

    @builtins.property
    @jsii.member(jsii_name="datasetIdPrefixInput")
    def dataset_id_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyNameInput")
    def kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetIdPrefix")
    def dataset_id_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetIdPrefix"))

    @dataset_id_prefix.setter
    def dataset_id_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fa782c14749e41909d2558ed573b112c4f62c763ad09af5bb8000ea5bb08163)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetIdPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyName")
    def kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyName"))

    @kms_key_name.setter
    def kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64830a54fe54f2f7da8fe9df8388f147273f845e49dbe02ce84b116489ccc0fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04028b6cda5a7527cf51ede06922de56ad34e57e9e59dc68cf55dbb105f0a0db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5de30ee6e92d12ceb0bda2317dd12bfa52377bec516b2b2a517385018ff4fd37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec59f9ec651149d0621d83bf49acbf8ee0bbd34767529437d0eaab1d43196fba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDatasetTemplate")
    def put_dataset_template(
        self,
        *,
        location: builtins.str,
        dataset_id_prefix: typing.Optional[builtins.str] = None,
        kms_key_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param location: The geographic location where the dataset should reside. See https://cloud.google.com/bigquery/docs/locations for supported locations. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#location GoogleDatastreamStream#location}
        :param dataset_id_prefix: If supplied, every created dataset will have its name prefixed by the provided value. The prefix and name will be separated by an underscore. i.e. _. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#dataset_id_prefix GoogleDatastreamStream#dataset_id_prefix}
        :param kms_key_name: Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key. i.e. projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{cryptoKey}. See https://cloud.google.com/bigquery/docs/customer-managed-encryption for more information. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#kms_key_name GoogleDatastreamStream#kms_key_name}
        '''
        value = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate(
            location=location,
            dataset_id_prefix=dataset_id_prefix,
            kms_key_name=kms_key_name,
        )

        return typing.cast(None, jsii.invoke(self, "putDatasetTemplate", [value]))

    @builtins.property
    @jsii.member(jsii_name="datasetTemplate")
    def dataset_template(
        self,
    ) -> GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference:
        return typing.cast(GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference, jsii.get(self, "datasetTemplate"))

    @builtins.property
    @jsii.member(jsii_name="datasetTemplateInput")
    def dataset_template_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate], jsii.get(self, "datasetTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ead61d6997a472aca9d935cc8910fa587fa5ce5f4d399617f914993534cca402)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigGcsDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "avro_file_format": "avroFileFormat",
        "file_rotation_interval": "fileRotationInterval",
        "file_rotation_mb": "fileRotationMb",
        "json_file_format": "jsonFileFormat",
        "path": "path",
    },
)
class GoogleDatastreamStreamDestinationConfigGcsDestinationConfig:
    def __init__(
        self,
        *,
        avro_file_format: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat", typing.Dict[builtins.str, typing.Any]]] = None,
        file_rotation_interval: typing.Optional[builtins.str] = None,
        file_rotation_mb: typing.Optional[jsii.Number] = None,
        json_file_format: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat", typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param avro_file_format: avro_file_format block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#avro_file_format GoogleDatastreamStream#avro_file_format}
        :param file_rotation_interval: The maximum duration for which new events are added before a file is closed and a new file is created. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#file_rotation_interval GoogleDatastreamStream#file_rotation_interval}
        :param file_rotation_mb: The maximum file size to be saved in the bucket. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#file_rotation_mb GoogleDatastreamStream#file_rotation_mb}
        :param json_file_format: json_file_format block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#json_file_format GoogleDatastreamStream#json_file_format}
        :param path: Path inside the Cloud Storage bucket to write data to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#path GoogleDatastreamStream#path}
        '''
        if isinstance(avro_file_format, dict):
            avro_file_format = GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat(**avro_file_format)
        if isinstance(json_file_format, dict):
            json_file_format = GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat(**json_file_format)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d10163a88a5e865a15e425114c10f9f67bb19cad50eff789fae98679356656a)
            check_type(argname="argument avro_file_format", value=avro_file_format, expected_type=type_hints["avro_file_format"])
            check_type(argname="argument file_rotation_interval", value=file_rotation_interval, expected_type=type_hints["file_rotation_interval"])
            check_type(argname="argument file_rotation_mb", value=file_rotation_mb, expected_type=type_hints["file_rotation_mb"])
            check_type(argname="argument json_file_format", value=json_file_format, expected_type=type_hints["json_file_format"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if avro_file_format is not None:
            self._values["avro_file_format"] = avro_file_format
        if file_rotation_interval is not None:
            self._values["file_rotation_interval"] = file_rotation_interval
        if file_rotation_mb is not None:
            self._values["file_rotation_mb"] = file_rotation_mb
        if json_file_format is not None:
            self._values["json_file_format"] = json_file_format
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def avro_file_format(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat"]:
        '''avro_file_format block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#avro_file_format GoogleDatastreamStream#avro_file_format}
        '''
        result = self._values.get("avro_file_format")
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat"], result)

    @builtins.property
    def file_rotation_interval(self) -> typing.Optional[builtins.str]:
        '''The maximum duration for which new events are added before a file is closed and a new file is created.

        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#file_rotation_interval GoogleDatastreamStream#file_rotation_interval}
        '''
        result = self._values.get("file_rotation_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_rotation_mb(self) -> typing.Optional[jsii.Number]:
        '''The maximum file size to be saved in the bucket.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#file_rotation_mb GoogleDatastreamStream#file_rotation_mb}
        '''
        result = self._values.get("file_rotation_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def json_file_format(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat"]:
        '''json_file_format block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#json_file_format GoogleDatastreamStream#json_file_format}
        '''
        result = self._values.get("json_file_format")
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat"], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path inside the Cloud Storage bucket to write data to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#path GoogleDatastreamStream#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigGcsDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d068a5a28bd2dac3ef4546b05167198e8dc3f67c53ef66378117e2eb38de3e13)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f08298ba4d0b3313ce13d92f69a9b0d3e473996f7259553f11037794731faf97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat",
    jsii_struct_bases=[],
    name_mapping={
        "compression": "compression",
        "schema_file_format": "schemaFileFormat",
    },
)
class GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat:
    def __init__(
        self,
        *,
        compression: typing.Optional[builtins.str] = None,
        schema_file_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param compression: Compression of the loaded JSON file. Possible values: ["NO_COMPRESSION", "GZIP"]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#compression GoogleDatastreamStream#compression}
        :param schema_file_format: The schema file format along JSON data files. Possible values: ["NO_SCHEMA_FILE", "AVRO_SCHEMA_FILE"]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema_file_format GoogleDatastreamStream#schema_file_format}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac5bf24309609d454116747fe1a8433f1d6909fbbae89e976eff2fea5165e8d7)
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument schema_file_format", value=schema_file_format, expected_type=type_hints["schema_file_format"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if compression is not None:
            self._values["compression"] = compression
        if schema_file_format is not None:
            self._values["schema_file_format"] = schema_file_format

    @builtins.property
    def compression(self) -> typing.Optional[builtins.str]:
        '''Compression of the loaded JSON file. Possible values: ["NO_COMPRESSION", "GZIP"].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#compression GoogleDatastreamStream#compression}
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_file_format(self) -> typing.Optional[builtins.str]:
        '''The schema file format along JSON data files. Possible values: ["NO_SCHEMA_FILE", "AVRO_SCHEMA_FILE"].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema_file_format GoogleDatastreamStream#schema_file_format}
        '''
        result = self._values.get("schema_file_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__56acedeeab88a59e046f3eda7acc9a87997bd1e847f3661a1d2ecffcaf8ece46)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCompression")
    def reset_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompression", []))

    @jsii.member(jsii_name="resetSchemaFileFormat")
    def reset_schema_file_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaFileFormat", []))

    @builtins.property
    @jsii.member(jsii_name="compressionInput")
    def compression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaFileFormatInput")
    def schema_file_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaFileFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca5cc438ef5b106f7a336d20a5581f3c31250831e9ffddefcd61b4d1d9ff878f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="schemaFileFormat")
    def schema_file_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaFileFormat"))

    @schema_file_format.setter
    def schema_file_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac1ec35e9777f4ddf604ec41ee7052c7ac0d48e85abfb0a0bc9ffd10834276d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaFileFormat", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d5e3c16b98749306678a7e9992adf27157907012286429f2c66df988d0f0bc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamDestinationConfigGcsDestinationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigGcsDestinationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__47a5f5a8a9d9f19534aeab03cc71f662ec8150fb452e35333840e1fa4d19587e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAvroFileFormat")
    def put_avro_file_format(self) -> None:
        value = GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat()

        return typing.cast(None, jsii.invoke(self, "putAvroFileFormat", [value]))

    @jsii.member(jsii_name="putJsonFileFormat")
    def put_json_file_format(
        self,
        *,
        compression: typing.Optional[builtins.str] = None,
        schema_file_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param compression: Compression of the loaded JSON file. Possible values: ["NO_COMPRESSION", "GZIP"]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#compression GoogleDatastreamStream#compression}
        :param schema_file_format: The schema file format along JSON data files. Possible values: ["NO_SCHEMA_FILE", "AVRO_SCHEMA_FILE"]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema_file_format GoogleDatastreamStream#schema_file_format}
        '''
        value = GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat(
            compression=compression, schema_file_format=schema_file_format
        )

        return typing.cast(None, jsii.invoke(self, "putJsonFileFormat", [value]))

    @jsii.member(jsii_name="resetAvroFileFormat")
    def reset_avro_file_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvroFileFormat", []))

    @jsii.member(jsii_name="resetFileRotationInterval")
    def reset_file_rotation_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileRotationInterval", []))

    @jsii.member(jsii_name="resetFileRotationMb")
    def reset_file_rotation_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileRotationMb", []))

    @jsii.member(jsii_name="resetJsonFileFormat")
    def reset_json_file_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonFileFormat", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="avroFileFormat")
    def avro_file_format(
        self,
    ) -> GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference:
        return typing.cast(GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference, jsii.get(self, "avroFileFormat"))

    @builtins.property
    @jsii.member(jsii_name="jsonFileFormat")
    def json_file_format(
        self,
    ) -> GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference:
        return typing.cast(GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference, jsii.get(self, "jsonFileFormat"))

    @builtins.property
    @jsii.member(jsii_name="avroFileFormatInput")
    def avro_file_format_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat], jsii.get(self, "avroFileFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="fileRotationIntervalInput")
    def file_rotation_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileRotationIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="fileRotationMbInput")
    def file_rotation_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fileRotationMbInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonFileFormatInput")
    def json_file_format_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat], jsii.get(self, "jsonFileFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="fileRotationInterval")
    def file_rotation_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileRotationInterval"))

    @file_rotation_interval.setter
    def file_rotation_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9074e840158c242a6584f690b9de8519093a095062560f763cb0081827756a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileRotationInterval", value)

    @builtins.property
    @jsii.member(jsii_name="fileRotationMb")
    def file_rotation_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fileRotationMb"))

    @file_rotation_mb.setter
    def file_rotation_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d6fa5c42e1b054c724b34adb45f27353c6ae294899a9d8e80d90a167757cf2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileRotationMb", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa2957bdccb90ef0e1d993d38c3afe8f4b14b633ee4a561bb96646544890cbd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7c83b1266ba6a9af784fac1c33e0f366fe2d370e2f056e83a4d926ae455c27b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamDestinationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7c6a55cbd18393a53cb1933e95b4e468f4a520e2aad658c6da60f7b52de2f3b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBigqueryDestinationConfig")
    def put_bigquery_destination_config(
        self,
        *,
        data_freshness: typing.Optional[builtins.str] = None,
        single_target_dataset: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset, typing.Dict[builtins.str, typing.Any]]] = None,
        source_hierarchy_datasets: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param data_freshness: The guaranteed data freshness (in seconds) when querying tables created by the stream. Editing this field will only affect new tables created in the future, but existing tables will not be impacted. Lower values mean that queries will return fresher data, but may result in higher cost. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_freshness GoogleDatastreamStream#data_freshness}
        :param single_target_dataset: single_target_dataset block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#single_target_dataset GoogleDatastreamStream#single_target_dataset}
        :param source_hierarchy_datasets: source_hierarchy_datasets block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#source_hierarchy_datasets GoogleDatastreamStream#source_hierarchy_datasets}
        '''
        value = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig(
            data_freshness=data_freshness,
            single_target_dataset=single_target_dataset,
            source_hierarchy_datasets=source_hierarchy_datasets,
        )

        return typing.cast(None, jsii.invoke(self, "putBigqueryDestinationConfig", [value]))

    @jsii.member(jsii_name="putGcsDestinationConfig")
    def put_gcs_destination_config(
        self,
        *,
        avro_file_format: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat, typing.Dict[builtins.str, typing.Any]]] = None,
        file_rotation_interval: typing.Optional[builtins.str] = None,
        file_rotation_mb: typing.Optional[jsii.Number] = None,
        json_file_format: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat, typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param avro_file_format: avro_file_format block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#avro_file_format GoogleDatastreamStream#avro_file_format}
        :param file_rotation_interval: The maximum duration for which new events are added before a file is closed and a new file is created. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#file_rotation_interval GoogleDatastreamStream#file_rotation_interval}
        :param file_rotation_mb: The maximum file size to be saved in the bucket. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#file_rotation_mb GoogleDatastreamStream#file_rotation_mb}
        :param json_file_format: json_file_format block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#json_file_format GoogleDatastreamStream#json_file_format}
        :param path: Path inside the Cloud Storage bucket to write data to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#path GoogleDatastreamStream#path}
        '''
        value = GoogleDatastreamStreamDestinationConfigGcsDestinationConfig(
            avro_file_format=avro_file_format,
            file_rotation_interval=file_rotation_interval,
            file_rotation_mb=file_rotation_mb,
            json_file_format=json_file_format,
            path=path,
        )

        return typing.cast(None, jsii.invoke(self, "putGcsDestinationConfig", [value]))

    @jsii.member(jsii_name="resetBigqueryDestinationConfig")
    def reset_bigquery_destination_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBigqueryDestinationConfig", []))

    @jsii.member(jsii_name="resetGcsDestinationConfig")
    def reset_gcs_destination_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcsDestinationConfig", []))

    @builtins.property
    @jsii.member(jsii_name="bigqueryDestinationConfig")
    def bigquery_destination_config(
        self,
    ) -> GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference:
        return typing.cast(GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference, jsii.get(self, "bigqueryDestinationConfig"))

    @builtins.property
    @jsii.member(jsii_name="gcsDestinationConfig")
    def gcs_destination_config(
        self,
    ) -> GoogleDatastreamStreamDestinationConfigGcsDestinationConfigOutputReference:
        return typing.cast(GoogleDatastreamStreamDestinationConfigGcsDestinationConfigOutputReference, jsii.get(self, "gcsDestinationConfig"))

    @builtins.property
    @jsii.member(jsii_name="bigqueryDestinationConfigInput")
    def bigquery_destination_config_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig], jsii.get(self, "bigqueryDestinationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationConnectionProfileInput")
    def destination_connection_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationConnectionProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsDestinationConfigInput")
    def gcs_destination_config_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig], jsii.get(self, "gcsDestinationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationConnectionProfile")
    def destination_connection_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationConnectionProfile"))

    @destination_connection_profile.setter
    def destination_connection_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4017d208188843d4929bba3e8132e98451cac7713ab722eee13604f90c45b18b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationConnectionProfile", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dcc83c10b6513136386af9d65f30bf2f699f914858eb91aaeeea5968e7dc3c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "source_connection_profile": "sourceConnectionProfile",
        "mysql_source_config": "mysqlSourceConfig",
        "oracle_source_config": "oracleSourceConfig",
        "postgresql_source_config": "postgresqlSourceConfig",
    },
)
class GoogleDatastreamStreamSourceConfig:
    def __init__(
        self,
        *,
        source_connection_profile: builtins.str,
        mysql_source_config: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        oracle_source_config: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigOracleSourceConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        postgresql_source_config: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param source_connection_profile: Source connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#source_connection_profile GoogleDatastreamStream#source_connection_profile}
        :param mysql_source_config: mysql_source_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_source_config GoogleDatastreamStream#mysql_source_config}
        :param oracle_source_config: oracle_source_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_source_config GoogleDatastreamStream#oracle_source_config}
        :param postgresql_source_config: postgresql_source_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_source_config GoogleDatastreamStream#postgresql_source_config}
        '''
        if isinstance(mysql_source_config, dict):
            mysql_source_config = GoogleDatastreamStreamSourceConfigMysqlSourceConfig(**mysql_source_config)
        if isinstance(oracle_source_config, dict):
            oracle_source_config = GoogleDatastreamStreamSourceConfigOracleSourceConfig(**oracle_source_config)
        if isinstance(postgresql_source_config, dict):
            postgresql_source_config = GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig(**postgresql_source_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2219a962a105c32324aa42c0ebabb89901efc5212a250e8d5cbf7c24fdf77d88)
            check_type(argname="argument source_connection_profile", value=source_connection_profile, expected_type=type_hints["source_connection_profile"])
            check_type(argname="argument mysql_source_config", value=mysql_source_config, expected_type=type_hints["mysql_source_config"])
            check_type(argname="argument oracle_source_config", value=oracle_source_config, expected_type=type_hints["oracle_source_config"])
            check_type(argname="argument postgresql_source_config", value=postgresql_source_config, expected_type=type_hints["postgresql_source_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_connection_profile": source_connection_profile,
        }
        if mysql_source_config is not None:
            self._values["mysql_source_config"] = mysql_source_config
        if oracle_source_config is not None:
            self._values["oracle_source_config"] = oracle_source_config
        if postgresql_source_config is not None:
            self._values["postgresql_source_config"] = postgresql_source_config

    @builtins.property
    def source_connection_profile(self) -> builtins.str:
        '''Source connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#source_connection_profile GoogleDatastreamStream#source_connection_profile}
        '''
        result = self._values.get("source_connection_profile")
        assert result is not None, "Required property 'source_connection_profile' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_source_config(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigMysqlSourceConfig"]:
        '''mysql_source_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_source_config GoogleDatastreamStream#mysql_source_config}
        '''
        result = self._values.get("mysql_source_config")
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigMysqlSourceConfig"], result)

    @builtins.property
    def oracle_source_config(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigOracleSourceConfig"]:
        '''oracle_source_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_source_config GoogleDatastreamStream#oracle_source_config}
        '''
        result = self._values.get("oracle_source_config")
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigOracleSourceConfig"], result)

    @builtins.property
    def postgresql_source_config(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig"]:
        '''postgresql_source_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_source_config GoogleDatastreamStream#postgresql_source_config}
        '''
        result = self._values.get("postgresql_source_config")
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "exclude_objects": "excludeObjects",
        "include_objects": "includeObjects",
        "max_concurrent_backfill_tasks": "maxConcurrentBackfillTasks",
        "max_concurrent_cdc_tasks": "maxConcurrentCdcTasks",
    },
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfig:
    def __init__(
        self,
        *,
        exclude_objects: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        include_objects: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        max_concurrent_backfill_tasks: typing.Optional[jsii.Number] = None,
        max_concurrent_cdc_tasks: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param exclude_objects: exclude_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#exclude_objects GoogleDatastreamStream#exclude_objects}
        :param include_objects: include_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#include_objects GoogleDatastreamStream#include_objects}
        :param max_concurrent_backfill_tasks: Maximum number of concurrent backfill tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_backfill_tasks GoogleDatastreamStream#max_concurrent_backfill_tasks}
        :param max_concurrent_cdc_tasks: Maximum number of concurrent CDC tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_cdc_tasks GoogleDatastreamStream#max_concurrent_cdc_tasks}
        '''
        if isinstance(exclude_objects, dict):
            exclude_objects = GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects(**exclude_objects)
        if isinstance(include_objects, dict):
            include_objects = GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects(**include_objects)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4778bbd828e1594c449bc443537ebe755eb4c886943cdf45c60649a2abdad88)
            check_type(argname="argument exclude_objects", value=exclude_objects, expected_type=type_hints["exclude_objects"])
            check_type(argname="argument include_objects", value=include_objects, expected_type=type_hints["include_objects"])
            check_type(argname="argument max_concurrent_backfill_tasks", value=max_concurrent_backfill_tasks, expected_type=type_hints["max_concurrent_backfill_tasks"])
            check_type(argname="argument max_concurrent_cdc_tasks", value=max_concurrent_cdc_tasks, expected_type=type_hints["max_concurrent_cdc_tasks"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exclude_objects is not None:
            self._values["exclude_objects"] = exclude_objects
        if include_objects is not None:
            self._values["include_objects"] = include_objects
        if max_concurrent_backfill_tasks is not None:
            self._values["max_concurrent_backfill_tasks"] = max_concurrent_backfill_tasks
        if max_concurrent_cdc_tasks is not None:
            self._values["max_concurrent_cdc_tasks"] = max_concurrent_cdc_tasks

    @builtins.property
    def exclude_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects"]:
        '''exclude_objects block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#exclude_objects GoogleDatastreamStream#exclude_objects}
        '''
        result = self._values.get("exclude_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects"], result)

    @builtins.property
    def include_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects"]:
        '''include_objects block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#include_objects GoogleDatastreamStream#include_objects}
        '''
        result = self._values.get("include_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects"], result)

    @builtins.property
    def max_concurrent_backfill_tasks(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of concurrent backfill tasks.

        The number should be non negative.
        If not set (or set to 0), the system's default value will be used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_backfill_tasks GoogleDatastreamStream#max_concurrent_backfill_tasks}
        '''
        result = self._values.get("max_concurrent_backfill_tasks")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_concurrent_cdc_tasks(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of concurrent CDC tasks.

        The number should be non negative.
        If not set (or set to 0), the system's default value will be used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_cdc_tasks GoogleDatastreamStream#max_concurrent_cdc_tasks}
        '''
        result = self._values.get("max_concurrent_cdc_tasks")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects",
    jsii_struct_bases=[],
    name_mapping={"mysql_databases": "mysqlDatabases"},
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects:
    def __init__(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d83157a8b7dabb6f6a578ba371ae7606ca73d8b886f676352d01e59c8b975065)
            check_type(argname="argument mysql_databases", value=mysql_databases, expected_type=type_hints["mysql_databases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mysql_databases": mysql_databases,
        }

    @builtins.property
    def mysql_databases(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases"]]:
        '''mysql_databases block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        result = self._values.get("mysql_databases")
        assert result is not None, "Required property 'mysql_databases' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "mysql_tables": "mysqlTables"},
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases:
    def __init__(
        self,
        *,
        database: builtins.str,
        mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param database: Database name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#database GoogleDatastreamStream#database}
        :param mysql_tables: mysql_tables block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_tables GoogleDatastreamStream#mysql_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb545565a9647ff9db741b384db4f82c54b58032c7b2d4e18818cd7d16eeeb69)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument mysql_tables", value=mysql_tables, expected_type=type_hints["mysql_tables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
        }
        if mysql_tables is not None:
            self._values["mysql_tables"] = mysql_tables

    @builtins.property
    def database(self) -> builtins.str:
        '''Database name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#database GoogleDatastreamStream#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables"]]]:
        '''mysql_tables block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_tables GoogleDatastreamStream#mysql_tables}
        '''
        result = self._values.get("mysql_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2e56eed75c4420627cc1b1ea20e73bc1bbede9df3a2fd8199d4497aa838d16d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a1012ecc8549b81e5e4aa9d9923e204f999b9b29fd4483cafcd96ee9d37e92a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__749cad1c5353daa5443baca3acaaa68fdf3ee0496883fec1e0a8e7bf6e478f43)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ed34b487f8807df8a3089ff0bf45f39c9f22d366421e027795a5d5ff3b031d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__47fc60e67695921f46d329ab49e84fb7a745d5f9e52ef95fd339c406ed1f5337)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6580eacf3a0fa9ef788be946237924b568d6c34ca0ce2997d700ceb0ec5909e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "mysql_columns": "mysqlColumns"},
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        :param mysql_columns: mysql_columns block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_columns GoogleDatastreamStream#mysql_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fd22251a137acbd8b6d4011e790c862bba2bc6baff5731831f4aaeb1f09bc8e)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument mysql_columns", value=mysql_columns, expected_type=type_hints["mysql_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table": table,
        }
        if mysql_columns is not None:
            self._values["mysql_columns"] = mysql_columns

    @builtins.property
    def table(self) -> builtins.str:
        '''Table name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]]:
        '''mysql_columns block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_columns GoogleDatastreamStream#mysql_columns}
        '''
        result = self._values.get("mysql_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb19d59bcaf47d9126f742045b4d73f2d47c6d705e98fc433966bc88d02bd5ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc62e64aa47cf54d533fff2c0ef281c96989464e75c918ffb64f1d14c9d9e79d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09ac2c33a67547e5fc09ad6eab15b4937398704f7e0dccd16e467818f83a6edd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__78f38e38e105221d16e5180f0a1d2c8909391494a32349303610ab95030c9c8c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d20ad137b3b082c078fd7a5bc38642356759a7fc420d24b61cf649a1f7ed1ad8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__244522fde9aceac31a2e149744987ae023545406b794b7618a16cb61f5434d3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    jsii_struct_bases=[],
    name_mapping={
        "collation": "collation",
        "column": "column",
        "data_type": "dataType",
        "nullable": "nullable",
        "ordinal_position": "ordinalPosition",
        "primary_key": "primaryKey",
    },
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns:
    def __init__(
        self,
        *,
        collation: typing.Optional[builtins.str] = None,
        column: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ordinal_position: typing.Optional[jsii.Number] = None,
        primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param collation: Column collation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#collation GoogleDatastreamStream#collation}
        :param column: Column name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        :param data_type: The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        :param nullable: Whether or not the column can accept a null value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        :param ordinal_position: The ordinal position of the column in the table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        :param primary_key: Whether or not the column represents a primary key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fe080b67925fa358036b8642a0299bcbe1d9e7f96a77e04e3df091ce8d56d79)
            check_type(argname="argument collation", value=collation, expected_type=type_hints["collation"])
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
            check_type(argname="argument ordinal_position", value=ordinal_position, expected_type=type_hints["ordinal_position"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if collation is not None:
            self._values["collation"] = collation
        if column is not None:
            self._values["column"] = column
        if data_type is not None:
            self._values["data_type"] = data_type
        if nullable is not None:
            self._values["nullable"] = nullable
        if ordinal_position is not None:
            self._values["ordinal_position"] = ordinal_position
        if primary_key is not None:
            self._values["primary_key"] = primary_key

    @builtins.property
    def collation(self) -> typing.Optional[builtins.str]:
        '''Column collation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#collation GoogleDatastreamStream#collation}
        '''
        result = self._values.get("collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column can accept a null value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ordinal_position(self) -> typing.Optional[jsii.Number]:
        '''The ordinal position of the column in the table.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        '''
        result = self._values.get("ordinal_position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column represents a primary key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__201e84943daf6e96eef782d9aca244517f562921989a0d02638fa0c6272b71f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa8e8e1d140504fda11f4c3773ed96c2555f2d0a8e4e54dd2649412cdce8913b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09f48286efb01f277d2532514c20596f929b4f09bdd712cce896d54029581845)
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
            type_hints = typing.get_type_hints(_typecheckingstub__412ca5ab78995949f165cc648a1345246edeca119614f829c8466a957611327d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8513a9f97f6e8b890e45ed0436f080d3b24af266ac66156a0234692ec528671)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d52d72230d6b4de322b1c93887aea771351503b11807485568c93d0e395bad14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cea7b45fb19736020b1719a17d6aec42bd6508059c9e7f8abc1ab4eff5bcf48b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCollation")
    def reset_collation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollation", []))

    @jsii.member(jsii_name="resetColumn")
    def reset_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumn", []))

    @jsii.member(jsii_name="resetDataType")
    def reset_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataType", []))

    @jsii.member(jsii_name="resetNullable")
    def reset_nullable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNullable", []))

    @jsii.member(jsii_name="resetOrdinalPosition")
    def reset_ordinal_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrdinalPosition", []))

    @jsii.member(jsii_name="resetPrimaryKey")
    def reset_primary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryKey", []))

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property
    @jsii.member(jsii_name="collationInput")
    def collation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "collationInput"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTypeInput")
    def data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nullableInput")
    def nullable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "nullableInput"))

    @builtins.property
    @jsii.member(jsii_name="ordinalPositionInput")
    def ordinal_position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ordinalPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="collation")
    def collation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "collation"))

    @collation.setter
    def collation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77e9ee7094ccb2bbda850d8033cde908a302188b4966ed9026a0addd79294f25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collation", value)

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3769df6b39afdb7b53797c325a30a0a86634ec6359d219686195fabb6bc4ade)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95e94c186c0638d6e197288bd999f087d07a4e38f94a0c930fded96c19b30a06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "nullable"))

    @nullable.setter
    def nullable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57c29013747c1114bb244cb6f55298a74d6c22ed57f735b6c3fcf456523e93bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @ordinal_position.setter
    def ordinal_position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8083b61ac53f7e64f6d293d8795f8cfcb1af5dcc4641991d8c21d7d14d6a090)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ordinalPosition", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "primaryKey"))

    @primary_key.setter
    def primary_key(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4ce157d33b04ca603a11a14e186e508173db15b13bca2edab6f487ed885c277)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a14532a7d8ee26125f14790252a94be3a764732ba59c7e09374d740bd35cb0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9ad39a49db2deb62da532182c908182089fb53ff855492f00ca108bfb38702e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlColumns")
    def put_mysql_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6805013dab1076ffb632b34e127ba4a5b8181fe496c7c0083216d785c6f51a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlColumns", [value]))

    @jsii.member(jsii_name="resetMysqlColumns")
    def reset_mysql_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlColumns", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList, jsii.get(self, "mysqlColumns"))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumnsInput")
    def mysql_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "mysqlColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f635e21d9372998fc0be54b333ef130ee85a23b090304aa7d38db1c57f56b6df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcc850b4e3cb4779e1466342590aca58d03c507861a481a9b9fd924abaa00461)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ba70a81582b78786b580f56388706a6188061700c80a5ac1049d58ea4ceda106)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlTables")
    def put_mysql_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25736e01b271cf2c953cc3fe6752d0c6af2a0cefb5fdadb58a006ce4cd317ca1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlTables", [value]))

    @jsii.member(jsii_name="resetMysqlTables")
    def reset_mysql_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlTables", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlTables")
    def mysql_tables(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList, jsii.get(self, "mysqlTables"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlTablesInput")
    def mysql_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "mysqlTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c255dc0ac974e3e989e48a72c5479f88eb080a9286525bb3f1310e4e41d29747)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78514113923d93d64011f19fc8e7df61bc8b692c1ca133f55e2039d7a76a635d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1c84a482c246e68a2697c2dbe687609ff014a57db45d072800f00517f2aa6a56)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlDatabases")
    def put_mysql_databases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__084ed61c2edc5493618eaa16135dff2755b5c72b0b42e1db898c18b18dc6f41f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlDatabases", [value]))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList, jsii.get(self, "mysqlDatabases"))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabasesInput")
    def mysql_databases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]], jsii.get(self, "mysqlDatabasesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e809bf11601f9faeac3e63217a488b72d3894ca5740326dce20994d858714f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects",
    jsii_struct_bases=[],
    name_mapping={"mysql_databases": "mysqlDatabases"},
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects:
    def __init__(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b782ad37d159e6fc26ccecf102c72c7754e16dda5dfcd19b2bc64b597b89e07)
            check_type(argname="argument mysql_databases", value=mysql_databases, expected_type=type_hints["mysql_databases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mysql_databases": mysql_databases,
        }

    @builtins.property
    def mysql_databases(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases"]]:
        '''mysql_databases block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        result = self._values.get("mysql_databases")
        assert result is not None, "Required property 'mysql_databases' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "mysql_tables": "mysqlTables"},
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases:
    def __init__(
        self,
        *,
        database: builtins.str,
        mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param database: Database name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#database GoogleDatastreamStream#database}
        :param mysql_tables: mysql_tables block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_tables GoogleDatastreamStream#mysql_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f44f39ebafbebf8e628605efe61a5348b73f5c5884eb1c28dde453f8bf8523a5)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument mysql_tables", value=mysql_tables, expected_type=type_hints["mysql_tables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
        }
        if mysql_tables is not None:
            self._values["mysql_tables"] = mysql_tables

    @builtins.property
    def database(self) -> builtins.str:
        '''Database name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#database GoogleDatastreamStream#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables"]]]:
        '''mysql_tables block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_tables GoogleDatastreamStream#mysql_tables}
        '''
        result = self._values.get("mysql_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3950f8fb1b59cab5c5f81358a344ffbf164f405bda8837307b833c993cc758d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90939e89008258e8e5fb13b17b64dcac780a64cb8cbe81abc7341daf57a122e8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__217aa69718caac050d609fc9d8ce57f8bb611e4fa934e6be20a0b57f11f7a1ee)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7dc49121ffff0463e398d82b102cb8ff336eb3cbcd5683e60e9dd1109e48f61)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7ba15a2cd54a82cbc63ae4621ab87db797cd62dcd7ed63ba155e2de063b189e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d004f44683df7b5074728264cf889cbf037304edfcd3f994117693183d9f5db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "mysql_columns": "mysqlColumns"},
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        :param mysql_columns: mysql_columns block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_columns GoogleDatastreamStream#mysql_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa194010af037f05469911f39778136fc3ed69ba254253f1224c1a9bbe628999)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument mysql_columns", value=mysql_columns, expected_type=type_hints["mysql_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table": table,
        }
        if mysql_columns is not None:
            self._values["mysql_columns"] = mysql_columns

    @builtins.property
    def table(self) -> builtins.str:
        '''Table name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]]:
        '''mysql_columns block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_columns GoogleDatastreamStream#mysql_columns}
        '''
        result = self._values.get("mysql_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dcb77d2e3fb3b195efed0d69e822264d59c5fbf7c1b4cee8e8964364dc9c2123)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba2fe890e741e0c6b63029866f84e111f3cd478bbf199d640a82d12c574d7aa7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1c7b2e8a8945bd904b6786cb2b4d1aea6874c1ee6838435ab9323baa835b2e0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e69a309bddb1478976b492ae7fb3fd3f17336bc920c0b40e545744ada6341c29)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2671e1f1942c6cb0e3c3ba36f58e950eb50a102df253a43e899c96a138842ff7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8af2eb875cdae7d71d393ba6e098c6da4c3110914133b1dd079c070354a7a205)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    jsii_struct_bases=[],
    name_mapping={
        "collation": "collation",
        "column": "column",
        "data_type": "dataType",
        "nullable": "nullable",
        "ordinal_position": "ordinalPosition",
        "primary_key": "primaryKey",
    },
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns:
    def __init__(
        self,
        *,
        collation: typing.Optional[builtins.str] = None,
        column: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ordinal_position: typing.Optional[jsii.Number] = None,
        primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param collation: Column collation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#collation GoogleDatastreamStream#collation}
        :param column: Column name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        :param data_type: The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        :param nullable: Whether or not the column can accept a null value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        :param ordinal_position: The ordinal position of the column in the table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        :param primary_key: Whether or not the column represents a primary key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41215ce0b14ba24427640cc4700269ad49a0faadf8295e7ac03b7f47f2b37132)
            check_type(argname="argument collation", value=collation, expected_type=type_hints["collation"])
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
            check_type(argname="argument ordinal_position", value=ordinal_position, expected_type=type_hints["ordinal_position"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if collation is not None:
            self._values["collation"] = collation
        if column is not None:
            self._values["column"] = column
        if data_type is not None:
            self._values["data_type"] = data_type
        if nullable is not None:
            self._values["nullable"] = nullable
        if ordinal_position is not None:
            self._values["ordinal_position"] = ordinal_position
        if primary_key is not None:
            self._values["primary_key"] = primary_key

    @builtins.property
    def collation(self) -> typing.Optional[builtins.str]:
        '''Column collation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#collation GoogleDatastreamStream#collation}
        '''
        result = self._values.get("collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column can accept a null value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ordinal_position(self) -> typing.Optional[jsii.Number]:
        '''The ordinal position of the column in the table.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        '''
        result = self._values.get("ordinal_position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column represents a primary key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6861e4975493055a6649272b537f648980427a9301bfb234da05242b7f0c49ec)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9427d6862c644b6d507a55730df9f5fdf5c926418390d5de45f4e2f3f5ee9f5e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69adb63c3ab9af12da7590f7aae32e0a5104845d11c1ddd67b18b08745828402)
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
            type_hints = typing.get_type_hints(_typecheckingstub__60e663fc168673b4aa74cd1ee2009d59cd03ee3b03440bc1bae19ab2dffb2cdf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b58a7d494136d2ac7db279ee2b91810061fadc45f6d73f86e92229382749f59a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fad90c17f32bc7ae1fccc7cb1431033ed4c2ce630fffd4d769c94decdd59083)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__65b3ccfaf3bad8ab5e06b93c91c603524b0f7f199e7256dfbce872b77ccc667a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCollation")
    def reset_collation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollation", []))

    @jsii.member(jsii_name="resetColumn")
    def reset_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumn", []))

    @jsii.member(jsii_name="resetDataType")
    def reset_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataType", []))

    @jsii.member(jsii_name="resetNullable")
    def reset_nullable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNullable", []))

    @jsii.member(jsii_name="resetOrdinalPosition")
    def reset_ordinal_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrdinalPosition", []))

    @jsii.member(jsii_name="resetPrimaryKey")
    def reset_primary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryKey", []))

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property
    @jsii.member(jsii_name="collationInput")
    def collation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "collationInput"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTypeInput")
    def data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nullableInput")
    def nullable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "nullableInput"))

    @builtins.property
    @jsii.member(jsii_name="ordinalPositionInput")
    def ordinal_position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ordinalPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="collation")
    def collation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "collation"))

    @collation.setter
    def collation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68e45a2b6f0d78f15e06a1e14dbc279680b842b3d346da672fb3da0ba499caa5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collation", value)

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a954aaaf4ecbb61bdb80680a5308a4650ff1f930fdff1565938a80865567e4b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bfd73c16927e583d02f4ece4c98e6e285936610b6ea37d64cb9c6731b30c6e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "nullable"))

    @nullable.setter
    def nullable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c58d677fcfdede4d959a221ab875d5089fa903aa656d2b774755c9e2be2e790)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @ordinal_position.setter
    def ordinal_position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c454d64cfc5be1fab8c89b6180a07485a1e3934e24523bc92f3900e58a45b43b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ordinalPosition", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "primaryKey"))

    @primary_key.setter
    def primary_key(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__990ed112f00ba5b2fd44cdebb437b9c639030938839325738ece2803bbbee1f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac1001f24a95b45f13518456c95010ca63139d5bf238d99bcc2e6386f283bc2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a6b4a00ce373e23cd5b51bfba3c664c9f9a51885d2951423d35c58dea7aa5613)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlColumns")
    def put_mysql_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c9a1375628b7f6b29a695647f3434428d773a775a513a4c340d0cf934ac7d32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlColumns", [value]))

    @jsii.member(jsii_name="resetMysqlColumns")
    def reset_mysql_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlColumns", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList, jsii.get(self, "mysqlColumns"))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumnsInput")
    def mysql_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "mysqlColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__629184c09083c28c9f035a8074dcd1f16f0a61d948bc2393377da3130506e2f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__759a721a0536fba67735d0dd4283007387dadc2eb076cdb2d65fda1402b5e5f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8548900250b3351b1c6d41c39a3f7fc3652815a7c6184c8c707341c35763ac3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlTables")
    def put_mysql_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b269534d2b5371b90449e0d4dd96df396fbca76931cb7a5f54a30f1b654543d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlTables", [value]))

    @jsii.member(jsii_name="resetMysqlTables")
    def reset_mysql_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlTables", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlTables")
    def mysql_tables(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList, jsii.get(self, "mysqlTables"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlTablesInput")
    def mysql_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "mysqlTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0dc2394f1204551f9f707dbf0479faf9458fafc6a03c129b132c5e409293bb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b6f477c199b7d70e86e7f6dec51b8b579ebe58c787a257fcb73e04d3cc5bcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b401a73888aa3eedea89455bd1d7e18731ee7412824c21d4be2f36a727cd8a7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlDatabases")
    def put_mysql_databases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__613d8a98ff90be15005996fdfac043d333f8645c71d52edfc24b79e3b6031649)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlDatabases", [value]))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList, jsii.get(self, "mysqlDatabases"))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabasesInput")
    def mysql_databases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]], jsii.get(self, "mysqlDatabasesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc63fda8e348ad1f4425fc05aec528be1a2b9aabab914770a3fb1f72c46604b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__efb86a24b39d875af0044075b654f055d4cf52279a7e2097cdcb5b797e5ff174)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExcludeObjects")
    def put_exclude_objects(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        value = GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects(
            mysql_databases=mysql_databases
        )

        return typing.cast(None, jsii.invoke(self, "putExcludeObjects", [value]))

    @jsii.member(jsii_name="putIncludeObjects")
    def put_include_objects(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        value = GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects(
            mysql_databases=mysql_databases
        )

        return typing.cast(None, jsii.invoke(self, "putIncludeObjects", [value]))

    @jsii.member(jsii_name="resetExcludeObjects")
    def reset_exclude_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeObjects", []))

    @jsii.member(jsii_name="resetIncludeObjects")
    def reset_include_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeObjects", []))

    @jsii.member(jsii_name="resetMaxConcurrentBackfillTasks")
    def reset_max_concurrent_backfill_tasks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentBackfillTasks", []))

    @jsii.member(jsii_name="resetMaxConcurrentCdcTasks")
    def reset_max_concurrent_cdc_tasks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentCdcTasks", []))

    @builtins.property
    @jsii.member(jsii_name="excludeObjects")
    def exclude_objects(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference, jsii.get(self, "excludeObjects"))

    @builtins.property
    @jsii.member(jsii_name="includeObjects")
    def include_objects(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference, jsii.get(self, "includeObjects"))

    @builtins.property
    @jsii.member(jsii_name="excludeObjectsInput")
    def exclude_objects_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects], jsii.get(self, "excludeObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeObjectsInput")
    def include_objects_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects], jsii.get(self, "includeObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentBackfillTasksInput")
    def max_concurrent_backfill_tasks_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentBackfillTasksInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentCdcTasksInput")
    def max_concurrent_cdc_tasks_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentCdcTasksInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentBackfillTasks"))

    @max_concurrent_backfill_tasks.setter
    def max_concurrent_backfill_tasks(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2735bcc93507e2cbfa21e107259e233d3beb340310fb8b4096ca3346a5c361f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentBackfillTasks", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentCdcTasks")
    def max_concurrent_cdc_tasks(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentCdcTasks"))

    @max_concurrent_cdc_tasks.setter
    def max_concurrent_cdc_tasks(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75042a2bfae52ebd1b965d7005d120750faa2993f31c1eeb04500e45bd87a769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentCdcTasks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5301d37e1a77c15dc3423d2d6672f672b5059dd74d24e85d8326831c85d9c317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "drop_large_objects": "dropLargeObjects",
        "exclude_objects": "excludeObjects",
        "include_objects": "includeObjects",
        "max_concurrent_backfill_tasks": "maxConcurrentBackfillTasks",
        "max_concurrent_cdc_tasks": "maxConcurrentCdcTasks",
        "stream_large_objects": "streamLargeObjects",
    },
)
class GoogleDatastreamStreamSourceConfigOracleSourceConfig:
    def __init__(
        self,
        *,
        drop_large_objects: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        exclude_objects: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        include_objects: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        max_concurrent_backfill_tasks: typing.Optional[jsii.Number] = None,
        max_concurrent_cdc_tasks: typing.Optional[jsii.Number] = None,
        stream_large_objects: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param drop_large_objects: drop_large_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#drop_large_objects GoogleDatastreamStream#drop_large_objects}
        :param exclude_objects: exclude_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#exclude_objects GoogleDatastreamStream#exclude_objects}
        :param include_objects: include_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#include_objects GoogleDatastreamStream#include_objects}
        :param max_concurrent_backfill_tasks: Maximum number of concurrent backfill tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_backfill_tasks GoogleDatastreamStream#max_concurrent_backfill_tasks}
        :param max_concurrent_cdc_tasks: Maximum number of concurrent CDC tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_cdc_tasks GoogleDatastreamStream#max_concurrent_cdc_tasks}
        :param stream_large_objects: stream_large_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#stream_large_objects GoogleDatastreamStream#stream_large_objects}
        '''
        if isinstance(drop_large_objects, dict):
            drop_large_objects = GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects(**drop_large_objects)
        if isinstance(exclude_objects, dict):
            exclude_objects = GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects(**exclude_objects)
        if isinstance(include_objects, dict):
            include_objects = GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects(**include_objects)
        if isinstance(stream_large_objects, dict):
            stream_large_objects = GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects(**stream_large_objects)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0746e488911fa190cba4ad48b5ba8569167b4dd9cb274d378bae346f3759f736)
            check_type(argname="argument drop_large_objects", value=drop_large_objects, expected_type=type_hints["drop_large_objects"])
            check_type(argname="argument exclude_objects", value=exclude_objects, expected_type=type_hints["exclude_objects"])
            check_type(argname="argument include_objects", value=include_objects, expected_type=type_hints["include_objects"])
            check_type(argname="argument max_concurrent_backfill_tasks", value=max_concurrent_backfill_tasks, expected_type=type_hints["max_concurrent_backfill_tasks"])
            check_type(argname="argument max_concurrent_cdc_tasks", value=max_concurrent_cdc_tasks, expected_type=type_hints["max_concurrent_cdc_tasks"])
            check_type(argname="argument stream_large_objects", value=stream_large_objects, expected_type=type_hints["stream_large_objects"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if drop_large_objects is not None:
            self._values["drop_large_objects"] = drop_large_objects
        if exclude_objects is not None:
            self._values["exclude_objects"] = exclude_objects
        if include_objects is not None:
            self._values["include_objects"] = include_objects
        if max_concurrent_backfill_tasks is not None:
            self._values["max_concurrent_backfill_tasks"] = max_concurrent_backfill_tasks
        if max_concurrent_cdc_tasks is not None:
            self._values["max_concurrent_cdc_tasks"] = max_concurrent_cdc_tasks
        if stream_large_objects is not None:
            self._values["stream_large_objects"] = stream_large_objects

    @builtins.property
    def drop_large_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects"]:
        '''drop_large_objects block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#drop_large_objects GoogleDatastreamStream#drop_large_objects}
        '''
        result = self._values.get("drop_large_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects"], result)

    @builtins.property
    def exclude_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects"]:
        '''exclude_objects block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#exclude_objects GoogleDatastreamStream#exclude_objects}
        '''
        result = self._values.get("exclude_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects"], result)

    @builtins.property
    def include_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects"]:
        '''include_objects block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#include_objects GoogleDatastreamStream#include_objects}
        '''
        result = self._values.get("include_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects"], result)

    @builtins.property
    def max_concurrent_backfill_tasks(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of concurrent backfill tasks.

        The number should be non negative.
        If not set (or set to 0), the system's default value will be used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_backfill_tasks GoogleDatastreamStream#max_concurrent_backfill_tasks}
        '''
        result = self._values.get("max_concurrent_backfill_tasks")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_concurrent_cdc_tasks(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of concurrent CDC tasks.

        The number should be non negative.
        If not set (or set to 0), the system's default value will be used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_cdc_tasks GoogleDatastreamStream#max_concurrent_cdc_tasks}
        '''
        result = self._values.get("max_concurrent_cdc_tasks")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stream_large_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects"]:
        '''stream_large_objects block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#stream_large_objects GoogleDatastreamStream#stream_large_objects}
        '''
        result = self._values.get("stream_large_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigOracleSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__60e644dd74339ca62deff701c0e07764a4674cb5c619be7d317899e07040ea30)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d65ef8ad20e9ab5236f355421fd25e6bdb30b1d250c3c9ecc8d26c58215f7ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects",
    jsii_struct_bases=[],
    name_mapping={"oracle_schemas": "oracleSchemas"},
)
class GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects:
    def __init__(
        self,
        *,
        oracle_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param oracle_schemas: oracle_schemas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_schemas GoogleDatastreamStream#oracle_schemas}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__610d578ff5a80ce274d5ec0c1fc01b310eaa82985cbae7ecc4c0be6959f1e37e)
            check_type(argname="argument oracle_schemas", value=oracle_schemas, expected_type=type_hints["oracle_schemas"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "oracle_schemas": oracle_schemas,
        }

    @builtins.property
    def oracle_schemas(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas"]]:
        '''oracle_schemas block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_schemas GoogleDatastreamStream#oracle_schemas}
        '''
        result = self._values.get("oracle_schemas")
        assert result is not None, "Required property 'oracle_schemas' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas",
    jsii_struct_bases=[],
    name_mapping={"schema": "schema", "oracle_tables": "oracleTables"},
)
class GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas:
    def __init__(
        self,
        *,
        schema: builtins.str,
        oracle_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param schema: Schema name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema GoogleDatastreamStream#schema}
        :param oracle_tables: oracle_tables block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_tables GoogleDatastreamStream#oracle_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3c73db535863aba2213698f0c778ec48e805f13de92d60ec3a324cc006d6d8a)
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument oracle_tables", value=oracle_tables, expected_type=type_hints["oracle_tables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema": schema,
        }
        if oracle_tables is not None:
            self._values["oracle_tables"] = oracle_tables

    @builtins.property
    def schema(self) -> builtins.str:
        '''Schema name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema GoogleDatastreamStream#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oracle_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables"]]]:
        '''oracle_tables block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_tables GoogleDatastreamStream#oracle_tables}
        '''
        result = self._values.get("oracle_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa66e9d03d74841c392450039a5e82254edcbe89869d85a10930236c6f8bbda3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb5f39e489992356e26aa4f345a253773f9f5830b1a3e9a187e3c1accbf43fda)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b61b668e748c315a5bf1659d576b93146914166667008d1b7a40b86a76b99a3f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__47ad29a1ca9bac7e5f763d1f92c78f12093fc9916a33072e9470122b7ba9b81a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5313fe3d09856bc331eee7c5a7bfeecd237b4c309675b8e0efb8f216796890a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13b218859bb362a860023f75c090cdec5e423a75b6065dca0d991b4ce96775a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "oracle_columns": "oracleColumns"},
)
class GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        oracle_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        :param oracle_columns: oracle_columns block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_columns GoogleDatastreamStream#oracle_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72945eecb48621a4fee2bddebd411ceb1f976f5c3a43d0672213685a3b71b441)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument oracle_columns", value=oracle_columns, expected_type=type_hints["oracle_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table": table,
        }
        if oracle_columns is not None:
            self._values["oracle_columns"] = oracle_columns

    @builtins.property
    def table(self) -> builtins.str:
        '''Table name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oracle_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns"]]]:
        '''oracle_columns block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_columns GoogleDatastreamStream#oracle_columns}
        '''
        result = self._values.get("oracle_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__170f35849c38654b7274c3bbe0cde9c0f1625e39bc5c72c8412df57f33ff5214)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51931767b7b4afa892cb5ec9d84c06f533953230fe98d01cf0863ee42a58a119)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0a6f474ed8fb2e1c32d0f32b37aa5c5896c09cdb4c531361e5bca1e0bf217fd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5c34a517c6b92c43e017368b9a6bb30da6731c76951a8d90b64b6132dd63741)
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
            type_hints = typing.get_type_hints(_typecheckingstub__026fe2e82c75504998c44d25e787d2f35af305244ca50485a68073a9cafa44ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be26bef57e570d4993112d124444fd5128b5f4967b31140609cf51c60ca9d504)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns",
    jsii_struct_bases=[],
    name_mapping={"column": "column", "data_type": "dataType"},
)
class GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns:
    def __init__(
        self,
        *,
        column: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param column: Column name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        :param data_type: The Oracle data type. Full data types list can be found here: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Data-Types.html. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__927804d3f0652f6879e48552afb307aede9a0dd7cd504e58d7e1c46bdf801acd)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if column is not None:
            self._values["column"] = column
        if data_type is not None:
            self._values["data_type"] = data_type

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The Oracle data type. Full data types list can be found here: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Data-Types.html.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f19319138fff89df246a22ec13e540b7aa96a77aa14f60eba28e01d6e23152d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edb51fffec9b37c1ca7ef84a3b48dea544f408e80b1beda7f218d830036a2f74)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bddfb7874f06e58758a6475e90c3d4e14086a293cd6cb1cb10cfcbea06d5e2d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9e985724e1382827e7b1632b299eab2811cc4e488b93ae914c89e6dcaea651e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2041884ce280b2fb9be136e1c7de9cc5fb5c110c846583106153358249a8b64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c623992c2c406508cbe09f48f58bceecd0ce77fa49ad9d46a053e9a2fa2f8883)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__23a632c77a902d63986a9c8e808f510b1487a1495271e2299cd5f3e3ebf4a96e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetColumn")
    def reset_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumn", []))

    @jsii.member(jsii_name="resetDataType")
    def reset_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataType", []))

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "nullable"))

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @builtins.property
    @jsii.member(jsii_name="precision")
    def precision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "precision"))

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "primaryKey"))

    @builtins.property
    @jsii.member(jsii_name="scale")
    def scale(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scale"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTypeInput")
    def data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dafaf81736bea926a31b688a9ef41667269b54d506346a7fbaaca1e9a935dd7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9978d38a6735e001b8587ae592bbaaf94a3591c52de2aab9663f4a6f37509e42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__821cc0f4a05ad272a6006e9fda801dafde1a5c6adf5b9c98860434e3c3c7f720)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1defe2cf3ef2295dd20f20a274de67143219892f15fe1c0ec2f7e4ed61f50394)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putOracleColumns")
    def put_oracle_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a297c0a90d9c9b664d36a0a07ddd35c5940573dab31d5cc43ebe5ad8af1b322)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOracleColumns", [value]))

    @jsii.member(jsii_name="resetOracleColumns")
    def reset_oracle_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOracleColumns", []))

    @builtins.property
    @jsii.member(jsii_name="oracleColumns")
    def oracle_columns(
        self,
    ) -> GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumnsList:
        return typing.cast(GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumnsList, jsii.get(self, "oracleColumns"))

    @builtins.property
    @jsii.member(jsii_name="oracleColumnsInput")
    def oracle_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns]]], jsii.get(self, "oracleColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2033547eb38f37fe35125a88c6a104b8070ded44d6069bc7514fa900344d4fb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11a32c231fa57efd2dbca27012b82854d2b91bf9c55d86766d2bbe2377579512)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c60d8456aa34ba08c5cbdea3ee033a688b01b6a1ceee1b3566f681be62e133ef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putOracleTables")
    def put_oracle_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c6e6542a24ee0fa9552302cc404ab540f4e4c9b3c6c906709d85bafed3029e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOracleTables", [value]))

    @jsii.member(jsii_name="resetOracleTables")
    def reset_oracle_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOracleTables", []))

    @builtins.property
    @jsii.member(jsii_name="oracleTables")
    def oracle_tables(
        self,
    ) -> GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesList:
        return typing.cast(GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesList, jsii.get(self, "oracleTables"))

    @builtins.property
    @jsii.member(jsii_name="oracleTablesInput")
    def oracle_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables]]], jsii.get(self, "oracleTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0177ebfad4be23c26b85e0aa50bdf2718495d3628f677c0be28fac3fde5eff10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73a7275153770bd368ca194d0499c9379d54374a979511821c3e12677715d28b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9eb86a65ae85d48b44d647559207b124a8120b7c32b78119c78f71332d3f0273)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOracleSchemas")
    def put_oracle_schemas(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66411d3bf6d5a0271afc2970730b4f28dd2eb4ffba2384ee6ee9b109b40e0d24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOracleSchemas", [value]))

    @builtins.property
    @jsii.member(jsii_name="oracleSchemas")
    def oracle_schemas(
        self,
    ) -> GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasList:
        return typing.cast(GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasList, jsii.get(self, "oracleSchemas"))

    @builtins.property
    @jsii.member(jsii_name="oracleSchemasInput")
    def oracle_schemas_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas]]], jsii.get(self, "oracleSchemasInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d52a5ede0f24000ac161573ac1629edec126f6cba00c3875ab09ed25aa6393f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects",
    jsii_struct_bases=[],
    name_mapping={"oracle_schemas": "oracleSchemas"},
)
class GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects:
    def __init__(
        self,
        *,
        oracle_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param oracle_schemas: oracle_schemas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_schemas GoogleDatastreamStream#oracle_schemas}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bf7adf8a1b3c9403fdb5890833e7a6863ca0b13208a0571d21d5c360b88b972)
            check_type(argname="argument oracle_schemas", value=oracle_schemas, expected_type=type_hints["oracle_schemas"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "oracle_schemas": oracle_schemas,
        }

    @builtins.property
    def oracle_schemas(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas"]]:
        '''oracle_schemas block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_schemas GoogleDatastreamStream#oracle_schemas}
        '''
        result = self._values.get("oracle_schemas")
        assert result is not None, "Required property 'oracle_schemas' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas",
    jsii_struct_bases=[],
    name_mapping={"schema": "schema", "oracle_tables": "oracleTables"},
)
class GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas:
    def __init__(
        self,
        *,
        schema: builtins.str,
        oracle_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param schema: Schema name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema GoogleDatastreamStream#schema}
        :param oracle_tables: oracle_tables block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_tables GoogleDatastreamStream#oracle_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1327fbf9aea1d708f05f9a5ae75009a20e135b2870b8dba66bea2d9bffd213db)
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument oracle_tables", value=oracle_tables, expected_type=type_hints["oracle_tables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema": schema,
        }
        if oracle_tables is not None:
            self._values["oracle_tables"] = oracle_tables

    @builtins.property
    def schema(self) -> builtins.str:
        '''Schema name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema GoogleDatastreamStream#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oracle_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables"]]]:
        '''oracle_tables block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_tables GoogleDatastreamStream#oracle_tables}
        '''
        result = self._values.get("oracle_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ba579256d9f634a2495f3f5f4f25f632092fb1ef0bc10cacbfb06fccf3ccdd5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57d26e99abe978882a877ee4f27f6685c003bc9077512b01ecfd65fefe266468)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf4e2df60def43855ba3cd939b4f8809e17204c8b3b6819abe11d85e4bb4011b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3321e9b9e486d56b416b6662b463afa6f42e5a2727fb0b207b739c89238d9655)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c393f3debb5f7eec855d2cc171b34bc06ff76cb3addf6cabee68379f49c0543)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__554c599b27578d800761ac0df689e2cd7fde662fe43dda570423339d2959cc57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "oracle_columns": "oracleColumns"},
)
class GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        oracle_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        :param oracle_columns: oracle_columns block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_columns GoogleDatastreamStream#oracle_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6735b041f43857ac6fcc259d83e8ec56b68237c970b2d0cba94db7ce6343dc6f)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument oracle_columns", value=oracle_columns, expected_type=type_hints["oracle_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table": table,
        }
        if oracle_columns is not None:
            self._values["oracle_columns"] = oracle_columns

    @builtins.property
    def table(self) -> builtins.str:
        '''Table name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oracle_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns"]]]:
        '''oracle_columns block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_columns GoogleDatastreamStream#oracle_columns}
        '''
        result = self._values.get("oracle_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c8e91fc15375ec7d0fb5908dc088b08f8665784dc71bad279489c4158e905747)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a5e759e6512a87212073f7fb6442ef00f2839eed1862a2b963ea7958f95c19a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bae040df948cedb813aabf4cec258e6afbcc224c88b32bc0a6b6a21a5edde5e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__93c29be1e152aed916678b6a2de99ed3420b6be1bb1f4004e512c8ede7d659ad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b9dbe0c171e14df5e7d5449a77f61d081dcefb8daa1216ce96f99aa80af8546)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6f21ec8ac603eb65e63a578eb7eb2e1750753d8ed904f4aa21b1533c09d48c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns",
    jsii_struct_bases=[],
    name_mapping={"column": "column", "data_type": "dataType"},
)
class GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns:
    def __init__(
        self,
        *,
        column: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param column: Column name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        :param data_type: The Oracle data type. Full data types list can be found here: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Data-Types.html. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92a1df38365a2804729811dab04b177001df36a2f42f89529d8a62a819106d9b)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if column is not None:
            self._values["column"] = column
        if data_type is not None:
            self._values["data_type"] = data_type

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The Oracle data type. Full data types list can be found here: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Data-Types.html.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__031f827bf69c01b95e88322ca6456a02600429ba27dcc273f2133a1c88eed803)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0868168a79526f32e97400a320d98b837bfe0a6bcde6265bf2832013c3a50198)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d0d245a2130500073a10053bb4f5180b3d68af83f097b2501db2376acf4c627)
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
            type_hints = typing.get_type_hints(_typecheckingstub__52fd0ead8467940ba152c4674ce6e64fdcdd1dacae8d089e71df6250b6b2f6af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9bde2091abb9dcbbb1dc5f50cab7a26031c642bcaa9f81b572961deaf8790ea6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7199f594524db12eb37d343fa910cd257845b8155baaa9c135952c2e62c48a16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__971651e5ad7cb1252fa28191c73caf5c797ab74d69d6ea96498d5bdeb81b6aa6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetColumn")
    def reset_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumn", []))

    @jsii.member(jsii_name="resetDataType")
    def reset_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataType", []))

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "nullable"))

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @builtins.property
    @jsii.member(jsii_name="precision")
    def precision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "precision"))

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "primaryKey"))

    @builtins.property
    @jsii.member(jsii_name="scale")
    def scale(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scale"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTypeInput")
    def data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__069e81b54d19a705d79474390a6d29a94100cca730a221287a70eeae38ed7811)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c27bcba7c7383beb6be3f02f43f68c3620659540fb5702a56dc8c9ca67a8b4f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a3691ef23b9e827eb24871dfac692bdfdea6098ae9d9eb4d58bf00756a10a1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__703996a518a97205ddd13c56342ef25b5b32f06afb40073750bdffb0c1d05946)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putOracleColumns")
    def put_oracle_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1327b38ab72b90f5c97174e958cc7fdab2332bdc5d9198bce1cc59894a633d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOracleColumns", [value]))

    @jsii.member(jsii_name="resetOracleColumns")
    def reset_oracle_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOracleColumns", []))

    @builtins.property
    @jsii.member(jsii_name="oracleColumns")
    def oracle_columns(
        self,
    ) -> GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumnsList:
        return typing.cast(GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumnsList, jsii.get(self, "oracleColumns"))

    @builtins.property
    @jsii.member(jsii_name="oracleColumnsInput")
    def oracle_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns]]], jsii.get(self, "oracleColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19b439f4d826233de8c7048ce84a3349625b11696fbcccf324f532ed9ff80cba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e86d5862462ad3d8d8e6b097839340587bfeb3b6fbd812e085358743fe812ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__43298af7a1bb0174c0dc93615c679aa431c04e61113eacb540534d5f9107e914)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putOracleTables")
    def put_oracle_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a25f7828051d869f0590c65de1031c10af877d13962b7c46ca5c4814c41660f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOracleTables", [value]))

    @jsii.member(jsii_name="resetOracleTables")
    def reset_oracle_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOracleTables", []))

    @builtins.property
    @jsii.member(jsii_name="oracleTables")
    def oracle_tables(
        self,
    ) -> GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesList:
        return typing.cast(GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesList, jsii.get(self, "oracleTables"))

    @builtins.property
    @jsii.member(jsii_name="oracleTablesInput")
    def oracle_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables]]], jsii.get(self, "oracleTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59e90ab428f843cf39f9c80b14b599b2aafa6f11b07ae6bc695b985f32dae601)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c55f58666603268776d8346063a5ab10e4e33365fbe0e2bdefaacecd7d8487a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c83610b88d1b62d65ba062cde85b32baac2a70a055481284c25b5881b81f960b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOracleSchemas")
    def put_oracle_schemas(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9ed97e64d1b360d876fefcb39e5a3d847f81735cbc25db6390ed2260683f432)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOracleSchemas", [value]))

    @builtins.property
    @jsii.member(jsii_name="oracleSchemas")
    def oracle_schemas(
        self,
    ) -> GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasList:
        return typing.cast(GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasList, jsii.get(self, "oracleSchemas"))

    @builtins.property
    @jsii.member(jsii_name="oracleSchemasInput")
    def oracle_schemas_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas]]], jsii.get(self, "oracleSchemasInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22425ca8735bfdcbb966f4900ec7590a3c024f1dc791f7c0aa684275ef1fe6b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigOracleSourceConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c53a4258512add2fed9eb6a736e76b66c1064e19937ba3da4134ad2b06544011)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDropLargeObjects")
    def put_drop_large_objects(self) -> None:
        value = GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects()

        return typing.cast(None, jsii.invoke(self, "putDropLargeObjects", [value]))

    @jsii.member(jsii_name="putExcludeObjects")
    def put_exclude_objects(
        self,
        *,
        oracle_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param oracle_schemas: oracle_schemas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_schemas GoogleDatastreamStream#oracle_schemas}
        '''
        value = GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects(
            oracle_schemas=oracle_schemas
        )

        return typing.cast(None, jsii.invoke(self, "putExcludeObjects", [value]))

    @jsii.member(jsii_name="putIncludeObjects")
    def put_include_objects(
        self,
        *,
        oracle_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param oracle_schemas: oracle_schemas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#oracle_schemas GoogleDatastreamStream#oracle_schemas}
        '''
        value = GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects(
            oracle_schemas=oracle_schemas
        )

        return typing.cast(None, jsii.invoke(self, "putIncludeObjects", [value]))

    @jsii.member(jsii_name="putStreamLargeObjects")
    def put_stream_large_objects(self) -> None:
        value = GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects()

        return typing.cast(None, jsii.invoke(self, "putStreamLargeObjects", [value]))

    @jsii.member(jsii_name="resetDropLargeObjects")
    def reset_drop_large_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDropLargeObjects", []))

    @jsii.member(jsii_name="resetExcludeObjects")
    def reset_exclude_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeObjects", []))

    @jsii.member(jsii_name="resetIncludeObjects")
    def reset_include_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeObjects", []))

    @jsii.member(jsii_name="resetMaxConcurrentBackfillTasks")
    def reset_max_concurrent_backfill_tasks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentBackfillTasks", []))

    @jsii.member(jsii_name="resetMaxConcurrentCdcTasks")
    def reset_max_concurrent_cdc_tasks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentCdcTasks", []))

    @jsii.member(jsii_name="resetStreamLargeObjects")
    def reset_stream_large_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamLargeObjects", []))

    @builtins.property
    @jsii.member(jsii_name="dropLargeObjects")
    def drop_large_objects(
        self,
    ) -> GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjectsOutputReference:
        return typing.cast(GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjectsOutputReference, jsii.get(self, "dropLargeObjects"))

    @builtins.property
    @jsii.member(jsii_name="excludeObjects")
    def exclude_objects(
        self,
    ) -> GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOutputReference:
        return typing.cast(GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOutputReference, jsii.get(self, "excludeObjects"))

    @builtins.property
    @jsii.member(jsii_name="includeObjects")
    def include_objects(
        self,
    ) -> GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOutputReference:
        return typing.cast(GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOutputReference, jsii.get(self, "includeObjects"))

    @builtins.property
    @jsii.member(jsii_name="streamLargeObjects")
    def stream_large_objects(
        self,
    ) -> "GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjectsOutputReference":
        return typing.cast("GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjectsOutputReference", jsii.get(self, "streamLargeObjects"))

    @builtins.property
    @jsii.member(jsii_name="dropLargeObjectsInput")
    def drop_large_objects_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects], jsii.get(self, "dropLargeObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeObjectsInput")
    def exclude_objects_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects], jsii.get(self, "excludeObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeObjectsInput")
    def include_objects_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects], jsii.get(self, "includeObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentBackfillTasksInput")
    def max_concurrent_backfill_tasks_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentBackfillTasksInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentCdcTasksInput")
    def max_concurrent_cdc_tasks_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentCdcTasksInput"))

    @builtins.property
    @jsii.member(jsii_name="streamLargeObjectsInput")
    def stream_large_objects_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects"], jsii.get(self, "streamLargeObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentBackfillTasks"))

    @max_concurrent_backfill_tasks.setter
    def max_concurrent_backfill_tasks(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cc8b5a7b0d761263926fc15e837433a99b479730491bd0feb8a5d25cc6f9fa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentBackfillTasks", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentCdcTasks")
    def max_concurrent_cdc_tasks(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentCdcTasks"))

    @max_concurrent_cdc_tasks.setter
    def max_concurrent_cdc_tasks(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e881dbbea9b91c03402c096c16e6face1b47542b9846c982ce06805d704b6e6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentCdcTasks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5330673f53c095c81dda41b1fade645e45c84457611569d902950dcb166a12b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ded02423cd20100f08f7649eace76f55291e6d74580d0f4f9548aaf2816958fb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecc80d37f0b1af62eefc2bf946f641acc2c7ada6e57c3188cd7b2705b7e930ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__935aa7233aaac0fbc524f35d41c8b42f4f855c3d54fd43f35f0e7b9d7528b61d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlSourceConfig")
    def put_mysql_source_config(
        self,
        *,
        exclude_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
        include_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
        max_concurrent_backfill_tasks: typing.Optional[jsii.Number] = None,
        max_concurrent_cdc_tasks: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param exclude_objects: exclude_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#exclude_objects GoogleDatastreamStream#exclude_objects}
        :param include_objects: include_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#include_objects GoogleDatastreamStream#include_objects}
        :param max_concurrent_backfill_tasks: Maximum number of concurrent backfill tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_backfill_tasks GoogleDatastreamStream#max_concurrent_backfill_tasks}
        :param max_concurrent_cdc_tasks: Maximum number of concurrent CDC tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_cdc_tasks GoogleDatastreamStream#max_concurrent_cdc_tasks}
        '''
        value = GoogleDatastreamStreamSourceConfigMysqlSourceConfig(
            exclude_objects=exclude_objects,
            include_objects=include_objects,
            max_concurrent_backfill_tasks=max_concurrent_backfill_tasks,
            max_concurrent_cdc_tasks=max_concurrent_cdc_tasks,
        )

        return typing.cast(None, jsii.invoke(self, "putMysqlSourceConfig", [value]))

    @jsii.member(jsii_name="putOracleSourceConfig")
    def put_oracle_source_config(
        self,
        *,
        drop_large_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
        exclude_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
        include_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
        max_concurrent_backfill_tasks: typing.Optional[jsii.Number] = None,
        max_concurrent_cdc_tasks: typing.Optional[jsii.Number] = None,
        stream_large_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param drop_large_objects: drop_large_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#drop_large_objects GoogleDatastreamStream#drop_large_objects}
        :param exclude_objects: exclude_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#exclude_objects GoogleDatastreamStream#exclude_objects}
        :param include_objects: include_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#include_objects GoogleDatastreamStream#include_objects}
        :param max_concurrent_backfill_tasks: Maximum number of concurrent backfill tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_backfill_tasks GoogleDatastreamStream#max_concurrent_backfill_tasks}
        :param max_concurrent_cdc_tasks: Maximum number of concurrent CDC tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_cdc_tasks GoogleDatastreamStream#max_concurrent_cdc_tasks}
        :param stream_large_objects: stream_large_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#stream_large_objects GoogleDatastreamStream#stream_large_objects}
        '''
        value = GoogleDatastreamStreamSourceConfigOracleSourceConfig(
            drop_large_objects=drop_large_objects,
            exclude_objects=exclude_objects,
            include_objects=include_objects,
            max_concurrent_backfill_tasks=max_concurrent_backfill_tasks,
            max_concurrent_cdc_tasks=max_concurrent_cdc_tasks,
            stream_large_objects=stream_large_objects,
        )

        return typing.cast(None, jsii.invoke(self, "putOracleSourceConfig", [value]))

    @jsii.member(jsii_name="putPostgresqlSourceConfig")
    def put_postgresql_source_config(
        self,
        *,
        publication: builtins.str,
        replication_slot: builtins.str,
        exclude_objects: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        include_objects: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        max_concurrent_backfill_tasks: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param publication: The name of the publication that includes the set of all tables that are defined in the stream's include_objects. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#publication GoogleDatastreamStream#publication}
        :param replication_slot: The name of the logical replication slot that's configured with the pgoutput plugin. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#replication_slot GoogleDatastreamStream#replication_slot}
        :param exclude_objects: exclude_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#exclude_objects GoogleDatastreamStream#exclude_objects}
        :param include_objects: include_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#include_objects GoogleDatastreamStream#include_objects}
        :param max_concurrent_backfill_tasks: Maximum number of concurrent backfill tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_backfill_tasks GoogleDatastreamStream#max_concurrent_backfill_tasks}
        '''
        value = GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig(
            publication=publication,
            replication_slot=replication_slot,
            exclude_objects=exclude_objects,
            include_objects=include_objects,
            max_concurrent_backfill_tasks=max_concurrent_backfill_tasks,
        )

        return typing.cast(None, jsii.invoke(self, "putPostgresqlSourceConfig", [value]))

    @jsii.member(jsii_name="resetMysqlSourceConfig")
    def reset_mysql_source_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlSourceConfig", []))

    @jsii.member(jsii_name="resetOracleSourceConfig")
    def reset_oracle_source_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOracleSourceConfig", []))

    @jsii.member(jsii_name="resetPostgresqlSourceConfig")
    def reset_postgresql_source_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostgresqlSourceConfig", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlSourceConfig")
    def mysql_source_config(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigOutputReference:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigOutputReference, jsii.get(self, "mysqlSourceConfig"))

    @builtins.property
    @jsii.member(jsii_name="oracleSourceConfig")
    def oracle_source_config(
        self,
    ) -> GoogleDatastreamStreamSourceConfigOracleSourceConfigOutputReference:
        return typing.cast(GoogleDatastreamStreamSourceConfigOracleSourceConfigOutputReference, jsii.get(self, "oracleSourceConfig"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlSourceConfig")
    def postgresql_source_config(
        self,
    ) -> "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigOutputReference":
        return typing.cast("GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigOutputReference", jsii.get(self, "postgresqlSourceConfig"))

    @builtins.property
    @jsii.member(jsii_name="mysqlSourceConfigInput")
    def mysql_source_config_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfig], jsii.get(self, "mysqlSourceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="oracleSourceConfigInput")
    def oracle_source_config_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfig], jsii.get(self, "oracleSourceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlSourceConfigInput")
    def postgresql_source_config_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig"], jsii.get(self, "postgresqlSourceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceConnectionProfileInput")
    def source_connection_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceConnectionProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceConnectionProfile")
    def source_connection_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceConnectionProfile"))

    @source_connection_profile.setter
    def source_connection_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad6aaf1380cfd2cad252287f4082eac6cb898c810899506186dbc4bf8daf22af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceConnectionProfile", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDatastreamStreamSourceConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31a3dae34b03d71885cecf9357ff558547f3eba368913731781633806d28251)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "publication": "publication",
        "replication_slot": "replicationSlot",
        "exclude_objects": "excludeObjects",
        "include_objects": "includeObjects",
        "max_concurrent_backfill_tasks": "maxConcurrentBackfillTasks",
    },
)
class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig:
    def __init__(
        self,
        *,
        publication: builtins.str,
        replication_slot: builtins.str,
        exclude_objects: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        include_objects: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        max_concurrent_backfill_tasks: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param publication: The name of the publication that includes the set of all tables that are defined in the stream's include_objects. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#publication GoogleDatastreamStream#publication}
        :param replication_slot: The name of the logical replication slot that's configured with the pgoutput plugin. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#replication_slot GoogleDatastreamStream#replication_slot}
        :param exclude_objects: exclude_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#exclude_objects GoogleDatastreamStream#exclude_objects}
        :param include_objects: include_objects block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#include_objects GoogleDatastreamStream#include_objects}
        :param max_concurrent_backfill_tasks: Maximum number of concurrent backfill tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_backfill_tasks GoogleDatastreamStream#max_concurrent_backfill_tasks}
        '''
        if isinstance(exclude_objects, dict):
            exclude_objects = GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects(**exclude_objects)
        if isinstance(include_objects, dict):
            include_objects = GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects(**include_objects)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__808428853b11ce5518f2909954a6060dbff2919f6b431ea29036573ec47a5a9e)
            check_type(argname="argument publication", value=publication, expected_type=type_hints["publication"])
            check_type(argname="argument replication_slot", value=replication_slot, expected_type=type_hints["replication_slot"])
            check_type(argname="argument exclude_objects", value=exclude_objects, expected_type=type_hints["exclude_objects"])
            check_type(argname="argument include_objects", value=include_objects, expected_type=type_hints["include_objects"])
            check_type(argname="argument max_concurrent_backfill_tasks", value=max_concurrent_backfill_tasks, expected_type=type_hints["max_concurrent_backfill_tasks"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "publication": publication,
            "replication_slot": replication_slot,
        }
        if exclude_objects is not None:
            self._values["exclude_objects"] = exclude_objects
        if include_objects is not None:
            self._values["include_objects"] = include_objects
        if max_concurrent_backfill_tasks is not None:
            self._values["max_concurrent_backfill_tasks"] = max_concurrent_backfill_tasks

    @builtins.property
    def publication(self) -> builtins.str:
        '''The name of the publication that includes the set of all tables that are defined in the stream's include_objects.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#publication GoogleDatastreamStream#publication}
        '''
        result = self._values.get("publication")
        assert result is not None, "Required property 'publication' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replication_slot(self) -> builtins.str:
        '''The name of the logical replication slot that's configured with the pgoutput plugin.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#replication_slot GoogleDatastreamStream#replication_slot}
        '''
        result = self._values.get("replication_slot")
        assert result is not None, "Required property 'replication_slot' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclude_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects"]:
        '''exclude_objects block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#exclude_objects GoogleDatastreamStream#exclude_objects}
        '''
        result = self._values.get("exclude_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects"], result)

    @builtins.property
    def include_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects"]:
        '''include_objects block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#include_objects GoogleDatastreamStream#include_objects}
        '''
        result = self._values.get("include_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects"], result)

    @builtins.property
    def max_concurrent_backfill_tasks(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of concurrent backfill tasks.

        The number should be non
        negative. If not set (or set to 0), the system's default value will be used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#max_concurrent_backfill_tasks GoogleDatastreamStream#max_concurrent_backfill_tasks}
        '''
        result = self._values.get("max_concurrent_backfill_tasks")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects",
    jsii_struct_bases=[],
    name_mapping={"postgresql_schemas": "postgresqlSchemas"},
)
class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects:
    def __init__(
        self,
        *,
        postgresql_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param postgresql_schemas: postgresql_schemas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_schemas GoogleDatastreamStream#postgresql_schemas}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e29e94db22db80391b825274aa101356ab7e352a304616a909e6af086988b3cd)
            check_type(argname="argument postgresql_schemas", value=postgresql_schemas, expected_type=type_hints["postgresql_schemas"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "postgresql_schemas": postgresql_schemas,
        }

    @builtins.property
    def postgresql_schemas(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas"]]:
        '''postgresql_schemas block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_schemas GoogleDatastreamStream#postgresql_schemas}
        '''
        result = self._values.get("postgresql_schemas")
        assert result is not None, "Required property 'postgresql_schemas' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f1ec7569d85a477ed8bff45a112423d432bebeda96fa3cba56b71f779320863)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPostgresqlSchemas")
    def put_postgresql_schemas(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7357a8de26fe6d19f0dc39335d8857dade1ef2d8a7607a53e9c8c90c853808c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPostgresqlSchemas", [value]))

    @builtins.property
    @jsii.member(jsii_name="postgresqlSchemas")
    def postgresql_schemas(
        self,
    ) -> "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasList":
        return typing.cast("GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasList", jsii.get(self, "postgresqlSchemas"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlSchemasInput")
    def postgresql_schemas_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas"]]], jsii.get(self, "postgresqlSchemasInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ca3e8dc69ad3d2a04515b87fd648477a52bee8a5b39096fa3c5f1b8799baf65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas",
    jsii_struct_bases=[],
    name_mapping={"schema": "schema", "postgresql_tables": "postgresqlTables"},
)
class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas:
    def __init__(
        self,
        *,
        schema: builtins.str,
        postgresql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param schema: Database name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema GoogleDatastreamStream#schema}
        :param postgresql_tables: postgresql_tables block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_tables GoogleDatastreamStream#postgresql_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ab9c755671dcb72ed7544f514c592145f56365e5b95a649b0d6f94c1c95cd36)
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument postgresql_tables", value=postgresql_tables, expected_type=type_hints["postgresql_tables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema": schema,
        }
        if postgresql_tables is not None:
            self._values["postgresql_tables"] = postgresql_tables

    @builtins.property
    def schema(self) -> builtins.str:
        '''Database name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema GoogleDatastreamStream#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postgresql_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables"]]]:
        '''postgresql_tables block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_tables GoogleDatastreamStream#postgresql_tables}
        '''
        result = self._values.get("postgresql_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2b23e3a8b8fff9849f506cdc5da63c51c5b568cf8e64f95e0747277f033a75b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ab280d0b6951dbf59487ee28ffa4dc7a0d415841e15d6bd729315e0f3d21658)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__026911ba6a8a154b26cce8f6076802108fd8ba8b5aae82217e54074449b09348)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4b544410ae0e335235da7a0485d647484c5107d1553f7bb5d77fda6f12b3ebb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__32465c8a5123f7748d5d12af75d50a02e4e03f7512e8d78d2ebf2800c09e0097)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__639c90a1909cb8e0b6351c5da127b0700e4b7e5aecff4ffb994acfeec41313b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb0f0a1788e31e44c2c857a038e0dcb2bf0873017a25bb7fc72a77aee9771a85)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPostgresqlTables")
    def put_postgresql_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__768f387107b3e2d568f3f615318c8008107d2a81b53fee05e6b09481297569a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPostgresqlTables", [value]))

    @jsii.member(jsii_name="resetPostgresqlTables")
    def reset_postgresql_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostgresqlTables", []))

    @builtins.property
    @jsii.member(jsii_name="postgresqlTables")
    def postgresql_tables(
        self,
    ) -> "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesList":
        return typing.cast("GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesList", jsii.get(self, "postgresqlTables"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlTablesInput")
    def postgresql_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables"]]], jsii.get(self, "postgresqlTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bb14576f9aae508454cdee9ae78f154183e3f5255aa0bb6a4ea5872cfe4e925)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bf88f993df9076cc30d2d153e548e44f07204c204fe62968953f7c9a4859b1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "postgresql_columns": "postgresqlColumns"},
)
class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        postgresql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        :param postgresql_columns: postgresql_columns block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_columns GoogleDatastreamStream#postgresql_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdf9f84e8cebb18a1de572b141bdbcb6ea00324ecc4f8c7ffb8c95c83888ef15)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument postgresql_columns", value=postgresql_columns, expected_type=type_hints["postgresql_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table": table,
        }
        if postgresql_columns is not None:
            self._values["postgresql_columns"] = postgresql_columns

    @builtins.property
    def table(self) -> builtins.str:
        '''Table name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postgresql_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns"]]]:
        '''postgresql_columns block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_columns GoogleDatastreamStream#postgresql_columns}
        '''
        result = self._values.get("postgresql_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9e5eb5ffbcdf5422543b94cc3b0acee516bd3dda38be6228abb7b293913bc51)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11a917b2a01055d4c5195a98215f278fbdd7fcc1a6c23d6bb32de79c0779fdb6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54cdf8ae6f8c1a5ec4622cd1096e5b446c2e5d0eb1e6f5b55cf0a65dc880e1e4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__48f72940785b8c1ed26db8cb02b9b3e6ab4f497e3eca292b3a34998038d74e35)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b776b0647aa3cf5afc6063ce5cd6c2e2fbba6ef586265125516eea01070b5fc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af611c34ab88e83e5e7c1c0ed901a79bf24c85b08a5f95cd430d129ad822feca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__985011c4b22efeb98f5eabc191eb3f29e884e8f772a8f104926e5be2a53257a7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPostgresqlColumns")
    def put_postgresql_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75518d4255529283a0cc3050eb38a2fe014e1b2bef989346e6926dce84cbbccd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPostgresqlColumns", [value]))

    @jsii.member(jsii_name="resetPostgresqlColumns")
    def reset_postgresql_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostgresqlColumns", []))

    @builtins.property
    @jsii.member(jsii_name="postgresqlColumns")
    def postgresql_columns(
        self,
    ) -> "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList":
        return typing.cast("GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList", jsii.get(self, "postgresqlColumns"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlColumnsInput")
    def postgresql_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns"]]], jsii.get(self, "postgresqlColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dec340d5930a9f31f5b82df61eb7380a68a44911d2cd51cf3227883f410579a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0479f6167dc3f97f4ed43abe9bda13447286b226c594efd4d9b1b71b2bee7c7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "data_type": "dataType",
        "nullable": "nullable",
        "ordinal_position": "ordinalPosition",
        "primary_key": "primaryKey",
    },
)
class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns:
    def __init__(
        self,
        *,
        column: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ordinal_position: typing.Optional[jsii.Number] = None,
        primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param column: Column name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        :param data_type: The PostgreSQL data type. Full data types list can be found here: https://www.postgresql.org/docs/current/datatype.html. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        :param nullable: Whether or not the column can accept a null value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        :param ordinal_position: The ordinal position of the column in the table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        :param primary_key: Whether or not the column represents a primary key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c374ba9568fefe81d56a433cddbb7dd8413494101c656d826bf8cb17e639a77e)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
            check_type(argname="argument ordinal_position", value=ordinal_position, expected_type=type_hints["ordinal_position"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if column is not None:
            self._values["column"] = column
        if data_type is not None:
            self._values["data_type"] = data_type
        if nullable is not None:
            self._values["nullable"] = nullable
        if ordinal_position is not None:
            self._values["ordinal_position"] = ordinal_position
        if primary_key is not None:
            self._values["primary_key"] = primary_key

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The PostgreSQL data type. Full data types list can be found here: https://www.postgresql.org/docs/current/datatype.html.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column can accept a null value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ordinal_position(self) -> typing.Optional[jsii.Number]:
        '''The ordinal position of the column in the table.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        '''
        result = self._values.get("ordinal_position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column represents a primary key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4c163c1c608ac6fbd89879bae3d1fd82f3963f0c1362f098dbcbb5f6c372aae)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5f321069c5eb542272547501bf026a807511ee4316279a122c694b71d5aa467)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac5961506383aff77857f29576d4a9c3ab8347fa5c8d1c082e9e6bc0cb38eb6d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cde000132a084546778016334e7c17d4ee0387c64e18da19a029204f02b036c7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c0df27265f0691ae5f8b39d925b58e9db8998b035520085e13fe34acf89e516)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7391d040483235dd4ad102211a520eaf092c8aba2e9e1bb784957badb166f46f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6af5c2b4ee3b0cd9a3d09265c0bfffddc8a98b483bdb545beba82b0158eefc3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetColumn")
    def reset_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumn", []))

    @jsii.member(jsii_name="resetDataType")
    def reset_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataType", []))

    @jsii.member(jsii_name="resetNullable")
    def reset_nullable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNullable", []))

    @jsii.member(jsii_name="resetOrdinalPosition")
    def reset_ordinal_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrdinalPosition", []))

    @jsii.member(jsii_name="resetPrimaryKey")
    def reset_primary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryKey", []))

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property
    @jsii.member(jsii_name="precision")
    def precision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "precision"))

    @builtins.property
    @jsii.member(jsii_name="scale")
    def scale(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scale"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTypeInput")
    def data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nullableInput")
    def nullable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "nullableInput"))

    @builtins.property
    @jsii.member(jsii_name="ordinalPositionInput")
    def ordinal_position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ordinalPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcb4cf98c716e9255acc7286b2746e598454f879f80548d3436897bbef6a529d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9591bd6c5ad0285c687125b4f8830670cd9e596ca2caf5fc88a87577bf632b57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "nullable"))

    @nullable.setter
    def nullable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9056760022d21d71916e50cecd95c0ea88a8dc446455402a3cb866bba251ae90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @ordinal_position.setter
    def ordinal_position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5a948729cf8e622a973d66bc24de9f6cdd493c4d0335053e61baaee36a0f2c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ordinalPosition", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "primaryKey"))

    @primary_key.setter
    def primary_key(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcb60d5f9f736982578cdbbc2e6c7fd16875488db500030a77cbd2b237532c3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c74d8384807d3bcc937f21dfeff59bbc32b552b0f278ba4bf058c68a539a883)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects",
    jsii_struct_bases=[],
    name_mapping={"postgresql_schemas": "postgresqlSchemas"},
)
class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects:
    def __init__(
        self,
        *,
        postgresql_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param postgresql_schemas: postgresql_schemas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_schemas GoogleDatastreamStream#postgresql_schemas}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a140786a024a194a696f5014921560df44580d133ecd1c619c8e5e18add8aeed)
            check_type(argname="argument postgresql_schemas", value=postgresql_schemas, expected_type=type_hints["postgresql_schemas"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "postgresql_schemas": postgresql_schemas,
        }

    @builtins.property
    def postgresql_schemas(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas"]]:
        '''postgresql_schemas block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_schemas GoogleDatastreamStream#postgresql_schemas}
        '''
        result = self._values.get("postgresql_schemas")
        assert result is not None, "Required property 'postgresql_schemas' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b819b27bd69565e53ec9752d2e1411f14eae784918386d890ac1bf7f8b7887c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPostgresqlSchemas")
    def put_postgresql_schemas(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7adbc8f5b6d1079cffd8cd37056f8d1cc7130846e8abe3717099c8b200809aff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPostgresqlSchemas", [value]))

    @builtins.property
    @jsii.member(jsii_name="postgresqlSchemas")
    def postgresql_schemas(
        self,
    ) -> "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasList":
        return typing.cast("GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasList", jsii.get(self, "postgresqlSchemas"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlSchemasInput")
    def postgresql_schemas_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas"]]], jsii.get(self, "postgresqlSchemasInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfd478c0d010a99b6044540a720948d8e0f62adadeaf70e010b547421e70b0d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas",
    jsii_struct_bases=[],
    name_mapping={"schema": "schema", "postgresql_tables": "postgresqlTables"},
)
class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas:
    def __init__(
        self,
        *,
        schema: builtins.str,
        postgresql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param schema: Database name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema GoogleDatastreamStream#schema}
        :param postgresql_tables: postgresql_tables block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_tables GoogleDatastreamStream#postgresql_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13cb4f6f5aaa105019489a12d97f546fe100ac275358231f6fa95081e265f3b8)
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument postgresql_tables", value=postgresql_tables, expected_type=type_hints["postgresql_tables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema": schema,
        }
        if postgresql_tables is not None:
            self._values["postgresql_tables"] = postgresql_tables

    @builtins.property
    def schema(self) -> builtins.str:
        '''Database name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#schema GoogleDatastreamStream#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postgresql_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables"]]]:
        '''postgresql_tables block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_tables GoogleDatastreamStream#postgresql_tables}
        '''
        result = self._values.get("postgresql_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ef5e5d16e6215393f7c7c0df02b441820ff5500bf553f6808ea670ea84b8da3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a5faf90af1108a5e02f7f75b630a45bd622bbc8837d6bff00db599ca227c9e9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1101edcddc787719f0312de054fa62df117f3d7fe04b08e13495f0d362f6c04a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c9cf3b739b955f1da379f0166ae6e51283a17b6a53ca615cde9d98675ab8e6a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fe2f1ad01b17ddd9140f903973ef32a45e1dbe5e1935cb1b2ece9e5a1e6c03be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8de245e9b46bb49bbbb8ddaa94a06821782f372d29f3fee031e86ccce933ead3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6032ba065b9e4b87b379b8451042de3f0349cc820b7aa0309abb3b56058edd22)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPostgresqlTables")
    def put_postgresql_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7292523b67a0d518360393a870bb8438d8670848954003d3370c30ca7968d63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPostgresqlTables", [value]))

    @jsii.member(jsii_name="resetPostgresqlTables")
    def reset_postgresql_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostgresqlTables", []))

    @builtins.property
    @jsii.member(jsii_name="postgresqlTables")
    def postgresql_tables(
        self,
    ) -> "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesList":
        return typing.cast("GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesList", jsii.get(self, "postgresqlTables"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlTablesInput")
    def postgresql_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables"]]], jsii.get(self, "postgresqlTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aa5ee58a7173fb4cd1f054b6caecfe39d3814741acfe79bcfc1be6a02b68a89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4c8d6aebe392f588ad76e59670ee0e8b202cb1c4a84a1332a22918f0d04ce18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "postgresql_columns": "postgresqlColumns"},
)
class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        postgresql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        :param postgresql_columns: postgresql_columns block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_columns GoogleDatastreamStream#postgresql_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eda4783896c6e83094c50a0c20ff8b5795507b65a1c411668c3007386dd22397)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument postgresql_columns", value=postgresql_columns, expected_type=type_hints["postgresql_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table": table,
        }
        if postgresql_columns is not None:
            self._values["postgresql_columns"] = postgresql_columns

    @builtins.property
    def table(self) -> builtins.str:
        '''Table name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#table GoogleDatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postgresql_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns"]]]:
        '''postgresql_columns block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_columns GoogleDatastreamStream#postgresql_columns}
        '''
        result = self._values.get("postgresql_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__901f53a8c246324974d705fbcc358f41e2324467f0e296c25328fda002b5b541)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bde972421b6a5a304a8e3e56adbf17a5df04ce271984af74c606e4642adb0a68)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d37fcde47ec92bc6b3dec6089539448ceff44482e571daaa2d0f47dafc995e02)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aad07e66bfd3e9879a014bda027e08327e4a301104fa9b400aab9ceccab94113)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b2b18bc9b4cc9e07eebfc90dea02c8f24c68782d43a5d14a8fc6925b7853340)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e420f9301810b955801e9e6a4354a88ed637705fffd17f0d4a856c58d54a1ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f788138d7ab18c27e953964d4ec3023d8adcf8c576164dd391d32fac6a60f06)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPostgresqlColumns")
    def put_postgresql_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec5868d2e76b06d37a92e521ee9bbcf947f9a8c5853435978e75c24566aeab90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPostgresqlColumns", [value]))

    @jsii.member(jsii_name="resetPostgresqlColumns")
    def reset_postgresql_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostgresqlColumns", []))

    @builtins.property
    @jsii.member(jsii_name="postgresqlColumns")
    def postgresql_columns(
        self,
    ) -> "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList":
        return typing.cast("GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList", jsii.get(self, "postgresqlColumns"))

    @builtins.property
    @jsii.member(jsii_name="postgresqlColumnsInput")
    def postgresql_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns"]]], jsii.get(self, "postgresqlColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f6d8a7718ce1edb7e595968bfae67d6878bf55795cb5a9518a05622366aa8a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efac68f460992bed8c5b38fb23f8db9e62c2d8f21eafc972d879e92a213d3922)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "data_type": "dataType",
        "nullable": "nullable",
        "ordinal_position": "ordinalPosition",
        "primary_key": "primaryKey",
    },
)
class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns:
    def __init__(
        self,
        *,
        column: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ordinal_position: typing.Optional[jsii.Number] = None,
        primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param column: Column name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        :param data_type: The PostgreSQL data type. Full data types list can be found here: https://www.postgresql.org/docs/current/datatype.html. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        :param nullable: Whether or not the column can accept a null value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        :param ordinal_position: The ordinal position of the column in the table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        :param primary_key: Whether or not the column represents a primary key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f82d6f2db315d340e7b88786b3820bff3c60d4dfb15a17d5710309de0cf7115)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
            check_type(argname="argument ordinal_position", value=ordinal_position, expected_type=type_hints["ordinal_position"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if column is not None:
            self._values["column"] = column
        if data_type is not None:
            self._values["data_type"] = data_type
        if nullable is not None:
            self._values["nullable"] = nullable
        if ordinal_position is not None:
            self._values["ordinal_position"] = ordinal_position
        if primary_key is not None:
            self._values["primary_key"] = primary_key

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#column GoogleDatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The PostgreSQL data type. Full data types list can be found here: https://www.postgresql.org/docs/current/datatype.html.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column can accept a null value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ordinal_position(self) -> typing.Optional[jsii.Number]:
        '''The ordinal position of the column in the table.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        '''
        result = self._values.get("ordinal_position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column represents a primary key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c916b7d36c1f33f96c1f7e3f40982cbce8712440c326abe11b70ce9cd546e14d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef889fa19c3b481432cd15069f649a9861b5eef469c50abe668f56ad80df5837)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afa250b1b76e0f59b5b3080037cae2d573072f89e0ba759e34a95b76efd0ed8a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a7b1297223926e11fe96e3036d07d8933c6dd01dcb7b6208f557a7434030aa2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2a0e22c8221b04cb9e91c46cfe8d45d269e68f82aa5eeff5e3d3bbda13ab3d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6e89e886c1cd65e2347c43b33c87451409113595815e3eb7152e5c88cbca782)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f876c0484c091043838839e387f742c77b38682ef567978c434e890da6cd43b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetColumn")
    def reset_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumn", []))

    @jsii.member(jsii_name="resetDataType")
    def reset_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataType", []))

    @jsii.member(jsii_name="resetNullable")
    def reset_nullable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNullable", []))

    @jsii.member(jsii_name="resetOrdinalPosition")
    def reset_ordinal_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrdinalPosition", []))

    @jsii.member(jsii_name="resetPrimaryKey")
    def reset_primary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryKey", []))

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property
    @jsii.member(jsii_name="precision")
    def precision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "precision"))

    @builtins.property
    @jsii.member(jsii_name="scale")
    def scale(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scale"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTypeInput")
    def data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nullableInput")
    def nullable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "nullableInput"))

    @builtins.property
    @jsii.member(jsii_name="ordinalPositionInput")
    def ordinal_position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ordinalPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a355c251a996ef1766abac034090658c23c783ec3df8928cc97a347f3c598332)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c288cf196dd4b751ca9c112fbffd013aaf86a8aa3f12c241780e27eb21c04356)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "nullable"))

    @nullable.setter
    def nullable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87ad480a8b9c4f6ca0e4a37d62573ad88402f62b2bf70f87586a53a3f2d257b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @ordinal_position.setter
    def ordinal_position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76871aab1d8b5486ac8ae2851dfb756949d38d10ef7ea66052bc445e029f8769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ordinalPosition", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "primaryKey"))

    @primary_key.setter
    def primary_key(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d32f13be1398922ee07a65d04d76515ec90fec2d8433c4d17ea0ee7c6467df5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d40e1798547f1ccc5023d425d24025692b6bab18ccb139aa66142bd7e50d3abf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1728459c0682ba074c24d877566017f422e2e8a4dfbddd884a5279a929f7ea90)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExcludeObjects")
    def put_exclude_objects(
        self,
        *,
        postgresql_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param postgresql_schemas: postgresql_schemas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_schemas GoogleDatastreamStream#postgresql_schemas}
        '''
        value = GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects(
            postgresql_schemas=postgresql_schemas
        )

        return typing.cast(None, jsii.invoke(self, "putExcludeObjects", [value]))

    @jsii.member(jsii_name="putIncludeObjects")
    def put_include_objects(
        self,
        *,
        postgresql_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param postgresql_schemas: postgresql_schemas block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#postgresql_schemas GoogleDatastreamStream#postgresql_schemas}
        '''
        value = GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects(
            postgresql_schemas=postgresql_schemas
        )

        return typing.cast(None, jsii.invoke(self, "putIncludeObjects", [value]))

    @jsii.member(jsii_name="resetExcludeObjects")
    def reset_exclude_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeObjects", []))

    @jsii.member(jsii_name="resetIncludeObjects")
    def reset_include_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeObjects", []))

    @jsii.member(jsii_name="resetMaxConcurrentBackfillTasks")
    def reset_max_concurrent_backfill_tasks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentBackfillTasks", []))

    @builtins.property
    @jsii.member(jsii_name="excludeObjects")
    def exclude_objects(
        self,
    ) -> GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsOutputReference:
        return typing.cast(GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsOutputReference, jsii.get(self, "excludeObjects"))

    @builtins.property
    @jsii.member(jsii_name="includeObjects")
    def include_objects(
        self,
    ) -> GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsOutputReference:
        return typing.cast(GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsOutputReference, jsii.get(self, "includeObjects"))

    @builtins.property
    @jsii.member(jsii_name="excludeObjectsInput")
    def exclude_objects_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects], jsii.get(self, "excludeObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeObjectsInput")
    def include_objects_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects], jsii.get(self, "includeObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentBackfillTasksInput")
    def max_concurrent_backfill_tasks_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentBackfillTasksInput"))

    @builtins.property
    @jsii.member(jsii_name="publicationInput")
    def publication_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicationInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationSlotInput")
    def replication_slot_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationSlotInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentBackfillTasks"))

    @max_concurrent_backfill_tasks.setter
    def max_concurrent_backfill_tasks(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__576c8fd329963d004ee0fa8801f4ecff13b9e62e022cbb2a59d04c0281764b17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentBackfillTasks", value)

    @builtins.property
    @jsii.member(jsii_name="publication")
    def publication(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publication"))

    @publication.setter
    def publication(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8b50c4dc34ecff31d1a38cb8a8407323ede120571e38eddc5365c67c3d2ceaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publication", value)

    @builtins.property
    @jsii.member(jsii_name="replicationSlot")
    def replication_slot(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationSlot"))

    @replication_slot.setter
    def replication_slot(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a08267f1f7e0fff1cf0bcec0dafca7e35cc564cf246dfcd184170786d8ca794d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationSlot", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c91f48dc73baf8eb82b8ce7b61498a8fbf3d58511e81bfcf60b0d05c2716c493)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDatastreamStreamTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#create GoogleDatastreamStream#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#delete GoogleDatastreamStream#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#update GoogleDatastreamStream#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a54b49f7561784b6ddbf39b45bfd0f91cd4d531a183f057a0f51c1fb036c6ee4)
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
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#create GoogleDatastreamStream#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#delete GoogleDatastreamStream#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_datastream_stream#update GoogleDatastreamStream#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a1e593819993f0b26e94eb2825132a675053b005efe8ffb05266fd2c2530166)
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
            type_hints = typing.get_type_hints(_typecheckingstub__72ae4642fb1a34ac292bc77f8755496644a696b2005d238ad3d096cf94340334)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f50f1677bf065b391c40444994d038f923d9d5c282b68e34cbff128a610e0e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27df4af47c20495c8bd3cfc96cc0d9e42b03499ba5a08622470954ed4ff13101)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9644ba1934244050f95ca839e3c9e108ad0d0d1156a6d8051eae93e46bb4269a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDatastreamStream",
    "GoogleDatastreamStreamBackfillAll",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjects",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference",
    "GoogleDatastreamStreamBackfillAllOracleExcludedObjects",
    "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas",
    "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasList",
    "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables",
    "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesList",
    "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns",
    "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumnsList",
    "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumnsOutputReference",
    "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOutputReference",
    "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOutputReference",
    "GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOutputReference",
    "GoogleDatastreamStreamBackfillAllOutputReference",
    "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects",
    "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsOutputReference",
    "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas",
    "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasList",
    "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasOutputReference",
    "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables",
    "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesList",
    "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesOutputReference",
    "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns",
    "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList",
    "GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference",
    "GoogleDatastreamStreamBackfillNone",
    "GoogleDatastreamStreamBackfillNoneOutputReference",
    "GoogleDatastreamStreamConfig",
    "GoogleDatastreamStreamDestinationConfig",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference",
    "GoogleDatastreamStreamDestinationConfigGcsDestinationConfig",
    "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat",
    "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference",
    "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat",
    "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference",
    "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigOutputReference",
    "GoogleDatastreamStreamDestinationConfigOutputReference",
    "GoogleDatastreamStreamSourceConfig",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfig",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigOutputReference",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfig",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjectsOutputReference",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasList",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesList",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumnsList",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumnsOutputReference",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOutputReference",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOutputReference",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOutputReference",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasList",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesList",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumnsList",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumnsOutputReference",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOutputReference",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOutputReference",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOutputReference",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigOutputReference",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects",
    "GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjectsOutputReference",
    "GoogleDatastreamStreamSourceConfigOutputReference",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsOutputReference",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasList",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasOutputReference",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesList",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesOutputReference",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsOutputReference",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasList",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasOutputReference",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesList",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesOutputReference",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsList",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumnsOutputReference",
    "GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigOutputReference",
    "GoogleDatastreamStreamTimeouts",
    "GoogleDatastreamStreamTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__b6cfa931a0c0c189dada75078e20e325e1684379e1ca40acf3c5e5b9c924ed26(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    destination_config: typing.Union[GoogleDatastreamStreamDestinationConfig, typing.Dict[builtins.str, typing.Any]],
    display_name: builtins.str,
    location: builtins.str,
    source_config: typing.Union[GoogleDatastreamStreamSourceConfig, typing.Dict[builtins.str, typing.Any]],
    stream_id: builtins.str,
    backfill_all: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAll, typing.Dict[builtins.str, typing.Any]]] = None,
    backfill_none: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillNone, typing.Dict[builtins.str, typing.Any]]] = None,
    customer_managed_encryption_key: typing.Optional[builtins.str] = None,
    desired_state: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleDatastreamStreamTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__649154746d40cf79873b5aae4fd16769e00b6f7d4efd62ad25a2ff95a0cd5f33(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74f7b558fd7d27092d7ff81ee82d13e54010ef0007382db2c763be48aea337d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f02e6d6086a6388386fbb0384210f4e368b675aedef36739e15a9b27dc467a86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ece6a77832fb6e89cc0916a10ebc588b04c7d7e93bf43677ad16f9563954cdc9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f14ff4627f324370937935159e22c59189775d0e3b599757fff0ae7935aca61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6f63ddf26cb02e92cafbfd7bc5446de232f6b8cb951cc5271c9cd8ef7edbd70(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08807dc9fe2f3212f60603e2be9674d576d9b9ebb97552f37256b43f078e57e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c2f2d9b51d02843746ef23bac88dfc96d8afb17d58d75cfc3fd4c132223b5fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83b1410afdedd1ac85863a7d2b94759e47bfea699a0ad11b60e2b915ef038f04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29d6dac06c9011c575a9755f405c8c91c314097f849d543ea610c2ae0604ac9(
    *,
    mysql_excluded_objects: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    oracle_excluded_objects: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllOracleExcludedObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    postgresql_excluded_objects: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d07bf1e73cbfa0c9924cbdd112f8758d8c5843cb05b182d0821feebbecf1bbfe(
    *,
    mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__520481cec23840384472636822f5e61482b5d1f652a122cd771b9d999695e41c(
    *,
    database: builtins.str,
    mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42870644565e23d6a0facda4476561b2c813f8b187a9bef2d4b42bd3b22f4ad7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c27e6265ec073c6cb9d937296a3009c85694518ceb542eb262dc396c0fa0643(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b9f5caf8e7a7472f002063d637ce85c365c019c129961190ee0484f83cb0204(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df989554faa58557b3cee076a0334b3352d497fa9a172a9bc1154b271b849c0d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff79f76bcf20116f1f916672658b25c9c6061a155abec3dc69a9fe18fcebc28(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef052bf283a0faa4298ce68f02ad4567fa25c2230ddec569bcbb3eee18d62299(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3636dc049bfc21560723eff546dfc6111fc1c67103fa20091fcb54e69eb14642(
    *,
    table: builtins.str,
    mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb36c3ec485d5aa4159c543dbc6060937941194b2d7d16197d5fb5b186c37df9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ea3aa0c93b140d0d206e8e869f0817da6984fb7a0b1aff3d6241d5e683dbbe6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ad0c9c602594fd4c30646475e0cb03862cdafe47fef23ee13c7b73b8b81d3bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e409c71a7a46ac3ff0a29f111eb9a54fb36f9b824b997eebe0be60e76c7c343(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0be506fa80b767248dcaa2cb7ed0462bf54b31e761efd4e0fa33f50b4cc6fe9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd33626f965d1fd3a29041aa974d9db1d19cf1b45b7027bfc2e9bd65550d21d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23a54185e20f6073f2e24e14685a1bb95703a2f3f4ab9e6eea9d3117b60799c9(
    *,
    collation: typing.Optional[builtins.str] = None,
    column: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ordinal_position: typing.Optional[jsii.Number] = None,
    primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e6d7e7079d2c891205e2b32b0cf2ceba725f724854f198bf8512979a5696ce8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84e67f89a6476bdc5c731333cf2029e4a5c782f368d3d69f03978d2ce9dcd94b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa3cdc2a83c6840973d4070e34bf50a07ee5f2c7d1f3c68e499ac847bfa79317(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22b091b27124f81de04d4b89dc1049358fc60349f3193740d406a0ce1c9e7eeb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88ef5e48f6385d0236f06a58e25f81251bbc3e6f2240cd75930e6be6beaec4de(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64de49e3b7a392b9d7c9e39a5e5b791d02929fb6fb384bc5ded7da1c10e90da(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7292c72a6c771de19158c3d655adc2ba6b3d55d617a83d86255518effa23ba98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbe8e9c9cb2a678b797af0d6f265ede6140c005c291f7a871610e2b0c46c1239(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5e78f3a0e42427fb9fe7d3218cf22fcd63107183474d933dbe292a0f22ada60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__801b81a5be1dff9dc10685707b5806e4749464fea9dee3509b069be09a39915d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a4491c86d6cbca170107672efa5ae073217977e38d890ee684dfabffcdc9bbc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8adf2449960f783a3598bbe1db28d2f83ca4c95a6ca774684164731a9ca4603(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3cfd6c4c2f5f53f106b06e68701b9e7338a0198f1de4971a3980cb71319134f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e5c86192b35d7aa9f1c9ff0b2312d4c56114766b1948aeaa6cdb4a187c7447(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5510498980068046efbd3bccc489edaa11d41baf610cf3c6d8b04640da29f441(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1393719f87438cd6e681938c318697c567154ef4d21de037b9794b496d5c053(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5cdd451c93c14f8bf1348dbc84d1613ee34bee075f1a7ef30641b00e9cc6ddf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40a46438b33027c86396b4bad6c02ccc4329f55d360d33ee604e8932c6d1d25f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb2b89ed5c7ab305b2df59f9f1fcae91cadc3414f28c3659364e57a3e1b6dbe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6be4542a5978109673a55f553153be687fb0155ae52e28084709f661e644b3d1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a8764873fb24dfdd954a5d2dbc34cad2573c675bedecb4826b1febb63d5437b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed873de9162601787f1de0b1f1d7bbc82ff2ff4f4f29dcdd5060713a530c99bb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b17ebe8e257a4918dda760ce5f15ec271e6f36463b2e0b3b2102f151e7afa5a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72168f0c6c5360f01d1caa68b898ee8a3874c0c09c031475e80aefbaf55f483b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49719e784f731e00fa4b5f129ee237712081738ae7d610fb8420b43adc072ede(
    value: typing.Optional[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91d62ed480f3fa3b3b42fa502a9ed016297cfd3f897f0d05c49b43aae31ddb03(
    *,
    oracle_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cde81619ce4f9773e3bcac1d1eac26e1b80fef0034c22df9c39c4e57b6311b4c(
    *,
    schema: builtins.str,
    oracle_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efd3094acab0bcbe30a0b24b7dad2112c364cfae80d2a80c6697772945bf2553(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__928c0c3beaf230a91a1648e8095c38efa703030d4607ea7fef17a1623a7d98dd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b57c8885adaf03769ebcea16cb4e45db9aa7f7de2bbd42b9b8c8d738b560f82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddb5bb1ba02934848b7dece18ad408f2efb82b210e3637cc254096f2d0814a51(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d3399ec8a222bb8a85a44b0854195351843bd4a4bb6613e6006fd9f37045295(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f267140b0f46f87b73bb114fa99a63577637d4a8dee15b398cca4b60ccbed71c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51232ab056e0830dca1741ae338bc8911ef6316f203b0c9de5aabfd3cb9b2cfd(
    *,
    table: builtins.str,
    oracle_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ac0558b1c2ece320fa4dd8665aa9be2324747ec194a0ee4842c9109d5ac45e8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c75cfd5dc4c03ddaf75df1d7d5a2db884121a8f1502de1723dfc2495d0bd21d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26a166dd5d37dc758abf6b4d97af1cf1665a16821eb73be6a3e752eeaa123335(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53ff14e96c500d547e3d544e1a0083ef9b73685b45888cb81fc03f912bdf93b4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca136cff12962de157b6784784f22f0c600e4e270e32ad220c5e85e0957cd868(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c19f83c7d83548c4ba9ca4024d69087f17cfa338fa7dcd1e98228c5218f442a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6355fb3a37c3f3b9017f417fa31d41e8a5e56b36ea746998b568fb7cc67e6588(
    *,
    column: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2c030ca32bf48f1135773c6c03c88149b97649d699cbaaf236e8eae9a3a6686(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f56c77e1951d088194c6ea4562e0f3ef439f4c6c1a1ef5c74627a0cee838ad3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__749a511324ac27fc60717fbc9ce9066c2dab773aab0878f7a0152671e39504e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4813c8156e1fdf7dd18e62a46dccc5f9bf4402e149c5f11a04cd2c70b38f083c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ace209faaa8a99572f83638be39226ba65475edc2ce0e6657afa9476701eaf5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fd0e3f4fe524540ed70bf1b235bf4cd87cb21e5055ddfdd90d12c9e5f0b5f68(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e060e394a8ce41c77c28adbb65536007b66f35a08382b6a21c86bbd4839c1b0a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d72ec20fa92d21619bfacfd46de060e09f08a3b95cfee84482c86ebaa856875a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__499a2274d77bc70280b900bdc07a22cfcf1b3f5138fcc8bd791fb02f5a772779(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c535116d5034ab37245aff3b1c42e402a0532da5c60a9b029e68a9ab047b084c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d02a3641f2ca7316c945da61c399ff690cacb68085cb3dba58aca46b209a39e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb210e0fee35ea40f225c994acfe3f4bf9a9f56055b4aa0c64aa1fdca4bd4c6d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTablesOracleColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01e7e8a63e4307997ac247f2dfeba2479e317c223d082c798e9e777556014ce1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f26d13db4081a2a4b32bbc3da771f78c6f7105dceeb3be840e605fe30edd7593(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9e126b93e12b18d38500307735ddc6ed1fc3cda056ef9e6e21d7812fd71e1cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__520f00bd2dcf608c4814507927cf9024a65f669914e7f2cf3c4c9ec5f9ce676c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemasOracleTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e4ef90208ebedc1c370f7d08defb352230959ad705bc14c6bed5b2469b301c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9a12920a531b030c68168a271c0023b324bca863476d97d397ed66b25f724c4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abf152989bccdbf713d22bf06bdbfe4777e9fd9b4b03d02d9e1e63abc37ae21d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b40950d0c225b2691d41a692c78d5b61b54fd9f92fc7642d3bfb6bdc468aa8d5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllOracleExcludedObjectsOracleSchemas, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfa0f6695759b22c658d74737ec0b2786a3083ffb1c2bbd240901cf4df8b607e(
    value: typing.Optional[GoogleDatastreamStreamBackfillAllOracleExcludedObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e274f1c79b478e8a9935941ed6e1cae337452327e7e0df1b2e287933f42cb449(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e18596f2739b568b00dc8878957e1a0ae36c322e4460e1efcc618a1fbd80dfb(
    value: typing.Optional[GoogleDatastreamStreamBackfillAll],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6934e68e3ff15aace86a557b5fcdef40790b7d1dcfeba766a0482fa1b38802a(
    *,
    postgresql_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef0e1e63c4b7a5a04debeff85c97f3fd7bd6c6cb80d20711b3ba3278d80ec353(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d91185c63066f069f351201e0ff47747a96ec09dd3d9962a3f4b1ecffa3cc223(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99032ce0897661a0f857e5fdc2766dd3f40641553834bb1514286172ba319d20(
    value: typing.Optional[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05a169c1d9312cae3424b4cf7316597bc578cadf1937be01bf6b4ef31ff318b0(
    *,
    schema: builtins.str,
    postgresql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ba383460f26f69ba509fb5e772f486a53c196fbdc4e4109ae394c6bda7d76e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c89c447c39c8b15f01815481c20a0fa4bc29a528957254b6fed496cdfa521837(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52e5ea0a86139b5c5893e6e74f4e56228601a4e9fdec1fb5cb8bc6efbdaf6c38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__025e75d4d4563f72d050a070442264c7450e2755ae7b3f1c8dbaf058003dcb8b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c24b1a64202a816b124f72f8206772a1574306d6747149d57b1abeeef5e0d253(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52aba87205fd056dc50e1d9ab17060ed7bcd93865687544a06530b6752afc77a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36573c962ad63512915d06f83c5854c269c638dbe7c38cb58a8d1fab15819375(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6831d7f7a468c6c62d6d3d695ca30ce45020caa7ead3c11a5a706b09a168e598(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00de054fb9da01b6f9d9713f3b8c7fc4cb3590238f567337fbd0c7dcaa42c50c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__699a4a9e23e2db77d0b2d6fe84ec37ae780ddbfc518797cb891ca259d802c120(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemas]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b66fc593b40d3a7b31ee6b94969b31d2e732a6d05aa0e9b4c3c7737cfdef21dd(
    *,
    table: builtins.str,
    postgresql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a24790b4632522537214a52da553dea21b2a740d5afcccf1e1b47fc04956b675(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b435f756e86cd7415b5bbb8004f2b3f6773179250ea89211b7aaa6f7d2421e0f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c52d8fdd0c3efc72761bf6ac3bf80e9b006889cf2bf36643054e3142c3ed34c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61b548f4d3f09166d5113b36c98d7908a6e5bf45402f26282847cc2dab9d224d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ce19649192b891826321da0402e0912b85150724012173ebb6747ac34670bf2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c44dd15e41e4216e2593b6cd4e5be954f6c1ffb2443e9a05cba66f99a6f104a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1c79a43e282268cfc73a2de510a4c49ef4819bcd34be3c28678519795254fb6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e5f7a8b9b86c0b9277ddebbb62854902117db8943f26ca12e6196c73668035(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dd4177e6b293e2281bec0b4667e1fcdcad37080a4f087467b0afc9ddb621c3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30e613c4dbcf9c96bda77a7ac2c0671acf5b6b35d9b3d82274aebeff963dae25(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTables]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011222891dbbe92444a6ae0e8752cd8607a8cdec716b117cfcee323e5e366464(
    *,
    column: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ordinal_position: typing.Optional[jsii.Number] = None,
    primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2492c75d0ab44294e30a17a291ba51204e50947e1bbf9288f00559561142edad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__601b097b3324b6691855ef65c2e51f0a8abc01adfc4f0ec18e55971bbb6d7d56(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4ee78b7df0d1bb3aa0efb76e5a9799adbfac935152947349902a90da95d4ccc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a173d2f2f24ab7b5e141d45d3b19cc57f72b9fc2d78f1aca0a4f1c769482300e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e67d04b5a0d51d107a8fbd1a497417942c8e8069e0df9c1731d8534753b21de(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9d933cf1d30658c9a9f7a46ac398cc952069a345aa2b6b31c8ce27f4e6fdcad(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f37c7b49c96139951341e37959e5380814a66382aa5fff66f9883a88c641b23(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d27d25ec834ff7241cf86e0235c339433b7fa6db163ae3862f8b73a25ffe6bbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd0c5fac24dec8a1750574e186d9ca3341b636104bc89b79c04f6b7cc590f7d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ae84dc4aedb19866d3c92c409974db9a499f250d06e5cd318eaa311a3ec2c49(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bf1287f27d9d8d62e80f8bcf3f03d5efc1a9bb0b5db2dda9a5a55ade660f0f8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4a5eb9e007468dac28d2d6c7c80ea552e014a3c9ed3825c336e28b548e08d09(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aacc1fba903eb1404c6a096687be6ef2b6887a9d9da5d17d7eabe3833f94cc71(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7d92abc899aebc8d6d75893b1acd1ccfce0f432db79b875d3d4e45b3724468b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa1cb735e7372c389d187e9df62ce48602d5e810e1d37efcc2c795f44eae0eb(
    value: typing.Optional[GoogleDatastreamStreamBackfillNone],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8212616678ebc8f5f13dc67f8ecb8284c7ae5d6006e98280adbb52774b08f47(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    destination_config: typing.Union[GoogleDatastreamStreamDestinationConfig, typing.Dict[builtins.str, typing.Any]],
    display_name: builtins.str,
    location: builtins.str,
    source_config: typing.Union[GoogleDatastreamStreamSourceConfig, typing.Dict[builtins.str, typing.Any]],
    stream_id: builtins.str,
    backfill_all: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAll, typing.Dict[builtins.str, typing.Any]]] = None,
    backfill_none: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillNone, typing.Dict[builtins.str, typing.Any]]] = None,
    customer_managed_encryption_key: typing.Optional[builtins.str] = None,
    desired_state: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleDatastreamStreamTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a082f18c6634f77c5c989c278a91ddf6916c61c1c1c1ecaeb403873feb786f6f(
    *,
    destination_connection_profile: builtins.str,
    bigquery_destination_config: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    gcs_destination_config: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a49c814b4f2ebe3deb762ed064f6ce81ac50435614e1bd2718d7e8651def96(
    *,
    data_freshness: typing.Optional[builtins.str] = None,
    single_target_dataset: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset, typing.Dict[builtins.str, typing.Any]]] = None,
    source_hierarchy_datasets: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3391270fd72825792750d900baabf072a22d3aa8bfdf9b72803fa90f89feb99(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc227360efefd83c13161506d90374637c3c2dba1821899cf3a429435283aaa2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1e71cd219e14ea812cecfdb4e16eae14cb53d03b3d7baea51323b1fb77a39c3(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8fb9ad9224f683a8eb1f9139234f286bd44fddeece5772c9709e709e591a645(
    *,
    dataset_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a3d055ab4e6752ba6dfdb4394295e7f7318d4a3b762834c187cc27231d4ca7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4c9b188fd123021caa994f45cf0394e7b3f43765b979d928e6f4d9f0621a963(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04350676f2a57de4c6c34fd5c31fe09fe4989c93a30002c55349461fcd324dd8(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe99655d10da1ece8d92b4b95410a92466fc73978fb56cabdd00ce4872af7f30(
    *,
    dataset_template: typing.Union[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10bc9309ea21fa94f6d71ec05001d53825566fb8b23e70b72f26ff70b216afbf(
    *,
    location: builtins.str,
    dataset_id_prefix: typing.Optional[builtins.str] = None,
    kms_key_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__589f4d7cacffa3fe9eaf1ee753fd3bb86c046e23b7c2e374b0f0fe1f59848e72(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fa782c14749e41909d2558ed573b112c4f62c763ad09af5bb8000ea5bb08163(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64830a54fe54f2f7da8fe9df8388f147273f845e49dbe02ce84b116489ccc0fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04028b6cda5a7527cf51ede06922de56ad34e57e9e59dc68cf55dbb105f0a0db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5de30ee6e92d12ceb0bda2317dd12bfa52377bec516b2b2a517385018ff4fd37(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec59f9ec651149d0621d83bf49acbf8ee0bbd34767529437d0eaab1d43196fba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ead61d6997a472aca9d935cc8910fa587fa5ce5f4d399617f914993534cca402(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d10163a88a5e865a15e425114c10f9f67bb19cad50eff789fae98679356656a(
    *,
    avro_file_format: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat, typing.Dict[builtins.str, typing.Any]]] = None,
    file_rotation_interval: typing.Optional[builtins.str] = None,
    file_rotation_mb: typing.Optional[jsii.Number] = None,
    json_file_format: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d068a5a28bd2dac3ef4546b05167198e8dc3f67c53ef66378117e2eb38de3e13(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f08298ba4d0b3313ce13d92f69a9b0d3e473996f7259553f11037794731faf97(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5bf24309609d454116747fe1a8433f1d6909fbbae89e976eff2fea5165e8d7(
    *,
    compression: typing.Optional[builtins.str] = None,
    schema_file_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56acedeeab88a59e046f3eda7acc9a87997bd1e847f3661a1d2ecffcaf8ece46(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca5cc438ef5b106f7a336d20a5581f3c31250831e9ffddefcd61b4d1d9ff878f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac1ec35e9777f4ddf604ec41ee7052c7ac0d48e85abfb0a0bc9ffd10834276d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d5e3c16b98749306678a7e9992adf27157907012286429f2c66df988d0f0bc0(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47a5f5a8a9d9f19534aeab03cc71f662ec8150fb452e35333840e1fa4d19587e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9074e840158c242a6584f690b9de8519093a095062560f763cb0081827756a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d6fa5c42e1b054c724b34adb45f27353c6ae294899a9d8e80d90a167757cf2f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa2957bdccb90ef0e1d993d38c3afe8f4b14b633ee4a561bb96646544890cbd0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7c83b1266ba6a9af784fac1c33e0f366fe2d370e2f056e83a4d926ae455c27b(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c6a55cbd18393a53cb1933e95b4e468f4a520e2aad658c6da60f7b52de2f3b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4017d208188843d4929bba3e8132e98451cac7713ab722eee13604f90c45b18b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dcc83c10b6513136386af9d65f30bf2f699f914858eb91aaeeea5968e7dc3c2(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2219a962a105c32324aa42c0ebabb89901efc5212a250e8d5cbf7c24fdf77d88(
    *,
    source_connection_profile: builtins.str,
    mysql_source_config: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    oracle_source_config: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    postgresql_source_config: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4778bbd828e1594c449bc443537ebe755eb4c886943cdf45c60649a2abdad88(
    *,
    exclude_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    include_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    max_concurrent_backfill_tasks: typing.Optional[jsii.Number] = None,
    max_concurrent_cdc_tasks: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d83157a8b7dabb6f6a578ba371ae7606ca73d8b886f676352d01e59c8b975065(
    *,
    mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb545565a9647ff9db741b384db4f82c54b58032c7b2d4e18818cd7d16eeeb69(
    *,
    database: builtins.str,
    mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e56eed75c4420627cc1b1ea20e73bc1bbede9df3a2fd8199d4497aa838d16d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a1012ecc8549b81e5e4aa9d9923e204f999b9b29fd4483cafcd96ee9d37e92a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__749cad1c5353daa5443baca3acaaa68fdf3ee0496883fec1e0a8e7bf6e478f43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ed34b487f8807df8a3089ff0bf45f39c9f22d366421e027795a5d5ff3b031d3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47fc60e67695921f46d329ab49e84fb7a745d5f9e52ef95fd339c406ed1f5337(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6580eacf3a0fa9ef788be946237924b568d6c34ca0ce2997d700ceb0ec5909e2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fd22251a137acbd8b6d4011e790c862bba2bc6baff5731831f4aaeb1f09bc8e(
    *,
    table: builtins.str,
    mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb19d59bcaf47d9126f742045b4d73f2d47c6d705e98fc433966bc88d02bd5ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc62e64aa47cf54d533fff2c0ef281c96989464e75c918ffb64f1d14c9d9e79d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09ac2c33a67547e5fc09ad6eab15b4937398704f7e0dccd16e467818f83a6edd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78f38e38e105221d16e5180f0a1d2c8909391494a32349303610ab95030c9c8c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d20ad137b3b082c078fd7a5bc38642356759a7fc420d24b61cf649a1f7ed1ad8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__244522fde9aceac31a2e149744987ae023545406b794b7618a16cb61f5434d3a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fe080b67925fa358036b8642a0299bcbe1d9e7f96a77e04e3df091ce8d56d79(
    *,
    collation: typing.Optional[builtins.str] = None,
    column: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ordinal_position: typing.Optional[jsii.Number] = None,
    primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__201e84943daf6e96eef782d9aca244517f562921989a0d02638fa0c6272b71f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa8e8e1d140504fda11f4c3773ed96c2555f2d0a8e4e54dd2649412cdce8913b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09f48286efb01f277d2532514c20596f929b4f09bdd712cce896d54029581845(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__412ca5ab78995949f165cc648a1345246edeca119614f829c8466a957611327d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8513a9f97f6e8b890e45ed0436f080d3b24af266ac66156a0234692ec528671(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d52d72230d6b4de322b1c93887aea771351503b11807485568c93d0e395bad14(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cea7b45fb19736020b1719a17d6aec42bd6508059c9e7f8abc1ab4eff5bcf48b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77e9ee7094ccb2bbda850d8033cde908a302188b4966ed9026a0addd79294f25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3769df6b39afdb7b53797c325a30a0a86634ec6359d219686195fabb6bc4ade(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95e94c186c0638d6e197288bd999f087d07a4e38f94a0c930fded96c19b30a06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57c29013747c1114bb244cb6f55298a74d6c22ed57f735b6c3fcf456523e93bb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8083b61ac53f7e64f6d293d8795f8cfcb1af5dcc4641991d8c21d7d14d6a090(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ce157d33b04ca603a11a14e186e508173db15b13bca2edab6f487ed885c277(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a14532a7d8ee26125f14790252a94be3a764732ba59c7e09374d740bd35cb0a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9ad39a49db2deb62da532182c908182089fb53ff855492f00ca108bfb38702e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6805013dab1076ffb632b34e127ba4a5b8181fe496c7c0083216d785c6f51a6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f635e21d9372998fc0be54b333ef130ee85a23b090304aa7d38db1c57f56b6df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcc850b4e3cb4779e1466342590aca58d03c507861a481a9b9fd924abaa00461(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba70a81582b78786b580f56388706a6188061700c80a5ac1049d58ea4ceda106(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25736e01b271cf2c953cc3fe6752d0c6af2a0cefb5fdadb58a006ce4cd317ca1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c255dc0ac974e3e989e48a72c5479f88eb080a9286525bb3f1310e4e41d29747(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78514113923d93d64011f19fc8e7df61bc8b692c1ca133f55e2039d7a76a635d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c84a482c246e68a2697c2dbe687609ff014a57db45d072800f00517f2aa6a56(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__084ed61c2edc5493618eaa16135dff2755b5c72b0b42e1db898c18b18dc6f41f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e809bf11601f9faeac3e63217a488b72d3894ca5740326dce20994d858714f2(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b782ad37d159e6fc26ccecf102c72c7754e16dda5dfcd19b2bc64b597b89e07(
    *,
    mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f44f39ebafbebf8e628605efe61a5348b73f5c5884eb1c28dde453f8bf8523a5(
    *,
    database: builtins.str,
    mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3950f8fb1b59cab5c5f81358a344ffbf164f405bda8837307b833c993cc758d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90939e89008258e8e5fb13b17b64dcac780a64cb8cbe81abc7341daf57a122e8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__217aa69718caac050d609fc9d8ce57f8bb611e4fa934e6be20a0b57f11f7a1ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7dc49121ffff0463e398d82b102cb8ff336eb3cbcd5683e60e9dd1109e48f61(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ba15a2cd54a82cbc63ae4621ab87db797cd62dcd7ed63ba155e2de063b189e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d004f44683df7b5074728264cf889cbf037304edfcd3f994117693183d9f5db(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa194010af037f05469911f39778136fc3ed69ba254253f1224c1a9bbe628999(
    *,
    table: builtins.str,
    mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcb77d2e3fb3b195efed0d69e822264d59c5fbf7c1b4cee8e8964364dc9c2123(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba2fe890e741e0c6b63029866f84e111f3cd478bbf199d640a82d12c574d7aa7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1c7b2e8a8945bd904b6786cb2b4d1aea6874c1ee6838435ab9323baa835b2e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e69a309bddb1478976b492ae7fb3fd3f17336bc920c0b40e545744ada6341c29(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2671e1f1942c6cb0e3c3ba36f58e950eb50a102df253a43e899c96a138842ff7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8af2eb875cdae7d71d393ba6e098c6da4c3110914133b1dd079c070354a7a205(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41215ce0b14ba24427640cc4700269ad49a0faadf8295e7ac03b7f47f2b37132(
    *,
    collation: typing.Optional[builtins.str] = None,
    column: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ordinal_position: typing.Optional[jsii.Number] = None,
    primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6861e4975493055a6649272b537f648980427a9301bfb234da05242b7f0c49ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9427d6862c644b6d507a55730df9f5fdf5c926418390d5de45f4e2f3f5ee9f5e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69adb63c3ab9af12da7590f7aae32e0a5104845d11c1ddd67b18b08745828402(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e663fc168673b4aa74cd1ee2009d59cd03ee3b03440bc1bae19ab2dffb2cdf(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b58a7d494136d2ac7db279ee2b91810061fadc45f6d73f86e92229382749f59a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fad90c17f32bc7ae1fccc7cb1431033ed4c2ce630fffd4d769c94decdd59083(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65b3ccfaf3bad8ab5e06b93c91c603524b0f7f199e7256dfbce872b77ccc667a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68e45a2b6f0d78f15e06a1e14dbc279680b842b3d346da672fb3da0ba499caa5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a954aaaf4ecbb61bdb80680a5308a4650ff1f930fdff1565938a80865567e4b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bfd73c16927e583d02f4ece4c98e6e285936610b6ea37d64cb9c6731b30c6e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c58d677fcfdede4d959a221ab875d5089fa903aa656d2b774755c9e2be2e790(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c454d64cfc5be1fab8c89b6180a07485a1e3934e24523bc92f3900e58a45b43b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__990ed112f00ba5b2fd44cdebb437b9c639030938839325738ece2803bbbee1f4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac1001f24a95b45f13518456c95010ca63139d5bf238d99bcc2e6386f283bc2d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6b4a00ce373e23cd5b51bfba3c664c9f9a51885d2951423d35c58dea7aa5613(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c9a1375628b7f6b29a695647f3434428d773a775a513a4c340d0cf934ac7d32(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__629184c09083c28c9f035a8074dcd1f16f0a61d948bc2393377da3130506e2f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__759a721a0536fba67735d0dd4283007387dadc2eb076cdb2d65fda1402b5e5f6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8548900250b3351b1c6d41c39a3f7fc3652815a7c6184c8c707341c35763ac3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b269534d2b5371b90449e0d4dd96df396fbca76931cb7a5f54a30f1b654543d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0dc2394f1204551f9f707dbf0479faf9458fafc6a03c129b132c5e409293bb9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b6f477c199b7d70e86e7f6dec51b8b579ebe58c787a257fcb73e04d3cc5bcf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b401a73888aa3eedea89455bd1d7e18731ee7412824c21d4be2f36a727cd8a7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__613d8a98ff90be15005996fdfac043d333f8645c71d52edfc24b79e3b6031649(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc63fda8e348ad1f4425fc05aec528be1a2b9aabab914770a3fb1f72c46604b1(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efb86a24b39d875af0044075b654f055d4cf52279a7e2097cdcb5b797e5ff174(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2735bcc93507e2cbfa21e107259e233d3beb340310fb8b4096ca3346a5c361f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75042a2bfae52ebd1b965d7005d120750faa2993f31c1eeb04500e45bd87a769(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5301d37e1a77c15dc3423d2d6672f672b5059dd74d24e85d8326831c85d9c317(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0746e488911fa190cba4ad48b5ba8569167b4dd9cb274d378bae346f3759f736(
    *,
    drop_large_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    exclude_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    include_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    max_concurrent_backfill_tasks: typing.Optional[jsii.Number] = None,
    max_concurrent_cdc_tasks: typing.Optional[jsii.Number] = None,
    stream_large_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e644dd74339ca62deff701c0e07764a4674cb5c619be7d317899e07040ea30(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d65ef8ad20e9ab5236f355421fd25e6bdb30b1d250c3c9ecc8d26c58215f7ec(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigDropLargeObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__610d578ff5a80ce274d5ec0c1fc01b310eaa82985cbae7ecc4c0be6959f1e37e(
    *,
    oracle_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3c73db535863aba2213698f0c778ec48e805f13de92d60ec3a324cc006d6d8a(
    *,
    schema: builtins.str,
    oracle_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa66e9d03d74841c392450039a5e82254edcbe89869d85a10930236c6f8bbda3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb5f39e489992356e26aa4f345a253773f9f5830b1a3e9a187e3c1accbf43fda(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b61b668e748c315a5bf1659d576b93146914166667008d1b7a40b86a76b99a3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47ad29a1ca9bac7e5f763d1f92c78f12093fc9916a33072e9470122b7ba9b81a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5313fe3d09856bc331eee7c5a7bfeecd237b4c309675b8e0efb8f216796890a6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13b218859bb362a860023f75c090cdec5e423a75b6065dca0d991b4ce96775a1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72945eecb48621a4fee2bddebd411ceb1f976f5c3a43d0672213685a3b71b441(
    *,
    table: builtins.str,
    oracle_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__170f35849c38654b7274c3bbe0cde9c0f1625e39bc5c72c8412df57f33ff5214(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51931767b7b4afa892cb5ec9d84c06f533953230fe98d01cf0863ee42a58a119(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0a6f474ed8fb2e1c32d0f32b37aa5c5896c09cdb4c531361e5bca1e0bf217fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5c34a517c6b92c43e017368b9a6bb30da6731c76951a8d90b64b6132dd63741(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__026fe2e82c75504998c44d25e787d2f35af305244ca50485a68073a9cafa44ee(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be26bef57e570d4993112d124444fd5128b5f4967b31140609cf51c60ca9d504(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__927804d3f0652f6879e48552afb307aede9a0dd7cd504e58d7e1c46bdf801acd(
    *,
    column: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f19319138fff89df246a22ec13e540b7aa96a77aa14f60eba28e01d6e23152d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edb51fffec9b37c1ca7ef84a3b48dea544f408e80b1beda7f218d830036a2f74(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bddfb7874f06e58758a6475e90c3d4e14086a293cd6cb1cb10cfcbea06d5e2d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9e985724e1382827e7b1632b299eab2811cc4e488b93ae914c89e6dcaea651e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2041884ce280b2fb9be136e1c7de9cc5fb5c110c846583106153358249a8b64(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c623992c2c406508cbe09f48f58bceecd0ce77fa49ad9d46a053e9a2fa2f8883(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23a632c77a902d63986a9c8e808f510b1487a1495271e2299cd5f3e3ebf4a96e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dafaf81736bea926a31b688a9ef41667269b54d506346a7fbaaca1e9a935dd7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9978d38a6735e001b8587ae592bbaaf94a3591c52de2aab9663f4a6f37509e42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__821cc0f4a05ad272a6006e9fda801dafde1a5c6adf5b9c98860434e3c3c7f720(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1defe2cf3ef2295dd20f20a274de67143219892f15fe1c0ec2f7e4ed61f50394(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a297c0a90d9c9b664d36a0a07ddd35c5940573dab31d5cc43ebe5ad8af1b322(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTablesOracleColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2033547eb38f37fe35125a88c6a104b8070ded44d6069bc7514fa900344d4fb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11a32c231fa57efd2dbca27012b82854d2b91bf9c55d86766d2bbe2377579512(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c60d8456aa34ba08c5cbdea3ee033a688b01b6a1ceee1b3566f681be62e133ef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c6e6542a24ee0fa9552302cc404ab540f4e4c9b3c6c906709d85bafed3029e5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemasOracleTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0177ebfad4be23c26b85e0aa50bdf2718495d3628f677c0be28fac3fde5eff10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73a7275153770bd368ca194d0499c9379d54374a979511821c3e12677715d28b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eb86a65ae85d48b44d647559207b124a8120b7c32b78119c78f71332d3f0273(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66411d3bf6d5a0271afc2970730b4f28dd2eb4ffba2384ee6ee9b109b40e0d24(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemas, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d52a5ede0f24000ac161573ac1629edec126f6cba00c3875ab09ed25aa6393f(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigExcludeObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf7adf8a1b3c9403fdb5890833e7a6863ca0b13208a0571d21d5c360b88b972(
    *,
    oracle_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1327fbf9aea1d708f05f9a5ae75009a20e135b2870b8dba66bea2d9bffd213db(
    *,
    schema: builtins.str,
    oracle_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ba579256d9f634a2495f3f5f4f25f632092fb1ef0bc10cacbfb06fccf3ccdd5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57d26e99abe978882a877ee4f27f6685c003bc9077512b01ecfd65fefe266468(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf4e2df60def43855ba3cd939b4f8809e17204c8b3b6819abe11d85e4bb4011b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3321e9b9e486d56b416b6662b463afa6f42e5a2727fb0b207b739c89238d9655(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c393f3debb5f7eec855d2cc171b34bc06ff76cb3addf6cabee68379f49c0543(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__554c599b27578d800761ac0df689e2cd7fde662fe43dda570423339d2959cc57(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6735b041f43857ac6fcc259d83e8ec56b68237c970b2d0cba94db7ce6343dc6f(
    *,
    table: builtins.str,
    oracle_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8e91fc15375ec7d0fb5908dc088b08f8665784dc71bad279489c4158e905747(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a5e759e6512a87212073f7fb6442ef00f2839eed1862a2b963ea7958f95c19a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bae040df948cedb813aabf4cec258e6afbcc224c88b32bc0a6b6a21a5edde5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93c29be1e152aed916678b6a2de99ed3420b6be1bb1f4004e512c8ede7d659ad(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b9dbe0c171e14df5e7d5449a77f61d081dcefb8daa1216ce96f99aa80af8546(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6f21ec8ac603eb65e63a578eb7eb2e1750753d8ed904f4aa21b1533c09d48c2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a1df38365a2804729811dab04b177001df36a2f42f89529d8a62a819106d9b(
    *,
    column: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__031f827bf69c01b95e88322ca6456a02600429ba27dcc273f2133a1c88eed803(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0868168a79526f32e97400a320d98b837bfe0a6bcde6265bf2832013c3a50198(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d0d245a2130500073a10053bb4f5180b3d68af83f097b2501db2376acf4c627(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52fd0ead8467940ba152c4674ce6e64fdcdd1dacae8d089e71df6250b6b2f6af(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bde2091abb9dcbbb1dc5f50cab7a26031c642bcaa9f81b572961deaf8790ea6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7199f594524db12eb37d343fa910cd257845b8155baaa9c135952c2e62c48a16(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__971651e5ad7cb1252fa28191c73caf5c797ab74d69d6ea96498d5bdeb81b6aa6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__069e81b54d19a705d79474390a6d29a94100cca730a221287a70eeae38ed7811(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c27bcba7c7383beb6be3f02f43f68c3620659540fb5702a56dc8c9ca67a8b4f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a3691ef23b9e827eb24871dfac692bdfdea6098ae9d9eb4d58bf00756a10a1a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__703996a518a97205ddd13c56342ef25b5b32f06afb40073750bdffb0c1d05946(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1327b38ab72b90f5c97174e958cc7fdab2332bdc5d9198bce1cc59894a633d0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTablesOracleColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19b439f4d826233de8c7048ce84a3349625b11696fbcccf324f532ed9ff80cba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e86d5862462ad3d8d8e6b097839340587bfeb3b6fbd812e085358743fe812ab(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43298af7a1bb0174c0dc93615c679aa431c04e61113eacb540534d5f9107e914(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a25f7828051d869f0590c65de1031c10af877d13962b7c46ca5c4814c41660f4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemasOracleTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e90ab428f843cf39f9c80b14b599b2aafa6f11b07ae6bc695b985f32dae601(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c55f58666603268776d8346063a5ab10e4e33365fbe0e2bdefaacecd7d8487a4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c83610b88d1b62d65ba062cde85b32baac2a70a055481284c25b5881b81f960b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9ed97e64d1b360d876fefcb39e5a3d847f81735cbc25db6390ed2260683f432(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemas, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22425ca8735bfdcbb966f4900ec7590a3c024f1dc791f7c0aa684275ef1fe6b6(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigIncludeObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53a4258512add2fed9eb6a736e76b66c1064e19937ba3da4134ad2b06544011(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cc8b5a7b0d761263926fc15e837433a99b479730491bd0feb8a5d25cc6f9fa7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e881dbbea9b91c03402c096c16e6face1b47542b9846c982ce06805d704b6e6b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5330673f53c095c81dda41b1fade645e45c84457611569d902950dcb166a12b7(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ded02423cd20100f08f7649eace76f55291e6d74580d0f4f9548aaf2816958fb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecc80d37f0b1af62eefc2bf946f641acc2c7ada6e57c3188cd7b2705b7e930ce(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigOracleSourceConfigStreamLargeObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__935aa7233aaac0fbc524f35d41c8b42f4f855c3d54fd43f35f0e7b9d7528b61d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad6aaf1380cfd2cad252287f4082eac6cb898c810899506186dbc4bf8daf22af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31a3dae34b03d71885cecf9357ff558547f3eba368913731781633806d28251(
    value: typing.Optional[GoogleDatastreamStreamSourceConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__808428853b11ce5518f2909954a6060dbff2919f6b431ea29036573ec47a5a9e(
    *,
    publication: builtins.str,
    replication_slot: builtins.str,
    exclude_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    include_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    max_concurrent_backfill_tasks: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29e94db22db80391b825274aa101356ab7e352a304616a909e6af086988b3cd(
    *,
    postgresql_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f1ec7569d85a477ed8bff45a112423d432bebeda96fa3cba56b71f779320863(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7357a8de26fe6d19f0dc39335d8857dade1ef2d8a7607a53e9c8c90c853808c7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca3e8dc69ad3d2a04515b87fd648477a52bee8a5b39096fa3c5f1b8799baf65(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ab9c755671dcb72ed7544f514c592145f56365e5b95a649b0d6f94c1c95cd36(
    *,
    schema: builtins.str,
    postgresql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2b23e3a8b8fff9849f506cdc5da63c51c5b568cf8e64f95e0747277f033a75b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ab280d0b6951dbf59487ee28ffa4dc7a0d415841e15d6bd729315e0f3d21658(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__026911ba6a8a154b26cce8f6076802108fd8ba8b5aae82217e54074449b09348(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4b544410ae0e335235da7a0485d647484c5107d1553f7bb5d77fda6f12b3ebb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32465c8a5123f7748d5d12af75d50a02e4e03f7512e8d78d2ebf2800c09e0097(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__639c90a1909cb8e0b6351c5da127b0700e4b7e5aecff4ffb994acfeec41313b5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb0f0a1788e31e44c2c857a038e0dcb2bf0873017a25bb7fc72a77aee9771a85(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__768f387107b3e2d568f3f615318c8008107d2a81b53fee05e6b09481297569a3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bb14576f9aae508454cdee9ae78f154183e3f5255aa0bb6a4ea5872cfe4e925(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bf88f993df9076cc30d2d153e548e44f07204c204fe62968953f7c9a4859b1a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemas]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdf9f84e8cebb18a1de572b141bdbcb6ea00324ecc4f8c7ffb8c95c83888ef15(
    *,
    table: builtins.str,
    postgresql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9e5eb5ffbcdf5422543b94cc3b0acee516bd3dda38be6228abb7b293913bc51(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11a917b2a01055d4c5195a98215f278fbdd7fcc1a6c23d6bb32de79c0779fdb6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54cdf8ae6f8c1a5ec4622cd1096e5b446c2e5d0eb1e6f5b55cf0a65dc880e1e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48f72940785b8c1ed26db8cb02b9b3e6ab4f497e3eca292b3a34998038d74e35(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b776b0647aa3cf5afc6063ce5cd6c2e2fbba6ef586265125516eea01070b5fc5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af611c34ab88e83e5e7c1c0ed901a79bf24c85b08a5f95cd430d129ad822feca(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__985011c4b22efeb98f5eabc191eb3f29e884e8f772a8f104926e5be2a53257a7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75518d4255529283a0cc3050eb38a2fe014e1b2bef989346e6926dce84cbbccd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dec340d5930a9f31f5b82df61eb7380a68a44911d2cd51cf3227883f410579a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0479f6167dc3f97f4ed43abe9bda13447286b226c594efd4d9b1b71b2bee7c7c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTables]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c374ba9568fefe81d56a433cddbb7dd8413494101c656d826bf8cb17e639a77e(
    *,
    column: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ordinal_position: typing.Optional[jsii.Number] = None,
    primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4c163c1c608ac6fbd89879bae3d1fd82f3963f0c1362f098dbcbb5f6c372aae(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5f321069c5eb542272547501bf026a807511ee4316279a122c694b71d5aa467(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5961506383aff77857f29576d4a9c3ab8347fa5c8d1c082e9e6bc0cb38eb6d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cde000132a084546778016334e7c17d4ee0387c64e18da19a029204f02b036c7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c0df27265f0691ae5f8b39d925b58e9db8998b035520085e13fe34acf89e516(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7391d040483235dd4ad102211a520eaf092c8aba2e9e1bb784957badb166f46f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6af5c2b4ee3b0cd9a3d09265c0bfffddc8a98b483bdb545beba82b0158eefc3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcb4cf98c716e9255acc7286b2746e598454f879f80548d3436897bbef6a529d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9591bd6c5ad0285c687125b4f8830670cd9e596ca2caf5fc88a87577bf632b57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9056760022d21d71916e50cecd95c0ea88a8dc446455402a3cb866bba251ae90(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5a948729cf8e622a973d66bc24de9f6cdd493c4d0335053e61baaee36a0f2c1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcb60d5f9f736982578cdbbc2e6c7fd16875488db500030a77cbd2b237532c3b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c74d8384807d3bcc937f21dfeff59bbc32b552b0f278ba4bf058c68a539a883(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a140786a024a194a696f5014921560df44580d133ecd1c619c8e5e18add8aeed(
    *,
    postgresql_schemas: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b819b27bd69565e53ec9752d2e1411f14eae784918386d890ac1bf7f8b7887c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7adbc8f5b6d1079cffd8cd37056f8d1cc7130846e8abe3717099c8b200809aff(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfd478c0d010a99b6044540a720948d8e0f62adadeaf70e010b547421e70b0d6(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13cb4f6f5aaa105019489a12d97f546fe100ac275358231f6fa95081e265f3b8(
    *,
    schema: builtins.str,
    postgresql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ef5e5d16e6215393f7c7c0df02b441820ff5500bf553f6808ea670ea84b8da3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a5faf90af1108a5e02f7f75b630a45bd622bbc8837d6bff00db599ca227c9e9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1101edcddc787719f0312de054fa62df117f3d7fe04b08e13495f0d362f6c04a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c9cf3b739b955f1da379f0166ae6e51283a17b6a53ca615cde9d98675ab8e6a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe2f1ad01b17ddd9140f903973ef32a45e1dbe5e1935cb1b2ece9e5a1e6c03be(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8de245e9b46bb49bbbb8ddaa94a06821782f372d29f3fee031e86ccce933ead3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6032ba065b9e4b87b379b8451042de3f0349cc820b7aa0309abb3b56058edd22(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7292523b67a0d518360393a870bb8438d8670848954003d3370c30ca7968d63(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aa5ee58a7173fb4cd1f054b6caecfe39d3814741acfe79bcfc1be6a02b68a89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4c8d6aebe392f588ad76e59670ee0e8b202cb1c4a84a1332a22918f0d04ce18(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemas]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eda4783896c6e83094c50a0c20ff8b5795507b65a1c411668c3007386dd22397(
    *,
    table: builtins.str,
    postgresql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__901f53a8c246324974d705fbcc358f41e2324467f0e296c25328fda002b5b541(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bde972421b6a5a304a8e3e56adbf17a5df04ce271984af74c606e4642adb0a68(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d37fcde47ec92bc6b3dec6089539448ceff44482e571daaa2d0f47dafc995e02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aad07e66bfd3e9879a014bda027e08327e4a301104fa9b400aab9ceccab94113(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b2b18bc9b4cc9e07eebfc90dea02c8f24c68782d43a5d14a8fc6925b7853340(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e420f9301810b955801e9e6a4354a88ed637705fffd17f0d4a856c58d54a1ab(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f788138d7ab18c27e953964d4ec3023d8adcf8c576164dd391d32fac6a60f06(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec5868d2e76b06d37a92e521ee9bbcf947f9a8c5853435978e75c24566aeab90(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f6d8a7718ce1edb7e595968bfae67d6878bf55795cb5a9518a05622366aa8a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efac68f460992bed8c5b38fb23f8db9e62c2d8f21eafc972d879e92a213d3922(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTables]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f82d6f2db315d340e7b88786b3820bff3c60d4dfb15a17d5710309de0cf7115(
    *,
    column: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ordinal_position: typing.Optional[jsii.Number] = None,
    primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c916b7d36c1f33f96c1f7e3f40982cbce8712440c326abe11b70ce9cd546e14d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef889fa19c3b481432cd15069f649a9861b5eef469c50abe668f56ad80df5837(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afa250b1b76e0f59b5b3080037cae2d573072f89e0ba759e34a95b76efd0ed8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a7b1297223926e11fe96e3036d07d8933c6dd01dcb7b6208f557a7434030aa2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2a0e22c8221b04cb9e91c46cfe8d45d269e68f82aa5eeff5e3d3bbda13ab3d2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6e89e886c1cd65e2347c43b33c87451409113595815e3eb7152e5c88cbca782(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f876c0484c091043838839e387f742c77b38682ef567978c434e890da6cd43b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a355c251a996ef1766abac034090658c23c783ec3df8928cc97a347f3c598332(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c288cf196dd4b751ca9c112fbffd013aaf86a8aa3f12c241780e27eb21c04356(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87ad480a8b9c4f6ca0e4a37d62573ad88402f62b2bf70f87586a53a3f2d257b2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76871aab1d8b5486ac8ae2851dfb756949d38d10ef7ea66052bc445e029f8769(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d32f13be1398922ee07a65d04d76515ec90fec2d8433c4d17ea0ee7c6467df5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d40e1798547f1ccc5023d425d24025692b6bab18ccb139aa66142bd7e50d3abf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemasPostgresqlTablesPostgresqlColumns]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1728459c0682ba074c24d877566017f422e2e8a4dfbddd884a5279a929f7ea90(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__576c8fd329963d004ee0fa8801f4ecff13b9e62e022cbb2a59d04c0281764b17(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8b50c4dc34ecff31d1a38cb8a8407323ede120571e38eddc5365c67c3d2ceaa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a08267f1f7e0fff1cf0bcec0dafca7e35cc564cf246dfcd184170786d8ca794d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c91f48dc73baf8eb82b8ce7b61498a8fbf3d58511e81bfcf60b0d05c2716c493(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigPostgresqlSourceConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a54b49f7561784b6ddbf39b45bfd0f91cd4d531a183f057a0f51c1fb036c6ee4(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a1e593819993f0b26e94eb2825132a675053b005efe8ffb05266fd2c2530166(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72ae4642fb1a34ac292bc77f8755496644a696b2005d238ad3d096cf94340334(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f50f1677bf065b391c40444994d038f923d9d5c282b68e34cbff128a610e0e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27df4af47c20495c8bd3cfc96cc0d9e42b03499ba5a08622470954ed4ff13101(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9644ba1934244050f95ca839e3c9e108ad0d0d1156a6d8051eae93e46bb4269a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDatastreamStreamTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
