'''
# `google_bigquery_table`

Refer to the Terraform Registry for docs: [`google_bigquery_table`](https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table).
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


class GoogleBigqueryTable(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTable",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table google_bigquery_table}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        dataset_id: builtins.str,
        table_id: builtins.str,
        clustering: typing.Optional[typing.Sequence[builtins.str]] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union["GoogleBigqueryTableEncryptionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        expiration_time: typing.Optional[jsii.Number] = None,
        external_data_configuration: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        materialized_view: typing.Optional[typing.Union["GoogleBigqueryTableMaterializedView", typing.Dict[builtins.str, typing.Any]]] = None,
        max_staleness: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        range_partitioning: typing.Optional[typing.Union["GoogleBigqueryTableRangePartitioning", typing.Dict[builtins.str, typing.Any]]] = None,
        require_partition_filter: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        schema: typing.Optional[builtins.str] = None,
        table_constraints: typing.Optional[typing.Union["GoogleBigqueryTableTableConstraints", typing.Dict[builtins.str, typing.Any]]] = None,
        table_replication_info: typing.Optional[typing.Union["GoogleBigqueryTableTableReplicationInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        time_partitioning: typing.Optional[typing.Union["GoogleBigqueryTableTimePartitioning", typing.Dict[builtins.str, typing.Any]]] = None,
        view: typing.Optional[typing.Union["GoogleBigqueryTableView", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table google_bigquery_table} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dataset_id: The dataset ID to create the table in. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#dataset_id GoogleBigqueryTable#dataset_id}
        :param table_id: A unique ID for the resource. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#table_id GoogleBigqueryTable#table_id}
        :param clustering: Specifies column names to use for data clustering. Up to four top-level columns are allowed, and should be specified in descending priority order. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#clustering GoogleBigqueryTable#clustering}
        :param deletion_protection: Whether or not to allow Terraform to destroy the instance. Unless this field is set to false in Terraform state, a terraform destroy or terraform apply that would delete the instance will fail. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#deletion_protection GoogleBigqueryTable#deletion_protection}
        :param description: The field description. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#description GoogleBigqueryTable#description}
        :param encryption_configuration: encryption_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#encryption_configuration GoogleBigqueryTable#encryption_configuration}
        :param expiration_time: The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#expiration_time GoogleBigqueryTable#expiration_time}
        :param external_data_configuration: external_data_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#external_data_configuration GoogleBigqueryTable#external_data_configuration}
        :param friendly_name: A descriptive name for the table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#friendly_name GoogleBigqueryTable#friendly_name}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#id GoogleBigqueryTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A mapping of labels to assign to the resource. **Note**: This field is non-authoritative, and will only manage the labels present in your configuration. Please refer to the field 'effective_labels' for all of the labels present on the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#labels GoogleBigqueryTable#labels}
        :param materialized_view: materialized_view block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#materialized_view GoogleBigqueryTable#materialized_view}
        :param max_staleness: The maximum staleness of data that could be returned when the table (or stale MV) is queried. Staleness encoded as a string encoding of `SQL IntervalValue type <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#interval_type>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#max_staleness GoogleBigqueryTable#max_staleness}
        :param project: The ID of the project in which the resource belongs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#project GoogleBigqueryTable#project}
        :param range_partitioning: range_partitioning block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#range_partitioning GoogleBigqueryTable#range_partitioning}
        :param require_partition_filter: If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        :param schema: A JSON schema for the table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#schema GoogleBigqueryTable#schema}
        :param table_constraints: table_constraints block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#table_constraints GoogleBigqueryTable#table_constraints}
        :param table_replication_info: table_replication_info block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#table_replication_info GoogleBigqueryTable#table_replication_info}
        :param time_partitioning: time_partitioning block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#time_partitioning GoogleBigqueryTable#time_partitioning}
        :param view: view block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#view GoogleBigqueryTable#view}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__946e9c37b2c299f568e9c744021d56f2d54e6961c5d3710ebb968cc14ac21454)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleBigqueryTableConfig(
            dataset_id=dataset_id,
            table_id=table_id,
            clustering=clustering,
            deletion_protection=deletion_protection,
            description=description,
            encryption_configuration=encryption_configuration,
            expiration_time=expiration_time,
            external_data_configuration=external_data_configuration,
            friendly_name=friendly_name,
            id=id,
            labels=labels,
            materialized_view=materialized_view,
            max_staleness=max_staleness,
            project=project,
            range_partitioning=range_partitioning,
            require_partition_filter=require_partition_filter,
            schema=schema,
            table_constraints=table_constraints,
            table_replication_info=table_replication_info,
            time_partitioning=time_partitioning,
            view=view,
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
        '''Generates CDKTF code for importing a GoogleBigqueryTable resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the GoogleBigqueryTable to import.
        :param import_from_id: The id of the existing GoogleBigqueryTable that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the GoogleBigqueryTable to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75322ff820709315badf9c34c6cf567800016adc6256e15129709cc9823edeab)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putEncryptionConfiguration")
    def put_encryption_configuration(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: The self link or full name of a key which should be used to encrypt this table. Note that the default bigquery service account will need to have encrypt/decrypt permissions on this key - you may want to see the google_bigquery_default_service_account datasource and the google_kms_crypto_key_iam_binding resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#kms_key_name GoogleBigqueryTable#kms_key_name}
        '''
        value = GoogleBigqueryTableEncryptionConfiguration(kms_key_name=kms_key_name)

        return typing.cast(None, jsii.invoke(self, "putEncryptionConfiguration", [value]))

    @jsii.member(jsii_name="putExternalDataConfiguration")
    def put_external_data_configuration(
        self,
        *,
        autodetect: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        source_uris: typing.Sequence[builtins.str],
        avro_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationAvroOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        compression: typing.Optional[builtins.str] = None,
        connection_id: typing.Optional[builtins.str] = None,
        csv_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationCsvOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        file_set_spec_type: typing.Optional[builtins.str] = None,
        google_sheets_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        hive_partitioning_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        ignore_unknown_values: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        json_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationJsonOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        max_bad_records: typing.Optional[jsii.Number] = None,
        metadata_cache_mode: typing.Optional[builtins.str] = None,
        object_metadata: typing.Optional[builtins.str] = None,
        parquet_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationParquetOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        reference_file_schema_uri: typing.Optional[builtins.str] = None,
        schema: typing.Optional[builtins.str] = None,
        source_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param autodetect: Let BigQuery try to autodetect the schema and format of the table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#autodetect GoogleBigqueryTable#autodetect}
        :param source_uris: A list of the fully-qualified URIs that point to your data in Google Cloud. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_uris GoogleBigqueryTable#source_uris}
        :param avro_options: avro_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#avro_options GoogleBigqueryTable#avro_options}
        :param compression: The compression type of the data source. Valid values are "NONE" or "GZIP". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#compression GoogleBigqueryTable#compression}
        :param connection_id: The connection specifying the credentials to be used to read external storage, such as Azure Blob, Cloud Storage, or S3. The connectionId can have the form "{{project}}.{{location}}.{{connection_id}}" or "projects/{{project}}/locations/{{location}}/connections/{{connection_id}}". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#connection_id GoogleBigqueryTable#connection_id}
        :param csv_options: csv_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#csv_options GoogleBigqueryTable#csv_options}
        :param file_set_spec_type: Specifies how source URIs are interpreted for constructing the file set to load. By default source URIs are expanded against the underlying storage. Other options include specifying manifest files. Only applicable to object storage systems. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#file_set_spec_type GoogleBigqueryTable#file_set_spec_type}
        :param google_sheets_options: google_sheets_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#google_sheets_options GoogleBigqueryTable#google_sheets_options}
        :param hive_partitioning_options: hive_partitioning_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#hive_partitioning_options GoogleBigqueryTable#hive_partitioning_options}
        :param ignore_unknown_values: Indicates if BigQuery should allow extra values that are not represented in the table schema. If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#ignore_unknown_values GoogleBigqueryTable#ignore_unknown_values}
        :param json_options: json_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#json_options GoogleBigqueryTable#json_options}
        :param max_bad_records: The maximum number of bad records that BigQuery can ignore when reading data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#max_bad_records GoogleBigqueryTable#max_bad_records}
        :param metadata_cache_mode: Metadata Cache Mode for the table. Set this to enable caching of metadata from external data source. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#metadata_cache_mode GoogleBigqueryTable#metadata_cache_mode}
        :param object_metadata: Object Metadata is used to create Object Tables. Object Tables contain a listing of objects (with their metadata) found at the sourceUris. If ObjectMetadata is set, sourceFormat should be omitted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#object_metadata GoogleBigqueryTable#object_metadata}
        :param parquet_options: parquet_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#parquet_options GoogleBigqueryTable#parquet_options}
        :param reference_file_schema_uri: When creating an external table, the user can provide a reference file with the table schema. This is enabled for the following formats: AVRO, PARQUET, ORC. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#reference_file_schema_uri GoogleBigqueryTable#reference_file_schema_uri}
        :param schema: A JSON schema for the external table. Schema is required for CSV and JSON formats and is disallowed for Google Cloud Bigtable, Cloud Datastore backups, and Avro formats when using external tables. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#schema GoogleBigqueryTable#schema}
        :param source_format: Please see sourceFormat under ExternalDataConfiguration in Bigquery's public API documentation (https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) for supported formats. To use "GOOGLE_SHEETS" the scopes must include "googleapis.com/auth/drive.readonly". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_format GoogleBigqueryTable#source_format}
        '''
        value = GoogleBigqueryTableExternalDataConfiguration(
            autodetect=autodetect,
            source_uris=source_uris,
            avro_options=avro_options,
            compression=compression,
            connection_id=connection_id,
            csv_options=csv_options,
            file_set_spec_type=file_set_spec_type,
            google_sheets_options=google_sheets_options,
            hive_partitioning_options=hive_partitioning_options,
            ignore_unknown_values=ignore_unknown_values,
            json_options=json_options,
            max_bad_records=max_bad_records,
            metadata_cache_mode=metadata_cache_mode,
            object_metadata=object_metadata,
            parquet_options=parquet_options,
            reference_file_schema_uri=reference_file_schema_uri,
            schema=schema,
            source_format=source_format,
        )

        return typing.cast(None, jsii.invoke(self, "putExternalDataConfiguration", [value]))

    @jsii.member(jsii_name="putMaterializedView")
    def put_materialized_view(
        self,
        *,
        query: builtins.str,
        allow_non_incremental_definition: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_refresh: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        refresh_interval_ms: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: A query whose result is persisted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#query GoogleBigqueryTable#query}
        :param allow_non_incremental_definition: Allow non incremental materialized view definition. The default value is false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#allow_non_incremental_definition GoogleBigqueryTable#allow_non_incremental_definition}
        :param enable_refresh: Specifies if BigQuery should automatically refresh materialized view when the base table is updated. The default is true. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#enable_refresh GoogleBigqueryTable#enable_refresh}
        :param refresh_interval_ms: Specifies maximum frequency at which this materialized view will be refreshed. The default is 1800000. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#refresh_interval_ms GoogleBigqueryTable#refresh_interval_ms}
        '''
        value = GoogleBigqueryTableMaterializedView(
            query=query,
            allow_non_incremental_definition=allow_non_incremental_definition,
            enable_refresh=enable_refresh,
            refresh_interval_ms=refresh_interval_ms,
        )

        return typing.cast(None, jsii.invoke(self, "putMaterializedView", [value]))

    @jsii.member(jsii_name="putRangePartitioning")
    def put_range_partitioning(
        self,
        *,
        field: builtins.str,
        range: typing.Union["GoogleBigqueryTableRangePartitioningRange", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param field: The field used to determine how to create a range-based partition. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#field GoogleBigqueryTable#field}
        :param range: range block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#range GoogleBigqueryTable#range}
        '''
        value = GoogleBigqueryTableRangePartitioning(field=field, range=range)

        return typing.cast(None, jsii.invoke(self, "putRangePartitioning", [value]))

    @jsii.member(jsii_name="putTableConstraints")
    def put_table_constraints(
        self,
        *,
        foreign_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleBigqueryTableTableConstraintsForeignKeys", typing.Dict[builtins.str, typing.Any]]]]] = None,
        primary_key: typing.Optional[typing.Union["GoogleBigqueryTableTableConstraintsPrimaryKey", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param foreign_keys: foreign_keys block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#foreign_keys GoogleBigqueryTable#foreign_keys}
        :param primary_key: primary_key block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#primary_key GoogleBigqueryTable#primary_key}
        '''
        value = GoogleBigqueryTableTableConstraints(
            foreign_keys=foreign_keys, primary_key=primary_key
        )

        return typing.cast(None, jsii.invoke(self, "putTableConstraints", [value]))

    @jsii.member(jsii_name="putTableReplicationInfo")
    def put_table_replication_info(
        self,
        *,
        source_dataset_id: builtins.str,
        source_project_id: builtins.str,
        source_table_id: builtins.str,
        replication_interval_ms: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param source_dataset_id: The ID of the source dataset. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_dataset_id GoogleBigqueryTable#source_dataset_id}
        :param source_project_id: The ID of the source project. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_project_id GoogleBigqueryTable#source_project_id}
        :param source_table_id: The ID of the source materialized view. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_table_id GoogleBigqueryTable#source_table_id}
        :param replication_interval_ms: The interval at which the source materialized view is polled for updates. The default is 300000. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#replication_interval_ms GoogleBigqueryTable#replication_interval_ms}
        '''
        value = GoogleBigqueryTableTableReplicationInfo(
            source_dataset_id=source_dataset_id,
            source_project_id=source_project_id,
            source_table_id=source_table_id,
            replication_interval_ms=replication_interval_ms,
        )

        return typing.cast(None, jsii.invoke(self, "putTableReplicationInfo", [value]))

    @jsii.member(jsii_name="putTimePartitioning")
    def put_time_partitioning(
        self,
        *,
        type: builtins.str,
        expiration_ms: typing.Optional[jsii.Number] = None,
        field: typing.Optional[builtins.str] = None,
        require_partition_filter: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param type: The supported types are DAY, HOUR, MONTH, and YEAR, which will generate one partition per day, hour, month, and year, respectively. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#type GoogleBigqueryTable#type}
        :param expiration_ms: Number of milliseconds for which to keep the storage for a partition. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#expiration_ms GoogleBigqueryTable#expiration_ms}
        :param field: The field used to determine how to create a time-based partition. If time-based partitioning is enabled without this value, the table is partitioned based on the load time. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#field GoogleBigqueryTable#field}
        :param require_partition_filter: If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        '''
        value = GoogleBigqueryTableTimePartitioning(
            type=type,
            expiration_ms=expiration_ms,
            field=field,
            require_partition_filter=require_partition_filter,
        )

        return typing.cast(None, jsii.invoke(self, "putTimePartitioning", [value]))

    @jsii.member(jsii_name="putView")
    def put_view(
        self,
        *,
        query: builtins.str,
        use_legacy_sql: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param query: A query that BigQuery executes when the view is referenced. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#query GoogleBigqueryTable#query}
        :param use_legacy_sql: Specifies whether to use BigQuery's legacy SQL for this view. The default value is true. If set to false, the view will use BigQuery's standard SQL Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#use_legacy_sql GoogleBigqueryTable#use_legacy_sql}
        '''
        value = GoogleBigqueryTableView(query=query, use_legacy_sql=use_legacy_sql)

        return typing.cast(None, jsii.invoke(self, "putView", [value]))

    @jsii.member(jsii_name="resetClustering")
    def reset_clustering(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClustering", []))

    @jsii.member(jsii_name="resetDeletionProtection")
    def reset_deletion_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeletionProtection", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEncryptionConfiguration")
    def reset_encryption_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionConfiguration", []))

    @jsii.member(jsii_name="resetExpirationTime")
    def reset_expiration_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationTime", []))

    @jsii.member(jsii_name="resetExternalDataConfiguration")
    def reset_external_data_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalDataConfiguration", []))

    @jsii.member(jsii_name="resetFriendlyName")
    def reset_friendly_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFriendlyName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMaterializedView")
    def reset_materialized_view(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaterializedView", []))

    @jsii.member(jsii_name="resetMaxStaleness")
    def reset_max_staleness(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxStaleness", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRangePartitioning")
    def reset_range_partitioning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangePartitioning", []))

    @jsii.member(jsii_name="resetRequirePartitionFilter")
    def reset_require_partition_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequirePartitionFilter", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @jsii.member(jsii_name="resetTableConstraints")
    def reset_table_constraints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTableConstraints", []))

    @jsii.member(jsii_name="resetTableReplicationInfo")
    def reset_table_replication_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTableReplicationInfo", []))

    @jsii.member(jsii_name="resetTimePartitioning")
    def reset_time_partitioning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimePartitioning", []))

    @jsii.member(jsii_name="resetView")
    def reset_view(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetView", []))

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
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "creationTime"))

    @builtins.property
    @jsii.member(jsii_name="effectiveLabels")
    def effective_labels(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "effectiveLabels"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> "GoogleBigqueryTableEncryptionConfigurationOutputReference":
        return typing.cast("GoogleBigqueryTableEncryptionConfigurationOutputReference", jsii.get(self, "encryptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="externalDataConfiguration")
    def external_data_configuration(
        self,
    ) -> "GoogleBigqueryTableExternalDataConfigurationOutputReference":
        return typing.cast("GoogleBigqueryTableExternalDataConfigurationOutputReference", jsii.get(self, "externalDataConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="lastModifiedTime")
    def last_modified_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @builtins.property
    @jsii.member(jsii_name="materializedView")
    def materialized_view(self) -> "GoogleBigqueryTableMaterializedViewOutputReference":
        return typing.cast("GoogleBigqueryTableMaterializedViewOutputReference", jsii.get(self, "materializedView"))

    @builtins.property
    @jsii.member(jsii_name="numBytes")
    def num_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numBytes"))

    @builtins.property
    @jsii.member(jsii_name="numLongTermBytes")
    def num_long_term_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numLongTermBytes"))

    @builtins.property
    @jsii.member(jsii_name="numRows")
    def num_rows(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numRows"))

    @builtins.property
    @jsii.member(jsii_name="rangePartitioning")
    def range_partitioning(
        self,
    ) -> "GoogleBigqueryTableRangePartitioningOutputReference":
        return typing.cast("GoogleBigqueryTableRangePartitioningOutputReference", jsii.get(self, "rangePartitioning"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="tableConstraints")
    def table_constraints(self) -> "GoogleBigqueryTableTableConstraintsOutputReference":
        return typing.cast("GoogleBigqueryTableTableConstraintsOutputReference", jsii.get(self, "tableConstraints"))

    @builtins.property
    @jsii.member(jsii_name="tableReplicationInfo")
    def table_replication_info(
        self,
    ) -> "GoogleBigqueryTableTableReplicationInfoOutputReference":
        return typing.cast("GoogleBigqueryTableTableReplicationInfoOutputReference", jsii.get(self, "tableReplicationInfo"))

    @builtins.property
    @jsii.member(jsii_name="terraformLabels")
    def terraform_labels(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "terraformLabels"))

    @builtins.property
    @jsii.member(jsii_name="timePartitioning")
    def time_partitioning(self) -> "GoogleBigqueryTableTimePartitioningOutputReference":
        return typing.cast("GoogleBigqueryTableTimePartitioningOutputReference", jsii.get(self, "timePartitioning"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="view")
    def view(self) -> "GoogleBigqueryTableViewOutputReference":
        return typing.cast("GoogleBigqueryTableViewOutputReference", jsii.get(self, "view"))

    @builtins.property
    @jsii.member(jsii_name="clusteringInput")
    def clustering_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clusteringInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionInput")
    def deletion_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deletionProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfigurationInput")
    def encryption_configuration_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableEncryptionConfiguration"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableEncryptionConfiguration"], jsii.get(self, "encryptionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationTimeInput")
    def expiration_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expirationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="externalDataConfigurationInput")
    def external_data_configuration_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfiguration"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfiguration"], jsii.get(self, "externalDataConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="friendlyNameInput")
    def friendly_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "friendlyNameInput"))

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
    @jsii.member(jsii_name="materializedViewInput")
    def materialized_view_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableMaterializedView"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableMaterializedView"], jsii.get(self, "materializedViewInput"))

    @builtins.property
    @jsii.member(jsii_name="maxStalenessInput")
    def max_staleness_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxStalenessInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="rangePartitioningInput")
    def range_partitioning_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableRangePartitioning"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableRangePartitioning"], jsii.get(self, "rangePartitioningInput"))

    @builtins.property
    @jsii.member(jsii_name="requirePartitionFilterInput")
    def require_partition_filter_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requirePartitionFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="tableConstraintsInput")
    def table_constraints_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableTableConstraints"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableTableConstraints"], jsii.get(self, "tableConstraintsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableReplicationInfoInput")
    def table_replication_info_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableTableReplicationInfo"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableTableReplicationInfo"], jsii.get(self, "tableReplicationInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="timePartitioningInput")
    def time_partitioning_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableTimePartitioning"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableTimePartitioning"], jsii.get(self, "timePartitioningInput"))

    @builtins.property
    @jsii.member(jsii_name="viewInput")
    def view_input(self) -> typing.Optional["GoogleBigqueryTableView"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableView"], jsii.get(self, "viewInput"))

    @builtins.property
    @jsii.member(jsii_name="clustering")
    def clustering(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clustering"))

    @clustering.setter
    def clustering(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76894c589838c9a082faa067db42cb728a27c971a2d0ad370b7b178204da57ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clustering", value)

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__444fde6c81e599222175cc658ae45fe6c093fe191c00a233a5f40f7bc1fb336d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1011cf482908614955015cc805e84f70ab837396dd842272769e4b6b3b7c5b75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a627661f82c2ab3dfa72214456e35f008c6e5e72c7b73b79d89bec9972dfcf18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expirationTime")
    def expiration_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "expirationTime"))

    @expiration_time.setter
    def expiration_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aad04d72634af56dec81efde39895a173adcdb8f175e82727f3c3db3c5b05318)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationTime", value)

    @builtins.property
    @jsii.member(jsii_name="friendlyName")
    def friendly_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "friendlyName"))

    @friendly_name.setter
    def friendly_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d02a1d409ed98f91e9798e6405fa6cc96c6dc7fc467092ba3a7da0653c4d6c21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "friendlyName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53c89c2133be9065c731f779e2d646063a756da3380001de916a368f2a8ae8c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c7c726340d6131315a61d2bb511d6f8909ffdaf68ed5e102831468ccc3f7ecf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="maxStaleness")
    def max_staleness(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxStaleness"))

    @max_staleness.setter
    def max_staleness(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa60c124f603637a061fca4fff84c8e2d3853b37e9290cbb8172e05919d4625d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxStaleness", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c0404a74d6978f79150373564d8fdae158668d579eed2956a2da670672f120b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="requirePartitionFilter")
    def require_partition_filter(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requirePartitionFilter"))

    @require_partition_filter.setter
    def require_partition_filter(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94fd9cbfaaef9b873460a28028bd420886528d67ece5838898c1d1f53b7283cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirePartitionFilter", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2b71b896e2687e4be682d51e900d0540d892d36776f184da069895f3c5f87ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe7711efd92dab86d211eaa8e00fef8b6bcd8445961a2714db64586f80c2f98f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dataset_id": "datasetId",
        "table_id": "tableId",
        "clustering": "clustering",
        "deletion_protection": "deletionProtection",
        "description": "description",
        "encryption_configuration": "encryptionConfiguration",
        "expiration_time": "expirationTime",
        "external_data_configuration": "externalDataConfiguration",
        "friendly_name": "friendlyName",
        "id": "id",
        "labels": "labels",
        "materialized_view": "materializedView",
        "max_staleness": "maxStaleness",
        "project": "project",
        "range_partitioning": "rangePartitioning",
        "require_partition_filter": "requirePartitionFilter",
        "schema": "schema",
        "table_constraints": "tableConstraints",
        "table_replication_info": "tableReplicationInfo",
        "time_partitioning": "timePartitioning",
        "view": "view",
    },
)
class GoogleBigqueryTableConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        dataset_id: builtins.str,
        table_id: builtins.str,
        clustering: typing.Optional[typing.Sequence[builtins.str]] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union["GoogleBigqueryTableEncryptionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        expiration_time: typing.Optional[jsii.Number] = None,
        external_data_configuration: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        materialized_view: typing.Optional[typing.Union["GoogleBigqueryTableMaterializedView", typing.Dict[builtins.str, typing.Any]]] = None,
        max_staleness: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        range_partitioning: typing.Optional[typing.Union["GoogleBigqueryTableRangePartitioning", typing.Dict[builtins.str, typing.Any]]] = None,
        require_partition_filter: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        schema: typing.Optional[builtins.str] = None,
        table_constraints: typing.Optional[typing.Union["GoogleBigqueryTableTableConstraints", typing.Dict[builtins.str, typing.Any]]] = None,
        table_replication_info: typing.Optional[typing.Union["GoogleBigqueryTableTableReplicationInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        time_partitioning: typing.Optional[typing.Union["GoogleBigqueryTableTimePartitioning", typing.Dict[builtins.str, typing.Any]]] = None,
        view: typing.Optional[typing.Union["GoogleBigqueryTableView", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dataset_id: The dataset ID to create the table in. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#dataset_id GoogleBigqueryTable#dataset_id}
        :param table_id: A unique ID for the resource. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#table_id GoogleBigqueryTable#table_id}
        :param clustering: Specifies column names to use for data clustering. Up to four top-level columns are allowed, and should be specified in descending priority order. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#clustering GoogleBigqueryTable#clustering}
        :param deletion_protection: Whether or not to allow Terraform to destroy the instance. Unless this field is set to false in Terraform state, a terraform destroy or terraform apply that would delete the instance will fail. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#deletion_protection GoogleBigqueryTable#deletion_protection}
        :param description: The field description. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#description GoogleBigqueryTable#description}
        :param encryption_configuration: encryption_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#encryption_configuration GoogleBigqueryTable#encryption_configuration}
        :param expiration_time: The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#expiration_time GoogleBigqueryTable#expiration_time}
        :param external_data_configuration: external_data_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#external_data_configuration GoogleBigqueryTable#external_data_configuration}
        :param friendly_name: A descriptive name for the table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#friendly_name GoogleBigqueryTable#friendly_name}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#id GoogleBigqueryTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A mapping of labels to assign to the resource. **Note**: This field is non-authoritative, and will only manage the labels present in your configuration. Please refer to the field 'effective_labels' for all of the labels present on the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#labels GoogleBigqueryTable#labels}
        :param materialized_view: materialized_view block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#materialized_view GoogleBigqueryTable#materialized_view}
        :param max_staleness: The maximum staleness of data that could be returned when the table (or stale MV) is queried. Staleness encoded as a string encoding of `SQL IntervalValue type <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#interval_type>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#max_staleness GoogleBigqueryTable#max_staleness}
        :param project: The ID of the project in which the resource belongs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#project GoogleBigqueryTable#project}
        :param range_partitioning: range_partitioning block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#range_partitioning GoogleBigqueryTable#range_partitioning}
        :param require_partition_filter: If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        :param schema: A JSON schema for the table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#schema GoogleBigqueryTable#schema}
        :param table_constraints: table_constraints block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#table_constraints GoogleBigqueryTable#table_constraints}
        :param table_replication_info: table_replication_info block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#table_replication_info GoogleBigqueryTable#table_replication_info}
        :param time_partitioning: time_partitioning block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#time_partitioning GoogleBigqueryTable#time_partitioning}
        :param view: view block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#view GoogleBigqueryTable#view}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(encryption_configuration, dict):
            encryption_configuration = GoogleBigqueryTableEncryptionConfiguration(**encryption_configuration)
        if isinstance(external_data_configuration, dict):
            external_data_configuration = GoogleBigqueryTableExternalDataConfiguration(**external_data_configuration)
        if isinstance(materialized_view, dict):
            materialized_view = GoogleBigqueryTableMaterializedView(**materialized_view)
        if isinstance(range_partitioning, dict):
            range_partitioning = GoogleBigqueryTableRangePartitioning(**range_partitioning)
        if isinstance(table_constraints, dict):
            table_constraints = GoogleBigqueryTableTableConstraints(**table_constraints)
        if isinstance(table_replication_info, dict):
            table_replication_info = GoogleBigqueryTableTableReplicationInfo(**table_replication_info)
        if isinstance(time_partitioning, dict):
            time_partitioning = GoogleBigqueryTableTimePartitioning(**time_partitioning)
        if isinstance(view, dict):
            view = GoogleBigqueryTableView(**view)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54b963582085445098c070f12dbc2aecf85c8a60e6c73ca013d35067bed2a4a7)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
            check_type(argname="argument clustering", value=clustering, expected_type=type_hints["clustering"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument expiration_time", value=expiration_time, expected_type=type_hints["expiration_time"])
            check_type(argname="argument external_data_configuration", value=external_data_configuration, expected_type=type_hints["external_data_configuration"])
            check_type(argname="argument friendly_name", value=friendly_name, expected_type=type_hints["friendly_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument materialized_view", value=materialized_view, expected_type=type_hints["materialized_view"])
            check_type(argname="argument max_staleness", value=max_staleness, expected_type=type_hints["max_staleness"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument range_partitioning", value=range_partitioning, expected_type=type_hints["range_partitioning"])
            check_type(argname="argument require_partition_filter", value=require_partition_filter, expected_type=type_hints["require_partition_filter"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument table_constraints", value=table_constraints, expected_type=type_hints["table_constraints"])
            check_type(argname="argument table_replication_info", value=table_replication_info, expected_type=type_hints["table_replication_info"])
            check_type(argname="argument time_partitioning", value=time_partitioning, expected_type=type_hints["time_partitioning"])
            check_type(argname="argument view", value=view, expected_type=type_hints["view"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_id": dataset_id,
            "table_id": table_id,
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
        if clustering is not None:
            self._values["clustering"] = clustering
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if description is not None:
            self._values["description"] = description
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if expiration_time is not None:
            self._values["expiration_time"] = expiration_time
        if external_data_configuration is not None:
            self._values["external_data_configuration"] = external_data_configuration
        if friendly_name is not None:
            self._values["friendly_name"] = friendly_name
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if materialized_view is not None:
            self._values["materialized_view"] = materialized_view
        if max_staleness is not None:
            self._values["max_staleness"] = max_staleness
        if project is not None:
            self._values["project"] = project
        if range_partitioning is not None:
            self._values["range_partitioning"] = range_partitioning
        if require_partition_filter is not None:
            self._values["require_partition_filter"] = require_partition_filter
        if schema is not None:
            self._values["schema"] = schema
        if table_constraints is not None:
            self._values["table_constraints"] = table_constraints
        if table_replication_info is not None:
            self._values["table_replication_info"] = table_replication_info
        if time_partitioning is not None:
            self._values["time_partitioning"] = time_partitioning
        if view is not None:
            self._values["view"] = view

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
    def dataset_id(self) -> builtins.str:
        '''The dataset ID to create the table in. Changing this forces a new resource to be created.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#dataset_id GoogleBigqueryTable#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_id(self) -> builtins.str:
        '''A unique ID for the resource. Changing this forces a new resource to be created.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#table_id GoogleBigqueryTable#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def clustering(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies column names to use for data clustering.

        Up to four top-level columns are allowed, and should be specified in descending priority order.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#clustering GoogleBigqueryTable#clustering}
        '''
        result = self._values.get("clustering")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not to allow Terraform to destroy the instance.

        Unless this field is set to false in Terraform state, a terraform destroy or terraform apply that would delete the instance will fail.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#deletion_protection GoogleBigqueryTable#deletion_protection}
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The field description.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#description GoogleBigqueryTable#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional["GoogleBigqueryTableEncryptionConfiguration"]:
        '''encryption_configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#encryption_configuration GoogleBigqueryTable#encryption_configuration}
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional["GoogleBigqueryTableEncryptionConfiguration"], result)

    @builtins.property
    def expiration_time(self) -> typing.Optional[jsii.Number]:
        '''The time when this table expires, in milliseconds since the epoch.

        If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#expiration_time GoogleBigqueryTable#expiration_time}
        '''
        result = self._values.get("expiration_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def external_data_configuration(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfiguration"]:
        '''external_data_configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#external_data_configuration GoogleBigqueryTable#external_data_configuration}
        '''
        result = self._values.get("external_data_configuration")
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfiguration"], result)

    @builtins.property
    def friendly_name(self) -> typing.Optional[builtins.str]:
        '''A descriptive name for the table.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#friendly_name GoogleBigqueryTable#friendly_name}
        '''
        result = self._values.get("friendly_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#id GoogleBigqueryTable#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A mapping of labels to assign to the resource.

        **Note**: This field is non-authoritative, and will only manage the labels present in your configuration.
        Please refer to the field 'effective_labels' for all of the labels present on the resource.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#labels GoogleBigqueryTable#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def materialized_view(
        self,
    ) -> typing.Optional["GoogleBigqueryTableMaterializedView"]:
        '''materialized_view block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#materialized_view GoogleBigqueryTable#materialized_view}
        '''
        result = self._values.get("materialized_view")
        return typing.cast(typing.Optional["GoogleBigqueryTableMaterializedView"], result)

    @builtins.property
    def max_staleness(self) -> typing.Optional[builtins.str]:
        '''The maximum staleness of data that could be returned when the table (or stale MV) is queried.

        Staleness encoded as a string encoding of `SQL IntervalValue type <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#interval_type>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#max_staleness GoogleBigqueryTable#max_staleness}
        '''
        result = self._values.get("max_staleness")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which the resource belongs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#project GoogleBigqueryTable#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def range_partitioning(
        self,
    ) -> typing.Optional["GoogleBigqueryTableRangePartitioning"]:
        '''range_partitioning block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#range_partitioning GoogleBigqueryTable#range_partitioning}
        '''
        result = self._values.get("range_partitioning")
        return typing.cast(typing.Optional["GoogleBigqueryTableRangePartitioning"], result)

    @builtins.property
    def require_partition_filter(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        '''
        result = self._values.get("require_partition_filter")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def schema(self) -> typing.Optional[builtins.str]:
        '''A JSON schema for the table.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#schema GoogleBigqueryTable#schema}
        '''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def table_constraints(
        self,
    ) -> typing.Optional["GoogleBigqueryTableTableConstraints"]:
        '''table_constraints block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#table_constraints GoogleBigqueryTable#table_constraints}
        '''
        result = self._values.get("table_constraints")
        return typing.cast(typing.Optional["GoogleBigqueryTableTableConstraints"], result)

    @builtins.property
    def table_replication_info(
        self,
    ) -> typing.Optional["GoogleBigqueryTableTableReplicationInfo"]:
        '''table_replication_info block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#table_replication_info GoogleBigqueryTable#table_replication_info}
        '''
        result = self._values.get("table_replication_info")
        return typing.cast(typing.Optional["GoogleBigqueryTableTableReplicationInfo"], result)

    @builtins.property
    def time_partitioning(
        self,
    ) -> typing.Optional["GoogleBigqueryTableTimePartitioning"]:
        '''time_partitioning block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#time_partitioning GoogleBigqueryTable#time_partitioning}
        '''
        result = self._values.get("time_partitioning")
        return typing.cast(typing.Optional["GoogleBigqueryTableTimePartitioning"], result)

    @builtins.property
    def view(self) -> typing.Optional["GoogleBigqueryTableView"]:
        '''view block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#view GoogleBigqueryTable#view}
        '''
        result = self._values.get("view")
        return typing.cast(typing.Optional["GoogleBigqueryTableView"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableEncryptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"kms_key_name": "kmsKeyName"},
)
class GoogleBigqueryTableEncryptionConfiguration:
    def __init__(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: The self link or full name of a key which should be used to encrypt this table. Note that the default bigquery service account will need to have encrypt/decrypt permissions on this key - you may want to see the google_bigquery_default_service_account datasource and the google_kms_crypto_key_iam_binding resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#kms_key_name GoogleBigqueryTable#kms_key_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a9e5b9d2635380dd8876b4ead6886d33a3f196be172509019ee1c62e4b0cac4)
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kms_key_name": kms_key_name,
        }

    @builtins.property
    def kms_key_name(self) -> builtins.str:
        '''The self link or full name of a key which should be used to encrypt this table.

        Note that the default bigquery service account will need to have encrypt/decrypt permissions on this key - you may want to see the google_bigquery_default_service_account datasource and the google_kms_crypto_key_iam_binding resource.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#kms_key_name GoogleBigqueryTable#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        assert result is not None, "Required property 'kms_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableEncryptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableEncryptionConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableEncryptionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac47feacba2ff63b4d4b6cd834c261973959eb828392257e86c965430b233935)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="kmsKeyVersion")
    def kms_key_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyVersion"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyNameInput")
    def kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyName")
    def kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyName"))

    @kms_key_name.setter
    def kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1866154c2a4e3aa1117ffef1107ae3842724380d443407d59da9ac9fed161a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableEncryptionConfiguration]:
        return typing.cast(typing.Optional[GoogleBigqueryTableEncryptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableEncryptionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdee95f64c6d871660e34e53f1d38adcb1b0ab6d2cee778ebef16086d73a96a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "autodetect": "autodetect",
        "source_uris": "sourceUris",
        "avro_options": "avroOptions",
        "compression": "compression",
        "connection_id": "connectionId",
        "csv_options": "csvOptions",
        "file_set_spec_type": "fileSetSpecType",
        "google_sheets_options": "googleSheetsOptions",
        "hive_partitioning_options": "hivePartitioningOptions",
        "ignore_unknown_values": "ignoreUnknownValues",
        "json_options": "jsonOptions",
        "max_bad_records": "maxBadRecords",
        "metadata_cache_mode": "metadataCacheMode",
        "object_metadata": "objectMetadata",
        "parquet_options": "parquetOptions",
        "reference_file_schema_uri": "referenceFileSchemaUri",
        "schema": "schema",
        "source_format": "sourceFormat",
    },
)
class GoogleBigqueryTableExternalDataConfiguration:
    def __init__(
        self,
        *,
        autodetect: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        source_uris: typing.Sequence[builtins.str],
        avro_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationAvroOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        compression: typing.Optional[builtins.str] = None,
        connection_id: typing.Optional[builtins.str] = None,
        csv_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationCsvOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        file_set_spec_type: typing.Optional[builtins.str] = None,
        google_sheets_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        hive_partitioning_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        ignore_unknown_values: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        json_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationJsonOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        max_bad_records: typing.Optional[jsii.Number] = None,
        metadata_cache_mode: typing.Optional[builtins.str] = None,
        object_metadata: typing.Optional[builtins.str] = None,
        parquet_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationParquetOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        reference_file_schema_uri: typing.Optional[builtins.str] = None,
        schema: typing.Optional[builtins.str] = None,
        source_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param autodetect: Let BigQuery try to autodetect the schema and format of the table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#autodetect GoogleBigqueryTable#autodetect}
        :param source_uris: A list of the fully-qualified URIs that point to your data in Google Cloud. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_uris GoogleBigqueryTable#source_uris}
        :param avro_options: avro_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#avro_options GoogleBigqueryTable#avro_options}
        :param compression: The compression type of the data source. Valid values are "NONE" or "GZIP". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#compression GoogleBigqueryTable#compression}
        :param connection_id: The connection specifying the credentials to be used to read external storage, such as Azure Blob, Cloud Storage, or S3. The connectionId can have the form "{{project}}.{{location}}.{{connection_id}}" or "projects/{{project}}/locations/{{location}}/connections/{{connection_id}}". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#connection_id GoogleBigqueryTable#connection_id}
        :param csv_options: csv_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#csv_options GoogleBigqueryTable#csv_options}
        :param file_set_spec_type: Specifies how source URIs are interpreted for constructing the file set to load. By default source URIs are expanded against the underlying storage. Other options include specifying manifest files. Only applicable to object storage systems. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#file_set_spec_type GoogleBigqueryTable#file_set_spec_type}
        :param google_sheets_options: google_sheets_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#google_sheets_options GoogleBigqueryTable#google_sheets_options}
        :param hive_partitioning_options: hive_partitioning_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#hive_partitioning_options GoogleBigqueryTable#hive_partitioning_options}
        :param ignore_unknown_values: Indicates if BigQuery should allow extra values that are not represented in the table schema. If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#ignore_unknown_values GoogleBigqueryTable#ignore_unknown_values}
        :param json_options: json_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#json_options GoogleBigqueryTable#json_options}
        :param max_bad_records: The maximum number of bad records that BigQuery can ignore when reading data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#max_bad_records GoogleBigqueryTable#max_bad_records}
        :param metadata_cache_mode: Metadata Cache Mode for the table. Set this to enable caching of metadata from external data source. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#metadata_cache_mode GoogleBigqueryTable#metadata_cache_mode}
        :param object_metadata: Object Metadata is used to create Object Tables. Object Tables contain a listing of objects (with their metadata) found at the sourceUris. If ObjectMetadata is set, sourceFormat should be omitted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#object_metadata GoogleBigqueryTable#object_metadata}
        :param parquet_options: parquet_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#parquet_options GoogleBigqueryTable#parquet_options}
        :param reference_file_schema_uri: When creating an external table, the user can provide a reference file with the table schema. This is enabled for the following formats: AVRO, PARQUET, ORC. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#reference_file_schema_uri GoogleBigqueryTable#reference_file_schema_uri}
        :param schema: A JSON schema for the external table. Schema is required for CSV and JSON formats and is disallowed for Google Cloud Bigtable, Cloud Datastore backups, and Avro formats when using external tables. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#schema GoogleBigqueryTable#schema}
        :param source_format: Please see sourceFormat under ExternalDataConfiguration in Bigquery's public API documentation (https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) for supported formats. To use "GOOGLE_SHEETS" the scopes must include "googleapis.com/auth/drive.readonly". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_format GoogleBigqueryTable#source_format}
        '''
        if isinstance(avro_options, dict):
            avro_options = GoogleBigqueryTableExternalDataConfigurationAvroOptions(**avro_options)
        if isinstance(csv_options, dict):
            csv_options = GoogleBigqueryTableExternalDataConfigurationCsvOptions(**csv_options)
        if isinstance(google_sheets_options, dict):
            google_sheets_options = GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions(**google_sheets_options)
        if isinstance(hive_partitioning_options, dict):
            hive_partitioning_options = GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions(**hive_partitioning_options)
        if isinstance(json_options, dict):
            json_options = GoogleBigqueryTableExternalDataConfigurationJsonOptions(**json_options)
        if isinstance(parquet_options, dict):
            parquet_options = GoogleBigqueryTableExternalDataConfigurationParquetOptions(**parquet_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__602e971b4bfcff52a501458a21051a2cd4a2d264003fefb408f07cedb18d84e5)
            check_type(argname="argument autodetect", value=autodetect, expected_type=type_hints["autodetect"])
            check_type(argname="argument source_uris", value=source_uris, expected_type=type_hints["source_uris"])
            check_type(argname="argument avro_options", value=avro_options, expected_type=type_hints["avro_options"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument csv_options", value=csv_options, expected_type=type_hints["csv_options"])
            check_type(argname="argument file_set_spec_type", value=file_set_spec_type, expected_type=type_hints["file_set_spec_type"])
            check_type(argname="argument google_sheets_options", value=google_sheets_options, expected_type=type_hints["google_sheets_options"])
            check_type(argname="argument hive_partitioning_options", value=hive_partitioning_options, expected_type=type_hints["hive_partitioning_options"])
            check_type(argname="argument ignore_unknown_values", value=ignore_unknown_values, expected_type=type_hints["ignore_unknown_values"])
            check_type(argname="argument json_options", value=json_options, expected_type=type_hints["json_options"])
            check_type(argname="argument max_bad_records", value=max_bad_records, expected_type=type_hints["max_bad_records"])
            check_type(argname="argument metadata_cache_mode", value=metadata_cache_mode, expected_type=type_hints["metadata_cache_mode"])
            check_type(argname="argument object_metadata", value=object_metadata, expected_type=type_hints["object_metadata"])
            check_type(argname="argument parquet_options", value=parquet_options, expected_type=type_hints["parquet_options"])
            check_type(argname="argument reference_file_schema_uri", value=reference_file_schema_uri, expected_type=type_hints["reference_file_schema_uri"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument source_format", value=source_format, expected_type=type_hints["source_format"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "autodetect": autodetect,
            "source_uris": source_uris,
        }
        if avro_options is not None:
            self._values["avro_options"] = avro_options
        if compression is not None:
            self._values["compression"] = compression
        if connection_id is not None:
            self._values["connection_id"] = connection_id
        if csv_options is not None:
            self._values["csv_options"] = csv_options
        if file_set_spec_type is not None:
            self._values["file_set_spec_type"] = file_set_spec_type
        if google_sheets_options is not None:
            self._values["google_sheets_options"] = google_sheets_options
        if hive_partitioning_options is not None:
            self._values["hive_partitioning_options"] = hive_partitioning_options
        if ignore_unknown_values is not None:
            self._values["ignore_unknown_values"] = ignore_unknown_values
        if json_options is not None:
            self._values["json_options"] = json_options
        if max_bad_records is not None:
            self._values["max_bad_records"] = max_bad_records
        if metadata_cache_mode is not None:
            self._values["metadata_cache_mode"] = metadata_cache_mode
        if object_metadata is not None:
            self._values["object_metadata"] = object_metadata
        if parquet_options is not None:
            self._values["parquet_options"] = parquet_options
        if reference_file_schema_uri is not None:
            self._values["reference_file_schema_uri"] = reference_file_schema_uri
        if schema is not None:
            self._values["schema"] = schema
        if source_format is not None:
            self._values["source_format"] = source_format

    @builtins.property
    def autodetect(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Let BigQuery try to autodetect the schema and format of the table.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#autodetect GoogleBigqueryTable#autodetect}
        '''
        result = self._values.get("autodetect")
        assert result is not None, "Required property 'autodetect' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def source_uris(self) -> typing.List[builtins.str]:
        '''A list of the fully-qualified URIs that point to your data in Google Cloud.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_uris GoogleBigqueryTable#source_uris}
        '''
        result = self._values.get("source_uris")
        assert result is not None, "Required property 'source_uris' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def avro_options(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfigurationAvroOptions"]:
        '''avro_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#avro_options GoogleBigqueryTable#avro_options}
        '''
        result = self._values.get("avro_options")
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfigurationAvroOptions"], result)

    @builtins.property
    def compression(self) -> typing.Optional[builtins.str]:
        '''The compression type of the data source. Valid values are "NONE" or "GZIP".

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#compression GoogleBigqueryTable#compression}
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_id(self) -> typing.Optional[builtins.str]:
        '''The connection specifying the credentials to be used to read external storage, such as Azure Blob, Cloud Storage, or S3.

        The connectionId can have the form "{{project}}.{{location}}.{{connection_id}}" or "projects/{{project}}/locations/{{location}}/connections/{{connection_id}}".

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#connection_id GoogleBigqueryTable#connection_id}
        '''
        result = self._values.get("connection_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_options(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfigurationCsvOptions"]:
        '''csv_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#csv_options GoogleBigqueryTable#csv_options}
        '''
        result = self._values.get("csv_options")
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfigurationCsvOptions"], result)

    @builtins.property
    def file_set_spec_type(self) -> typing.Optional[builtins.str]:
        '''Specifies how source URIs are interpreted for constructing the file set to load.

        By default source URIs are expanded against the underlying storage.  Other options include specifying manifest files. Only applicable to object storage systems.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#file_set_spec_type GoogleBigqueryTable#file_set_spec_type}
        '''
        result = self._values.get("file_set_spec_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def google_sheets_options(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions"]:
        '''google_sheets_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#google_sheets_options GoogleBigqueryTable#google_sheets_options}
        '''
        result = self._values.get("google_sheets_options")
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions"], result)

    @builtins.property
    def hive_partitioning_options(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions"]:
        '''hive_partitioning_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#hive_partitioning_options GoogleBigqueryTable#hive_partitioning_options}
        '''
        result = self._values.get("hive_partitioning_options")
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions"], result)

    @builtins.property
    def ignore_unknown_values(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates if BigQuery should allow extra values that are not represented in the table schema.

        If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#ignore_unknown_values GoogleBigqueryTable#ignore_unknown_values}
        '''
        result = self._values.get("ignore_unknown_values")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def json_options(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfigurationJsonOptions"]:
        '''json_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#json_options GoogleBigqueryTable#json_options}
        '''
        result = self._values.get("json_options")
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfigurationJsonOptions"], result)

    @builtins.property
    def max_bad_records(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of bad records that BigQuery can ignore when reading data.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#max_bad_records GoogleBigqueryTable#max_bad_records}
        '''
        result = self._values.get("max_bad_records")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metadata_cache_mode(self) -> typing.Optional[builtins.str]:
        '''Metadata Cache Mode for the table. Set this to enable caching of metadata from external data source.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#metadata_cache_mode GoogleBigqueryTable#metadata_cache_mode}
        '''
        result = self._values.get("metadata_cache_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_metadata(self) -> typing.Optional[builtins.str]:
        '''Object Metadata is used to create Object Tables.

        Object Tables contain a listing of objects (with their metadata) found at the sourceUris. If ObjectMetadata is set, sourceFormat should be omitted.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#object_metadata GoogleBigqueryTable#object_metadata}
        '''
        result = self._values.get("object_metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parquet_options(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfigurationParquetOptions"]:
        '''parquet_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#parquet_options GoogleBigqueryTable#parquet_options}
        '''
        result = self._values.get("parquet_options")
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfigurationParquetOptions"], result)

    @builtins.property
    def reference_file_schema_uri(self) -> typing.Optional[builtins.str]:
        '''When creating an external table, the user can provide a reference file with the table schema.

        This is enabled for the following formats: AVRO, PARQUET, ORC.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#reference_file_schema_uri GoogleBigqueryTable#reference_file_schema_uri}
        '''
        result = self._values.get("reference_file_schema_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema(self) -> typing.Optional[builtins.str]:
        '''A JSON schema for the external table.

        Schema is required for CSV and JSON formats and is disallowed for Google Cloud Bigtable, Cloud Datastore backups, and Avro formats when using external tables.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#schema GoogleBigqueryTable#schema}
        '''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_format(self) -> typing.Optional[builtins.str]:
        '''Please see sourceFormat under ExternalDataConfiguration in Bigquery's public API documentation (https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) for supported formats. To use "GOOGLE_SHEETS" the scopes must include "googleapis.com/auth/drive.readonly".

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_format GoogleBigqueryTable#source_format}
        '''
        result = self._values.get("source_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableExternalDataConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationAvroOptions",
    jsii_struct_bases=[],
    name_mapping={"use_avro_logical_types": "useAvroLogicalTypes"},
)
class GoogleBigqueryTableExternalDataConfigurationAvroOptions:
    def __init__(
        self,
        *,
        use_avro_logical_types: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param use_avro_logical_types: If sourceFormat is set to "AVRO", indicates whether to interpret logical types as the corresponding BigQuery data type (for example, TIMESTAMP), instead of using the raw type (for example, INTEGER). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#use_avro_logical_types GoogleBigqueryTable#use_avro_logical_types}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e056d587d279501e907787fbdde8bcd72c0bbc0a0b7ebf5a1966e26a43c6d82e)
            check_type(argname="argument use_avro_logical_types", value=use_avro_logical_types, expected_type=type_hints["use_avro_logical_types"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "use_avro_logical_types": use_avro_logical_types,
        }

    @builtins.property
    def use_avro_logical_types(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''If sourceFormat is set to "AVRO", indicates whether to interpret logical types as the corresponding BigQuery data type (for example, TIMESTAMP), instead of using the raw type (for example, INTEGER).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#use_avro_logical_types GoogleBigqueryTable#use_avro_logical_types}
        '''
        result = self._values.get("use_avro_logical_types")
        assert result is not None, "Required property 'use_avro_logical_types' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableExternalDataConfigurationAvroOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableExternalDataConfigurationAvroOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationAvroOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a447dc5261f83cb375ec248b63ed2dc1f0f81b51042f2c5ceb195795eba3ddd3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="useAvroLogicalTypesInput")
    def use_avro_logical_types_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useAvroLogicalTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="useAvroLogicalTypes")
    def use_avro_logical_types(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useAvroLogicalTypes"))

    @use_avro_logical_types.setter
    def use_avro_logical_types(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e208c6280c6864ccc073f452c7f7b498650e985d39ac2611b3694de7d527104c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useAvroLogicalTypes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationAvroOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationAvroOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationAvroOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beb84d5b86dff064b1da2c8a64bdb0a380f12846ab88737aba25a25c6198c639)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationCsvOptions",
    jsii_struct_bases=[],
    name_mapping={
        "quote": "quote",
        "allow_jagged_rows": "allowJaggedRows",
        "allow_quoted_newlines": "allowQuotedNewlines",
        "encoding": "encoding",
        "field_delimiter": "fieldDelimiter",
        "skip_leading_rows": "skipLeadingRows",
    },
)
class GoogleBigqueryTableExternalDataConfigurationCsvOptions:
    def __init__(
        self,
        *,
        quote: builtins.str,
        allow_jagged_rows: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_quoted_newlines: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encoding: typing.Optional[builtins.str] = None,
        field_delimiter: typing.Optional[builtins.str] = None,
        skip_leading_rows: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param quote: The value that is used to quote data sections in a CSV file. If your data does not contain quoted sections, set the property value to an empty string. If your data contains quoted newline characters, you must also set the allow_quoted_newlines property to true. The API-side default is ", specified in Terraform escaped as ". Due to limitations with Terraform default values, this value is required to be explicitly set. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#quote GoogleBigqueryTable#quote}
        :param allow_jagged_rows: Indicates if BigQuery should accept rows that are missing trailing optional columns. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#allow_jagged_rows GoogleBigqueryTable#allow_jagged_rows}
        :param allow_quoted_newlines: Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file. The default value is false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#allow_quoted_newlines GoogleBigqueryTable#allow_quoted_newlines}
        :param encoding: The character encoding of the data. The supported values are UTF-8 or ISO-8859-1. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#encoding GoogleBigqueryTable#encoding}
        :param field_delimiter: The separator for fields in a CSV file. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#field_delimiter GoogleBigqueryTable#field_delimiter}
        :param skip_leading_rows: The number of rows at the top of a CSV file that BigQuery will skip when reading the data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#skip_leading_rows GoogleBigqueryTable#skip_leading_rows}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12886bff655293afef73b291df9192fb56405e7c329c57e8a0de15ce78a5a687)
            check_type(argname="argument quote", value=quote, expected_type=type_hints["quote"])
            check_type(argname="argument allow_jagged_rows", value=allow_jagged_rows, expected_type=type_hints["allow_jagged_rows"])
            check_type(argname="argument allow_quoted_newlines", value=allow_quoted_newlines, expected_type=type_hints["allow_quoted_newlines"])
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
            check_type(argname="argument field_delimiter", value=field_delimiter, expected_type=type_hints["field_delimiter"])
            check_type(argname="argument skip_leading_rows", value=skip_leading_rows, expected_type=type_hints["skip_leading_rows"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "quote": quote,
        }
        if allow_jagged_rows is not None:
            self._values["allow_jagged_rows"] = allow_jagged_rows
        if allow_quoted_newlines is not None:
            self._values["allow_quoted_newlines"] = allow_quoted_newlines
        if encoding is not None:
            self._values["encoding"] = encoding
        if field_delimiter is not None:
            self._values["field_delimiter"] = field_delimiter
        if skip_leading_rows is not None:
            self._values["skip_leading_rows"] = skip_leading_rows

    @builtins.property
    def quote(self) -> builtins.str:
        '''The value that is used to quote data sections in a CSV file.

        If your data does not contain quoted sections, set the property value to an empty string. If your data contains quoted newline characters, you must also set the allow_quoted_newlines property to true. The API-side default is ", specified in Terraform escaped as ". Due to limitations with Terraform default values, this value is required to be explicitly set.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#quote GoogleBigqueryTable#quote}
        '''
        result = self._values.get("quote")
        assert result is not None, "Required property 'quote' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_jagged_rows(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates if BigQuery should accept rows that are missing trailing optional columns.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#allow_jagged_rows GoogleBigqueryTable#allow_jagged_rows}
        '''
        result = self._values.get("allow_jagged_rows")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def allow_quoted_newlines(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file.

        The default value is false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#allow_quoted_newlines GoogleBigqueryTable#allow_quoted_newlines}
        '''
        result = self._values.get("allow_quoted_newlines")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''The character encoding of the data. The supported values are UTF-8 or ISO-8859-1.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#encoding GoogleBigqueryTable#encoding}
        '''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def field_delimiter(self) -> typing.Optional[builtins.str]:
        '''The separator for fields in a CSV file.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#field_delimiter GoogleBigqueryTable#field_delimiter}
        '''
        result = self._values.get("field_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_leading_rows(self) -> typing.Optional[jsii.Number]:
        '''The number of rows at the top of a CSV file that BigQuery will skip when reading the data.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#skip_leading_rows GoogleBigqueryTable#skip_leading_rows}
        '''
        result = self._values.get("skip_leading_rows")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableExternalDataConfigurationCsvOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd07c9c96ed9b19dd5ba802a45c23f740ecb00994e422a16c0f3138eaa554a3d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowJaggedRows")
    def reset_allow_jagged_rows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowJaggedRows", []))

    @jsii.member(jsii_name="resetAllowQuotedNewlines")
    def reset_allow_quoted_newlines(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowQuotedNewlines", []))

    @jsii.member(jsii_name="resetEncoding")
    def reset_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncoding", []))

    @jsii.member(jsii_name="resetFieldDelimiter")
    def reset_field_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldDelimiter", []))

    @jsii.member(jsii_name="resetSkipLeadingRows")
    def reset_skip_leading_rows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipLeadingRows", []))

    @builtins.property
    @jsii.member(jsii_name="allowJaggedRowsInput")
    def allow_jagged_rows_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowJaggedRowsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowQuotedNewlinesInput")
    def allow_quoted_newlines_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowQuotedNewlinesInput"))

    @builtins.property
    @jsii.member(jsii_name="encodingInput")
    def encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encodingInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiterInput")
    def field_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="quoteInput")
    def quote_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "quoteInput"))

    @builtins.property
    @jsii.member(jsii_name="skipLeadingRowsInput")
    def skip_leading_rows_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "skipLeadingRowsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowJaggedRows")
    def allow_jagged_rows(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowJaggedRows"))

    @allow_jagged_rows.setter
    def allow_jagged_rows(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3794c0cb6a1584814b84ae5434a720bcae9eb2cfb647dec3e2fe56b746e2ae3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowJaggedRows", value)

    @builtins.property
    @jsii.member(jsii_name="allowQuotedNewlines")
    def allow_quoted_newlines(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowQuotedNewlines"))

    @allow_quoted_newlines.setter
    def allow_quoted_newlines(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cedafbb2f52e2caa5061dcaccd997685b4d9b2d11327013d36c840bcdf69a4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowQuotedNewlines", value)

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @encoding.setter
    def encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25462329f0702812ae812048222a7c1828f1c922da3763306e621f23e8291833)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encoding", value)

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiter")
    def field_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldDelimiter"))

    @field_delimiter.setter
    def field_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b81281ef2bbb77df0332f2b6f45606d3ce76122b2fa1c41a4ff7e02a977aa56b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="quote")
    def quote(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "quote"))

    @quote.setter
    def quote(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a88a05bf6e3a36fa26d8489b6ddaf4ab0f893cbaf94f1dcabe1e5e76136ac07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quote", value)

    @builtins.property
    @jsii.member(jsii_name="skipLeadingRows")
    def skip_leading_rows(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "skipLeadingRows"))

    @skip_leading_rows.setter
    def skip_leading_rows(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10ce05ad5bae5f5b21acb656d5e17260b399553a206fe308196c04011bab6140)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipLeadingRows", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationCsvOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationCsvOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationCsvOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99511cd60bdd6c471eb9418878c3699e447213d0702e54295f09a24c85ece31b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions",
    jsii_struct_bases=[],
    name_mapping={"range": "range", "skip_leading_rows": "skipLeadingRows"},
)
class GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions:
    def __init__(
        self,
        *,
        range: typing.Optional[builtins.str] = None,
        skip_leading_rows: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param range: Range of a sheet to query from. Only used when non-empty. At least one of range or skip_leading_rows must be set. Typical format: "sheet_name!top_left_cell_id:bottom_right_cell_id" For example: "sheet1!A1:B20" Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#range GoogleBigqueryTable#range}
        :param skip_leading_rows: The number of rows at the top of the sheet that BigQuery will skip when reading the data. At least one of range or skip_leading_rows must be set. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#skip_leading_rows GoogleBigqueryTable#skip_leading_rows}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0c5c07c152a25c24c896eba15ec4821802c924adb0a35c5578737eed3ec2699)
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
            check_type(argname="argument skip_leading_rows", value=skip_leading_rows, expected_type=type_hints["skip_leading_rows"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if range is not None:
            self._values["range"] = range
        if skip_leading_rows is not None:
            self._values["skip_leading_rows"] = skip_leading_rows

    @builtins.property
    def range(self) -> typing.Optional[builtins.str]:
        '''Range of a sheet to query from.

        Only used when non-empty. At least one of range or skip_leading_rows must be set. Typical format: "sheet_name!top_left_cell_id:bottom_right_cell_id" For example: "sheet1!A1:B20"

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#range GoogleBigqueryTable#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_leading_rows(self) -> typing.Optional[jsii.Number]:
        '''The number of rows at the top of the sheet that BigQuery will skip when reading the data.

        At least one of range or skip_leading_rows must be set.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#skip_leading_rows GoogleBigqueryTable#skip_leading_rows}
        '''
        result = self._values.get("skip_leading_rows")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__802ed1a4f414daf0b7342072c7063594445f9784fbd6117b5114e8d347b328d8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @jsii.member(jsii_name="resetSkipLeadingRows")
    def reset_skip_leading_rows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipLeadingRows", []))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="skipLeadingRowsInput")
    def skip_leading_rows_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "skipLeadingRowsInput"))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "range"))

    @range.setter
    def range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f0a8f3dabdc8cc44976d3718f4735b85c26d5da2eff68d2460f851e4e258650)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "range", value)

    @builtins.property
    @jsii.member(jsii_name="skipLeadingRows")
    def skip_leading_rows(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "skipLeadingRows"))

    @skip_leading_rows.setter
    def skip_leading_rows(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84e6b9419149cfdd5b5c57c1983e78b0c22575ed10ed62a2ef75c9e03ec2e9b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipLeadingRows", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__543fb036cb1d4ae8a5cb906d78d84f1fbec5c451721196f5afb5163f5904720e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions",
    jsii_struct_bases=[],
    name_mapping={
        "mode": "mode",
        "require_partition_filter": "requirePartitionFilter",
        "source_uri_prefix": "sourceUriPrefix",
    },
)
class GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions:
    def __init__(
        self,
        *,
        mode: typing.Optional[builtins.str] = None,
        require_partition_filter: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source_uri_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mode: When set, what mode of hive partitioning to use when reading data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#mode GoogleBigqueryTable#mode}
        :param require_partition_filter: If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        :param source_uri_prefix: When hive partition detection is requested, a common for all source uris must be required. The prefix must end immediately before the partition key encoding begins. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_uri_prefix GoogleBigqueryTable#source_uri_prefix}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7ad8f75d82703f801eb14e586fe0669594ed903d631d67a19cbfef1ba2ef922)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument require_partition_filter", value=require_partition_filter, expected_type=type_hints["require_partition_filter"])
            check_type(argname="argument source_uri_prefix", value=source_uri_prefix, expected_type=type_hints["source_uri_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode
        if require_partition_filter is not None:
            self._values["require_partition_filter"] = require_partition_filter
        if source_uri_prefix is not None:
            self._values["source_uri_prefix"] = source_uri_prefix

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''When set, what mode of hive partitioning to use when reading data.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#mode GoogleBigqueryTable#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_partition_filter(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        '''
        result = self._values.get("require_partition_filter")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def source_uri_prefix(self) -> typing.Optional[builtins.str]:
        '''When hive partition detection is requested, a common for all source uris must be required.

        The prefix must end immediately before the partition key encoding begins.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_uri_prefix GoogleBigqueryTable#source_uri_prefix}
        '''
        result = self._values.get("source_uri_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6493145b3124699867b574fb56803b73d3db19fdf2381934c9d969b502a3b9f7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetRequirePartitionFilter")
    def reset_require_partition_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequirePartitionFilter", []))

    @jsii.member(jsii_name="resetSourceUriPrefix")
    def reset_source_uri_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceUriPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="requirePartitionFilterInput")
    def require_partition_filter_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requirePartitionFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceUriPrefixInput")
    def source_uri_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceUriPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27e7d819fc1fdac87c67e7a2695fb8e5a54b9eba8e9ece0c544d686074fe166c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="requirePartitionFilter")
    def require_partition_filter(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requirePartitionFilter"))

    @require_partition_filter.setter
    def require_partition_filter(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a5749971cb8004a36db956ffa9d734ac17003403dfb128157b8298754a1db02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirePartitionFilter", value)

    @builtins.property
    @jsii.member(jsii_name="sourceUriPrefix")
    def source_uri_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceUriPrefix"))

    @source_uri_prefix.setter
    def source_uri_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5ed152323e0e80c83bbc7c6133044d3251baa8b8250cce5b98d27b10e1abb37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceUriPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3be43eb2768828a2618edc1bd2340d9d54617c94a1a08224a5edf9007073face)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationJsonOptions",
    jsii_struct_bases=[],
    name_mapping={"encoding": "encoding"},
)
class GoogleBigqueryTableExternalDataConfigurationJsonOptions:
    def __init__(self, *, encoding: typing.Optional[builtins.str] = None) -> None:
        '''
        :param encoding: The character encoding of the data. The supported values are UTF-8, UTF-16BE, UTF-16LE, UTF-32BE, and UTF-32LE. The default value is UTF-8. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#encoding GoogleBigqueryTable#encoding}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4107b273f8e893e0eacacf07eb6c23c076cca6c323ab5e6fe3e564e281e5835f)
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if encoding is not None:
            self._values["encoding"] = encoding

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''The character encoding of the data.

        The supported values are UTF-8, UTF-16BE, UTF-16LE, UTF-32BE, and UTF-32LE. The default value is UTF-8.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#encoding GoogleBigqueryTable#encoding}
        '''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableExternalDataConfigurationJsonOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableExternalDataConfigurationJsonOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationJsonOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0956af7c573daa31d7303e6eb30233d8c0289fbd4747b2c93a91ede7e7166bcf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEncoding")
    def reset_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncoding", []))

    @builtins.property
    @jsii.member(jsii_name="encodingInput")
    def encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encodingInput"))

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @encoding.setter
    def encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73f69eded064ae86a2ab7bc18fed75e5cfe18d536b073008fc7456427147329a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encoding", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationJsonOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationJsonOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationJsonOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca6f44b8a8c90f68f65e1673c8d71080f5713414defb9e5505ae5738d6e159bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryTableExternalDataConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d5f4874ee8829862ba38fc77ca71ca6e97e3ce71b54a8461418565931e66d5c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAvroOptions")
    def put_avro_options(
        self,
        *,
        use_avro_logical_types: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param use_avro_logical_types: If sourceFormat is set to "AVRO", indicates whether to interpret logical types as the corresponding BigQuery data type (for example, TIMESTAMP), instead of using the raw type (for example, INTEGER). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#use_avro_logical_types GoogleBigqueryTable#use_avro_logical_types}
        '''
        value = GoogleBigqueryTableExternalDataConfigurationAvroOptions(
            use_avro_logical_types=use_avro_logical_types
        )

        return typing.cast(None, jsii.invoke(self, "putAvroOptions", [value]))

    @jsii.member(jsii_name="putCsvOptions")
    def put_csv_options(
        self,
        *,
        quote: builtins.str,
        allow_jagged_rows: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_quoted_newlines: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encoding: typing.Optional[builtins.str] = None,
        field_delimiter: typing.Optional[builtins.str] = None,
        skip_leading_rows: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param quote: The value that is used to quote data sections in a CSV file. If your data does not contain quoted sections, set the property value to an empty string. If your data contains quoted newline characters, you must also set the allow_quoted_newlines property to true. The API-side default is ", specified in Terraform escaped as ". Due to limitations with Terraform default values, this value is required to be explicitly set. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#quote GoogleBigqueryTable#quote}
        :param allow_jagged_rows: Indicates if BigQuery should accept rows that are missing trailing optional columns. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#allow_jagged_rows GoogleBigqueryTable#allow_jagged_rows}
        :param allow_quoted_newlines: Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file. The default value is false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#allow_quoted_newlines GoogleBigqueryTable#allow_quoted_newlines}
        :param encoding: The character encoding of the data. The supported values are UTF-8 or ISO-8859-1. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#encoding GoogleBigqueryTable#encoding}
        :param field_delimiter: The separator for fields in a CSV file. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#field_delimiter GoogleBigqueryTable#field_delimiter}
        :param skip_leading_rows: The number of rows at the top of a CSV file that BigQuery will skip when reading the data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#skip_leading_rows GoogleBigqueryTable#skip_leading_rows}
        '''
        value = GoogleBigqueryTableExternalDataConfigurationCsvOptions(
            quote=quote,
            allow_jagged_rows=allow_jagged_rows,
            allow_quoted_newlines=allow_quoted_newlines,
            encoding=encoding,
            field_delimiter=field_delimiter,
            skip_leading_rows=skip_leading_rows,
        )

        return typing.cast(None, jsii.invoke(self, "putCsvOptions", [value]))

    @jsii.member(jsii_name="putGoogleSheetsOptions")
    def put_google_sheets_options(
        self,
        *,
        range: typing.Optional[builtins.str] = None,
        skip_leading_rows: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param range: Range of a sheet to query from. Only used when non-empty. At least one of range or skip_leading_rows must be set. Typical format: "sheet_name!top_left_cell_id:bottom_right_cell_id" For example: "sheet1!A1:B20" Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#range GoogleBigqueryTable#range}
        :param skip_leading_rows: The number of rows at the top of the sheet that BigQuery will skip when reading the data. At least one of range or skip_leading_rows must be set. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#skip_leading_rows GoogleBigqueryTable#skip_leading_rows}
        '''
        value = GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions(
            range=range, skip_leading_rows=skip_leading_rows
        )

        return typing.cast(None, jsii.invoke(self, "putGoogleSheetsOptions", [value]))

    @jsii.member(jsii_name="putHivePartitioningOptions")
    def put_hive_partitioning_options(
        self,
        *,
        mode: typing.Optional[builtins.str] = None,
        require_partition_filter: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source_uri_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mode: When set, what mode of hive partitioning to use when reading data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#mode GoogleBigqueryTable#mode}
        :param require_partition_filter: If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        :param source_uri_prefix: When hive partition detection is requested, a common for all source uris must be required. The prefix must end immediately before the partition key encoding begins. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_uri_prefix GoogleBigqueryTable#source_uri_prefix}
        '''
        value = GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions(
            mode=mode,
            require_partition_filter=require_partition_filter,
            source_uri_prefix=source_uri_prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putHivePartitioningOptions", [value]))

    @jsii.member(jsii_name="putJsonOptions")
    def put_json_options(
        self,
        *,
        encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param encoding: The character encoding of the data. The supported values are UTF-8, UTF-16BE, UTF-16LE, UTF-32BE, and UTF-32LE. The default value is UTF-8. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#encoding GoogleBigqueryTable#encoding}
        '''
        value = GoogleBigqueryTableExternalDataConfigurationJsonOptions(
            encoding=encoding
        )

        return typing.cast(None, jsii.invoke(self, "putJsonOptions", [value]))

    @jsii.member(jsii_name="putParquetOptions")
    def put_parquet_options(
        self,
        *,
        enable_list_inference: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enum_as_string: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_list_inference: Indicates whether to use schema inference specifically for Parquet LIST logical type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#enable_list_inference GoogleBigqueryTable#enable_list_inference}
        :param enum_as_string: Indicates whether to infer Parquet ENUM logical type as STRING instead of BYTES by default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#enum_as_string GoogleBigqueryTable#enum_as_string}
        '''
        value = GoogleBigqueryTableExternalDataConfigurationParquetOptions(
            enable_list_inference=enable_list_inference, enum_as_string=enum_as_string
        )

        return typing.cast(None, jsii.invoke(self, "putParquetOptions", [value]))

    @jsii.member(jsii_name="resetAvroOptions")
    def reset_avro_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvroOptions", []))

    @jsii.member(jsii_name="resetCompression")
    def reset_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompression", []))

    @jsii.member(jsii_name="resetConnectionId")
    def reset_connection_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionId", []))

    @jsii.member(jsii_name="resetCsvOptions")
    def reset_csv_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvOptions", []))

    @jsii.member(jsii_name="resetFileSetSpecType")
    def reset_file_set_spec_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileSetSpecType", []))

    @jsii.member(jsii_name="resetGoogleSheetsOptions")
    def reset_google_sheets_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleSheetsOptions", []))

    @jsii.member(jsii_name="resetHivePartitioningOptions")
    def reset_hive_partitioning_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHivePartitioningOptions", []))

    @jsii.member(jsii_name="resetIgnoreUnknownValues")
    def reset_ignore_unknown_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreUnknownValues", []))

    @jsii.member(jsii_name="resetJsonOptions")
    def reset_json_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonOptions", []))

    @jsii.member(jsii_name="resetMaxBadRecords")
    def reset_max_bad_records(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBadRecords", []))

    @jsii.member(jsii_name="resetMetadataCacheMode")
    def reset_metadata_cache_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadataCacheMode", []))

    @jsii.member(jsii_name="resetObjectMetadata")
    def reset_object_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectMetadata", []))

    @jsii.member(jsii_name="resetParquetOptions")
    def reset_parquet_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParquetOptions", []))

    @jsii.member(jsii_name="resetReferenceFileSchemaUri")
    def reset_reference_file_schema_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReferenceFileSchemaUri", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @jsii.member(jsii_name="resetSourceFormat")
    def reset_source_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFormat", []))

    @builtins.property
    @jsii.member(jsii_name="avroOptions")
    def avro_options(
        self,
    ) -> GoogleBigqueryTableExternalDataConfigurationAvroOptionsOutputReference:
        return typing.cast(GoogleBigqueryTableExternalDataConfigurationAvroOptionsOutputReference, jsii.get(self, "avroOptions"))

    @builtins.property
    @jsii.member(jsii_name="csvOptions")
    def csv_options(
        self,
    ) -> GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference:
        return typing.cast(GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference, jsii.get(self, "csvOptions"))

    @builtins.property
    @jsii.member(jsii_name="googleSheetsOptions")
    def google_sheets_options(
        self,
    ) -> GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference:
        return typing.cast(GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference, jsii.get(self, "googleSheetsOptions"))

    @builtins.property
    @jsii.member(jsii_name="hivePartitioningOptions")
    def hive_partitioning_options(
        self,
    ) -> GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference:
        return typing.cast(GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference, jsii.get(self, "hivePartitioningOptions"))

    @builtins.property
    @jsii.member(jsii_name="jsonOptions")
    def json_options(
        self,
    ) -> GoogleBigqueryTableExternalDataConfigurationJsonOptionsOutputReference:
        return typing.cast(GoogleBigqueryTableExternalDataConfigurationJsonOptionsOutputReference, jsii.get(self, "jsonOptions"))

    @builtins.property
    @jsii.member(jsii_name="parquetOptions")
    def parquet_options(
        self,
    ) -> "GoogleBigqueryTableExternalDataConfigurationParquetOptionsOutputReference":
        return typing.cast("GoogleBigqueryTableExternalDataConfigurationParquetOptionsOutputReference", jsii.get(self, "parquetOptions"))

    @builtins.property
    @jsii.member(jsii_name="autodetectInput")
    def autodetect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autodetectInput"))

    @builtins.property
    @jsii.member(jsii_name="avroOptionsInput")
    def avro_options_input(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationAvroOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationAvroOptions], jsii.get(self, "avroOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionInput")
    def compression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionIdInput")
    def connection_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="csvOptionsInput")
    def csv_options_input(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationCsvOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationCsvOptions], jsii.get(self, "csvOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSetSpecTypeInput")
    def file_set_spec_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSetSpecTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="googleSheetsOptionsInput")
    def google_sheets_options_input(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions], jsii.get(self, "googleSheetsOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="hivePartitioningOptionsInput")
    def hive_partitioning_options_input(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions], jsii.get(self, "hivePartitioningOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreUnknownValuesInput")
    def ignore_unknown_values_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ignoreUnknownValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonOptionsInput")
    def json_options_input(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationJsonOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationJsonOptions], jsii.get(self, "jsonOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxBadRecordsInput")
    def max_bad_records_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBadRecordsInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataCacheModeInput")
    def metadata_cache_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataCacheModeInput"))

    @builtins.property
    @jsii.member(jsii_name="objectMetadataInput")
    def object_metadata_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectMetadataInput"))

    @builtins.property
    @jsii.member(jsii_name="parquetOptionsInput")
    def parquet_options_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfigurationParquetOptions"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfigurationParquetOptions"], jsii.get(self, "parquetOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="referenceFileSchemaUriInput")
    def reference_file_schema_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "referenceFileSchemaUriInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFormatInput")
    def source_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceUrisInput")
    def source_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="autodetect")
    def autodetect(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autodetect"))

    @autodetect.setter
    def autodetect(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d50459652227b9ff45eb1306bdfc41d945b0c6d6d574624e27d1f3684515f1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autodetect", value)

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__093a2d981c69283998e5f97acd4c0e649b8c697eb3e87dec4111ed2ee33712df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="connectionId")
    def connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionId"))

    @connection_id.setter
    def connection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35b47a224774a6a12439bb1bf2ed94bf03bc3ca43e76dd9bdf62c00458b7f287)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionId", value)

    @builtins.property
    @jsii.member(jsii_name="fileSetSpecType")
    def file_set_spec_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSetSpecType"))

    @file_set_spec_type.setter
    def file_set_spec_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1956f05128314b1de32ed2fbe90e54a096b2629ffbf0a7001028c2c6124aede9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSetSpecType", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreUnknownValues")
    def ignore_unknown_values(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ignoreUnknownValues"))

    @ignore_unknown_values.setter
    def ignore_unknown_values(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09a19404a32b0087f8a9b762fafdc3e3639cf1b3bba5abee4a9955ef9f74f6e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreUnknownValues", value)

    @builtins.property
    @jsii.member(jsii_name="maxBadRecords")
    def max_bad_records(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxBadRecords"))

    @max_bad_records.setter
    def max_bad_records(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cce2e1884e8724c36e010e250e64db6320f24055534a528e53b09e1ae86f793e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBadRecords", value)

    @builtins.property
    @jsii.member(jsii_name="metadataCacheMode")
    def metadata_cache_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadataCacheMode"))

    @metadata_cache_mode.setter
    def metadata_cache_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5efafd923c05641244575bc3ff0c2918f9242d754f72050394e34cc85655edc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadataCacheMode", value)

    @builtins.property
    @jsii.member(jsii_name="objectMetadata")
    def object_metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectMetadata"))

    @object_metadata.setter
    def object_metadata(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ab81df88a4136eea0e777f0daad1716940d8a909199bfa2adb926f044ea6b9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectMetadata", value)

    @builtins.property
    @jsii.member(jsii_name="referenceFileSchemaUri")
    def reference_file_schema_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "referenceFileSchemaUri"))

    @reference_file_schema_uri.setter
    def reference_file_schema_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3cdec1e56d8db55bbe10f42f4f9592af981ad3062a8da7e3890f9eb124a766f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "referenceFileSchemaUri", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deab5426036d789b5d7c69bab30d83e50ae27623a20b0a8e1c652d6adcf605cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFormat")
    def source_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFormat"))

    @source_format.setter
    def source_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a27a87ef92af9ef06814d5c99204b644bce025a6e8eeb46ef0ee50e4df9eb627)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFormat", value)

    @builtins.property
    @jsii.member(jsii_name="sourceUris")
    def source_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceUris"))

    @source_uris.setter
    def source_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfbe1f7ce93a0ea610a7fcbae3691977d5e14c4a2b067c0c886577b890568bf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceUris", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfiguration]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableExternalDataConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b71b35a269d54765944fa7cb6dd7e00af7c09fce2233c1cf8b806e85e1308169)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationParquetOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enable_list_inference": "enableListInference",
        "enum_as_string": "enumAsString",
    },
)
class GoogleBigqueryTableExternalDataConfigurationParquetOptions:
    def __init__(
        self,
        *,
        enable_list_inference: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enum_as_string: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_list_inference: Indicates whether to use schema inference specifically for Parquet LIST logical type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#enable_list_inference GoogleBigqueryTable#enable_list_inference}
        :param enum_as_string: Indicates whether to infer Parquet ENUM logical type as STRING instead of BYTES by default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#enum_as_string GoogleBigqueryTable#enum_as_string}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a80e45df433f5a95b4103694f0064452da3152f728ba9b6eab20e711eb31afc5)
            check_type(argname="argument enable_list_inference", value=enable_list_inference, expected_type=type_hints["enable_list_inference"])
            check_type(argname="argument enum_as_string", value=enum_as_string, expected_type=type_hints["enum_as_string"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enable_list_inference is not None:
            self._values["enable_list_inference"] = enable_list_inference
        if enum_as_string is not None:
            self._values["enum_as_string"] = enum_as_string

    @builtins.property
    def enable_list_inference(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether to use schema inference specifically for Parquet LIST logical type.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#enable_list_inference GoogleBigqueryTable#enable_list_inference}
        '''
        result = self._values.get("enable_list_inference")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enum_as_string(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether to infer Parquet ENUM logical type as STRING instead of BYTES by default.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#enum_as_string GoogleBigqueryTable#enum_as_string}
        '''
        result = self._values.get("enum_as_string")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableExternalDataConfigurationParquetOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableExternalDataConfigurationParquetOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationParquetOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3b5934508f0214af865c4a131fdf94293b155ffc226e110610eef6c6e78275f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableListInference")
    def reset_enable_list_inference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableListInference", []))

    @jsii.member(jsii_name="resetEnumAsString")
    def reset_enum_as_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnumAsString", []))

    @builtins.property
    @jsii.member(jsii_name="enableListInferenceInput")
    def enable_list_inference_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableListInferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="enumAsStringInput")
    def enum_as_string_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enumAsStringInput"))

    @builtins.property
    @jsii.member(jsii_name="enableListInference")
    def enable_list_inference(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableListInference"))

    @enable_list_inference.setter
    def enable_list_inference(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a63982f55e5282b7ceaa52d65cd0ce044cd22d28474bf679cd66fb14fb8caf0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableListInference", value)

    @builtins.property
    @jsii.member(jsii_name="enumAsString")
    def enum_as_string(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enumAsString"))

    @enum_as_string.setter
    def enum_as_string(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0e4301f6bc15a2078e09cbec2af4a4f020bb2c6a7aad4ff01d8c496e95e7356)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enumAsString", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationParquetOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationParquetOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationParquetOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca7d3f7bda0456b85782cc56d44aaa7c369ef45b186d7843ea93c09455352de4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableMaterializedView",
    jsii_struct_bases=[],
    name_mapping={
        "query": "query",
        "allow_non_incremental_definition": "allowNonIncrementalDefinition",
        "enable_refresh": "enableRefresh",
        "refresh_interval_ms": "refreshIntervalMs",
    },
)
class GoogleBigqueryTableMaterializedView:
    def __init__(
        self,
        *,
        query: builtins.str,
        allow_non_incremental_definition: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_refresh: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        refresh_interval_ms: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: A query whose result is persisted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#query GoogleBigqueryTable#query}
        :param allow_non_incremental_definition: Allow non incremental materialized view definition. The default value is false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#allow_non_incremental_definition GoogleBigqueryTable#allow_non_incremental_definition}
        :param enable_refresh: Specifies if BigQuery should automatically refresh materialized view when the base table is updated. The default is true. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#enable_refresh GoogleBigqueryTable#enable_refresh}
        :param refresh_interval_ms: Specifies maximum frequency at which this materialized view will be refreshed. The default is 1800000. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#refresh_interval_ms GoogleBigqueryTable#refresh_interval_ms}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67c9007c097b1868a28cde3dcb6414c32a0dd5bde75bd8cb579b6f16f6952558)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument allow_non_incremental_definition", value=allow_non_incremental_definition, expected_type=type_hints["allow_non_incremental_definition"])
            check_type(argname="argument enable_refresh", value=enable_refresh, expected_type=type_hints["enable_refresh"])
            check_type(argname="argument refresh_interval_ms", value=refresh_interval_ms, expected_type=type_hints["refresh_interval_ms"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query": query,
        }
        if allow_non_incremental_definition is not None:
            self._values["allow_non_incremental_definition"] = allow_non_incremental_definition
        if enable_refresh is not None:
            self._values["enable_refresh"] = enable_refresh
        if refresh_interval_ms is not None:
            self._values["refresh_interval_ms"] = refresh_interval_ms

    @builtins.property
    def query(self) -> builtins.str:
        '''A query whose result is persisted.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#query GoogleBigqueryTable#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_non_incremental_definition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Allow non incremental materialized view definition. The default value is false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#allow_non_incremental_definition GoogleBigqueryTable#allow_non_incremental_definition}
        '''
        result = self._values.get("allow_non_incremental_definition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_refresh(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies if BigQuery should automatically refresh materialized view when the base table is updated. The default is true.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#enable_refresh GoogleBigqueryTable#enable_refresh}
        '''
        result = self._values.get("enable_refresh")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def refresh_interval_ms(self) -> typing.Optional[jsii.Number]:
        '''Specifies maximum frequency at which this materialized view will be refreshed. The default is 1800000.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#refresh_interval_ms GoogleBigqueryTable#refresh_interval_ms}
        '''
        result = self._values.get("refresh_interval_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableMaterializedView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableMaterializedViewOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableMaterializedViewOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__76d4310ce3220e4311399768d0d65dfe628ebe569c9c1d1aae69b73490bc6eb7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowNonIncrementalDefinition")
    def reset_allow_non_incremental_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowNonIncrementalDefinition", []))

    @jsii.member(jsii_name="resetEnableRefresh")
    def reset_enable_refresh(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableRefresh", []))

    @jsii.member(jsii_name="resetRefreshIntervalMs")
    def reset_refresh_interval_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshIntervalMs", []))

    @builtins.property
    @jsii.member(jsii_name="allowNonIncrementalDefinitionInput")
    def allow_non_incremental_definition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowNonIncrementalDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="enableRefreshInput")
    def enable_refresh_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableRefreshInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshIntervalMsInput")
    def refresh_interval_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "refreshIntervalMsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowNonIncrementalDefinition")
    def allow_non_incremental_definition(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowNonIncrementalDefinition"))

    @allow_non_incremental_definition.setter
    def allow_non_incremental_definition(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26e558f13e4dc47793f44ca98c13e0b86b9cb6e40643455be7dc716344763f82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowNonIncrementalDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="enableRefresh")
    def enable_refresh(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableRefresh"))

    @enable_refresh.setter
    def enable_refresh(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d7fd6a8ab03bf2cdc7505d1986ba182dcaedc329db48b8894cf7c58fd3ced8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableRefresh", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2498add99e863c54284fd157d68632ffbbd5b2a15b18df5e976b642b6469150d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="refreshIntervalMs")
    def refresh_interval_ms(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "refreshIntervalMs"))

    @refresh_interval_ms.setter
    def refresh_interval_ms(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a72eae716dc687a0de9c73e693e07d89bf9cb88054056ea18cf57a0d11b1808f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshIntervalMs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryTableMaterializedView]:
        return typing.cast(typing.Optional[GoogleBigqueryTableMaterializedView], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableMaterializedView],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__384b0ce977605dd8b4519b93855ccd336931d6e0d1bf9f020ab7032d048780f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableRangePartitioning",
    jsii_struct_bases=[],
    name_mapping={"field": "field", "range": "range"},
)
class GoogleBigqueryTableRangePartitioning:
    def __init__(
        self,
        *,
        field: builtins.str,
        range: typing.Union["GoogleBigqueryTableRangePartitioningRange", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param field: The field used to determine how to create a range-based partition. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#field GoogleBigqueryTable#field}
        :param range: range block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#range GoogleBigqueryTable#range}
        '''
        if isinstance(range, dict):
            range = GoogleBigqueryTableRangePartitioningRange(**range)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35fdc34928dd2c4fb6fde71af4628fc3301a2e4c3186594446175cf54b68e24c)
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field": field,
            "range": range,
        }

    @builtins.property
    def field(self) -> builtins.str:
        '''The field used to determine how to create a range-based partition.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#field GoogleBigqueryTable#field}
        '''
        result = self._values.get("field")
        assert result is not None, "Required property 'field' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(self) -> "GoogleBigqueryTableRangePartitioningRange":
        '''range block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#range GoogleBigqueryTable#range}
        '''
        result = self._values.get("range")
        assert result is not None, "Required property 'range' is missing"
        return typing.cast("GoogleBigqueryTableRangePartitioningRange", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableRangePartitioning(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableRangePartitioningOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableRangePartitioningOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a635990a30f5b0f38742af12a74e7e64dee33fe080cfb39c8bc609e972f166e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        *,
        end: jsii.Number,
        interval: jsii.Number,
        start: jsii.Number,
    ) -> None:
        '''
        :param end: End of the range partitioning, exclusive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#end GoogleBigqueryTable#end}
        :param interval: The width of each range within the partition. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#interval GoogleBigqueryTable#interval}
        :param start: Start of the range partitioning, inclusive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#start GoogleBigqueryTable#start}
        '''
        value = GoogleBigqueryTableRangePartitioningRange(
            end=end, interval=interval, start=start
        )

        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "GoogleBigqueryTableRangePartitioningRangeOutputReference":
        return typing.cast("GoogleBigqueryTableRangePartitioningRangeOutputReference", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableRangePartitioningRange"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableRangePartitioningRange"], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87d25dc939d584638dedb87b1f5763b0b81d7843c92eb97ee91bace3924c69e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryTableRangePartitioning]:
        return typing.cast(typing.Optional[GoogleBigqueryTableRangePartitioning], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableRangePartitioning],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3391981cb2b5b4c6cbdc2027d2dc19e8f91b47809c56cabde852193877c715c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableRangePartitioningRange",
    jsii_struct_bases=[],
    name_mapping={"end": "end", "interval": "interval", "start": "start"},
)
class GoogleBigqueryTableRangePartitioningRange:
    def __init__(
        self,
        *,
        end: jsii.Number,
        interval: jsii.Number,
        start: jsii.Number,
    ) -> None:
        '''
        :param end: End of the range partitioning, exclusive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#end GoogleBigqueryTable#end}
        :param interval: The width of each range within the partition. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#interval GoogleBigqueryTable#interval}
        :param start: Start of the range partitioning, inclusive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#start GoogleBigqueryTable#start}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d750860c0abe8bd5c3c946f56ada1355e0e94088874e25c9b1c55ffcabf7f295)
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "end": end,
            "interval": interval,
            "start": start,
        }

    @builtins.property
    def end(self) -> jsii.Number:
        '''End of the range partitioning, exclusive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#end GoogleBigqueryTable#end}
        '''
        result = self._values.get("end")
        assert result is not None, "Required property 'end' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> jsii.Number:
        '''The width of each range within the partition.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#interval GoogleBigqueryTable#interval}
        '''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def start(self) -> jsii.Number:
        '''Start of the range partitioning, inclusive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#start GoogleBigqueryTable#start}
        '''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableRangePartitioningRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableRangePartitioningRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableRangePartitioningRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c419c0328857a9a010254db2c200d098159c1cdf40b5c5f19cb37cad4dcf584)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "end"))

    @end.setter
    def end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcd21d99a42cf977585d7a9b9497e2d29e2bc2b20b227b63fff8b04d2af98388)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5017979f3ec443c0a4a68da0880bb782c785060c75b5adf4968b7ccc1f67110)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "start"))

    @start.setter
    def start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a204c84f1c4fbebf944db13b86709bc6e816b2b1369184742e6ba62eaf29d34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableRangePartitioningRange]:
        return typing.cast(typing.Optional[GoogleBigqueryTableRangePartitioningRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableRangePartitioningRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0413bb15900a5a0292e1393186cd6c4320145552e16f70d86a2db180ac1f1834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTableConstraints",
    jsii_struct_bases=[],
    name_mapping={"foreign_keys": "foreignKeys", "primary_key": "primaryKey"},
)
class GoogleBigqueryTableTableConstraints:
    def __init__(
        self,
        *,
        foreign_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleBigqueryTableTableConstraintsForeignKeys", typing.Dict[builtins.str, typing.Any]]]]] = None,
        primary_key: typing.Optional[typing.Union["GoogleBigqueryTableTableConstraintsPrimaryKey", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param foreign_keys: foreign_keys block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#foreign_keys GoogleBigqueryTable#foreign_keys}
        :param primary_key: primary_key block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#primary_key GoogleBigqueryTable#primary_key}
        '''
        if isinstance(primary_key, dict):
            primary_key = GoogleBigqueryTableTableConstraintsPrimaryKey(**primary_key)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3089b462815c89868a1c275d77454881d0914012504c685849e4b7eaf2274249)
            check_type(argname="argument foreign_keys", value=foreign_keys, expected_type=type_hints["foreign_keys"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if foreign_keys is not None:
            self._values["foreign_keys"] = foreign_keys
        if primary_key is not None:
            self._values["primary_key"] = primary_key

    @builtins.property
    def foreign_keys(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleBigqueryTableTableConstraintsForeignKeys"]]]:
        '''foreign_keys block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#foreign_keys GoogleBigqueryTable#foreign_keys}
        '''
        result = self._values.get("foreign_keys")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleBigqueryTableTableConstraintsForeignKeys"]]], result)

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional["GoogleBigqueryTableTableConstraintsPrimaryKey"]:
        '''primary_key block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#primary_key GoogleBigqueryTable#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional["GoogleBigqueryTableTableConstraintsPrimaryKey"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableTableConstraints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTableConstraintsForeignKeys",
    jsii_struct_bases=[],
    name_mapping={
        "column_references": "columnReferences",
        "referenced_table": "referencedTable",
        "name": "name",
    },
)
class GoogleBigqueryTableTableConstraintsForeignKeys:
    def __init__(
        self,
        *,
        column_references: typing.Union["GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences", typing.Dict[builtins.str, typing.Any]],
        referenced_table: typing.Union["GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable", typing.Dict[builtins.str, typing.Any]],
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param column_references: column_references block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#column_references GoogleBigqueryTable#column_references}
        :param referenced_table: referenced_table block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#referenced_table GoogleBigqueryTable#referenced_table}
        :param name: Set only if the foreign key constraint is named. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#name GoogleBigqueryTable#name}
        '''
        if isinstance(column_references, dict):
            column_references = GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences(**column_references)
        if isinstance(referenced_table, dict):
            referenced_table = GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable(**referenced_table)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__134a9be75b79720fc947d828706fb2c13782775aa904cc2437305871a4a1b3cd)
            check_type(argname="argument column_references", value=column_references, expected_type=type_hints["column_references"])
            check_type(argname="argument referenced_table", value=referenced_table, expected_type=type_hints["referenced_table"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "column_references": column_references,
            "referenced_table": referenced_table,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def column_references(
        self,
    ) -> "GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences":
        '''column_references block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#column_references GoogleBigqueryTable#column_references}
        '''
        result = self._values.get("column_references")
        assert result is not None, "Required property 'column_references' is missing"
        return typing.cast("GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences", result)

    @builtins.property
    def referenced_table(
        self,
    ) -> "GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable":
        '''referenced_table block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#referenced_table GoogleBigqueryTable#referenced_table}
        '''
        result = self._values.get("referenced_table")
        assert result is not None, "Required property 'referenced_table' is missing"
        return typing.cast("GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable", result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Set only if the foreign key constraint is named.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#name GoogleBigqueryTable#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableTableConstraintsForeignKeys(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences",
    jsii_struct_bases=[],
    name_mapping={
        "referenced_column": "referencedColumn",
        "referencing_column": "referencingColumn",
    },
)
class GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences:
    def __init__(
        self,
        *,
        referenced_column: builtins.str,
        referencing_column: builtins.str,
    ) -> None:
        '''
        :param referenced_column: The column in the primary key that are referenced by the referencingColumn. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#referenced_column GoogleBigqueryTable#referenced_column}
        :param referencing_column: The column that composes the foreign key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#referencing_column GoogleBigqueryTable#referencing_column}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24d1b7a0ae52e500449afb4993b7e95bf0b9f1cf57b2bfb14c1f75503293f2e0)
            check_type(argname="argument referenced_column", value=referenced_column, expected_type=type_hints["referenced_column"])
            check_type(argname="argument referencing_column", value=referencing_column, expected_type=type_hints["referencing_column"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "referenced_column": referenced_column,
            "referencing_column": referencing_column,
        }

    @builtins.property
    def referenced_column(self) -> builtins.str:
        '''The column in the primary key that are referenced by the referencingColumn.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#referenced_column GoogleBigqueryTable#referenced_column}
        '''
        result = self._values.get("referenced_column")
        assert result is not None, "Required property 'referenced_column' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def referencing_column(self) -> builtins.str:
        '''The column that composes the foreign key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#referencing_column GoogleBigqueryTable#referencing_column}
        '''
        result = self._values.get("referencing_column")
        assert result is not None, "Required property 'referencing_column' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableTableConstraintsForeignKeysColumnReferencesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTableConstraintsForeignKeysColumnReferencesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1292ccbf14a30fa8d4c9853a23dc266bf0440f7b496fa6f1aae28b319b058b45)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="referencedColumnInput")
    def referenced_column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "referencedColumnInput"))

    @builtins.property
    @jsii.member(jsii_name="referencingColumnInput")
    def referencing_column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "referencingColumnInput"))

    @builtins.property
    @jsii.member(jsii_name="referencedColumn")
    def referenced_column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "referencedColumn"))

    @referenced_column.setter
    def referenced_column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04a9a289299078f0172b2903e15af1e8ee9f0003904d7440f5273c15dd9d4bc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "referencedColumn", value)

    @builtins.property
    @jsii.member(jsii_name="referencingColumn")
    def referencing_column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "referencingColumn"))

    @referencing_column.setter
    def referencing_column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3bf3a49d1034bdecf5e94fb583f425f23be1838492f384d8f4a4ea1ac88908a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "referencingColumn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences]:
        return typing.cast(typing.Optional[GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f82e2b61eab0b1bacbaf79cbf9be3c98cf24337b0ca75b6ded7655f826860868)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryTableTableConstraintsForeignKeysList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTableConstraintsForeignKeysList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__36ae60b93b646a53152afea2a3b2f08e9f1aa12020a79399a7661c04e319c644)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleBigqueryTableTableConstraintsForeignKeysOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1492186e9542bff1b62444b6ab0da4e6d032caf872d09e8481f028364f5637dd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleBigqueryTableTableConstraintsForeignKeysOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9878e2af5e4692dc0c7cd35272139fb989050ee159287a02f65d0640d1d9b3b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__33de6d96564b512f03291e9dcaeb577dfc89de07cc262d053fd89da86f434cc9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__273162998daee6d72bdcbfa2fb8542936f2b46556f81c38d6c88b50568861b58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleBigqueryTableTableConstraintsForeignKeys]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleBigqueryTableTableConstraintsForeignKeys]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleBigqueryTableTableConstraintsForeignKeys]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c774aa04f261060eeacfa0bcd7a2dbe6fecfedfcd43d7888329b1a5787fd889)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryTableTableConstraintsForeignKeysOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTableConstraintsForeignKeysOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c96287c0a3f7d63c5305d0cb931d2e2d1df0b843e93b0096337c630b982d7f2b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putColumnReferences")
    def put_column_references(
        self,
        *,
        referenced_column: builtins.str,
        referencing_column: builtins.str,
    ) -> None:
        '''
        :param referenced_column: The column in the primary key that are referenced by the referencingColumn. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#referenced_column GoogleBigqueryTable#referenced_column}
        :param referencing_column: The column that composes the foreign key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#referencing_column GoogleBigqueryTable#referencing_column}
        '''
        value = GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences(
            referenced_column=referenced_column, referencing_column=referencing_column
        )

        return typing.cast(None, jsii.invoke(self, "putColumnReferences", [value]))

    @jsii.member(jsii_name="putReferencedTable")
    def put_referenced_table(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#dataset_id GoogleBigqueryTable#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#project_id GoogleBigqueryTable#project_id}
        :param table_id: The ID of the table. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters. Certain operations allow suffixing of the table ID with a partition decorator, such as sample_table$20190123. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#table_id GoogleBigqueryTable#table_id}
        '''
        value = GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable(
            dataset_id=dataset_id, project_id=project_id, table_id=table_id
        )

        return typing.cast(None, jsii.invoke(self, "putReferencedTable", [value]))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="columnReferences")
    def column_references(
        self,
    ) -> GoogleBigqueryTableTableConstraintsForeignKeysColumnReferencesOutputReference:
        return typing.cast(GoogleBigqueryTableTableConstraintsForeignKeysColumnReferencesOutputReference, jsii.get(self, "columnReferences"))

    @builtins.property
    @jsii.member(jsii_name="referencedTable")
    def referenced_table(
        self,
    ) -> "GoogleBigqueryTableTableConstraintsForeignKeysReferencedTableOutputReference":
        return typing.cast("GoogleBigqueryTableTableConstraintsForeignKeysReferencedTableOutputReference", jsii.get(self, "referencedTable"))

    @builtins.property
    @jsii.member(jsii_name="columnReferencesInput")
    def column_references_input(
        self,
    ) -> typing.Optional[GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences]:
        return typing.cast(typing.Optional[GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences], jsii.get(self, "columnReferencesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="referencedTableInput")
    def referenced_table_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable"], jsii.get(self, "referencedTableInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__882cdd1eed070f60b2fbcdbf8887c93fc6b9dc6277915194f3573a2afde4f932)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleBigqueryTableTableConstraintsForeignKeys]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleBigqueryTableTableConstraintsForeignKeys]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleBigqueryTableTableConstraintsForeignKeys]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d503796a604ec9d479d577c584b1389b203132de9e0efe56d4f9a22bf5b68a04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_id": "datasetId",
        "project_id": "projectId",
        "table_id": "tableId",
    },
)
class GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable:
    def __init__(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#dataset_id GoogleBigqueryTable#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#project_id GoogleBigqueryTable#project_id}
        :param table_id: The ID of the table. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters. Certain operations allow suffixing of the table ID with a partition decorator, such as sample_table$20190123. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#table_id GoogleBigqueryTable#table_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dabaa08d6b9445ed09c1fe2122a795b3df4b32db90ef82f20ba5260070a81b0b)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_id": dataset_id,
            "project_id": project_id,
            "table_id": table_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''The ID of the dataset containing this table.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#dataset_id GoogleBigqueryTable#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The ID of the project containing this table.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#project_id GoogleBigqueryTable#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_id(self) -> builtins.str:
        '''The ID of the table.

        The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters. Certain operations allow suffixing of the table ID with a partition decorator, such as sample_table$20190123.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#table_id GoogleBigqueryTable#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableTableConstraintsForeignKeysReferencedTableOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTableConstraintsForeignKeysReferencedTableOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__34ceb18c1f75fe8d989ceed920356aff85642f07bee8249b49847f3fe1ccbdf7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09101c0b500e91cd649fa3044044374a4d34b2f4b0c05b4c6dc8f93dc9caf340)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef0e3d3040cab761c5850af3efc76cb771eba90f3600b74d6d68d57ef7e5057b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9990f15255aef97330511c44f4eb6794948eadaca1467912e224e60b9cf40206)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable]:
        return typing.cast(typing.Optional[GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08decc1e28e41f4d786d698f2d1feecc213724f1b905bd726e999c44887fea5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryTableTableConstraintsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTableConstraintsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__420af46f9e50ec2e9534b17fd7458e6c3541698ea0f5248f440d5ee894878913)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putForeignKeys")
    def put_foreign_keys(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleBigqueryTableTableConstraintsForeignKeys, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8515862cd3de01201a8f41886429f90be48e3712a650d2be2c0013acbe17b0f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putForeignKeys", [value]))

    @jsii.member(jsii_name="putPrimaryKey")
    def put_primary_key(self, *, columns: typing.Sequence[builtins.str]) -> None:
        '''
        :param columns: The columns that are composed of the primary key constraint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#columns GoogleBigqueryTable#columns}
        '''
        value = GoogleBigqueryTableTableConstraintsPrimaryKey(columns=columns)

        return typing.cast(None, jsii.invoke(self, "putPrimaryKey", [value]))

    @jsii.member(jsii_name="resetForeignKeys")
    def reset_foreign_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForeignKeys", []))

    @jsii.member(jsii_name="resetPrimaryKey")
    def reset_primary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryKey", []))

    @builtins.property
    @jsii.member(jsii_name="foreignKeys")
    def foreign_keys(self) -> GoogleBigqueryTableTableConstraintsForeignKeysList:
        return typing.cast(GoogleBigqueryTableTableConstraintsForeignKeysList, jsii.get(self, "foreignKeys"))

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(
        self,
    ) -> "GoogleBigqueryTableTableConstraintsPrimaryKeyOutputReference":
        return typing.cast("GoogleBigqueryTableTableConstraintsPrimaryKeyOutputReference", jsii.get(self, "primaryKey"))

    @builtins.property
    @jsii.member(jsii_name="foreignKeysInput")
    def foreign_keys_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleBigqueryTableTableConstraintsForeignKeys]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleBigqueryTableTableConstraintsForeignKeys]]], jsii.get(self, "foreignKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableTableConstraintsPrimaryKey"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableTableConstraintsPrimaryKey"], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryTableTableConstraints]:
        return typing.cast(typing.Optional[GoogleBigqueryTableTableConstraints], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableTableConstraints],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d26ca8a30ed10893fa202a98f5f6955fa3e1547e1182d66cda0c907e18b0767)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTableConstraintsPrimaryKey",
    jsii_struct_bases=[],
    name_mapping={"columns": "columns"},
)
class GoogleBigqueryTableTableConstraintsPrimaryKey:
    def __init__(self, *, columns: typing.Sequence[builtins.str]) -> None:
        '''
        :param columns: The columns that are composed of the primary key constraint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#columns GoogleBigqueryTable#columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9b8a7927e0f726a7e13ed2d5ea330114e2b8f308e2ccbda7565681b99dbf0df)
            check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "columns": columns,
        }

    @builtins.property
    def columns(self) -> typing.List[builtins.str]:
        '''The columns that are composed of the primary key constraint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#columns GoogleBigqueryTable#columns}
        '''
        result = self._values.get("columns")
        assert result is not None, "Required property 'columns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableTableConstraintsPrimaryKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableTableConstraintsPrimaryKeyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTableConstraintsPrimaryKeyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__13bec339a4b73128a45147a819606a85699dab069f3d93a3dc0d3aeb666bc1ff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="columnsInput")
    def columns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "columnsInput"))

    @builtins.property
    @jsii.member(jsii_name="columns")
    def columns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "columns"))

    @columns.setter
    def columns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4ae6218f68d4f2b60eadc5e307488d73cddac580b8487c21e553b38aa0fcfba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableTableConstraintsPrimaryKey]:
        return typing.cast(typing.Optional[GoogleBigqueryTableTableConstraintsPrimaryKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableTableConstraintsPrimaryKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39792b8e805f59e99c37b6120ede7d5c3f66321c29d04ab10451120a77cb02f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTableReplicationInfo",
    jsii_struct_bases=[],
    name_mapping={
        "source_dataset_id": "sourceDatasetId",
        "source_project_id": "sourceProjectId",
        "source_table_id": "sourceTableId",
        "replication_interval_ms": "replicationIntervalMs",
    },
)
class GoogleBigqueryTableTableReplicationInfo:
    def __init__(
        self,
        *,
        source_dataset_id: builtins.str,
        source_project_id: builtins.str,
        source_table_id: builtins.str,
        replication_interval_ms: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param source_dataset_id: The ID of the source dataset. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_dataset_id GoogleBigqueryTable#source_dataset_id}
        :param source_project_id: The ID of the source project. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_project_id GoogleBigqueryTable#source_project_id}
        :param source_table_id: The ID of the source materialized view. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_table_id GoogleBigqueryTable#source_table_id}
        :param replication_interval_ms: The interval at which the source materialized view is polled for updates. The default is 300000. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#replication_interval_ms GoogleBigqueryTable#replication_interval_ms}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84bd36017a02b353fb1b062d8d8470796dbae88096175f677b97b6cfc54e9498)
            check_type(argname="argument source_dataset_id", value=source_dataset_id, expected_type=type_hints["source_dataset_id"])
            check_type(argname="argument source_project_id", value=source_project_id, expected_type=type_hints["source_project_id"])
            check_type(argname="argument source_table_id", value=source_table_id, expected_type=type_hints["source_table_id"])
            check_type(argname="argument replication_interval_ms", value=replication_interval_ms, expected_type=type_hints["replication_interval_ms"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_dataset_id": source_dataset_id,
            "source_project_id": source_project_id,
            "source_table_id": source_table_id,
        }
        if replication_interval_ms is not None:
            self._values["replication_interval_ms"] = replication_interval_ms

    @builtins.property
    def source_dataset_id(self) -> builtins.str:
        '''The ID of the source dataset.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_dataset_id GoogleBigqueryTable#source_dataset_id}
        '''
        result = self._values.get("source_dataset_id")
        assert result is not None, "Required property 'source_dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_project_id(self) -> builtins.str:
        '''The ID of the source project.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_project_id GoogleBigqueryTable#source_project_id}
        '''
        result = self._values.get("source_project_id")
        assert result is not None, "Required property 'source_project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_table_id(self) -> builtins.str:
        '''The ID of the source materialized view.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#source_table_id GoogleBigqueryTable#source_table_id}
        '''
        result = self._values.get("source_table_id")
        assert result is not None, "Required property 'source_table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replication_interval_ms(self) -> typing.Optional[jsii.Number]:
        '''The interval at which the source materialized view is polled for updates. The default is 300000.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#replication_interval_ms GoogleBigqueryTable#replication_interval_ms}
        '''
        result = self._values.get("replication_interval_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableTableReplicationInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableTableReplicationInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTableReplicationInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3924682e9298366c0a4fbfc0bd3bf00182813035b2965f2aeeec12813fca982b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReplicationIntervalMs")
    def reset_replication_interval_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicationIntervalMs", []))

    @builtins.property
    @jsii.member(jsii_name="replicationIntervalMsInput")
    def replication_interval_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicationIntervalMsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDatasetIdInput")
    def source_dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDatasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceProjectIdInput")
    def source_project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceProjectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTableIdInput")
    def source_table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceTableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationIntervalMs")
    def replication_interval_ms(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "replicationIntervalMs"))

    @replication_interval_ms.setter
    def replication_interval_ms(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f075ce5ae4733f419da7ec6c14acf1fc2fadd0df99ced48b486c3649d29af5de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationIntervalMs", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDatasetId")
    def source_dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDatasetId"))

    @source_dataset_id.setter
    def source_dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e289440179ee88b8ca0367c7f548231e40968876ae7b313442d46a8984372387)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDatasetId", value)

    @builtins.property
    @jsii.member(jsii_name="sourceProjectId")
    def source_project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceProjectId"))

    @source_project_id.setter
    def source_project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a12419d1dbfd881f4df7f3eafe6deb1b6d10b5694720cc649b270058f75c57de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceProjectId", value)

    @builtins.property
    @jsii.member(jsii_name="sourceTableId")
    def source_table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceTableId"))

    @source_table_id.setter
    def source_table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c62ab55673a3bfef22929e51af833937ceec90582a04d34d4d8efca38150e21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceTableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableTableReplicationInfo]:
        return typing.cast(typing.Optional[GoogleBigqueryTableTableReplicationInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableTableReplicationInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35ed9c303e3d2916793eab7758d7bbfb022915db191d416b1ccaa3cb6a9d9656)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTimePartitioning",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "expiration_ms": "expirationMs",
        "field": "field",
        "require_partition_filter": "requirePartitionFilter",
    },
)
class GoogleBigqueryTableTimePartitioning:
    def __init__(
        self,
        *,
        type: builtins.str,
        expiration_ms: typing.Optional[jsii.Number] = None,
        field: typing.Optional[builtins.str] = None,
        require_partition_filter: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param type: The supported types are DAY, HOUR, MONTH, and YEAR, which will generate one partition per day, hour, month, and year, respectively. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#type GoogleBigqueryTable#type}
        :param expiration_ms: Number of milliseconds for which to keep the storage for a partition. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#expiration_ms GoogleBigqueryTable#expiration_ms}
        :param field: The field used to determine how to create a time-based partition. If time-based partitioning is enabled without this value, the table is partitioned based on the load time. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#field GoogleBigqueryTable#field}
        :param require_partition_filter: If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1df0ab0e8806c224128b1c51c326d81d95cd4271fa5aceff72cec126fb7e4ee2)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument expiration_ms", value=expiration_ms, expected_type=type_hints["expiration_ms"])
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
            check_type(argname="argument require_partition_filter", value=require_partition_filter, expected_type=type_hints["require_partition_filter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if expiration_ms is not None:
            self._values["expiration_ms"] = expiration_ms
        if field is not None:
            self._values["field"] = field
        if require_partition_filter is not None:
            self._values["require_partition_filter"] = require_partition_filter

    @builtins.property
    def type(self) -> builtins.str:
        '''The supported types are DAY, HOUR, MONTH, and YEAR, which will generate one partition per day, hour, month, and year, respectively.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#type GoogleBigqueryTable#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expiration_ms(self) -> typing.Optional[jsii.Number]:
        '''Number of milliseconds for which to keep the storage for a partition.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#expiration_ms GoogleBigqueryTable#expiration_ms}
        '''
        result = self._values.get("expiration_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def field(self) -> typing.Optional[builtins.str]:
        '''The field used to determine how to create a time-based partition.

        If time-based partitioning is enabled without this value, the table is partitioned based on the load time.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#field GoogleBigqueryTable#field}
        '''
        result = self._values.get("field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_partition_filter(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        '''
        result = self._values.get("require_partition_filter")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableTimePartitioning(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableTimePartitioningOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTimePartitioningOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__42812d96236b76d63b17fdd86092408d36cd5e1286a59f5c6f82a10e3dc80b19)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExpirationMs")
    def reset_expiration_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationMs", []))

    @jsii.member(jsii_name="resetField")
    def reset_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetField", []))

    @jsii.member(jsii_name="resetRequirePartitionFilter")
    def reset_require_partition_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequirePartitionFilter", []))

    @builtins.property
    @jsii.member(jsii_name="expirationMsInput")
    def expiration_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expirationMsInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="requirePartitionFilterInput")
    def require_partition_filter_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requirePartitionFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationMs")
    def expiration_ms(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "expirationMs"))

    @expiration_ms.setter
    def expiration_ms(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a5bf706f5417828e1ccb6a5ceb05430a1d1a68e81cb5b8edadcc77f02e03d15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationMs", value)

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b78dc47a51c564a7b5f54575167bd8103bd159370f1545df2e894bd42b447d72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value)

    @builtins.property
    @jsii.member(jsii_name="requirePartitionFilter")
    def require_partition_filter(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requirePartitionFilter"))

    @require_partition_filter.setter
    def require_partition_filter(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e382f46e01b92366c33e81df494fe6ec706ddaa10274d9984104a39b894a9d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirePartitionFilter", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbaf9da3ad8acfa74bececc655e3e89874c960937a2674e4ca24741c119f9e0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryTableTimePartitioning]:
        return typing.cast(typing.Optional[GoogleBigqueryTableTimePartitioning], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableTimePartitioning],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__997f0368b485b38815ce50305ca539594e906263bfea139b70011d2dc3ae7e7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableView",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "use_legacy_sql": "useLegacySql"},
)
class GoogleBigqueryTableView:
    def __init__(
        self,
        *,
        query: builtins.str,
        use_legacy_sql: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param query: A query that BigQuery executes when the view is referenced. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#query GoogleBigqueryTable#query}
        :param use_legacy_sql: Specifies whether to use BigQuery's legacy SQL for this view. The default value is true. If set to false, the view will use BigQuery's standard SQL Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#use_legacy_sql GoogleBigqueryTable#use_legacy_sql}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1705b8378ab7fd3fd81f26efcd434d2da641203732353a1873ef4ffb48f595cc)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument use_legacy_sql", value=use_legacy_sql, expected_type=type_hints["use_legacy_sql"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query": query,
        }
        if use_legacy_sql is not None:
            self._values["use_legacy_sql"] = use_legacy_sql

    @builtins.property
    def query(self) -> builtins.str:
        '''A query that BigQuery executes when the view is referenced.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#query GoogleBigqueryTable#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_legacy_sql(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies whether to use BigQuery's legacy SQL for this view.

        The default value is true. If set to false, the view will use BigQuery's standard SQL

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_bigquery_table#use_legacy_sql GoogleBigqueryTable#use_legacy_sql}
        '''
        result = self._values.get("use_legacy_sql")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableViewOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableViewOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0ff858f7eaf8bdbf1884700c9db423f847e6e28c99eb79e1dd2cfcd5b78f89c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUseLegacySql")
    def reset_use_legacy_sql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseLegacySql", []))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="useLegacySqlInput")
    def use_legacy_sql_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useLegacySqlInput"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8287ce91c406d25e0fd7a20413964d999d4e84cfcc59411aaaa2220bcd30bb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="useLegacySql")
    def use_legacy_sql(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useLegacySql"))

    @use_legacy_sql.setter
    def use_legacy_sql(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__483ac9fc41c2114b7aaa5037d0d13c6aa7f3e609f6d19454dac7e27a45a2e492)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useLegacySql", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryTableView]:
        return typing.cast(typing.Optional[GoogleBigqueryTableView], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GoogleBigqueryTableView]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c5f882adf18101b2912fc5ee177e905556951f66d8300c84401c3ef43f76a1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleBigqueryTable",
    "GoogleBigqueryTableConfig",
    "GoogleBigqueryTableEncryptionConfiguration",
    "GoogleBigqueryTableEncryptionConfigurationOutputReference",
    "GoogleBigqueryTableExternalDataConfiguration",
    "GoogleBigqueryTableExternalDataConfigurationAvroOptions",
    "GoogleBigqueryTableExternalDataConfigurationAvroOptionsOutputReference",
    "GoogleBigqueryTableExternalDataConfigurationCsvOptions",
    "GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference",
    "GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions",
    "GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference",
    "GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions",
    "GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference",
    "GoogleBigqueryTableExternalDataConfigurationJsonOptions",
    "GoogleBigqueryTableExternalDataConfigurationJsonOptionsOutputReference",
    "GoogleBigqueryTableExternalDataConfigurationOutputReference",
    "GoogleBigqueryTableExternalDataConfigurationParquetOptions",
    "GoogleBigqueryTableExternalDataConfigurationParquetOptionsOutputReference",
    "GoogleBigqueryTableMaterializedView",
    "GoogleBigqueryTableMaterializedViewOutputReference",
    "GoogleBigqueryTableRangePartitioning",
    "GoogleBigqueryTableRangePartitioningOutputReference",
    "GoogleBigqueryTableRangePartitioningRange",
    "GoogleBigqueryTableRangePartitioningRangeOutputReference",
    "GoogleBigqueryTableTableConstraints",
    "GoogleBigqueryTableTableConstraintsForeignKeys",
    "GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences",
    "GoogleBigqueryTableTableConstraintsForeignKeysColumnReferencesOutputReference",
    "GoogleBigqueryTableTableConstraintsForeignKeysList",
    "GoogleBigqueryTableTableConstraintsForeignKeysOutputReference",
    "GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable",
    "GoogleBigqueryTableTableConstraintsForeignKeysReferencedTableOutputReference",
    "GoogleBigqueryTableTableConstraintsOutputReference",
    "GoogleBigqueryTableTableConstraintsPrimaryKey",
    "GoogleBigqueryTableTableConstraintsPrimaryKeyOutputReference",
    "GoogleBigqueryTableTableReplicationInfo",
    "GoogleBigqueryTableTableReplicationInfoOutputReference",
    "GoogleBigqueryTableTimePartitioning",
    "GoogleBigqueryTableTimePartitioningOutputReference",
    "GoogleBigqueryTableView",
    "GoogleBigqueryTableViewOutputReference",
]

publication.publish()

def _typecheckingstub__946e9c37b2c299f568e9c744021d56f2d54e6961c5d3710ebb968cc14ac21454(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    dataset_id: builtins.str,
    table_id: builtins.str,
    clustering: typing.Optional[typing.Sequence[builtins.str]] = None,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[GoogleBigqueryTableEncryptionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    expiration_time: typing.Optional[jsii.Number] = None,
    external_data_configuration: typing.Optional[typing.Union[GoogleBigqueryTableExternalDataConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    friendly_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    materialized_view: typing.Optional[typing.Union[GoogleBigqueryTableMaterializedView, typing.Dict[builtins.str, typing.Any]]] = None,
    max_staleness: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
    range_partitioning: typing.Optional[typing.Union[GoogleBigqueryTableRangePartitioning, typing.Dict[builtins.str, typing.Any]]] = None,
    require_partition_filter: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    schema: typing.Optional[builtins.str] = None,
    table_constraints: typing.Optional[typing.Union[GoogleBigqueryTableTableConstraints, typing.Dict[builtins.str, typing.Any]]] = None,
    table_replication_info: typing.Optional[typing.Union[GoogleBigqueryTableTableReplicationInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    time_partitioning: typing.Optional[typing.Union[GoogleBigqueryTableTimePartitioning, typing.Dict[builtins.str, typing.Any]]] = None,
    view: typing.Optional[typing.Union[GoogleBigqueryTableView, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__75322ff820709315badf9c34c6cf567800016adc6256e15129709cc9823edeab(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76894c589838c9a082faa067db42cb728a27c971a2d0ad370b7b178204da57ff(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__444fde6c81e599222175cc658ae45fe6c093fe191c00a233a5f40f7bc1fb336d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1011cf482908614955015cc805e84f70ab837396dd842272769e4b6b3b7c5b75(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a627661f82c2ab3dfa72214456e35f008c6e5e72c7b73b79d89bec9972dfcf18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aad04d72634af56dec81efde39895a173adcdb8f175e82727f3c3db3c5b05318(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d02a1d409ed98f91e9798e6405fa6cc96c6dc7fc467092ba3a7da0653c4d6c21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53c89c2133be9065c731f779e2d646063a756da3380001de916a368f2a8ae8c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c7c726340d6131315a61d2bb511d6f8909ffdaf68ed5e102831468ccc3f7ecf(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa60c124f603637a061fca4fff84c8e2d3853b37e9290cbb8172e05919d4625d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c0404a74d6978f79150373564d8fdae158668d579eed2956a2da670672f120b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94fd9cbfaaef9b873460a28028bd420886528d67ece5838898c1d1f53b7283cf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2b71b896e2687e4be682d51e900d0540d892d36776f184da069895f3c5f87ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe7711efd92dab86d211eaa8e00fef8b6bcd8445961a2714db64586f80c2f98f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54b963582085445098c070f12dbc2aecf85c8a60e6c73ca013d35067bed2a4a7(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    dataset_id: builtins.str,
    table_id: builtins.str,
    clustering: typing.Optional[typing.Sequence[builtins.str]] = None,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[GoogleBigqueryTableEncryptionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    expiration_time: typing.Optional[jsii.Number] = None,
    external_data_configuration: typing.Optional[typing.Union[GoogleBigqueryTableExternalDataConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    friendly_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    materialized_view: typing.Optional[typing.Union[GoogleBigqueryTableMaterializedView, typing.Dict[builtins.str, typing.Any]]] = None,
    max_staleness: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
    range_partitioning: typing.Optional[typing.Union[GoogleBigqueryTableRangePartitioning, typing.Dict[builtins.str, typing.Any]]] = None,
    require_partition_filter: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    schema: typing.Optional[builtins.str] = None,
    table_constraints: typing.Optional[typing.Union[GoogleBigqueryTableTableConstraints, typing.Dict[builtins.str, typing.Any]]] = None,
    table_replication_info: typing.Optional[typing.Union[GoogleBigqueryTableTableReplicationInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    time_partitioning: typing.Optional[typing.Union[GoogleBigqueryTableTimePartitioning, typing.Dict[builtins.str, typing.Any]]] = None,
    view: typing.Optional[typing.Union[GoogleBigqueryTableView, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a9e5b9d2635380dd8876b4ead6886d33a3f196be172509019ee1c62e4b0cac4(
    *,
    kms_key_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac47feacba2ff63b4d4b6cd834c261973959eb828392257e86c965430b233935(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1866154c2a4e3aa1117ffef1107ae3842724380d443407d59da9ac9fed161a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdee95f64c6d871660e34e53f1d38adcb1b0ab6d2cee778ebef16086d73a96a1(
    value: typing.Optional[GoogleBigqueryTableEncryptionConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__602e971b4bfcff52a501458a21051a2cd4a2d264003fefb408f07cedb18d84e5(
    *,
    autodetect: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    source_uris: typing.Sequence[builtins.str],
    avro_options: typing.Optional[typing.Union[GoogleBigqueryTableExternalDataConfigurationAvroOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    compression: typing.Optional[builtins.str] = None,
    connection_id: typing.Optional[builtins.str] = None,
    csv_options: typing.Optional[typing.Union[GoogleBigqueryTableExternalDataConfigurationCsvOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    file_set_spec_type: typing.Optional[builtins.str] = None,
    google_sheets_options: typing.Optional[typing.Union[GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    hive_partitioning_options: typing.Optional[typing.Union[GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ignore_unknown_values: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    json_options: typing.Optional[typing.Union[GoogleBigqueryTableExternalDataConfigurationJsonOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    max_bad_records: typing.Optional[jsii.Number] = None,
    metadata_cache_mode: typing.Optional[builtins.str] = None,
    object_metadata: typing.Optional[builtins.str] = None,
    parquet_options: typing.Optional[typing.Union[GoogleBigqueryTableExternalDataConfigurationParquetOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    reference_file_schema_uri: typing.Optional[builtins.str] = None,
    schema: typing.Optional[builtins.str] = None,
    source_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e056d587d279501e907787fbdde8bcd72c0bbc0a0b7ebf5a1966e26a43c6d82e(
    *,
    use_avro_logical_types: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a447dc5261f83cb375ec248b63ed2dc1f0f81b51042f2c5ceb195795eba3ddd3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e208c6280c6864ccc073f452c7f7b498650e985d39ac2611b3694de7d527104c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beb84d5b86dff064b1da2c8a64bdb0a380f12846ab88737aba25a25c6198c639(
    value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationAvroOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12886bff655293afef73b291df9192fb56405e7c329c57e8a0de15ce78a5a687(
    *,
    quote: builtins.str,
    allow_jagged_rows: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_quoted_newlines: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encoding: typing.Optional[builtins.str] = None,
    field_delimiter: typing.Optional[builtins.str] = None,
    skip_leading_rows: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd07c9c96ed9b19dd5ba802a45c23f740ecb00994e422a16c0f3138eaa554a3d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3794c0cb6a1584814b84ae5434a720bcae9eb2cfb647dec3e2fe56b746e2ae3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cedafbb2f52e2caa5061dcaccd997685b4d9b2d11327013d36c840bcdf69a4c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25462329f0702812ae812048222a7c1828f1c922da3763306e621f23e8291833(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b81281ef2bbb77df0332f2b6f45606d3ce76122b2fa1c41a4ff7e02a977aa56b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a88a05bf6e3a36fa26d8489b6ddaf4ab0f893cbaf94f1dcabe1e5e76136ac07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10ce05ad5bae5f5b21acb656d5e17260b399553a206fe308196c04011bab6140(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99511cd60bdd6c471eb9418878c3699e447213d0702e54295f09a24c85ece31b(
    value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationCsvOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0c5c07c152a25c24c896eba15ec4821802c924adb0a35c5578737eed3ec2699(
    *,
    range: typing.Optional[builtins.str] = None,
    skip_leading_rows: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__802ed1a4f414daf0b7342072c7063594445f9784fbd6117b5114e8d347b328d8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f0a8f3dabdc8cc44976d3718f4735b85c26d5da2eff68d2460f851e4e258650(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84e6b9419149cfdd5b5c57c1983e78b0c22575ed10ed62a2ef75c9e03ec2e9b0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__543fb036cb1d4ae8a5cb906d78d84f1fbec5c451721196f5afb5163f5904720e(
    value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7ad8f75d82703f801eb14e586fe0669594ed903d631d67a19cbfef1ba2ef922(
    *,
    mode: typing.Optional[builtins.str] = None,
    require_partition_filter: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    source_uri_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6493145b3124699867b574fb56803b73d3db19fdf2381934c9d969b502a3b9f7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27e7d819fc1fdac87c67e7a2695fb8e5a54b9eba8e9ece0c544d686074fe166c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a5749971cb8004a36db956ffa9d734ac17003403dfb128157b8298754a1db02(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5ed152323e0e80c83bbc7c6133044d3251baa8b8250cce5b98d27b10e1abb37(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3be43eb2768828a2618edc1bd2340d9d54617c94a1a08224a5edf9007073face(
    value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4107b273f8e893e0eacacf07eb6c23c076cca6c323ab5e6fe3e564e281e5835f(
    *,
    encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0956af7c573daa31d7303e6eb30233d8c0289fbd4747b2c93a91ede7e7166bcf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73f69eded064ae86a2ab7bc18fed75e5cfe18d536b073008fc7456427147329a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca6f44b8a8c90f68f65e1673c8d71080f5713414defb9e5505ae5738d6e159bb(
    value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationJsonOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d5f4874ee8829862ba38fc77ca71ca6e97e3ce71b54a8461418565931e66d5c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d50459652227b9ff45eb1306bdfc41d945b0c6d6d574624e27d1f3684515f1a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__093a2d981c69283998e5f97acd4c0e649b8c697eb3e87dec4111ed2ee33712df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35b47a224774a6a12439bb1bf2ed94bf03bc3ca43e76dd9bdf62c00458b7f287(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1956f05128314b1de32ed2fbe90e54a096b2629ffbf0a7001028c2c6124aede9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09a19404a32b0087f8a9b762fafdc3e3639cf1b3bba5abee4a9955ef9f74f6e3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cce2e1884e8724c36e010e250e64db6320f24055534a528e53b09e1ae86f793e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5efafd923c05641244575bc3ff0c2918f9242d754f72050394e34cc85655edc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ab81df88a4136eea0e777f0daad1716940d8a909199bfa2adb926f044ea6b9a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3cdec1e56d8db55bbe10f42f4f9592af981ad3062a8da7e3890f9eb124a766f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deab5426036d789b5d7c69bab30d83e50ae27623a20b0a8e1c652d6adcf605cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a27a87ef92af9ef06814d5c99204b644bce025a6e8eeb46ef0ee50e4df9eb627(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfbe1f7ce93a0ea610a7fcbae3691977d5e14c4a2b067c0c886577b890568bf4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b71b35a269d54765944fa7cb6dd7e00af7c09fce2233c1cf8b806e85e1308169(
    value: typing.Optional[GoogleBigqueryTableExternalDataConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a80e45df433f5a95b4103694f0064452da3152f728ba9b6eab20e711eb31afc5(
    *,
    enable_list_inference: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enum_as_string: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3b5934508f0214af865c4a131fdf94293b155ffc226e110610eef6c6e78275f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a63982f55e5282b7ceaa52d65cd0ce044cd22d28474bf679cd66fb14fb8caf0b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0e4301f6bc15a2078e09cbec2af4a4f020bb2c6a7aad4ff01d8c496e95e7356(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca7d3f7bda0456b85782cc56d44aaa7c369ef45b186d7843ea93c09455352de4(
    value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationParquetOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67c9007c097b1868a28cde3dcb6414c32a0dd5bde75bd8cb579b6f16f6952558(
    *,
    query: builtins.str,
    allow_non_incremental_definition: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_refresh: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    refresh_interval_ms: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76d4310ce3220e4311399768d0d65dfe628ebe569c9c1d1aae69b73490bc6eb7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26e558f13e4dc47793f44ca98c13e0b86b9cb6e40643455be7dc716344763f82(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d7fd6a8ab03bf2cdc7505d1986ba182dcaedc329db48b8894cf7c58fd3ced8f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2498add99e863c54284fd157d68632ffbbd5b2a15b18df5e976b642b6469150d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a72eae716dc687a0de9c73e693e07d89bf9cb88054056ea18cf57a0d11b1808f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__384b0ce977605dd8b4519b93855ccd336931d6e0d1bf9f020ab7032d048780f5(
    value: typing.Optional[GoogleBigqueryTableMaterializedView],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35fdc34928dd2c4fb6fde71af4628fc3301a2e4c3186594446175cf54b68e24c(
    *,
    field: builtins.str,
    range: typing.Union[GoogleBigqueryTableRangePartitioningRange, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a635990a30f5b0f38742af12a74e7e64dee33fe080cfb39c8bc609e972f166e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87d25dc939d584638dedb87b1f5763b0b81d7843c92eb97ee91bace3924c69e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3391981cb2b5b4c6cbdc2027d2dc19e8f91b47809c56cabde852193877c715c6(
    value: typing.Optional[GoogleBigqueryTableRangePartitioning],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d750860c0abe8bd5c3c946f56ada1355e0e94088874e25c9b1c55ffcabf7f295(
    *,
    end: jsii.Number,
    interval: jsii.Number,
    start: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c419c0328857a9a010254db2c200d098159c1cdf40b5c5f19cb37cad4dcf584(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcd21d99a42cf977585d7a9b9497e2d29e2bc2b20b227b63fff8b04d2af98388(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5017979f3ec443c0a4a68da0880bb782c785060c75b5adf4968b7ccc1f67110(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a204c84f1c4fbebf944db13b86709bc6e816b2b1369184742e6ba62eaf29d34(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0413bb15900a5a0292e1393186cd6c4320145552e16f70d86a2db180ac1f1834(
    value: typing.Optional[GoogleBigqueryTableRangePartitioningRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3089b462815c89868a1c275d77454881d0914012504c685849e4b7eaf2274249(
    *,
    foreign_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleBigqueryTableTableConstraintsForeignKeys, typing.Dict[builtins.str, typing.Any]]]]] = None,
    primary_key: typing.Optional[typing.Union[GoogleBigqueryTableTableConstraintsPrimaryKey, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__134a9be75b79720fc947d828706fb2c13782775aa904cc2437305871a4a1b3cd(
    *,
    column_references: typing.Union[GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences, typing.Dict[builtins.str, typing.Any]],
    referenced_table: typing.Union[GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable, typing.Dict[builtins.str, typing.Any]],
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24d1b7a0ae52e500449afb4993b7e95bf0b9f1cf57b2bfb14c1f75503293f2e0(
    *,
    referenced_column: builtins.str,
    referencing_column: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1292ccbf14a30fa8d4c9853a23dc266bf0440f7b496fa6f1aae28b319b058b45(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04a9a289299078f0172b2903e15af1e8ee9f0003904d7440f5273c15dd9d4bc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3bf3a49d1034bdecf5e94fb583f425f23be1838492f384d8f4a4ea1ac88908a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f82e2b61eab0b1bacbaf79cbf9be3c98cf24337b0ca75b6ded7655f826860868(
    value: typing.Optional[GoogleBigqueryTableTableConstraintsForeignKeysColumnReferences],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36ae60b93b646a53152afea2a3b2f08e9f1aa12020a79399a7661c04e319c644(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1492186e9542bff1b62444b6ab0da4e6d032caf872d09e8481f028364f5637dd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9878e2af5e4692dc0c7cd35272139fb989050ee159287a02f65d0640d1d9b3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33de6d96564b512f03291e9dcaeb577dfc89de07cc262d053fd89da86f434cc9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__273162998daee6d72bdcbfa2fb8542936f2b46556f81c38d6c88b50568861b58(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c774aa04f261060eeacfa0bcd7a2dbe6fecfedfcd43d7888329b1a5787fd889(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleBigqueryTableTableConstraintsForeignKeys]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c96287c0a3f7d63c5305d0cb931d2e2d1df0b843e93b0096337c630b982d7f2b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__882cdd1eed070f60b2fbcdbf8887c93fc6b9dc6277915194f3573a2afde4f932(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d503796a604ec9d479d577c584b1389b203132de9e0efe56d4f9a22bf5b68a04(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleBigqueryTableTableConstraintsForeignKeys]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dabaa08d6b9445ed09c1fe2122a795b3df4b32db90ef82f20ba5260070a81b0b(
    *,
    dataset_id: builtins.str,
    project_id: builtins.str,
    table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34ceb18c1f75fe8d989ceed920356aff85642f07bee8249b49847f3fe1ccbdf7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09101c0b500e91cd649fa3044044374a4d34b2f4b0c05b4c6dc8f93dc9caf340(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef0e3d3040cab761c5850af3efc76cb771eba90f3600b74d6d68d57ef7e5057b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9990f15255aef97330511c44f4eb6794948eadaca1467912e224e60b9cf40206(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08decc1e28e41f4d786d698f2d1feecc213724f1b905bd726e999c44887fea5b(
    value: typing.Optional[GoogleBigqueryTableTableConstraintsForeignKeysReferencedTable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__420af46f9e50ec2e9534b17fd7458e6c3541698ea0f5248f440d5ee894878913(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8515862cd3de01201a8f41886429f90be48e3712a650d2be2c0013acbe17b0f6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleBigqueryTableTableConstraintsForeignKeys, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d26ca8a30ed10893fa202a98f5f6955fa3e1547e1182d66cda0c907e18b0767(
    value: typing.Optional[GoogleBigqueryTableTableConstraints],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9b8a7927e0f726a7e13ed2d5ea330114e2b8f308e2ccbda7565681b99dbf0df(
    *,
    columns: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13bec339a4b73128a45147a819606a85699dab069f3d93a3dc0d3aeb666bc1ff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4ae6218f68d4f2b60eadc5e307488d73cddac580b8487c21e553b38aa0fcfba(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39792b8e805f59e99c37b6120ede7d5c3f66321c29d04ab10451120a77cb02f8(
    value: typing.Optional[GoogleBigqueryTableTableConstraintsPrimaryKey],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84bd36017a02b353fb1b062d8d8470796dbae88096175f677b97b6cfc54e9498(
    *,
    source_dataset_id: builtins.str,
    source_project_id: builtins.str,
    source_table_id: builtins.str,
    replication_interval_ms: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3924682e9298366c0a4fbfc0bd3bf00182813035b2965f2aeeec12813fca982b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f075ce5ae4733f419da7ec6c14acf1fc2fadd0df99ced48b486c3649d29af5de(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e289440179ee88b8ca0367c7f548231e40968876ae7b313442d46a8984372387(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a12419d1dbfd881f4df7f3eafe6deb1b6d10b5694720cc649b270058f75c57de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c62ab55673a3bfef22929e51af833937ceec90582a04d34d4d8efca38150e21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ed9c303e3d2916793eab7758d7bbfb022915db191d416b1ccaa3cb6a9d9656(
    value: typing.Optional[GoogleBigqueryTableTableReplicationInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1df0ab0e8806c224128b1c51c326d81d95cd4271fa5aceff72cec126fb7e4ee2(
    *,
    type: builtins.str,
    expiration_ms: typing.Optional[jsii.Number] = None,
    field: typing.Optional[builtins.str] = None,
    require_partition_filter: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42812d96236b76d63b17fdd86092408d36cd5e1286a59f5c6f82a10e3dc80b19(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a5bf706f5417828e1ccb6a5ceb05430a1d1a68e81cb5b8edadcc77f02e03d15(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b78dc47a51c564a7b5f54575167bd8103bd159370f1545df2e894bd42b447d72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e382f46e01b92366c33e81df494fe6ec706ddaa10274d9984104a39b894a9d0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbaf9da3ad8acfa74bececc655e3e89874c960937a2674e4ca24741c119f9e0d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__997f0368b485b38815ce50305ca539594e906263bfea139b70011d2dc3ae7e7f(
    value: typing.Optional[GoogleBigqueryTableTimePartitioning],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1705b8378ab7fd3fd81f26efcd434d2da641203732353a1873ef4ffb48f595cc(
    *,
    query: builtins.str,
    use_legacy_sql: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0ff858f7eaf8bdbf1884700c9db423f847e6e28c99eb79e1dd2cfcd5b78f89c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8287ce91c406d25e0fd7a20413964d999d4e84cfcc59411aaaa2220bcd30bb4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__483ac9fc41c2114b7aaa5037d0d13c6aa7f3e609f6d19454dac7e27a45a2e492(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c5f882adf18101b2912fc5ee177e905556951f66d8300c84401c3ef43f76a1f(
    value: typing.Optional[GoogleBigqueryTableView],
) -> None:
    """Type checking stubs"""
    pass
