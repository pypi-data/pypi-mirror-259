'''
# `google_dialogflow_cx_flow`

Refer to the Terraform Registry for docs: [`google_dialogflow_cx_flow`](https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow).
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


class GoogleDialogflowCxFlow(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlow",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow google_dialogflow_cx_flow}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        advanced_settings: typing.Optional[typing.Union["GoogleDialogflowCxFlowAdvancedSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        event_handlers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowEventHandlers", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        is_default_start_flow: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        language_code: typing.Optional[builtins.str] = None,
        nlu_settings: typing.Optional[typing.Union["GoogleDialogflowCxFlowNluSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        parent: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDialogflowCxFlowTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        transition_route_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        transition_routes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowTransitionRoutes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow google_dialogflow_cx_flow} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: The human-readable name of the flow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#display_name GoogleDialogflowCxFlow#display_name}
        :param advanced_settings: advanced_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#advanced_settings GoogleDialogflowCxFlow#advanced_settings}
        :param description: The description of the flow. The maximum length is 500 characters. If exceeded, the request is rejected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#description GoogleDialogflowCxFlow#description}
        :param event_handlers: event_handlers block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#event_handlers GoogleDialogflowCxFlow#event_handlers}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#id GoogleDialogflowCxFlow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_default_start_flow: Marks this as the `Default Start Flow <https://cloud.google.com/dialogflow/cx/docs/concept/flow#start>`_ for an agent. When you create an agent, the Default Start Flow is created automatically. The Default Start Flow cannot be deleted; deleting the 'google_dialogflow_cx_flow' resource does nothing to the underlying GCP resources. ~> Avoid having multiple 'google_dialogflow_cx_flow' resources linked to the same agent with 'is_default_start_flow = true' because they will compete to control a single Default Start Flow resource in GCP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#is_default_start_flow GoogleDialogflowCxFlow#is_default_start_flow}
        :param language_code: The language of the following fields in flow: Flow.event_handlers.trigger_fulfillment.messages Flow.event_handlers.trigger_fulfillment.conditional_cases Flow.transition_routes.trigger_fulfillment.messages Flow.transition_routes.trigger_fulfillment.conditional_cases If not specified, the agent's default language is used. Many languages are supported. Note: languages must be enabled in the agent before they can be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#language_code GoogleDialogflowCxFlow#language_code}
        :param nlu_settings: nlu_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#nlu_settings GoogleDialogflowCxFlow#nlu_settings}
        :param parent: The agent to create a flow for. Format: projects//locations//agents/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#parent GoogleDialogflowCxFlow#parent}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#timeouts GoogleDialogflowCxFlow#timeouts}
        :param transition_route_groups: A flow's transition route group serve two purposes: They are responsible for matching the user's first utterances in the flow. They are inherited by every page's [transition route groups][Page.transition_route_groups]. Transition route groups defined in the page have higher priority than those defined in the flow. Format:projects//locations//agents//flows//transitionRouteGroups/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#transition_route_groups GoogleDialogflowCxFlow#transition_route_groups}
        :param transition_routes: transition_routes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#transition_routes GoogleDialogflowCxFlow#transition_routes}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ddc1c9bd1aaab871a2b80768c2bc499e93a36227c2ec26b6797aac6fac61ceb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDialogflowCxFlowConfig(
            display_name=display_name,
            advanced_settings=advanced_settings,
            description=description,
            event_handlers=event_handlers,
            id=id,
            is_default_start_flow=is_default_start_flow,
            language_code=language_code,
            nlu_settings=nlu_settings,
            parent=parent,
            timeouts=timeouts,
            transition_route_groups=transition_route_groups,
            transition_routes=transition_routes,
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
        '''Generates CDKTF code for importing a GoogleDialogflowCxFlow resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the GoogleDialogflowCxFlow to import.
        :param import_from_id: The id of the existing GoogleDialogflowCxFlow that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the GoogleDialogflowCxFlow to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad3b054a471de21d0a367ca38d61ec2a1c86d28c7c7e15d0fa29c34cef2e8ffa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAdvancedSettings")
    def put_advanced_settings(
        self,
        *,
        audio_export_gcs_destination: typing.Optional[typing.Union["GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination", typing.Dict[builtins.str, typing.Any]]] = None,
        dtmf_settings: typing.Optional[typing.Union["GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param audio_export_gcs_destination: audio_export_gcs_destination block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#audio_export_gcs_destination GoogleDialogflowCxFlow#audio_export_gcs_destination}
        :param dtmf_settings: dtmf_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#dtmf_settings GoogleDialogflowCxFlow#dtmf_settings}
        '''
        value = GoogleDialogflowCxFlowAdvancedSettings(
            audio_export_gcs_destination=audio_export_gcs_destination,
            dtmf_settings=dtmf_settings,
        )

        return typing.cast(None, jsii.invoke(self, "putAdvancedSettings", [value]))

    @jsii.member(jsii_name="putEventHandlers")
    def put_event_handlers(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowEventHandlers", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d5763a95f2a19a20a2cee1cd63b8e22e995b6ccdda0bc67f0a8ba7c9afea462)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEventHandlers", [value]))

    @jsii.member(jsii_name="putNluSettings")
    def put_nlu_settings(
        self,
        *,
        classification_threshold: typing.Optional[jsii.Number] = None,
        model_training_mode: typing.Optional[builtins.str] = None,
        model_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param classification_threshold: To filter out false positive results and still get variety in matched natural language inputs for your agent, you can tune the machine learning classification threshold. If the returned score value is less than the threshold value, then a no-match event will be triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the default of 0.3 is used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#classification_threshold GoogleDialogflowCxFlow#classification_threshold}
        :param model_training_mode: Indicates NLU model training mode. - MODEL_TRAINING_MODE_AUTOMATIC: NLU model training is automatically triggered when a flow gets modified. User can also manually trigger model training in this mode. - MODEL_TRAINING_MODE_MANUAL: User needs to manually trigger NLU model training. Best for large flows whose models take long time to train. Possible values: ["MODEL_TRAINING_MODE_AUTOMATIC", "MODEL_TRAINING_MODE_MANUAL"] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#model_training_mode GoogleDialogflowCxFlow#model_training_mode}
        :param model_type: Indicates the type of NLU model. - MODEL_TYPE_STANDARD: Use standard NLU model. - MODEL_TYPE_ADVANCED: Use advanced NLU model. Possible values: ["MODEL_TYPE_STANDARD", "MODEL_TYPE_ADVANCED"] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#model_type GoogleDialogflowCxFlow#model_type}
        '''
        value = GoogleDialogflowCxFlowNluSettings(
            classification_threshold=classification_threshold,
            model_training_mode=model_training_mode,
            model_type=model_type,
        )

        return typing.cast(None, jsii.invoke(self, "putNluSettings", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#create GoogleDialogflowCxFlow#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#delete GoogleDialogflowCxFlow#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#update GoogleDialogflowCxFlow#update}.
        '''
        value = GoogleDialogflowCxFlowTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTransitionRoutes")
    def put_transition_routes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowTransitionRoutes", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f67d14e084641d1578e154aed126fcf46d108e0c8f21351b034db072abbe3b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTransitionRoutes", [value]))

    @jsii.member(jsii_name="resetAdvancedSettings")
    def reset_advanced_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedSettings", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEventHandlers")
    def reset_event_handlers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventHandlers", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsDefaultStartFlow")
    def reset_is_default_start_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsDefaultStartFlow", []))

    @jsii.member(jsii_name="resetLanguageCode")
    def reset_language_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLanguageCode", []))

    @jsii.member(jsii_name="resetNluSettings")
    def reset_nlu_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNluSettings", []))

    @jsii.member(jsii_name="resetParent")
    def reset_parent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParent", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTransitionRouteGroups")
    def reset_transition_route_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitionRouteGroups", []))

    @jsii.member(jsii_name="resetTransitionRoutes")
    def reset_transition_routes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitionRoutes", []))

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
    @jsii.member(jsii_name="advancedSettings")
    def advanced_settings(
        self,
    ) -> "GoogleDialogflowCxFlowAdvancedSettingsOutputReference":
        return typing.cast("GoogleDialogflowCxFlowAdvancedSettingsOutputReference", jsii.get(self, "advancedSettings"))

    @builtins.property
    @jsii.member(jsii_name="eventHandlers")
    def event_handlers(self) -> "GoogleDialogflowCxFlowEventHandlersList":
        return typing.cast("GoogleDialogflowCxFlowEventHandlersList", jsii.get(self, "eventHandlers"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="nluSettings")
    def nlu_settings(self) -> "GoogleDialogflowCxFlowNluSettingsOutputReference":
        return typing.cast("GoogleDialogflowCxFlowNluSettingsOutputReference", jsii.get(self, "nluSettings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDialogflowCxFlowTimeoutsOutputReference":
        return typing.cast("GoogleDialogflowCxFlowTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="transitionRoutes")
    def transition_routes(self) -> "GoogleDialogflowCxFlowTransitionRoutesList":
        return typing.cast("GoogleDialogflowCxFlowTransitionRoutesList", jsii.get(self, "transitionRoutes"))

    @builtins.property
    @jsii.member(jsii_name="advancedSettingsInput")
    def advanced_settings_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowAdvancedSettings"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowAdvancedSettings"], jsii.get(self, "advancedSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="eventHandlersInput")
    def event_handlers_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowEventHandlers"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowEventHandlers"]]], jsii.get(self, "eventHandlersInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isDefaultStartFlowInput")
    def is_default_start_flow_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isDefaultStartFlowInput"))

    @builtins.property
    @jsii.member(jsii_name="languageCodeInput")
    def language_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "languageCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="nluSettingsInput")
    def nlu_settings_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowNluSettings"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowNluSettings"], jsii.get(self, "nluSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "GoogleDialogflowCxFlowTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "GoogleDialogflowCxFlowTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="transitionRouteGroupsInput")
    def transition_route_groups_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transitionRouteGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="transitionRoutesInput")
    def transition_routes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowTransitionRoutes"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowTransitionRoutes"]]], jsii.get(self, "transitionRoutesInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7564a7905ff3d080ec73fd5b3674d80316185888f34b793426007f2891348fc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d57e353ea4e0c1dbefde806a99b8c916a02fa1ed2fdd994823bfcf5422e9934)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eab5ec690ece1ff9fa75d59b2a15d2b7ececfba9a83206cd737e9f2f7198cb5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isDefaultStartFlow")
    def is_default_start_flow(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isDefaultStartFlow"))

    @is_default_start_flow.setter
    def is_default_start_flow(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc61fcc21cb3d353f84d5d4e88bdffe57d189d4c895ab85b7d3f152168394a73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isDefaultStartFlow", value)

    @builtins.property
    @jsii.member(jsii_name="languageCode")
    def language_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "languageCode"))

    @language_code.setter
    def language_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb70b48e85ea80ce1f103a0c05a4b3466c57a382c528c7a81ce07b3b8df410ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageCode", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a48c675e5612a9b38a6595f66082b141506e7336639e253e7d20e4b003a2e87d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)

    @builtins.property
    @jsii.member(jsii_name="transitionRouteGroups")
    def transition_route_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transitionRouteGroups"))

    @transition_route_groups.setter
    def transition_route_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8b9d2da6f549846ac8b8c3ea7bb8b102639d483550c7cb5ff7fa1924d572b11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitionRouteGroups", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowAdvancedSettings",
    jsii_struct_bases=[],
    name_mapping={
        "audio_export_gcs_destination": "audioExportGcsDestination",
        "dtmf_settings": "dtmfSettings",
    },
)
class GoogleDialogflowCxFlowAdvancedSettings:
    def __init__(
        self,
        *,
        audio_export_gcs_destination: typing.Optional[typing.Union["GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination", typing.Dict[builtins.str, typing.Any]]] = None,
        dtmf_settings: typing.Optional[typing.Union["GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param audio_export_gcs_destination: audio_export_gcs_destination block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#audio_export_gcs_destination GoogleDialogflowCxFlow#audio_export_gcs_destination}
        :param dtmf_settings: dtmf_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#dtmf_settings GoogleDialogflowCxFlow#dtmf_settings}
        '''
        if isinstance(audio_export_gcs_destination, dict):
            audio_export_gcs_destination = GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination(**audio_export_gcs_destination)
        if isinstance(dtmf_settings, dict):
            dtmf_settings = GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings(**dtmf_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74522f9b5137db65e0921cf1c5e8aa67898022072b01667d01626b26b51a97d4)
            check_type(argname="argument audio_export_gcs_destination", value=audio_export_gcs_destination, expected_type=type_hints["audio_export_gcs_destination"])
            check_type(argname="argument dtmf_settings", value=dtmf_settings, expected_type=type_hints["dtmf_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if audio_export_gcs_destination is not None:
            self._values["audio_export_gcs_destination"] = audio_export_gcs_destination
        if dtmf_settings is not None:
            self._values["dtmf_settings"] = dtmf_settings

    @builtins.property
    def audio_export_gcs_destination(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination"]:
        '''audio_export_gcs_destination block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#audio_export_gcs_destination GoogleDialogflowCxFlow#audio_export_gcs_destination}
        '''
        result = self._values.get("audio_export_gcs_destination")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination"], result)

    @builtins.property
    def dtmf_settings(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings"]:
        '''dtmf_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#dtmf_settings GoogleDialogflowCxFlow#dtmf_settings}
        '''
        result = self._values.get("dtmf_settings")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowAdvancedSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination",
    jsii_struct_bases=[],
    name_mapping={"uri": "uri"},
)
class GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination:
    def __init__(self, *, uri: typing.Optional[builtins.str] = None) -> None:
        '''
        :param uri: The Google Cloud Storage URI for the exported objects. Whether a full object name, or just a prefix, its usage depends on the Dialogflow operation. Format: gs://bucket/object-name-or-prefix Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#uri GoogleDialogflowCxFlow#uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f14a90e7cb3882840e4ec911e01e5451e2d8b19a9979b602f4294dbcd64ba59c)
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''The Google Cloud Storage URI for the exported objects.

        Whether a full object name, or just a prefix, its usage depends on the Dialogflow operation.
        Format: gs://bucket/object-name-or-prefix

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#uri GoogleDialogflowCxFlow#uri}
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestinationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestinationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__126bfaf474003387ad65638cfd0a1d944237446dd9255e7e0c74b0ed088028dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUri")
    def reset_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUri", []))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcf8efda4b84a8fbcd37d884c901b0367ea99053549c30a600b982d7b6ae0208)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6753a3d1e6d9677e891ba03b4be61d55b680366939ab6a465ec78726af5affdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "finish_digit": "finishDigit",
        "max_digits": "maxDigits",
    },
)
class GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        finish_digit: typing.Optional[builtins.str] = None,
        max_digits: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: If true, incoming audio is processed for DTMF (dual tone multi frequency) events. For example, if the caller presses a button on their telephone keypad and DTMF processing is enabled, Dialogflow will detect the event (e.g. a "3" was pressed) in the incoming audio and pass the event to the bot to drive business logic (e.g. when 3 is pressed, return the account balance). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#enabled GoogleDialogflowCxFlow#enabled}
        :param finish_digit: The digit that terminates a DTMF digit sequence. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#finish_digit GoogleDialogflowCxFlow#finish_digit}
        :param max_digits: Max length of DTMF digits. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#max_digits GoogleDialogflowCxFlow#max_digits}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbbd4cad34ff6aa630667af905d7c23565c8b573fc94b53aeedc8657f064a053)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument finish_digit", value=finish_digit, expected_type=type_hints["finish_digit"])
            check_type(argname="argument max_digits", value=max_digits, expected_type=type_hints["max_digits"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if finish_digit is not None:
            self._values["finish_digit"] = finish_digit
        if max_digits is not None:
            self._values["max_digits"] = max_digits

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, incoming audio is processed for DTMF (dual tone multi frequency) events.

        For example, if the caller presses a button on their telephone keypad and DTMF processing is enabled, Dialogflow will detect the event (e.g. a "3" was pressed) in the incoming audio and pass the event to the bot to drive business logic (e.g. when 3 is pressed, return the account balance).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#enabled GoogleDialogflowCxFlow#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def finish_digit(self) -> typing.Optional[builtins.str]:
        '''The digit that terminates a DTMF digit sequence.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#finish_digit GoogleDialogflowCxFlow#finish_digit}
        '''
        result = self._values.get("finish_digit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_digits(self) -> typing.Optional[jsii.Number]:
        '''Max length of DTMF digits.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#max_digits GoogleDialogflowCxFlow#max_digits}
        '''
        result = self._values.get("max_digits")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowAdvancedSettingsDtmfSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowAdvancedSettingsDtmfSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__94e13c969a0969e8c13bac2c5a7a19f17db5928989f957c7eff5e02b1285b21c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFinishDigit")
    def reset_finish_digit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFinishDigit", []))

    @jsii.member(jsii_name="resetMaxDigits")
    def reset_max_digits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxDigits", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="finishDigitInput")
    def finish_digit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "finishDigitInput"))

    @builtins.property
    @jsii.member(jsii_name="maxDigitsInput")
    def max_digits_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxDigitsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__444113a02773315b4f4224c440ff697f2d51c4eb404fb307174f2a56c5ff5bfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="finishDigit")
    def finish_digit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "finishDigit"))

    @finish_digit.setter
    def finish_digit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__080fea3290e7f671c0b7921f05c14cfde7ad37d6a3ae820c5301a730c89c0ba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finishDigit", value)

    @builtins.property
    @jsii.member(jsii_name="maxDigits")
    def max_digits(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxDigits"))

    @max_digits.setter
    def max_digits(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79d79812fc802c105c6e8454b68dff149578f978375c174f256286489e456019)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDigits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d36606aa4eb8bd597c3494f9c89fb89e5f555047331abb521468e0e51933e94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxFlowAdvancedSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowAdvancedSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a4cfef87b8c76c85a3fbfc1b57d3fdf6b29e64131a20d9a3f54dc95a49cf56d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAudioExportGcsDestination")
    def put_audio_export_gcs_destination(
        self,
        *,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param uri: The Google Cloud Storage URI for the exported objects. Whether a full object name, or just a prefix, its usage depends on the Dialogflow operation. Format: gs://bucket/object-name-or-prefix Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#uri GoogleDialogflowCxFlow#uri}
        '''
        value = GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination(
            uri=uri
        )

        return typing.cast(None, jsii.invoke(self, "putAudioExportGcsDestination", [value]))

    @jsii.member(jsii_name="putDtmfSettings")
    def put_dtmf_settings(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        finish_digit: typing.Optional[builtins.str] = None,
        max_digits: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: If true, incoming audio is processed for DTMF (dual tone multi frequency) events. For example, if the caller presses a button on their telephone keypad and DTMF processing is enabled, Dialogflow will detect the event (e.g. a "3" was pressed) in the incoming audio and pass the event to the bot to drive business logic (e.g. when 3 is pressed, return the account balance). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#enabled GoogleDialogflowCxFlow#enabled}
        :param finish_digit: The digit that terminates a DTMF digit sequence. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#finish_digit GoogleDialogflowCxFlow#finish_digit}
        :param max_digits: Max length of DTMF digits. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#max_digits GoogleDialogflowCxFlow#max_digits}
        '''
        value = GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings(
            enabled=enabled, finish_digit=finish_digit, max_digits=max_digits
        )

        return typing.cast(None, jsii.invoke(self, "putDtmfSettings", [value]))

    @jsii.member(jsii_name="resetAudioExportGcsDestination")
    def reset_audio_export_gcs_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudioExportGcsDestination", []))

    @jsii.member(jsii_name="resetDtmfSettings")
    def reset_dtmf_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDtmfSettings", []))

    @builtins.property
    @jsii.member(jsii_name="audioExportGcsDestination")
    def audio_export_gcs_destination(
        self,
    ) -> GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestinationOutputReference:
        return typing.cast(GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestinationOutputReference, jsii.get(self, "audioExportGcsDestination"))

    @builtins.property
    @jsii.member(jsii_name="dtmfSettings")
    def dtmf_settings(
        self,
    ) -> GoogleDialogflowCxFlowAdvancedSettingsDtmfSettingsOutputReference:
        return typing.cast(GoogleDialogflowCxFlowAdvancedSettingsDtmfSettingsOutputReference, jsii.get(self, "dtmfSettings"))

    @builtins.property
    @jsii.member(jsii_name="audioExportGcsDestinationInput")
    def audio_export_gcs_destination_input(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination], jsii.get(self, "audioExportGcsDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="dtmfSettingsInput")
    def dtmf_settings_input(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings], jsii.get(self, "dtmfSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDialogflowCxFlowAdvancedSettings]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowAdvancedSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowAdvancedSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf2a7517d1b6799be5bbd2bca26336584a9c1d7021407f29c7456dedcdffaa7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "display_name": "displayName",
        "advanced_settings": "advancedSettings",
        "description": "description",
        "event_handlers": "eventHandlers",
        "id": "id",
        "is_default_start_flow": "isDefaultStartFlow",
        "language_code": "languageCode",
        "nlu_settings": "nluSettings",
        "parent": "parent",
        "timeouts": "timeouts",
        "transition_route_groups": "transitionRouteGroups",
        "transition_routes": "transitionRoutes",
    },
)
class GoogleDialogflowCxFlowConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        display_name: builtins.str,
        advanced_settings: typing.Optional[typing.Union[GoogleDialogflowCxFlowAdvancedSettings, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        event_handlers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowEventHandlers", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        is_default_start_flow: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        language_code: typing.Optional[builtins.str] = None,
        nlu_settings: typing.Optional[typing.Union["GoogleDialogflowCxFlowNluSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        parent: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDialogflowCxFlowTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        transition_route_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        transition_routes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowTransitionRoutes", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: The human-readable name of the flow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#display_name GoogleDialogflowCxFlow#display_name}
        :param advanced_settings: advanced_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#advanced_settings GoogleDialogflowCxFlow#advanced_settings}
        :param description: The description of the flow. The maximum length is 500 characters. If exceeded, the request is rejected. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#description GoogleDialogflowCxFlow#description}
        :param event_handlers: event_handlers block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#event_handlers GoogleDialogflowCxFlow#event_handlers}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#id GoogleDialogflowCxFlow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_default_start_flow: Marks this as the `Default Start Flow <https://cloud.google.com/dialogflow/cx/docs/concept/flow#start>`_ for an agent. When you create an agent, the Default Start Flow is created automatically. The Default Start Flow cannot be deleted; deleting the 'google_dialogflow_cx_flow' resource does nothing to the underlying GCP resources. ~> Avoid having multiple 'google_dialogflow_cx_flow' resources linked to the same agent with 'is_default_start_flow = true' because they will compete to control a single Default Start Flow resource in GCP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#is_default_start_flow GoogleDialogflowCxFlow#is_default_start_flow}
        :param language_code: The language of the following fields in flow: Flow.event_handlers.trigger_fulfillment.messages Flow.event_handlers.trigger_fulfillment.conditional_cases Flow.transition_routes.trigger_fulfillment.messages Flow.transition_routes.trigger_fulfillment.conditional_cases If not specified, the agent's default language is used. Many languages are supported. Note: languages must be enabled in the agent before they can be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#language_code GoogleDialogflowCxFlow#language_code}
        :param nlu_settings: nlu_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#nlu_settings GoogleDialogflowCxFlow#nlu_settings}
        :param parent: The agent to create a flow for. Format: projects//locations//agents/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#parent GoogleDialogflowCxFlow#parent}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#timeouts GoogleDialogflowCxFlow#timeouts}
        :param transition_route_groups: A flow's transition route group serve two purposes: They are responsible for matching the user's first utterances in the flow. They are inherited by every page's [transition route groups][Page.transition_route_groups]. Transition route groups defined in the page have higher priority than those defined in the flow. Format:projects//locations//agents//flows//transitionRouteGroups/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#transition_route_groups GoogleDialogflowCxFlow#transition_route_groups}
        :param transition_routes: transition_routes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#transition_routes GoogleDialogflowCxFlow#transition_routes}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(advanced_settings, dict):
            advanced_settings = GoogleDialogflowCxFlowAdvancedSettings(**advanced_settings)
        if isinstance(nlu_settings, dict):
            nlu_settings = GoogleDialogflowCxFlowNluSettings(**nlu_settings)
        if isinstance(timeouts, dict):
            timeouts = GoogleDialogflowCxFlowTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5b6d22821ccb6c1261edc07f6bc6656e98299156ae0eaee2da8542a3e22cb90)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument advanced_settings", value=advanced_settings, expected_type=type_hints["advanced_settings"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument event_handlers", value=event_handlers, expected_type=type_hints["event_handlers"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_default_start_flow", value=is_default_start_flow, expected_type=type_hints["is_default_start_flow"])
            check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
            check_type(argname="argument nlu_settings", value=nlu_settings, expected_type=type_hints["nlu_settings"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument transition_route_groups", value=transition_route_groups, expected_type=type_hints["transition_route_groups"])
            check_type(argname="argument transition_routes", value=transition_routes, expected_type=type_hints["transition_routes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
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
        if advanced_settings is not None:
            self._values["advanced_settings"] = advanced_settings
        if description is not None:
            self._values["description"] = description
        if event_handlers is not None:
            self._values["event_handlers"] = event_handlers
        if id is not None:
            self._values["id"] = id
        if is_default_start_flow is not None:
            self._values["is_default_start_flow"] = is_default_start_flow
        if language_code is not None:
            self._values["language_code"] = language_code
        if nlu_settings is not None:
            self._values["nlu_settings"] = nlu_settings
        if parent is not None:
            self._values["parent"] = parent
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if transition_route_groups is not None:
            self._values["transition_route_groups"] = transition_route_groups
        if transition_routes is not None:
            self._values["transition_routes"] = transition_routes

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
    def display_name(self) -> builtins.str:
        '''The human-readable name of the flow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#display_name GoogleDialogflowCxFlow#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def advanced_settings(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowAdvancedSettings]:
        '''advanced_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#advanced_settings GoogleDialogflowCxFlow#advanced_settings}
        '''
        result = self._values.get("advanced_settings")
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowAdvancedSettings], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the flow. The maximum length is 500 characters. If exceeded, the request is rejected.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#description GoogleDialogflowCxFlow#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_handlers(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowEventHandlers"]]]:
        '''event_handlers block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#event_handlers GoogleDialogflowCxFlow#event_handlers}
        '''
        result = self._values.get("event_handlers")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowEventHandlers"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#id GoogleDialogflowCxFlow#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_default_start_flow(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Marks this as the `Default Start Flow <https://cloud.google.com/dialogflow/cx/docs/concept/flow#start>`_ for an agent. When you create an agent, the Default Start Flow is created automatically. The Default Start Flow cannot be deleted; deleting the 'google_dialogflow_cx_flow' resource does nothing to the underlying GCP resources.

        ~> Avoid having multiple 'google_dialogflow_cx_flow' resources linked to the same agent with 'is_default_start_flow = true' because they will compete to control a single Default Start Flow resource in GCP.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#is_default_start_flow GoogleDialogflowCxFlow#is_default_start_flow}
        '''
        result = self._values.get("is_default_start_flow")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def language_code(self) -> typing.Optional[builtins.str]:
        '''The language of the following fields in flow: Flow.event_handlers.trigger_fulfillment.messages Flow.event_handlers.trigger_fulfillment.conditional_cases Flow.transition_routes.trigger_fulfillment.messages Flow.transition_routes.trigger_fulfillment.conditional_cases If not specified, the agent's default language is used. Many languages are supported. Note: languages must be enabled in the agent before they can be used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#language_code GoogleDialogflowCxFlow#language_code}
        '''
        result = self._values.get("language_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nlu_settings(self) -> typing.Optional["GoogleDialogflowCxFlowNluSettings"]:
        '''nlu_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#nlu_settings GoogleDialogflowCxFlow#nlu_settings}
        '''
        result = self._values.get("nlu_settings")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowNluSettings"], result)

    @builtins.property
    def parent(self) -> typing.Optional[builtins.str]:
        '''The agent to create a flow for. Format: projects//locations//agents/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#parent GoogleDialogflowCxFlow#parent}
        '''
        result = self._values.get("parent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDialogflowCxFlowTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#timeouts GoogleDialogflowCxFlow#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowTimeouts"], result)

    @builtins.property
    def transition_route_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A flow's transition route group serve two purposes: They are responsible for matching the user's first utterances in the flow.

        They are inherited by every page's [transition route groups][Page.transition_route_groups]. Transition route groups defined in the page have higher priority than those defined in the flow.
        Format:projects//locations//agents//flows//transitionRouteGroups/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#transition_route_groups GoogleDialogflowCxFlow#transition_route_groups}
        '''
        result = self._values.get("transition_route_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def transition_routes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowTransitionRoutes"]]]:
        '''transition_routes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#transition_routes GoogleDialogflowCxFlow#transition_routes}
        '''
        result = self._values.get("transition_routes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowTransitionRoutes"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlers",
    jsii_struct_bases=[],
    name_mapping={
        "event": "event",
        "target_flow": "targetFlow",
        "target_page": "targetPage",
        "trigger_fulfillment": "triggerFulfillment",
    },
)
class GoogleDialogflowCxFlowEventHandlers:
    def __init__(
        self,
        *,
        event: typing.Optional[builtins.str] = None,
        target_flow: typing.Optional[builtins.str] = None,
        target_page: typing.Optional[builtins.str] = None,
        trigger_fulfillment: typing.Optional[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillment", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param event: The name of the event to handle. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#event GoogleDialogflowCxFlow#event}
        :param target_flow: The target flow to transition to. Format: projects//locations//agents//flows/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#target_flow GoogleDialogflowCxFlow#target_flow}
        :param target_page: The target page to transition to. Format: projects//locations//agents//flows//pages/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#target_page GoogleDialogflowCxFlow#target_page}
        :param trigger_fulfillment: trigger_fulfillment block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#trigger_fulfillment GoogleDialogflowCxFlow#trigger_fulfillment}
        '''
        if isinstance(trigger_fulfillment, dict):
            trigger_fulfillment = GoogleDialogflowCxFlowEventHandlersTriggerFulfillment(**trigger_fulfillment)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98d6b437f59c96e369e9a65e8cba23f38e57df796929bbd75224bcedc388b721)
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
            check_type(argname="argument target_flow", value=target_flow, expected_type=type_hints["target_flow"])
            check_type(argname="argument target_page", value=target_page, expected_type=type_hints["target_page"])
            check_type(argname="argument trigger_fulfillment", value=trigger_fulfillment, expected_type=type_hints["trigger_fulfillment"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if event is not None:
            self._values["event"] = event
        if target_flow is not None:
            self._values["target_flow"] = target_flow
        if target_page is not None:
            self._values["target_page"] = target_page
        if trigger_fulfillment is not None:
            self._values["trigger_fulfillment"] = trigger_fulfillment

    @builtins.property
    def event(self) -> typing.Optional[builtins.str]:
        '''The name of the event to handle.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#event GoogleDialogflowCxFlow#event}
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_flow(self) -> typing.Optional[builtins.str]:
        '''The target flow to transition to. Format: projects//locations//agents//flows/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#target_flow GoogleDialogflowCxFlow#target_flow}
        '''
        result = self._values.get("target_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_page(self) -> typing.Optional[builtins.str]:
        '''The target page to transition to. Format: projects//locations//agents//flows//pages/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#target_page GoogleDialogflowCxFlow#target_page}
        '''
        result = self._values.get("target_page")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger_fulfillment(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillment"]:
        '''trigger_fulfillment block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#trigger_fulfillment GoogleDialogflowCxFlow#trigger_fulfillment}
        '''
        result = self._values.get("trigger_fulfillment")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowEventHandlers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowEventHandlersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ea6d2385130136ba9ba2449229da1e1d3e391e41dfafc4c8ca3bb1631d4ce14)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxFlowEventHandlersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b72692e2f83b58047d9ef491b2c6b8d6d65b1d0576f01c8e029ece54d7ca94a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxFlowEventHandlersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10e47925b00e47f983de73bfa202626a1e3135e199f22fe97d586dabb330c1f3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a87ff1ba2605882bab6a41459482a8d5ce15d04140c213017f7aa60d0f1f8cd4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__797650aaec31e7ca6bb8bc45d5cb90e35913ad807f256a34b97189d1d969d736)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlers]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__550686a1780bbee4f9f8564add05760636a98a28cf7e02f3c02b086103f5e3dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxFlowEventHandlersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0b49a2bf192f63cb5a72c1bd7cdffb07f5cdb45767d0977c9c0af70fe72a68a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTriggerFulfillment")
    def put_trigger_fulfillment(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases", typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#conditional_cases GoogleDialogflowCxFlow#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#messages GoogleDialogflowCxFlow#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#return_partial_responses GoogleDialogflowCxFlow#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#set_parameter_actions GoogleDialogflowCxFlow#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#tag GoogleDialogflowCxFlow#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#webhook GoogleDialogflowCxFlow#webhook}
        '''
        value = GoogleDialogflowCxFlowEventHandlersTriggerFulfillment(
            conditional_cases=conditional_cases,
            messages=messages,
            return_partial_responses=return_partial_responses,
            set_parameter_actions=set_parameter_actions,
            tag=tag,
            webhook=webhook,
        )

        return typing.cast(None, jsii.invoke(self, "putTriggerFulfillment", [value]))

    @jsii.member(jsii_name="resetEvent")
    def reset_event(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvent", []))

    @jsii.member(jsii_name="resetTargetFlow")
    def reset_target_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetFlow", []))

    @jsii.member(jsii_name="resetTargetPage")
    def reset_target_page(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetPage", []))

    @jsii.member(jsii_name="resetTriggerFulfillment")
    def reset_trigger_fulfillment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerFulfillment", []))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="triggerFulfillment")
    def trigger_fulfillment(
        self,
    ) -> "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentOutputReference":
        return typing.cast("GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentOutputReference", jsii.get(self, "triggerFulfillment"))

    @builtins.property
    @jsii.member(jsii_name="eventInput")
    def event_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventInput"))

    @builtins.property
    @jsii.member(jsii_name="targetFlowInput")
    def target_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetFlowInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPageInput")
    def target_page_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetPageInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerFulfillmentInput")
    def trigger_fulfillment_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillment"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillment"], jsii.get(self, "triggerFulfillmentInput"))

    @builtins.property
    @jsii.member(jsii_name="event")
    def event(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "event"))

    @event.setter
    def event(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65b6f23d473fdfa3616c5c573a6311ed0c64ca67237e5fc371844d19be8d4b06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "event", value)

    @builtins.property
    @jsii.member(jsii_name="targetFlow")
    def target_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetFlow"))

    @target_flow.setter
    def target_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8232a76d7dd21a85014f51ee2b25961374daa0e33aba5d27aed553abf55ee0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetFlow", value)

    @builtins.property
    @jsii.member(jsii_name="targetPage")
    def target_page(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPage"))

    @target_page.setter
    def target_page(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf6d60b11ea63adf1c7be2210f0b5cecc0c0346fad1ab06f7f78bd60d2f16a37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlers]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlers]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlers]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22b10706871c1d1f665ef2d90bd0d58a208650af42514f7be1dca25fb9f02432)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillment",
    jsii_struct_bases=[],
    name_mapping={
        "conditional_cases": "conditionalCases",
        "messages": "messages",
        "return_partial_responses": "returnPartialResponses",
        "set_parameter_actions": "setParameterActions",
        "tag": "tag",
        "webhook": "webhook",
    },
)
class GoogleDialogflowCxFlowEventHandlersTriggerFulfillment:
    def __init__(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases", typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#conditional_cases GoogleDialogflowCxFlow#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#messages GoogleDialogflowCxFlow#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#return_partial_responses GoogleDialogflowCxFlow#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#set_parameter_actions GoogleDialogflowCxFlow#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#tag GoogleDialogflowCxFlow#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#webhook GoogleDialogflowCxFlow#webhook}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2b0b5e0e8e08564eff12bc1e01fd9807cb7a628d58f0aa0ac775e881f69e3fe)
            check_type(argname="argument conditional_cases", value=conditional_cases, expected_type=type_hints["conditional_cases"])
            check_type(argname="argument messages", value=messages, expected_type=type_hints["messages"])
            check_type(argname="argument return_partial_responses", value=return_partial_responses, expected_type=type_hints["return_partial_responses"])
            check_type(argname="argument set_parameter_actions", value=set_parameter_actions, expected_type=type_hints["set_parameter_actions"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if conditional_cases is not None:
            self._values["conditional_cases"] = conditional_cases
        if messages is not None:
            self._values["messages"] = messages
        if return_partial_responses is not None:
            self._values["return_partial_responses"] = return_partial_responses
        if set_parameter_actions is not None:
            self._values["set_parameter_actions"] = set_parameter_actions
        if tag is not None:
            self._values["tag"] = tag
        if webhook is not None:
            self._values["webhook"] = webhook

    @builtins.property
    def conditional_cases(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases"]]]:
        '''conditional_cases block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#conditional_cases GoogleDialogflowCxFlow#conditional_cases}
        '''
        result = self._values.get("conditional_cases")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases"]]], result)

    @builtins.property
    def messages(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages"]]]:
        '''messages block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#messages GoogleDialogflowCxFlow#messages}
        '''
        result = self._values.get("messages")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages"]]], result)

    @builtins.property
    def return_partial_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs.

        If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#return_partial_responses GoogleDialogflowCxFlow#return_partial_responses}
        '''
        result = self._values.get("return_partial_responses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def set_parameter_actions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions"]]]:
        '''set_parameter_actions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#set_parameter_actions GoogleDialogflowCxFlow#set_parameter_actions}
        '''
        result = self._values.get("set_parameter_actions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions"]]], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The tag used by the webhook to identify which fulfillment is being called.

        This field is required if webhook is specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#tag GoogleDialogflowCxFlow#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook(self) -> typing.Optional[builtins.str]:
        '''The webhook to call. Format: projects//locations//agents//webhooks/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#webhook GoogleDialogflowCxFlow#webhook}
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowEventHandlersTriggerFulfillment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases",
    jsii_struct_bases=[],
    name_mapping={"cases": "cases"},
)
class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases:
    def __init__(self, *, cases: typing.Optional[builtins.str] = None) -> None:
        '''
        :param cases: A JSON encoded list of cascading if-else conditions. Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored. See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#cases GoogleDialogflowCxFlow#cases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c91d12edab2a2dbd0bf7747bb2162e7c5824f681ff0be9abf60fd5a33549bd1)
            check_type(argname="argument cases", value=cases, expected_type=type_hints["cases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cases is not None:
            self._values["cases"] = cases

    @builtins.property
    def cases(self) -> typing.Optional[builtins.str]:
        '''A JSON encoded list of cascading if-else conditions.

        Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored.
        See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#cases GoogleDialogflowCxFlow#cases}
        '''
        result = self._values.get("cases")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8dc297fa3b4deca51bde040af9d3d85d51244a4f502dc3dc2edfd6b442cd6cf3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5085cb33cee60f0351f3707232a96f794e06e88c9214ab90efd906fee9c0034)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ba859ff220cb9d944e616471ac511e557a5570ae65fcc73358ef0b6aee8b570)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e5d1ff8d188984b06b917cc566fa0b77d1abdc648bc70011da6ca2c1425ef353)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c046a332b2e188696b71b7ebb514bc26bebd1e040aebcd934005665a2890fc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaf545456d221be7117ea8e6a65ac1c3cc6ce3dc384d83d3d6f8aec0539adb64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d18f9237ed20e32840fe9794f3f02ec81890ca29521cd3ea20bff5398ba6515)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCases")
    def reset_cases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCases", []))

    @builtins.property
    @jsii.member(jsii_name="casesInput")
    def cases_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "casesInput"))

    @builtins.property
    @jsii.member(jsii_name="cases")
    def cases(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cases"))

    @cases.setter
    def cases(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6059d8a6d6d9cc3d499120d5011eeb5726168e3b30d8845649011bb6ea07f40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cases", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c97cb0f6e6865d8ec850b8cbeedc765de0021d6a630119f6ace7b60ba3f5d0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages",
    jsii_struct_bases=[],
    name_mapping={
        "channel": "channel",
        "conversation_success": "conversationSuccess",
        "live_agent_handoff": "liveAgentHandoff",
        "output_audio_text": "outputAudioText",
        "payload": "payload",
        "play_audio": "playAudio",
        "telephony_transfer_call": "telephonyTransferCall",
        "text": "text",
    },
)
class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages:
    def __init__(
        self,
        *,
        channel: typing.Optional[builtins.str] = None,
        conversation_success: typing.Optional[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess", typing.Dict[builtins.str, typing.Any]]] = None,
        live_agent_handoff: typing.Optional[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff", typing.Dict[builtins.str, typing.Any]]] = None,
        output_audio_text: typing.Optional[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText", typing.Dict[builtins.str, typing.Any]]] = None,
        payload: typing.Optional[builtins.str] = None,
        play_audio: typing.Optional[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio", typing.Dict[builtins.str, typing.Any]]] = None,
        telephony_transfer_call: typing.Optional[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall", typing.Dict[builtins.str, typing.Any]]] = None,
        text: typing.Optional[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param channel: The channel which the response is associated with. Clients can specify the channel via QueryParameters.channel, and only associated channel response will be returned. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#channel GoogleDialogflowCxFlow#channel}
        :param conversation_success: conversation_success block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#conversation_success GoogleDialogflowCxFlow#conversation_success}
        :param live_agent_handoff: live_agent_handoff block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#live_agent_handoff GoogleDialogflowCxFlow#live_agent_handoff}
        :param output_audio_text: output_audio_text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#output_audio_text GoogleDialogflowCxFlow#output_audio_text}
        :param payload: A custom, platform-specific payload. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#payload GoogleDialogflowCxFlow#payload}
        :param play_audio: play_audio block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#play_audio GoogleDialogflowCxFlow#play_audio}
        :param telephony_transfer_call: telephony_transfer_call block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#telephony_transfer_call GoogleDialogflowCxFlow#telephony_transfer_call}
        :param text: text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        if isinstance(conversation_success, dict):
            conversation_success = GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess(**conversation_success)
        if isinstance(live_agent_handoff, dict):
            live_agent_handoff = GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff(**live_agent_handoff)
        if isinstance(output_audio_text, dict):
            output_audio_text = GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText(**output_audio_text)
        if isinstance(play_audio, dict):
            play_audio = GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio(**play_audio)
        if isinstance(telephony_transfer_call, dict):
            telephony_transfer_call = GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall(**telephony_transfer_call)
        if isinstance(text, dict):
            text = GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText(**text)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47cf1b77ff3ec061bdddb90036c33368f3e5b8f584b5d70cb6c8d6c442148a4f)
            check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
            check_type(argname="argument conversation_success", value=conversation_success, expected_type=type_hints["conversation_success"])
            check_type(argname="argument live_agent_handoff", value=live_agent_handoff, expected_type=type_hints["live_agent_handoff"])
            check_type(argname="argument output_audio_text", value=output_audio_text, expected_type=type_hints["output_audio_text"])
            check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            check_type(argname="argument play_audio", value=play_audio, expected_type=type_hints["play_audio"])
            check_type(argname="argument telephony_transfer_call", value=telephony_transfer_call, expected_type=type_hints["telephony_transfer_call"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if channel is not None:
            self._values["channel"] = channel
        if conversation_success is not None:
            self._values["conversation_success"] = conversation_success
        if live_agent_handoff is not None:
            self._values["live_agent_handoff"] = live_agent_handoff
        if output_audio_text is not None:
            self._values["output_audio_text"] = output_audio_text
        if payload is not None:
            self._values["payload"] = payload
        if play_audio is not None:
            self._values["play_audio"] = play_audio
        if telephony_transfer_call is not None:
            self._values["telephony_transfer_call"] = telephony_transfer_call
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def channel(self) -> typing.Optional[builtins.str]:
        '''The channel which the response is associated with.

        Clients can specify the channel via QueryParameters.channel, and only associated channel response will be returned.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#channel GoogleDialogflowCxFlow#channel}
        '''
        result = self._values.get("channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conversation_success(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess"]:
        '''conversation_success block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#conversation_success GoogleDialogflowCxFlow#conversation_success}
        '''
        result = self._values.get("conversation_success")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess"], result)

    @builtins.property
    def live_agent_handoff(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff"]:
        '''live_agent_handoff block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#live_agent_handoff GoogleDialogflowCxFlow#live_agent_handoff}
        '''
        result = self._values.get("live_agent_handoff")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff"], result)

    @builtins.property
    def output_audio_text(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText"]:
        '''output_audio_text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#output_audio_text GoogleDialogflowCxFlow#output_audio_text}
        '''
        result = self._values.get("output_audio_text")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText"], result)

    @builtins.property
    def payload(self) -> typing.Optional[builtins.str]:
        '''A custom, platform-specific payload.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#payload GoogleDialogflowCxFlow#payload}
        '''
        result = self._values.get("payload")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def play_audio(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio"]:
        '''play_audio block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#play_audio GoogleDialogflowCxFlow#play_audio}
        '''
        result = self._values.get("play_audio")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio"], result)

    @builtins.property
    def telephony_transfer_call(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall"]:
        '''telephony_transfer_call block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#telephony_transfer_call GoogleDialogflowCxFlow#telephony_transfer_call}
        '''
        result = self._values.get("telephony_transfer_call")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall"], result)

    @builtins.property
    def text(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText"]:
        '''text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#metadata GoogleDialogflowCxFlow#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71ba2f39b3e982d1ed7e0151541fccd54bbba72eb06788d47077001ea900f65b)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#metadata GoogleDialogflowCxFlow#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__999db007c9c1915b58c71b617ffb2b51d98449f40e550093ac8de4804f4b8bab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80c92f6879994241f8be0374257b2000fb20537e65d4e70e623aacebb56b8da9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad2092c5876164f320659d6b4e0c9ee2959f15bfc8ab9c6240bed7c672aca6db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__91a30f242e5ea4183f4a388675dae2a39a85ebb559121c69b38971a70ae0259b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef209c5de032bddd5d5f68a59e2625324e8d419c75f45bb6c212f1afcdcf5337)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fb9eaee16e8332e5d899c05745620e138957c5e96c41b0be100922470cea560)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8df20db12f6bf4a2136b74d845969b82f6c72d29f3160edf5aaf3e9607405c84)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc59802a7434cb11ca69be912e59b031a4a61b4c64c7c3877cf2b86eedfb6dc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66fc6f716cf1db773623fff9494d38d2fd97eaa1964cbad881bf5cb7c48ed834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#metadata GoogleDialogflowCxFlow#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de157fcd6751d9db70e1e58531c48002ac6b8c5e271e1629c9cfe53f64074595)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#metadata GoogleDialogflowCxFlow#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2d9347e9d2f662db1ce7f21c8a413ffd0a12b9032e84ad52c72b13bb5a38b4c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6de09dd2cb920aec8c6fa2d52287a5fe3f6517d58922ee571408de959977b10e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17248d3513fcfd5a6bdcb22aa7baa4cc0a70cd192852dbe9123ed496586b7418)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText",
    jsii_struct_bases=[],
    name_mapping={"ssml": "ssml", "text": "text"},
)
class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText:
    def __init__(
        self,
        *,
        ssml: typing.Optional[builtins.str] = None,
        text: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#ssml GoogleDialogflowCxFlow#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cd4b98e2ab2e75f2d752a959a0b0e1ef2932096b760b53b77c60a04151f4085)
            check_type(argname="argument ssml", value=ssml, expected_type=type_hints["ssml"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ssml is not None:
            self._values["ssml"] = ssml
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def ssml(self) -> typing.Optional[builtins.str]:
        '''The SSML text to be synthesized. For more information, see SSML.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#ssml GoogleDialogflowCxFlow#ssml}
        '''
        result = self._values.get("ssml")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def text(self) -> typing.Optional[builtins.str]:
        '''The raw text to be synthesized.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__54f4bdf6f12fb261e41faa5a2b0f3246d66e76f40c88d4a533e2192eb312f928)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSsml")
    def reset_ssml(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsml", []))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "allowPlaybackInterruption"))

    @builtins.property
    @jsii.member(jsii_name="ssmlInput")
    def ssml_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ssmlInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="ssml")
    def ssml(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssml"))

    @ssml.setter
    def ssml(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d4b85156c1116cd26e4873b89c1a4966f7a568ab35aebf2d9be598cd25c2003)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssml", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aed58b632dd33e478da2b95a0c954d89c8684469ad93a8c05bf1fefb92334ef6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__407c042b8ffe7beb5fd352f1cc631efea66dd2870ba4c36b89578b5c469a4725)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a5d7394da129220d20cf2d3e9de1e4a8bc97cf36ff80f93157bd345d447f814)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putConversationSuccess")
    def put_conversation_success(
        self,
        *,
        metadata: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#metadata GoogleDialogflowCxFlow#metadata}
        '''
        value = GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess(
            metadata=metadata
        )

        return typing.cast(None, jsii.invoke(self, "putConversationSuccess", [value]))

    @jsii.member(jsii_name="putLiveAgentHandoff")
    def put_live_agent_handoff(
        self,
        *,
        metadata: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#metadata GoogleDialogflowCxFlow#metadata}
        '''
        value = GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff(
            metadata=metadata
        )

        return typing.cast(None, jsii.invoke(self, "putLiveAgentHandoff", [value]))

    @jsii.member(jsii_name="putOutputAudioText")
    def put_output_audio_text(
        self,
        *,
        ssml: typing.Optional[builtins.str] = None,
        text: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#ssml GoogleDialogflowCxFlow#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        value = GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText(
            ssml=ssml, text=text
        )

        return typing.cast(None, jsii.invoke(self, "putOutputAudioText", [value]))

    @jsii.member(jsii_name="putPlayAudio")
    def put_play_audio(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#audio_uri GoogleDialogflowCxFlow#audio_uri}
        '''
        value = GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio(
            audio_uri=audio_uri
        )

        return typing.cast(None, jsii.invoke(self, "putPlayAudio", [value]))

    @jsii.member(jsii_name="putTelephonyTransferCall")
    def put_telephony_transfer_call(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#phone_number GoogleDialogflowCxFlow#phone_number}
        '''
        value = GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall(
            phone_number=phone_number
        )

        return typing.cast(None, jsii.invoke(self, "putTelephonyTransferCall", [value]))

    @jsii.member(jsii_name="putText")
    def put_text(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        value = GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText(
            text=text
        )

        return typing.cast(None, jsii.invoke(self, "putText", [value]))

    @jsii.member(jsii_name="resetChannel")
    def reset_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannel", []))

    @jsii.member(jsii_name="resetConversationSuccess")
    def reset_conversation_success(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConversationSuccess", []))

    @jsii.member(jsii_name="resetLiveAgentHandoff")
    def reset_live_agent_handoff(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLiveAgentHandoff", []))

    @jsii.member(jsii_name="resetOutputAudioText")
    def reset_output_audio_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputAudioText", []))

    @jsii.member(jsii_name="resetPayload")
    def reset_payload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPayload", []))

    @jsii.member(jsii_name="resetPlayAudio")
    def reset_play_audio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlayAudio", []))

    @jsii.member(jsii_name="resetTelephonyTransferCall")
    def reset_telephony_transfer_call(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTelephonyTransferCall", []))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="conversationSuccess")
    def conversation_success(
        self,
    ) -> GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference:
        return typing.cast(GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference, jsii.get(self, "conversationSuccess"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference:
        return typing.cast(GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference, jsii.get(self, "liveAgentHandoff"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioText")
    def output_audio_text(
        self,
    ) -> GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference:
        return typing.cast(GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference, jsii.get(self, "outputAudioText"))

    @builtins.property
    @jsii.member(jsii_name="playAudio")
    def play_audio(
        self,
    ) -> "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference":
        return typing.cast("GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference", jsii.get(self, "playAudio"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference":
        return typing.cast("GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference", jsii.get(self, "telephonyTransferCall"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(
        self,
    ) -> "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTextOutputReference":
        return typing.cast("GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTextOutputReference", jsii.get(self, "text"))

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="conversationSuccessInput")
    def conversation_success_input(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess], jsii.get(self, "conversationSuccessInput"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoffInput")
    def live_agent_handoff_input(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "liveAgentHandoffInput"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioTextInput")
    def output_audio_text_input(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText], jsii.get(self, "outputAudioTextInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadInput")
    def payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadInput"))

    @builtins.property
    @jsii.member(jsii_name="playAudioInput")
    def play_audio_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio"], jsii.get(self, "playAudioInput"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCallInput")
    def telephony_transfer_call_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall"], jsii.get(self, "telephonyTransferCallInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText"], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channel"))

    @channel.setter
    def channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ee365bd5e7ad02443edec08b36d422ebd6ba0925fb54f56b43c0d0b5b6e08f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="payload")
    def payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payload"))

    @payload.setter
    def payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2cd3500edffc79de60595b43ccb8b511bac26f94034afd27658ce0f1dbb34d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payload", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b33fd52d5aee1abc2af7510c2d810adabcf29a9323ff8a75fac9e0e5a9b3d8e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio",
    jsii_struct_bases=[],
    name_mapping={"audio_uri": "audioUri"},
)
class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio:
    def __init__(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#audio_uri GoogleDialogflowCxFlow#audio_uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efa71b0a2ce84c87ecd1d7c824a1b3d735c9cf5482efb3d60fc9b5a4a0486262)
            check_type(argname="argument audio_uri", value=audio_uri, expected_type=type_hints["audio_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "audio_uri": audio_uri,
        }

    @builtins.property
    def audio_uri(self) -> builtins.str:
        '''URI of the audio clip.

        Dialogflow does not impose any validation on this value. It is specific to the client that reads it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#audio_uri GoogleDialogflowCxFlow#audio_uri}
        '''
        result = self._values.get("audio_uri")
        assert result is not None, "Required property 'audio_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ecc3fe6bb8b710da9ac63e4d0055e56679e0eebb090c310213eff1a90119e934)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "allowPlaybackInterruption"))

    @builtins.property
    @jsii.member(jsii_name="audioUriInput")
    def audio_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "audioUriInput"))

    @builtins.property
    @jsii.member(jsii_name="audioUri")
    def audio_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audioUri"))

    @audio_uri.setter
    def audio_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e7dc243844b4f75b91211ae2d27b9887c7baa9733bc9bdbed88745218e44d94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11fdc1ebecce9edee0dd805324d6cf8aee3e2b30bd7204e4a9f3d3dbbe9424e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall",
    jsii_struct_bases=[],
    name_mapping={"phone_number": "phoneNumber"},
)
class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall:
    def __init__(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#phone_number GoogleDialogflowCxFlow#phone_number}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e89b70a63040a97046353aa145e0c5def89f523a28e0e3192d56cb96c46a58d1)
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "phone_number": phone_number,
        }

    @builtins.property
    def phone_number(self) -> builtins.str:
        '''Transfer the call to a phone number in E.164 format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#phone_number GoogleDialogflowCxFlow#phone_number}
        '''
        result = self._values.get("phone_number")
        assert result is not None, "Required property 'phone_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d1e51f50aa052e9299e27e0ff1c13913459e9ec3fb03cdd73bb574e8248a106)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="phoneNumberInput")
    def phone_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneNumber")
    def phone_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phoneNumber"))

    @phone_number.setter
    def phone_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54701318c05c962d1797c39a43227a0a786172c08ece78e448a8f61fcc24f506)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc6365e33a446197ecc983cc3b6027917a4bd3902601a9e02ecc1c5923b39d43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caf968656644d2b99fc0f819ca3a16b23f096995475b7b3a6e08e5c1c1358318)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A collection of text responses.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c4ec1e46f38dd2a469bcfc5e0b204a6b11595e08e119b7981575105910d8c78d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "allowPlaybackInterruption"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "text"))

    @text.setter
    def text(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__037aec295bb472f589ea596cbfebb45456ce81962af528f351d6b6e616e3b242)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__479b59249a9dfb3608d4dc0fed24b0337e07fe844e83827b6f943b301566db71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3bad15ed6b01e2d0546b46b152ea04c1371cb3c7d4324e188ef4e47b66fade90)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConditionalCases")
    def put_conditional_cases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__819a5d95220721c41d98998c537993544cc544bb52e5607faed5c09e1193c8a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConditionalCases", [value]))

    @jsii.member(jsii_name="putMessages")
    def put_messages(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42f5acfd4c64d5ac63b8f15f48c10d2fd9d8bc9b56ae86ee6bab6d18e6328278)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessages", [value]))

    @jsii.member(jsii_name="putSetParameterActions")
    def put_set_parameter_actions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__760234eadd3578b5586974b36f2ac0369361d386d0d7c7e1288fef584b33164c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSetParameterActions", [value]))

    @jsii.member(jsii_name="resetConditionalCases")
    def reset_conditional_cases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionalCases", []))

    @jsii.member(jsii_name="resetMessages")
    def reset_messages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessages", []))

    @jsii.member(jsii_name="resetReturnPartialResponses")
    def reset_return_partial_responses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnPartialResponses", []))

    @jsii.member(jsii_name="resetSetParameterActions")
    def reset_set_parameter_actions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSetParameterActions", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetWebhook")
    def reset_webhook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhook", []))

    @builtins.property
    @jsii.member(jsii_name="conditionalCases")
    def conditional_cases(
        self,
    ) -> GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCasesList:
        return typing.cast(GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCasesList, jsii.get(self, "conditionalCases"))

    @builtins.property
    @jsii.member(jsii_name="messages")
    def messages(
        self,
    ) -> GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesList:
        return typing.cast(GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesList, jsii.get(self, "messages"))

    @builtins.property
    @jsii.member(jsii_name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActionsList":
        return typing.cast("GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActionsList", jsii.get(self, "setParameterActions"))

    @builtins.property
    @jsii.member(jsii_name="conditionalCasesInput")
    def conditional_cases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases]]], jsii.get(self, "conditionalCasesInput"))

    @builtins.property
    @jsii.member(jsii_name="messagesInput")
    def messages_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages]]], jsii.get(self, "messagesInput"))

    @builtins.property
    @jsii.member(jsii_name="returnPartialResponsesInput")
    def return_partial_responses_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "returnPartialResponsesInput"))

    @builtins.property
    @jsii.member(jsii_name="setParameterActionsInput")
    def set_parameter_actions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions"]]], jsii.get(self, "setParameterActionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookInput")
    def webhook_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webhookInput"))

    @builtins.property
    @jsii.member(jsii_name="returnPartialResponses")
    def return_partial_responses(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "returnPartialResponses"))

    @return_partial_responses.setter
    def return_partial_responses(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b357e6f9c60440207ddaad42c083f61899fd2ca2bcace2737949eb6ea6851467)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnPartialResponses", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05e50fe901dbf61aa635a56e265013a777da162a618815e4ec01998dc21f697c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhook"))

    @webhook.setter
    def webhook(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91bf4cce913b48aa52137ae8d78dc55d18dccf652b6d505fed4dc622a5a91a55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhook", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillment]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3744515a4e7ffc4c34a960ba8fd725e26afa66704674a5e14177efa17342c58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions",
    jsii_struct_bases=[],
    name_mapping={"parameter": "parameter", "value": "value"},
)
class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions:
    def __init__(
        self,
        *,
        parameter: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param parameter: Display name of the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#parameter GoogleDialogflowCxFlow#parameter}
        :param value: The new JSON-encoded value of the parameter. A null value clears the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#value GoogleDialogflowCxFlow#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93c78aaa9dc78e546841f3429b21f134fd3cdfc47dbb4d8f2861327ff41bba56)
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameter is not None:
            self._values["parameter"] = parameter
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def parameter(self) -> typing.Optional[builtins.str]:
        '''Display name of the parameter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#parameter GoogleDialogflowCxFlow#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The new JSON-encoded value of the parameter. A null value clears the parameter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#value GoogleDialogflowCxFlow#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9baca73387f09f5353e93c5f8700bc045106f221b0359c2d131fbe7055705769)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c9ad8bc904ef45fbdb508b5a50c2dfc3a1b4e647fee04655b5392a8520e079e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c541f89743bc296f16f4c020a2a70c5dc373b7354aa36161ab1482de47aeb6fe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b3a0503fe09a702f31a139eb8a7dfb556ff06b6c53476a4294840f14b231b11c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6cf7ea8214c4ca0a99eee21e0cf65fee0b65d6581d592e2d3d31b0952b82d5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c918962fb69ac22fe5c492c71097cef5730be8d3a6fdd704d0a953706262f01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e849e95ac9146804ad1cc766b09fdac80cb113b5fc45e4da4325aecd79c3bb9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameter"))

    @parameter.setter
    def parameter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee39d77d0d3a755ced9500b7843b711e233e1f5458838cf3e5f254227d056d77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameter", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__645180431c81e6015f9b747ca228f3de8abb61a09f9c6aaca262bc6f8bdfe421)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__404abb45a68419b24509e89c3c666e1384d97c4fb58a267936d63a46cd84b790)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowNluSettings",
    jsii_struct_bases=[],
    name_mapping={
        "classification_threshold": "classificationThreshold",
        "model_training_mode": "modelTrainingMode",
        "model_type": "modelType",
    },
)
class GoogleDialogflowCxFlowNluSettings:
    def __init__(
        self,
        *,
        classification_threshold: typing.Optional[jsii.Number] = None,
        model_training_mode: typing.Optional[builtins.str] = None,
        model_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param classification_threshold: To filter out false positive results and still get variety in matched natural language inputs for your agent, you can tune the machine learning classification threshold. If the returned score value is less than the threshold value, then a no-match event will be triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the default of 0.3 is used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#classification_threshold GoogleDialogflowCxFlow#classification_threshold}
        :param model_training_mode: Indicates NLU model training mode. - MODEL_TRAINING_MODE_AUTOMATIC: NLU model training is automatically triggered when a flow gets modified. User can also manually trigger model training in this mode. - MODEL_TRAINING_MODE_MANUAL: User needs to manually trigger NLU model training. Best for large flows whose models take long time to train. Possible values: ["MODEL_TRAINING_MODE_AUTOMATIC", "MODEL_TRAINING_MODE_MANUAL"] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#model_training_mode GoogleDialogflowCxFlow#model_training_mode}
        :param model_type: Indicates the type of NLU model. - MODEL_TYPE_STANDARD: Use standard NLU model. - MODEL_TYPE_ADVANCED: Use advanced NLU model. Possible values: ["MODEL_TYPE_STANDARD", "MODEL_TYPE_ADVANCED"] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#model_type GoogleDialogflowCxFlow#model_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e11d2415d17184287951f07c3c59b5989b582c6777731b857475cbefa2994ab9)
            check_type(argname="argument classification_threshold", value=classification_threshold, expected_type=type_hints["classification_threshold"])
            check_type(argname="argument model_training_mode", value=model_training_mode, expected_type=type_hints["model_training_mode"])
            check_type(argname="argument model_type", value=model_type, expected_type=type_hints["model_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if classification_threshold is not None:
            self._values["classification_threshold"] = classification_threshold
        if model_training_mode is not None:
            self._values["model_training_mode"] = model_training_mode
        if model_type is not None:
            self._values["model_type"] = model_type

    @builtins.property
    def classification_threshold(self) -> typing.Optional[jsii.Number]:
        '''To filter out false positive results and still get variety in matched natural language inputs for your agent, you can tune the machine learning classification threshold.

        If the returned score value is less than the threshold value, then a no-match event will be triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the default of 0.3 is used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#classification_threshold GoogleDialogflowCxFlow#classification_threshold}
        '''
        result = self._values.get("classification_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def model_training_mode(self) -> typing.Optional[builtins.str]:
        '''Indicates NLU model training mode.

        - MODEL_TRAINING_MODE_AUTOMATIC: NLU model training is automatically triggered when a flow gets modified. User can also manually trigger model training in this mode.
        - MODEL_TRAINING_MODE_MANUAL: User needs to manually trigger NLU model training. Best for large flows whose models take long time to train. Possible values: ["MODEL_TRAINING_MODE_AUTOMATIC", "MODEL_TRAINING_MODE_MANUAL"]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#model_training_mode GoogleDialogflowCxFlow#model_training_mode}
        '''
        result = self._values.get("model_training_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_type(self) -> typing.Optional[builtins.str]:
        '''Indicates the type of NLU model.

        - MODEL_TYPE_STANDARD: Use standard NLU model.
        - MODEL_TYPE_ADVANCED: Use advanced NLU model. Possible values: ["MODEL_TYPE_STANDARD", "MODEL_TYPE_ADVANCED"]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#model_type GoogleDialogflowCxFlow#model_type}
        '''
        result = self._values.get("model_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowNluSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowNluSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowNluSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__98d9f3909bba7513ded942dd49ab4eff31602cdb034f4a4e1475a92d9195e3cd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClassificationThreshold")
    def reset_classification_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClassificationThreshold", []))

    @jsii.member(jsii_name="resetModelTrainingMode")
    def reset_model_training_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModelTrainingMode", []))

    @jsii.member(jsii_name="resetModelType")
    def reset_model_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModelType", []))

    @builtins.property
    @jsii.member(jsii_name="classificationThresholdInput")
    def classification_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "classificationThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="modelTrainingModeInput")
    def model_training_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelTrainingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="modelTypeInput")
    def model_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="classificationThreshold")
    def classification_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "classificationThreshold"))

    @classification_threshold.setter
    def classification_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45305366a1d242576564cf317b03d1a334294e16921345b493918e93aecceff7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classificationThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="modelTrainingMode")
    def model_training_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modelTrainingMode"))

    @model_training_mode.setter
    def model_training_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__536cbd1264bd06bfdfe3cee75d9622418afef8311158512d4f56b6ab9158e3f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelTrainingMode", value)

    @builtins.property
    @jsii.member(jsii_name="modelType")
    def model_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modelType"))

    @model_type.setter
    def model_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbe96da0683e88b188041d7de4c92fed18d30c2e19f30792d01ac81a7e8fc06f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDialogflowCxFlowNluSettings]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowNluSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowNluSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__524f25a80f58940c6773cd38d1d4a7c6ddb98c11023b57dd08686d71d4bec644)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDialogflowCxFlowTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#create GoogleDialogflowCxFlow#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#delete GoogleDialogflowCxFlow#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#update GoogleDialogflowCxFlow#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0210a03cea17a8ef6bb6c8d12573cd1b0d7140688721c228c725071420680dd6)
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
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#create GoogleDialogflowCxFlow#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#delete GoogleDialogflowCxFlow#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#update GoogleDialogflowCxFlow#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a0e68db04b76164173d2591ddd75bb1b9b052a340e3f358976041e891232cfc2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c8fa4d3bd2d4d417cd91617f1a451745bf4aaf04d58d7966be4fba2c6597fe3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d5975630e9faa60ef9b199ec40a0b2873f5df8a921e7f852dabdc8a78073309)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e778f648906def1b0b98d5164ec361e201a715e15a0d72467b7788a670fc5c4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86c6d5b814a990c8b13a0674f1e520f123196a9fc67d10ff966cfed6d664ab5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutes",
    jsii_struct_bases=[],
    name_mapping={
        "condition": "condition",
        "intent": "intent",
        "target_flow": "targetFlow",
        "target_page": "targetPage",
        "trigger_fulfillment": "triggerFulfillment",
    },
)
class GoogleDialogflowCxFlowTransitionRoutes:
    def __init__(
        self,
        *,
        condition: typing.Optional[builtins.str] = None,
        intent: typing.Optional[builtins.str] = None,
        target_flow: typing.Optional[builtins.str] = None,
        target_page: typing.Optional[builtins.str] = None,
        trigger_fulfillment: typing.Optional[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition: The condition to evaluate against form parameters or session parameters. At least one of intent or condition must be specified. When both intent and condition are specified, the transition can only happen when both are fulfilled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#condition GoogleDialogflowCxFlow#condition}
        :param intent: The unique identifier of an Intent. Format: projects//locations//agents//intents/. Indicates that the transition can only happen when the given intent is matched. At least one of intent or condition must be specified. When both intent and condition are specified, the transition can only happen when both are fulfilled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#intent GoogleDialogflowCxFlow#intent}
        :param target_flow: The target flow to transition to. Format: projects//locations//agents//flows/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#target_flow GoogleDialogflowCxFlow#target_flow}
        :param target_page: The target page to transition to. Format: projects//locations//agents//flows//pages/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#target_page GoogleDialogflowCxFlow#target_page}
        :param trigger_fulfillment: trigger_fulfillment block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#trigger_fulfillment GoogleDialogflowCxFlow#trigger_fulfillment}
        '''
        if isinstance(trigger_fulfillment, dict):
            trigger_fulfillment = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment(**trigger_fulfillment)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d1a18960d79eb590c9d5bf3e090bd2e010515560266b7c63ff53264e0f013b1)
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument intent", value=intent, expected_type=type_hints["intent"])
            check_type(argname="argument target_flow", value=target_flow, expected_type=type_hints["target_flow"])
            check_type(argname="argument target_page", value=target_page, expected_type=type_hints["target_page"])
            check_type(argname="argument trigger_fulfillment", value=trigger_fulfillment, expected_type=type_hints["trigger_fulfillment"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if condition is not None:
            self._values["condition"] = condition
        if intent is not None:
            self._values["intent"] = intent
        if target_flow is not None:
            self._values["target_flow"] = target_flow
        if target_page is not None:
            self._values["target_page"] = target_page
        if trigger_fulfillment is not None:
            self._values["trigger_fulfillment"] = trigger_fulfillment

    @builtins.property
    def condition(self) -> typing.Optional[builtins.str]:
        '''The condition to evaluate against form parameters or session parameters.

        At least one of intent or condition must be specified. When both intent and condition are specified, the transition can only happen when both are fulfilled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#condition GoogleDialogflowCxFlow#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def intent(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an Intent.

        Format: projects//locations//agents//intents/. Indicates that the transition can only happen when the given intent is matched. At least one of intent or condition must be specified. When both intent and condition are specified, the transition can only happen when both are fulfilled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#intent GoogleDialogflowCxFlow#intent}
        '''
        result = self._values.get("intent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_flow(self) -> typing.Optional[builtins.str]:
        '''The target flow to transition to. Format: projects//locations//agents//flows/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#target_flow GoogleDialogflowCxFlow#target_flow}
        '''
        result = self._values.get("target_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_page(self) -> typing.Optional[builtins.str]:
        '''The target page to transition to. Format: projects//locations//agents//flows//pages/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#target_page GoogleDialogflowCxFlow#target_page}
        '''
        result = self._values.get("target_page")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger_fulfillment(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment"]:
        '''trigger_fulfillment block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#trigger_fulfillment GoogleDialogflowCxFlow#trigger_fulfillment}
        '''
        result = self._values.get("trigger_fulfillment")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowTransitionRoutes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowTransitionRoutesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c658a26b791ed47c005526f0d203bf77af0ce5f404c11ebc43fd87ecac58b40b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxFlowTransitionRoutesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3785a2a26b46925c4961926dbf735621325bd370269361e64e4cae714adf64c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxFlowTransitionRoutesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72390c857e2ae72ecbbe1a54bb412b4ff281d146112ca0926eef1c03e9ab9c40)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bef78f412e276f63bb4c9db73a3c134a65b4d12146688888d6a4695ad3ac274b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__be10637d5d8fa7172423bd8f96a2561a939265c1e9b1d560cbb735def4faa7a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4831c1a17de10c1ab5840826b85ccb8471666de0b3bafe39b6002b027cc2f31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxFlowTransitionRoutesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__48ac555298c8903d2371e18de384242e6abe071a26c75bfecc87cdb684fc1f5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTriggerFulfillment")
    def put_trigger_fulfillment(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases", typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#conditional_cases GoogleDialogflowCxFlow#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#messages GoogleDialogflowCxFlow#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#return_partial_responses GoogleDialogflowCxFlow#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#set_parameter_actions GoogleDialogflowCxFlow#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#tag GoogleDialogflowCxFlow#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#webhook GoogleDialogflowCxFlow#webhook}
        '''
        value = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment(
            conditional_cases=conditional_cases,
            messages=messages,
            return_partial_responses=return_partial_responses,
            set_parameter_actions=set_parameter_actions,
            tag=tag,
            webhook=webhook,
        )

        return typing.cast(None, jsii.invoke(self, "putTriggerFulfillment", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetIntent")
    def reset_intent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntent", []))

    @jsii.member(jsii_name="resetTargetFlow")
    def reset_target_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetFlow", []))

    @jsii.member(jsii_name="resetTargetPage")
    def reset_target_page(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetPage", []))

    @jsii.member(jsii_name="resetTriggerFulfillment")
    def reset_trigger_fulfillment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerFulfillment", []))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="triggerFulfillment")
    def trigger_fulfillment(
        self,
    ) -> "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentOutputReference":
        return typing.cast("GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentOutputReference", jsii.get(self, "triggerFulfillment"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="intentInput")
    def intent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intentInput"))

    @builtins.property
    @jsii.member(jsii_name="targetFlowInput")
    def target_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetFlowInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPageInput")
    def target_page_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetPageInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerFulfillmentInput")
    def trigger_fulfillment_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment"], jsii.get(self, "triggerFulfillmentInput"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "condition"))

    @condition.setter
    def condition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76e46873b24a3efeb8ec6f6a61f81217f1e21900852c2da220810827b27be97d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "condition", value)

    @builtins.property
    @jsii.member(jsii_name="intent")
    def intent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intent"))

    @intent.setter
    def intent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7bbd5463bb362fe073852100eb5bc655db95f2128105531a3af0073f278523b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intent", value)

    @builtins.property
    @jsii.member(jsii_name="targetFlow")
    def target_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetFlow"))

    @target_flow.setter
    def target_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76d249e51248c27f926d6d592e9b4877379d8f9d5c09d9cc691e3dc24dab1974)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetFlow", value)

    @builtins.property
    @jsii.member(jsii_name="targetPage")
    def target_page(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPage"))

    @target_page.setter
    def target_page(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ec782606f320f8dceb8e53942677095abfe92dc2acf5f176bf57abeb0a5f8ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutes]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutes]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutes]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c71428de0494ae2981349f4c2a95e9ba77bf5b1e6a1b3ec8c23594a99918944a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment",
    jsii_struct_bases=[],
    name_mapping={
        "conditional_cases": "conditionalCases",
        "messages": "messages",
        "return_partial_responses": "returnPartialResponses",
        "set_parameter_actions": "setParameterActions",
        "tag": "tag",
        "webhook": "webhook",
    },
)
class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment:
    def __init__(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases", typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#conditional_cases GoogleDialogflowCxFlow#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#messages GoogleDialogflowCxFlow#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#return_partial_responses GoogleDialogflowCxFlow#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#set_parameter_actions GoogleDialogflowCxFlow#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#tag GoogleDialogflowCxFlow#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#webhook GoogleDialogflowCxFlow#webhook}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__944315f63373bd1968029dfa9b00946a674228d84fcc82289742d14c69a9a569)
            check_type(argname="argument conditional_cases", value=conditional_cases, expected_type=type_hints["conditional_cases"])
            check_type(argname="argument messages", value=messages, expected_type=type_hints["messages"])
            check_type(argname="argument return_partial_responses", value=return_partial_responses, expected_type=type_hints["return_partial_responses"])
            check_type(argname="argument set_parameter_actions", value=set_parameter_actions, expected_type=type_hints["set_parameter_actions"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if conditional_cases is not None:
            self._values["conditional_cases"] = conditional_cases
        if messages is not None:
            self._values["messages"] = messages
        if return_partial_responses is not None:
            self._values["return_partial_responses"] = return_partial_responses
        if set_parameter_actions is not None:
            self._values["set_parameter_actions"] = set_parameter_actions
        if tag is not None:
            self._values["tag"] = tag
        if webhook is not None:
            self._values["webhook"] = webhook

    @builtins.property
    def conditional_cases(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases"]]]:
        '''conditional_cases block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#conditional_cases GoogleDialogflowCxFlow#conditional_cases}
        '''
        result = self._values.get("conditional_cases")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases"]]], result)

    @builtins.property
    def messages(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages"]]]:
        '''messages block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#messages GoogleDialogflowCxFlow#messages}
        '''
        result = self._values.get("messages")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages"]]], result)

    @builtins.property
    def return_partial_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs.

        If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#return_partial_responses GoogleDialogflowCxFlow#return_partial_responses}
        '''
        result = self._values.get("return_partial_responses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def set_parameter_actions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions"]]]:
        '''set_parameter_actions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#set_parameter_actions GoogleDialogflowCxFlow#set_parameter_actions}
        '''
        result = self._values.get("set_parameter_actions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions"]]], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The tag used by the webhook to identify which fulfillment is being called.

        This field is required if webhook is specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#tag GoogleDialogflowCxFlow#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook(self) -> typing.Optional[builtins.str]:
        '''The webhook to call. Format: projects//locations//agents//webhooks/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#webhook GoogleDialogflowCxFlow#webhook}
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases",
    jsii_struct_bases=[],
    name_mapping={"cases": "cases"},
)
class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases:
    def __init__(self, *, cases: typing.Optional[builtins.str] = None) -> None:
        '''
        :param cases: A JSON encoded list of cascading if-else conditions. Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored. See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#cases GoogleDialogflowCxFlow#cases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__073564628f5e4b1c595d0ca2ef50b8c8b21b6fcd3d9829ed222747ee2033d788)
            check_type(argname="argument cases", value=cases, expected_type=type_hints["cases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cases is not None:
            self._values["cases"] = cases

    @builtins.property
    def cases(self) -> typing.Optional[builtins.str]:
        '''A JSON encoded list of cascading if-else conditions.

        Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored.
        See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#cases GoogleDialogflowCxFlow#cases}
        '''
        result = self._values.get("cases")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dccd900a9d9cd7c15f9a0c287a2f99de34596f9a2f5812f158211134371b883f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d64b4fa477655ece9114be172123489468135e33629d889949ef5b326669db33)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11e9aac43e2eaf7698d6c27ae81848e22e314ec08d9dc72e608142031ca45f04)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc763207d105bcd2b733520647fced1e0d09ea742305106dcf6f6d380450b38a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce5f923d4c327212d62c992838d955b10993908e731036936ae74e3e27b5d7ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b94ce98d4da9e0fb393f8633e49995caf36570b625f581b6bc2c1c719a1e6000)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__84305fb27b217397ad3c42dba23ed2b0f210bab4cbe3d6933666a8a28542afa3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCases")
    def reset_cases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCases", []))

    @builtins.property
    @jsii.member(jsii_name="casesInput")
    def cases_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "casesInput"))

    @builtins.property
    @jsii.member(jsii_name="cases")
    def cases(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cases"))

    @cases.setter
    def cases(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f43465b9e291c5c5b7730cac16168be734ee87b24422e2c0956f46ae12735ef6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cases", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69319f6b9393fa10bdaed0904605aae7b5596401b7f85dbab7ab898f27bedee3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages",
    jsii_struct_bases=[],
    name_mapping={
        "channel": "channel",
        "conversation_success": "conversationSuccess",
        "live_agent_handoff": "liveAgentHandoff",
        "output_audio_text": "outputAudioText",
        "payload": "payload",
        "play_audio": "playAudio",
        "telephony_transfer_call": "telephonyTransferCall",
        "text": "text",
    },
)
class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages:
    def __init__(
        self,
        *,
        channel: typing.Optional[builtins.str] = None,
        conversation_success: typing.Optional[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess", typing.Dict[builtins.str, typing.Any]]] = None,
        live_agent_handoff: typing.Optional[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff", typing.Dict[builtins.str, typing.Any]]] = None,
        output_audio_text: typing.Optional[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText", typing.Dict[builtins.str, typing.Any]]] = None,
        payload: typing.Optional[builtins.str] = None,
        play_audio: typing.Optional[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio", typing.Dict[builtins.str, typing.Any]]] = None,
        telephony_transfer_call: typing.Optional[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall", typing.Dict[builtins.str, typing.Any]]] = None,
        text: typing.Optional[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param channel: The channel which the response is associated with. Clients can specify the channel via QueryParameters.channel, and only associated channel response will be returned. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#channel GoogleDialogflowCxFlow#channel}
        :param conversation_success: conversation_success block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#conversation_success GoogleDialogflowCxFlow#conversation_success}
        :param live_agent_handoff: live_agent_handoff block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#live_agent_handoff GoogleDialogflowCxFlow#live_agent_handoff}
        :param output_audio_text: output_audio_text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#output_audio_text GoogleDialogflowCxFlow#output_audio_text}
        :param payload: A custom, platform-specific payload. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#payload GoogleDialogflowCxFlow#payload}
        :param play_audio: play_audio block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#play_audio GoogleDialogflowCxFlow#play_audio}
        :param telephony_transfer_call: telephony_transfer_call block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#telephony_transfer_call GoogleDialogflowCxFlow#telephony_transfer_call}
        :param text: text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        if isinstance(conversation_success, dict):
            conversation_success = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess(**conversation_success)
        if isinstance(live_agent_handoff, dict):
            live_agent_handoff = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff(**live_agent_handoff)
        if isinstance(output_audio_text, dict):
            output_audio_text = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText(**output_audio_text)
        if isinstance(play_audio, dict):
            play_audio = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio(**play_audio)
        if isinstance(telephony_transfer_call, dict):
            telephony_transfer_call = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall(**telephony_transfer_call)
        if isinstance(text, dict):
            text = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText(**text)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65436ee4b59d66753768513811493c2a9d9e47b34fd247b3f479f85953b0e120)
            check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
            check_type(argname="argument conversation_success", value=conversation_success, expected_type=type_hints["conversation_success"])
            check_type(argname="argument live_agent_handoff", value=live_agent_handoff, expected_type=type_hints["live_agent_handoff"])
            check_type(argname="argument output_audio_text", value=output_audio_text, expected_type=type_hints["output_audio_text"])
            check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            check_type(argname="argument play_audio", value=play_audio, expected_type=type_hints["play_audio"])
            check_type(argname="argument telephony_transfer_call", value=telephony_transfer_call, expected_type=type_hints["telephony_transfer_call"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if channel is not None:
            self._values["channel"] = channel
        if conversation_success is not None:
            self._values["conversation_success"] = conversation_success
        if live_agent_handoff is not None:
            self._values["live_agent_handoff"] = live_agent_handoff
        if output_audio_text is not None:
            self._values["output_audio_text"] = output_audio_text
        if payload is not None:
            self._values["payload"] = payload
        if play_audio is not None:
            self._values["play_audio"] = play_audio
        if telephony_transfer_call is not None:
            self._values["telephony_transfer_call"] = telephony_transfer_call
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def channel(self) -> typing.Optional[builtins.str]:
        '''The channel which the response is associated with.

        Clients can specify the channel via QueryParameters.channel, and only associated channel response will be returned.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#channel GoogleDialogflowCxFlow#channel}
        '''
        result = self._values.get("channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conversation_success(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess"]:
        '''conversation_success block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#conversation_success GoogleDialogflowCxFlow#conversation_success}
        '''
        result = self._values.get("conversation_success")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess"], result)

    @builtins.property
    def live_agent_handoff(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff"]:
        '''live_agent_handoff block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#live_agent_handoff GoogleDialogflowCxFlow#live_agent_handoff}
        '''
        result = self._values.get("live_agent_handoff")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff"], result)

    @builtins.property
    def output_audio_text(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText"]:
        '''output_audio_text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#output_audio_text GoogleDialogflowCxFlow#output_audio_text}
        '''
        result = self._values.get("output_audio_text")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText"], result)

    @builtins.property
    def payload(self) -> typing.Optional[builtins.str]:
        '''A custom, platform-specific payload.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#payload GoogleDialogflowCxFlow#payload}
        '''
        result = self._values.get("payload")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def play_audio(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio"]:
        '''play_audio block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#play_audio GoogleDialogflowCxFlow#play_audio}
        '''
        result = self._values.get("play_audio")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio"], result)

    @builtins.property
    def telephony_transfer_call(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall"]:
        '''telephony_transfer_call block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#telephony_transfer_call GoogleDialogflowCxFlow#telephony_transfer_call}
        '''
        result = self._values.get("telephony_transfer_call")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall"], result)

    @builtins.property
    def text(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText"]:
        '''text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#metadata GoogleDialogflowCxFlow#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__443cb296068677570ca31681b7a23fce70b15134c83624ecdfa4d4d7d48c4e54)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#metadata GoogleDialogflowCxFlow#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccessOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a62fef97b7856041a1713b9b5ae779fb408afd1be81ba4f16c1ba424089cb264)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ada7298689527b5c065cde8e48c22db97db2e508e922c6fd36a87403bf090ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5103b2b839d9b966e63faeba0e1d3965459265a261e7c5f637daa589b15b432f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7435871870af685282002420434c13db7b6579027b6925f2e68d8de4a5c3fc9e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6be189241fff7bf38c1fca21ad4f28dc6cccdf2f4f554aaea715de229737a76e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ae7d59f0511c56d7eb840244429c79966ee48fc81349d5f84f2319907031903)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9a46f9994035fdfbc69bb83a7a8c239a963e6e9eecfe39d1df33a45f82ec229)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3eda6061a4d7d2bdf6484af0aac95aaeab9ba650ee6cb0480fade59673b8fade)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25a4af56b921e555a8e66e8345e3e8709927bd080ce8209d365603fa341a6b54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#metadata GoogleDialogflowCxFlow#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__037577492ee768c84baa425a81e9da4bed7eca07320eb112467dd187e32ab818)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#metadata GoogleDialogflowCxFlow#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoffOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoffOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__29c23b527aedf7f56b05ebd207e8bf44b96dead12716c5f2ad05f70660f45f63)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3ec186ffc12bc91a22be609e0440c45a7148cd2adf3d8455c03443084b991c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b99adafea9b3ca2b24c5226c7aed674a5a7acb0b2cf866a9968359adc9b2328)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText",
    jsii_struct_bases=[],
    name_mapping={"ssml": "ssml", "text": "text"},
)
class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText:
    def __init__(
        self,
        *,
        ssml: typing.Optional[builtins.str] = None,
        text: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#ssml GoogleDialogflowCxFlow#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__754cf0eb58c8b5554cec150e39db7d963e7b5a5ccab6c9ea5619b02e0953ac39)
            check_type(argname="argument ssml", value=ssml, expected_type=type_hints["ssml"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ssml is not None:
            self._values["ssml"] = ssml
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def ssml(self) -> typing.Optional[builtins.str]:
        '''The SSML text to be synthesized. For more information, see SSML.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#ssml GoogleDialogflowCxFlow#ssml}
        '''
        result = self._values.get("ssml")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def text(self) -> typing.Optional[builtins.str]:
        '''The raw text to be synthesized.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f98db449db3742aa31405a7fb2f355780ca03773173b8e1e5094869b9a3e7fb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSsml")
    def reset_ssml(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsml", []))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "allowPlaybackInterruption"))

    @builtins.property
    @jsii.member(jsii_name="ssmlInput")
    def ssml_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ssmlInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="ssml")
    def ssml(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssml"))

    @ssml.setter
    def ssml(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3de77f51bd45be075e048dd6cd7856fca94294384103b6e481857cee90bce522)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssml", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b51f673294b2e4d47f56a817c0f960b1ecaef6d00f7708f6309d8e6488be465)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b36fe60a0dd9d4a7f3180cdb0e06de888cd52e708d8c6a2b52160de645883ee6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e09d82d13a056100809df1747e9032e7cff75fcd0fd2e85fd7cac7fe514183f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putConversationSuccess")
    def put_conversation_success(
        self,
        *,
        metadata: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#metadata GoogleDialogflowCxFlow#metadata}
        '''
        value = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess(
            metadata=metadata
        )

        return typing.cast(None, jsii.invoke(self, "putConversationSuccess", [value]))

    @jsii.member(jsii_name="putLiveAgentHandoff")
    def put_live_agent_handoff(
        self,
        *,
        metadata: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#metadata GoogleDialogflowCxFlow#metadata}
        '''
        value = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff(
            metadata=metadata
        )

        return typing.cast(None, jsii.invoke(self, "putLiveAgentHandoff", [value]))

    @jsii.member(jsii_name="putOutputAudioText")
    def put_output_audio_text(
        self,
        *,
        ssml: typing.Optional[builtins.str] = None,
        text: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#ssml GoogleDialogflowCxFlow#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        value = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText(
            ssml=ssml, text=text
        )

        return typing.cast(None, jsii.invoke(self, "putOutputAudioText", [value]))

    @jsii.member(jsii_name="putPlayAudio")
    def put_play_audio(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#audio_uri GoogleDialogflowCxFlow#audio_uri}
        '''
        value = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio(
            audio_uri=audio_uri
        )

        return typing.cast(None, jsii.invoke(self, "putPlayAudio", [value]))

    @jsii.member(jsii_name="putTelephonyTransferCall")
    def put_telephony_transfer_call(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#phone_number GoogleDialogflowCxFlow#phone_number}
        '''
        value = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall(
            phone_number=phone_number
        )

        return typing.cast(None, jsii.invoke(self, "putTelephonyTransferCall", [value]))

    @jsii.member(jsii_name="putText")
    def put_text(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        value = GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText(
            text=text
        )

        return typing.cast(None, jsii.invoke(self, "putText", [value]))

    @jsii.member(jsii_name="resetChannel")
    def reset_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannel", []))

    @jsii.member(jsii_name="resetConversationSuccess")
    def reset_conversation_success(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConversationSuccess", []))

    @jsii.member(jsii_name="resetLiveAgentHandoff")
    def reset_live_agent_handoff(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLiveAgentHandoff", []))

    @jsii.member(jsii_name="resetOutputAudioText")
    def reset_output_audio_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputAudioText", []))

    @jsii.member(jsii_name="resetPayload")
    def reset_payload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPayload", []))

    @jsii.member(jsii_name="resetPlayAudio")
    def reset_play_audio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlayAudio", []))

    @jsii.member(jsii_name="resetTelephonyTransferCall")
    def reset_telephony_transfer_call(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTelephonyTransferCall", []))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="conversationSuccess")
    def conversation_success(
        self,
    ) -> GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccessOutputReference:
        return typing.cast(GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccessOutputReference, jsii.get(self, "conversationSuccess"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoffOutputReference:
        return typing.cast(GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoffOutputReference, jsii.get(self, "liveAgentHandoff"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioText")
    def output_audio_text(
        self,
    ) -> GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioTextOutputReference:
        return typing.cast(GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioTextOutputReference, jsii.get(self, "outputAudioText"))

    @builtins.property
    @jsii.member(jsii_name="playAudio")
    def play_audio(
        self,
    ) -> "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudioOutputReference":
        return typing.cast("GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudioOutputReference", jsii.get(self, "playAudio"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCallOutputReference":
        return typing.cast("GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCallOutputReference", jsii.get(self, "telephonyTransferCall"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(
        self,
    ) -> "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTextOutputReference":
        return typing.cast("GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTextOutputReference", jsii.get(self, "text"))

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="conversationSuccessInput")
    def conversation_success_input(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess], jsii.get(self, "conversationSuccessInput"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoffInput")
    def live_agent_handoff_input(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "liveAgentHandoffInput"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioTextInput")
    def output_audio_text_input(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText], jsii.get(self, "outputAudioTextInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadInput")
    def payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadInput"))

    @builtins.property
    @jsii.member(jsii_name="playAudioInput")
    def play_audio_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio"], jsii.get(self, "playAudioInput"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCallInput")
    def telephony_transfer_call_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall"], jsii.get(self, "telephonyTransferCallInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText"], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channel"))

    @channel.setter
    def channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8690d15b9137257d6f9ee9213315231c41ec83f5b4527dd525e724ffc5c480ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="payload")
    def payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payload"))

    @payload.setter
    def payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fccc74f5e06ef36a07f83277c279bc200de603b16835ff1e70a68b0d957c5334)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payload", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__453d82510f9adc9db614143cd517ba4f565b2a6db300b9f8a6faedcdb1372282)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio",
    jsii_struct_bases=[],
    name_mapping={"audio_uri": "audioUri"},
)
class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio:
    def __init__(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#audio_uri GoogleDialogflowCxFlow#audio_uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeaa482bfaa5dfaad614fee2fef6fef4103da1f019699ea086f8687451a0debb)
            check_type(argname="argument audio_uri", value=audio_uri, expected_type=type_hints["audio_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "audio_uri": audio_uri,
        }

    @builtins.property
    def audio_uri(self) -> builtins.str:
        '''URI of the audio clip.

        Dialogflow does not impose any validation on this value. It is specific to the client that reads it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#audio_uri GoogleDialogflowCxFlow#audio_uri}
        '''
        result = self._values.get("audio_uri")
        assert result is not None, "Required property 'audio_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudioOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudioOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b742708f1595104a689aa6369edb59ed9c8fcbb51ce27e58cc79fc6a27527fb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "allowPlaybackInterruption"))

    @builtins.property
    @jsii.member(jsii_name="audioUriInput")
    def audio_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "audioUriInput"))

    @builtins.property
    @jsii.member(jsii_name="audioUri")
    def audio_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audioUri"))

    @audio_uri.setter
    def audio_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53fdde3b49c83d9a3cbd9f2f9efbefcf3b82f2fa111960ae5924e9c818cdd315)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf03831b63f25ea1a0403eaadd1fbd9036d0e7001aba80950ccb6658ab717806)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall",
    jsii_struct_bases=[],
    name_mapping={"phone_number": "phoneNumber"},
)
class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall:
    def __init__(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#phone_number GoogleDialogflowCxFlow#phone_number}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e186a2b1ef179a0437ddfd4ae0f6eca9225a010c0d1c190a0b679f3c0e8e3e4)
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "phone_number": phone_number,
        }

    @builtins.property
    def phone_number(self) -> builtins.str:
        '''Transfer the call to a phone number in E.164 format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#phone_number GoogleDialogflowCxFlow#phone_number}
        '''
        result = self._values.get("phone_number")
        assert result is not None, "Required property 'phone_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCallOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCallOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57331cb9c6069d413867ce93e466e0c1ab9e4abab3d9a67e5aa4a394dff4fca7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="phoneNumberInput")
    def phone_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneNumber")
    def phone_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phoneNumber"))

    @phone_number.setter
    def phone_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ab54ecaf8c1ed91aa519e07af5b72d0e7cfed9b66a102d9e11c0b00beed5e7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cf35e97d6bbfc5664a8f38870f4d775a25938b2e2fa5e4b158d016e49b7b04c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0153409442fb161b628945747122cdf8ddc6e15a3d6d3a0948bc10c7a26885f6)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A collection of text responses.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#text GoogleDialogflowCxFlow#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a06dd4513f065ad9309d0a96051645e8a1e25667073f4ca1e04b988bc1877e2e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "allowPlaybackInterruption"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "text"))

    @text.setter
    def text(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4129b5304583b960d5f0beec820380ae650c062c078679046d54b3e60db3a84c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50f2da856a359f6e13479ee354302498446f8687051668ea56ea87c957f0b2cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7dbb19ced0b6c9b1d22198ba4a7f0983290defd105af87f66c03662cda69e461)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConditionalCases")
    def put_conditional_cases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0582dbdbcdfcc015af334e2c55df9c543eb7cc8aab2c8f879e6ac28e82843b26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConditionalCases", [value]))

    @jsii.member(jsii_name="putMessages")
    def put_messages(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b0b934ff43ca7625a4f7b3d2b74223683bab64ed983cdb10e1e244620b05270)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessages", [value]))

    @jsii.member(jsii_name="putSetParameterActions")
    def put_set_parameter_actions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__189b19022a0a37d65f611da92ce86132c15753dff6e3d735ffc2a5bb2f5f7d9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSetParameterActions", [value]))

    @jsii.member(jsii_name="resetConditionalCases")
    def reset_conditional_cases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionalCases", []))

    @jsii.member(jsii_name="resetMessages")
    def reset_messages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessages", []))

    @jsii.member(jsii_name="resetReturnPartialResponses")
    def reset_return_partial_responses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnPartialResponses", []))

    @jsii.member(jsii_name="resetSetParameterActions")
    def reset_set_parameter_actions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSetParameterActions", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetWebhook")
    def reset_webhook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhook", []))

    @builtins.property
    @jsii.member(jsii_name="conditionalCases")
    def conditional_cases(
        self,
    ) -> GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCasesList:
        return typing.cast(GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCasesList, jsii.get(self, "conditionalCases"))

    @builtins.property
    @jsii.member(jsii_name="messages")
    def messages(
        self,
    ) -> GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesList:
        return typing.cast(GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesList, jsii.get(self, "messages"))

    @builtins.property
    @jsii.member(jsii_name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActionsList":
        return typing.cast("GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActionsList", jsii.get(self, "setParameterActions"))

    @builtins.property
    @jsii.member(jsii_name="conditionalCasesInput")
    def conditional_cases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases]]], jsii.get(self, "conditionalCasesInput"))

    @builtins.property
    @jsii.member(jsii_name="messagesInput")
    def messages_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages]]], jsii.get(self, "messagesInput"))

    @builtins.property
    @jsii.member(jsii_name="returnPartialResponsesInput")
    def return_partial_responses_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "returnPartialResponsesInput"))

    @builtins.property
    @jsii.member(jsii_name="setParameterActionsInput")
    def set_parameter_actions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions"]]], jsii.get(self, "setParameterActionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookInput")
    def webhook_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webhookInput"))

    @builtins.property
    @jsii.member(jsii_name="returnPartialResponses")
    def return_partial_responses(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "returnPartialResponses"))

    @return_partial_responses.setter
    def return_partial_responses(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bc3ed29a6fe1a6c56df7a77a6dafca943bcfc091afa8b6d48041ad775e8b814)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnPartialResponses", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9f70849da3e966fdf6b96ed7433d72b3121157e46ef03cb37bcc66ac4dd2b01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhook"))

    @webhook.setter
    def webhook(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeee2472db9caa2d47a89521789e8b35f36e94f69faeb5e8e3a183a96628c091)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhook", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment]:
        return typing.cast(typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__220977d5a118b7da09035631babbb52080bd1f81cc737ffa8743eebdfbed6d4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions",
    jsii_struct_bases=[],
    name_mapping={"parameter": "parameter", "value": "value"},
)
class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions:
    def __init__(
        self,
        *,
        parameter: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param parameter: Display name of the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#parameter GoogleDialogflowCxFlow#parameter}
        :param value: The new JSON-encoded value of the parameter. A null value clears the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#value GoogleDialogflowCxFlow#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64ce5b4c1ad6bc6fd3c99bb3cb134de4b9fbc58d10cb9c822cba3d1ab87681a4)
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameter is not None:
            self._values["parameter"] = parameter
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def parameter(self) -> typing.Optional[builtins.str]:
        '''Display name of the parameter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#parameter GoogleDialogflowCxFlow#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The new JSON-encoded value of the parameter. A null value clears the parameter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_dialogflow_cx_flow#value GoogleDialogflowCxFlow#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1009379d86a81f455f149be928b5167054ab533b589dbe561f7f79d4c5d25510)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d630eb93806d039a7a3be4015b25441367e050cb2051227e0697b8350fa2b188)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3678a2a493a46d2caed937bb0e6d6d7d7ab5f74e63263abbd8de24e174040145)
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
            type_hints = typing.get_type_hints(_typecheckingstub__db8186aeed4322c4b8712a7e1d8ae779695931b38a479f99a2fee24571c061cf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__65ccf02e547b9c9c1c79f52b2913957dae39dd5af3cf05dc2598d8c185979bfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23361771f23ebe9a1ed4c64c22b1f9725c28b96f39af11c1428dd0a53a053b33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxFlow.GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__918e7e9ba3fde7d211de3237538cae953afc374dedfa658ae13f2ece422f5bb8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameter"))

    @parameter.setter
    def parameter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b67d67b07417c3d48974e8f75da3e2985e69a745d9600461aba776c5232c103d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameter", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b65d59229d975c4b30135574d2a00ab712add1d09ac284b6f5f22b4fc3ed795)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbf8ba72500a2f738831af42f750ba19782166ea872ad100c0378e20368d07e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDialogflowCxFlow",
    "GoogleDialogflowCxFlowAdvancedSettings",
    "GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination",
    "GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestinationOutputReference",
    "GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings",
    "GoogleDialogflowCxFlowAdvancedSettingsDtmfSettingsOutputReference",
    "GoogleDialogflowCxFlowAdvancedSettingsOutputReference",
    "GoogleDialogflowCxFlowConfig",
    "GoogleDialogflowCxFlowEventHandlers",
    "GoogleDialogflowCxFlowEventHandlersList",
    "GoogleDialogflowCxFlowEventHandlersOutputReference",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillment",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCasesList",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCasesOutputReference",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesList",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputReference",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTextOutputReference",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentOutputReference",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActionsList",
    "GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActionsOutputReference",
    "GoogleDialogflowCxFlowNluSettings",
    "GoogleDialogflowCxFlowNluSettingsOutputReference",
    "GoogleDialogflowCxFlowTimeouts",
    "GoogleDialogflowCxFlowTimeoutsOutputReference",
    "GoogleDialogflowCxFlowTransitionRoutes",
    "GoogleDialogflowCxFlowTransitionRoutesList",
    "GoogleDialogflowCxFlowTransitionRoutesOutputReference",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCasesList",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCasesOutputReference",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccessOutputReference",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesList",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoffOutputReference",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioTextOutputReference",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputReference",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudioOutputReference",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCallOutputReference",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTextOutputReference",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentOutputReference",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActionsList",
    "GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActionsOutputReference",
]

publication.publish()

def _typecheckingstub__8ddc1c9bd1aaab871a2b80768c2bc499e93a36227c2ec26b6797aac6fac61ceb(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    display_name: builtins.str,
    advanced_settings: typing.Optional[typing.Union[GoogleDialogflowCxFlowAdvancedSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    event_handlers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowEventHandlers, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    is_default_start_flow: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    language_code: typing.Optional[builtins.str] = None,
    nlu_settings: typing.Optional[typing.Union[GoogleDialogflowCxFlowNluSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    parent: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleDialogflowCxFlowTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    transition_route_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    transition_routes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowTransitionRoutes, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__ad3b054a471de21d0a367ca38d61ec2a1c86d28c7c7e15d0fa29c34cef2e8ffa(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d5763a95f2a19a20a2cee1cd63b8e22e995b6ccdda0bc67f0a8ba7c9afea462(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowEventHandlers, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f67d14e084641d1578e154aed126fcf46d108e0c8f21351b034db072abbe3b8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowTransitionRoutes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7564a7905ff3d080ec73fd5b3674d80316185888f34b793426007f2891348fc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d57e353ea4e0c1dbefde806a99b8c916a02fa1ed2fdd994823bfcf5422e9934(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eab5ec690ece1ff9fa75d59b2a15d2b7ececfba9a83206cd737e9f2f7198cb5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc61fcc21cb3d353f84d5d4e88bdffe57d189d4c895ab85b7d3f152168394a73(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb70b48e85ea80ce1f103a0c05a4b3466c57a382c528c7a81ce07b3b8df410ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a48c675e5612a9b38a6595f66082b141506e7336639e253e7d20e4b003a2e87d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8b9d2da6f549846ac8b8c3ea7bb8b102639d483550c7cb5ff7fa1924d572b11(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74522f9b5137db65e0921cf1c5e8aa67898022072b01667d01626b26b51a97d4(
    *,
    audio_export_gcs_destination: typing.Optional[typing.Union[GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination, typing.Dict[builtins.str, typing.Any]]] = None,
    dtmf_settings: typing.Optional[typing.Union[GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f14a90e7cb3882840e4ec911e01e5451e2d8b19a9979b602f4294dbcd64ba59c(
    *,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__126bfaf474003387ad65638cfd0a1d944237446dd9255e7e0c74b0ed088028dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcf8efda4b84a8fbcd37d884c901b0367ea99053549c30a600b982d7b6ae0208(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6753a3d1e6d9677e891ba03b4be61d55b680366939ab6a465ec78726af5affdc(
    value: typing.Optional[GoogleDialogflowCxFlowAdvancedSettingsAudioExportGcsDestination],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbbd4cad34ff6aa630667af905d7c23565c8b573fc94b53aeedc8657f064a053(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    finish_digit: typing.Optional[builtins.str] = None,
    max_digits: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94e13c969a0969e8c13bac2c5a7a19f17db5928989f957c7eff5e02b1285b21c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__444113a02773315b4f4224c440ff697f2d51c4eb404fb307174f2a56c5ff5bfb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__080fea3290e7f671c0b7921f05c14cfde7ad37d6a3ae820c5301a730c89c0ba4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79d79812fc802c105c6e8454b68dff149578f978375c174f256286489e456019(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d36606aa4eb8bd597c3494f9c89fb89e5f555047331abb521468e0e51933e94(
    value: typing.Optional[GoogleDialogflowCxFlowAdvancedSettingsDtmfSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a4cfef87b8c76c85a3fbfc1b57d3fdf6b29e64131a20d9a3f54dc95a49cf56d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf2a7517d1b6799be5bbd2bca26336584a9c1d7021407f29c7456dedcdffaa7c(
    value: typing.Optional[GoogleDialogflowCxFlowAdvancedSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5b6d22821ccb6c1261edc07f6bc6656e98299156ae0eaee2da8542a3e22cb90(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    display_name: builtins.str,
    advanced_settings: typing.Optional[typing.Union[GoogleDialogflowCxFlowAdvancedSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    event_handlers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowEventHandlers, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    is_default_start_flow: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    language_code: typing.Optional[builtins.str] = None,
    nlu_settings: typing.Optional[typing.Union[GoogleDialogflowCxFlowNluSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    parent: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleDialogflowCxFlowTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    transition_route_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    transition_routes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowTransitionRoutes, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98d6b437f59c96e369e9a65e8cba23f38e57df796929bbd75224bcedc388b721(
    *,
    event: typing.Optional[builtins.str] = None,
    target_flow: typing.Optional[builtins.str] = None,
    target_page: typing.Optional[builtins.str] = None,
    trigger_fulfillment: typing.Optional[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillment, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ea6d2385130136ba9ba2449229da1e1d3e391e41dfafc4c8ca3bb1631d4ce14(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b72692e2f83b58047d9ef491b2c6b8d6d65b1d0576f01c8e029ece54d7ca94a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10e47925b00e47f983de73bfa202626a1e3135e199f22fe97d586dabb330c1f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a87ff1ba2605882bab6a41459482a8d5ce15d04140c213017f7aa60d0f1f8cd4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__797650aaec31e7ca6bb8bc45d5cb90e35913ad807f256a34b97189d1d969d736(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__550686a1780bbee4f9f8564add05760636a98a28cf7e02f3c02b086103f5e3dc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlers]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0b49a2bf192f63cb5a72c1bd7cdffb07f5cdb45767d0977c9c0af70fe72a68a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65b6f23d473fdfa3616c5c573a6311ed0c64ca67237e5fc371844d19be8d4b06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8232a76d7dd21a85014f51ee2b25961374daa0e33aba5d27aed553abf55ee0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf6d60b11ea63adf1c7be2210f0b5cecc0c0346fad1ab06f7f78bd60d2f16a37(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22b10706871c1d1f665ef2d90bd0d58a208650af42514f7be1dca25fb9f02432(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlers]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2b0b5e0e8e08564eff12bc1e01fd9807cb7a628d58f0aa0ac775e881f69e3fe(
    *,
    conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]]] = None,
    messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]]] = None,
    return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tag: typing.Optional[builtins.str] = None,
    webhook: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c91d12edab2a2dbd0bf7747bb2162e7c5824f681ff0be9abf60fd5a33549bd1(
    *,
    cases: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dc297fa3b4deca51bde040af9d3d85d51244a4f502dc3dc2edfd6b442cd6cf3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5085cb33cee60f0351f3707232a96f794e06e88c9214ab90efd906fee9c0034(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ba859ff220cb9d944e616471ac511e557a5570ae65fcc73358ef0b6aee8b570(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5d1ff8d188984b06b917cc566fa0b77d1abdc648bc70011da6ca2c1425ef353(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c046a332b2e188696b71b7ebb514bc26bebd1e040aebcd934005665a2890fc2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaf545456d221be7117ea8e6a65ac1c3cc6ce3dc384d83d3d6f8aec0539adb64(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d18f9237ed20e32840fe9794f3f02ec81890ca29521cd3ea20bff5398ba6515(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6059d8a6d6d9cc3d499120d5011eeb5726168e3b30d8845649011bb6ea07f40(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c97cb0f6e6865d8ec850b8cbeedc765de0021d6a630119f6ace7b60ba3f5d0f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47cf1b77ff3ec061bdddb90036c33368f3e5b8f584b5d70cb6c8d6c442148a4f(
    *,
    channel: typing.Optional[builtins.str] = None,
    conversation_success: typing.Optional[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess, typing.Dict[builtins.str, typing.Any]]] = None,
    live_agent_handoff: typing.Optional[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff, typing.Dict[builtins.str, typing.Any]]] = None,
    output_audio_text: typing.Optional[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText, typing.Dict[builtins.str, typing.Any]]] = None,
    payload: typing.Optional[builtins.str] = None,
    play_audio: typing.Optional[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio, typing.Dict[builtins.str, typing.Any]]] = None,
    telephony_transfer_call: typing.Optional[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall, typing.Dict[builtins.str, typing.Any]]] = None,
    text: typing.Optional[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71ba2f39b3e982d1ed7e0151541fccd54bbba72eb06788d47077001ea900f65b(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__999db007c9c1915b58c71b617ffb2b51d98449f40e550093ac8de4804f4b8bab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80c92f6879994241f8be0374257b2000fb20537e65d4e70e623aacebb56b8da9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad2092c5876164f320659d6b4e0c9ee2959f15bfc8ab9c6240bed7c672aca6db(
    value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesConversationSuccess],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91a30f242e5ea4183f4a388675dae2a39a85ebb559121c69b38971a70ae0259b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef209c5de032bddd5d5f68a59e2625324e8d419c75f45bb6c212f1afcdcf5337(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fb9eaee16e8332e5d899c05745620e138957c5e96c41b0be100922470cea560(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8df20db12f6bf4a2136b74d845969b82f6c72d29f3160edf5aaf3e9607405c84(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc59802a7434cb11ca69be912e59b031a4a61b4c64c7c3877cf2b86eedfb6dc5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66fc6f716cf1db773623fff9494d38d2fd97eaa1964cbad881bf5cb7c48ed834(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de157fcd6751d9db70e1e58531c48002ac6b8c5e271e1629c9cfe53f64074595(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2d9347e9d2f662db1ce7f21c8a413ffd0a12b9032e84ad52c72b13bb5a38b4c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6de09dd2cb920aec8c6fa2d52287a5fe3f6517d58922ee571408de959977b10e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17248d3513fcfd5a6bdcb22aa7baa4cc0a70cd192852dbe9123ed496586b7418(
    value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cd4b98e2ab2e75f2d752a959a0b0e1ef2932096b760b53b77c60a04151f4085(
    *,
    ssml: typing.Optional[builtins.str] = None,
    text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54f4bdf6f12fb261e41faa5a2b0f3246d66e76f40c88d4a533e2192eb312f928(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d4b85156c1116cd26e4873b89c1a4966f7a568ab35aebf2d9be598cd25c2003(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aed58b632dd33e478da2b95a0c954d89c8684469ad93a8c05bf1fefb92334ef6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__407c042b8ffe7beb5fd352f1cc631efea66dd2870ba4c36b89578b5c469a4725(
    value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesOutputAudioText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a5d7394da129220d20cf2d3e9de1e4a8bc97cf36ff80f93157bd345d447f814(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ee365bd5e7ad02443edec08b36d422ebd6ba0925fb54f56b43c0d0b5b6e08f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2cd3500edffc79de60595b43ccb8b511bac26f94034afd27658ce0f1dbb34d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b33fd52d5aee1abc2af7510c2d810adabcf29a9323ff8a75fac9e0e5a9b3d8e2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efa71b0a2ce84c87ecd1d7c824a1b3d735c9cf5482efb3d60fc9b5a4a0486262(
    *,
    audio_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecc3fe6bb8b710da9ac63e4d0055e56679e0eebb090c310213eff1a90119e934(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e7dc243844b4f75b91211ae2d27b9887c7baa9733bc9bdbed88745218e44d94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11fdc1ebecce9edee0dd805324d6cf8aee3e2b30bd7204e4a9f3d3dbbe9424e4(
    value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesPlayAudio],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e89b70a63040a97046353aa145e0c5def89f523a28e0e3192d56cb96c46a58d1(
    *,
    phone_number: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d1e51f50aa052e9299e27e0ff1c13913459e9ec3fb03cdd73bb574e8248a106(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54701318c05c962d1797c39a43227a0a786172c08ece78e448a8f61fcc24f506(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc6365e33a446197ecc983cc3b6027917a4bd3902601a9e02ecc1c5923b39d43(
    value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caf968656644d2b99fc0f819ca3a16b23f096995475b7b3a6e08e5c1c1358318(
    *,
    text: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4ec1e46f38dd2a469bcfc5e0b204a6b11595e08e119b7981575105910d8c78d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__037aec295bb472f589ea596cbfebb45456ce81962af528f351d6b6e616e3b242(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__479b59249a9dfb3608d4dc0fed24b0337e07fe844e83827b6f943b301566db71(
    value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessagesText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bad15ed6b01e2d0546b46b152ea04c1371cb3c7d4324e188ef4e47b66fade90(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__819a5d95220721c41d98998c537993544cc544bb52e5607faed5c09e1193c8a8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42f5acfd4c64d5ac63b8f15f48c10d2fd9d8bc9b56ae86ee6bab6d18e6328278(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__760234eadd3578b5586974b36f2ac0369361d386d0d7c7e1288fef584b33164c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b357e6f9c60440207ddaad42c083f61899fd2ca2bcace2737949eb6ea6851467(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05e50fe901dbf61aa635a56e265013a777da162a618815e4ec01998dc21f697c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91bf4cce913b48aa52137ae8d78dc55d18dccf652b6d505fed4dc622a5a91a55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3744515a4e7ffc4c34a960ba8fd725e26afa66704674a5e14177efa17342c58(
    value: typing.Optional[GoogleDialogflowCxFlowEventHandlersTriggerFulfillment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93c78aaa9dc78e546841f3429b21f134fd3cdfc47dbb4d8f2861327ff41bba56(
    *,
    parameter: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9baca73387f09f5353e93c5f8700bc045106f221b0359c2d131fbe7055705769(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c9ad8bc904ef45fbdb508b5a50c2dfc3a1b4e647fee04655b5392a8520e079e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c541f89743bc296f16f4c020a2a70c5dc373b7354aa36161ab1482de47aeb6fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3a0503fe09a702f31a139eb8a7dfb556ff06b6c53476a4294840f14b231b11c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6cf7ea8214c4ca0a99eee21e0cf65fee0b65d6581d592e2d3d31b0952b82d5e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c918962fb69ac22fe5c492c71097cef5730be8d3a6fdd704d0a953706262f01(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e849e95ac9146804ad1cc766b09fdac80cb113b5fc45e4da4325aecd79c3bb9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee39d77d0d3a755ced9500b7843b711e233e1f5458838cf3e5f254227d056d77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__645180431c81e6015f9b747ca228f3de8abb61a09f9c6aaca262bc6f8bdfe421(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__404abb45a68419b24509e89c3c666e1384d97c4fb58a267936d63a46cd84b790(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowEventHandlersTriggerFulfillmentSetParameterActions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e11d2415d17184287951f07c3c59b5989b582c6777731b857475cbefa2994ab9(
    *,
    classification_threshold: typing.Optional[jsii.Number] = None,
    model_training_mode: typing.Optional[builtins.str] = None,
    model_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98d9f3909bba7513ded942dd49ab4eff31602cdb034f4a4e1475a92d9195e3cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45305366a1d242576564cf317b03d1a334294e16921345b493918e93aecceff7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__536cbd1264bd06bfdfe3cee75d9622418afef8311158512d4f56b6ab9158e3f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbe96da0683e88b188041d7de4c92fed18d30c2e19f30792d01ac81a7e8fc06f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__524f25a80f58940c6773cd38d1d4a7c6ddb98c11023b57dd08686d71d4bec644(
    value: typing.Optional[GoogleDialogflowCxFlowNluSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0210a03cea17a8ef6bb6c8d12573cd1b0d7140688721c228c725071420680dd6(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0e68db04b76164173d2591ddd75bb1b9b052a340e3f358976041e891232cfc2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c8fa4d3bd2d4d417cd91617f1a451745bf4aaf04d58d7966be4fba2c6597fe3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d5975630e9faa60ef9b199ec40a0b2873f5df8a921e7f852dabdc8a78073309(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e778f648906def1b0b98d5164ec361e201a715e15a0d72467b7788a670fc5c4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86c6d5b814a990c8b13a0674f1e520f123196a9fc67d10ff966cfed6d664ab5a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTimeouts]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d1a18960d79eb590c9d5bf3e090bd2e010515560266b7c63ff53264e0f013b1(
    *,
    condition: typing.Optional[builtins.str] = None,
    intent: typing.Optional[builtins.str] = None,
    target_flow: typing.Optional[builtins.str] = None,
    target_page: typing.Optional[builtins.str] = None,
    trigger_fulfillment: typing.Optional[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c658a26b791ed47c005526f0d203bf77af0ce5f404c11ebc43fd87ecac58b40b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3785a2a26b46925c4961926dbf735621325bd370269361e64e4cae714adf64c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72390c857e2ae72ecbbe1a54bb412b4ff281d146112ca0926eef1c03e9ab9c40(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bef78f412e276f63bb4c9db73a3c134a65b4d12146688888d6a4695ad3ac274b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be10637d5d8fa7172423bd8f96a2561a939265c1e9b1d560cbb735def4faa7a2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4831c1a17de10c1ab5840826b85ccb8471666de0b3bafe39b6002b027cc2f31(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48ac555298c8903d2371e18de384242e6abe071a26c75bfecc87cdb684fc1f5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76e46873b24a3efeb8ec6f6a61f81217f1e21900852c2da220810827b27be97d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7bbd5463bb362fe073852100eb5bc655db95f2128105531a3af0073f278523b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76d249e51248c27f926d6d592e9b4877379d8f9d5c09d9cc691e3dc24dab1974(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ec782606f320f8dceb8e53942677095abfe92dc2acf5f176bf57abeb0a5f8ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c71428de0494ae2981349f4c2a95e9ba77bf5b1e6a1b3ec8c23594a99918944a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutes]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__944315f63373bd1968029dfa9b00946a674228d84fcc82289742d14c69a9a569(
    *,
    conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]]] = None,
    messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]]] = None,
    return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tag: typing.Optional[builtins.str] = None,
    webhook: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__073564628f5e4b1c595d0ca2ef50b8c8b21b6fcd3d9829ed222747ee2033d788(
    *,
    cases: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dccd900a9d9cd7c15f9a0c287a2f99de34596f9a2f5812f158211134371b883f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64b4fa477655ece9114be172123489468135e33629d889949ef5b326669db33(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11e9aac43e2eaf7698d6c27ae81848e22e314ec08d9dc72e608142031ca45f04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc763207d105bcd2b733520647fced1e0d09ea742305106dcf6f6d380450b38a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce5f923d4c327212d62c992838d955b10993908e731036936ae74e3e27b5d7ca(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b94ce98d4da9e0fb393f8633e49995caf36570b625f581b6bc2c1c719a1e6000(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84305fb27b217397ad3c42dba23ed2b0f210bab4cbe3d6933666a8a28542afa3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f43465b9e291c5c5b7730cac16168be734ee87b24422e2c0956f46ae12735ef6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69319f6b9393fa10bdaed0904605aae7b5596401b7f85dbab7ab898f27bedee3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65436ee4b59d66753768513811493c2a9d9e47b34fd247b3f479f85953b0e120(
    *,
    channel: typing.Optional[builtins.str] = None,
    conversation_success: typing.Optional[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess, typing.Dict[builtins.str, typing.Any]]] = None,
    live_agent_handoff: typing.Optional[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff, typing.Dict[builtins.str, typing.Any]]] = None,
    output_audio_text: typing.Optional[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText, typing.Dict[builtins.str, typing.Any]]] = None,
    payload: typing.Optional[builtins.str] = None,
    play_audio: typing.Optional[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio, typing.Dict[builtins.str, typing.Any]]] = None,
    telephony_transfer_call: typing.Optional[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall, typing.Dict[builtins.str, typing.Any]]] = None,
    text: typing.Optional[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__443cb296068677570ca31681b7a23fce70b15134c83624ecdfa4d4d7d48c4e54(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a62fef97b7856041a1713b9b5ae779fb408afd1be81ba4f16c1ba424089cb264(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ada7298689527b5c065cde8e48c22db97db2e508e922c6fd36a87403bf090ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5103b2b839d9b966e63faeba0e1d3965459265a261e7c5f637daa589b15b432f(
    value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesConversationSuccess],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7435871870af685282002420434c13db7b6579027b6925f2e68d8de4a5c3fc9e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6be189241fff7bf38c1fca21ad4f28dc6cccdf2f4f554aaea715de229737a76e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ae7d59f0511c56d7eb840244429c79966ee48fc81349d5f84f2319907031903(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9a46f9994035fdfbc69bb83a7a8c239a963e6e9eecfe39d1df33a45f82ec229(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eda6061a4d7d2bdf6484af0aac95aaeab9ba650ee6cb0480fade59673b8fade(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25a4af56b921e555a8e66e8345e3e8709927bd080ce8209d365603fa341a6b54(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__037577492ee768c84baa425a81e9da4bed7eca07320eb112467dd187e32ab818(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29c23b527aedf7f56b05ebd207e8bf44b96dead12716c5f2ad05f70660f45f63(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3ec186ffc12bc91a22be609e0440c45a7148cd2adf3d8455c03443084b991c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b99adafea9b3ca2b24c5226c7aed674a5a7acb0b2cf866a9968359adc9b2328(
    value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__754cf0eb58c8b5554cec150e39db7d963e7b5a5ccab6c9ea5619b02e0953ac39(
    *,
    ssml: typing.Optional[builtins.str] = None,
    text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f98db449db3742aa31405a7fb2f355780ca03773173b8e1e5094869b9a3e7fb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3de77f51bd45be075e048dd6cd7856fca94294384103b6e481857cee90bce522(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b51f673294b2e4d47f56a817c0f960b1ecaef6d00f7708f6309d8e6488be465(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b36fe60a0dd9d4a7f3180cdb0e06de888cd52e708d8c6a2b52160de645883ee6(
    value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesOutputAudioText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e09d82d13a056100809df1747e9032e7cff75fcd0fd2e85fd7cac7fe514183f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8690d15b9137257d6f9ee9213315231c41ec83f5b4527dd525e724ffc5c480ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fccc74f5e06ef36a07f83277c279bc200de603b16835ff1e70a68b0d957c5334(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__453d82510f9adc9db614143cd517ba4f565b2a6db300b9f8a6faedcdb1372282(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeaa482bfaa5dfaad614fee2fef6fef4103da1f019699ea086f8687451a0debb(
    *,
    audio_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b742708f1595104a689aa6369edb59ed9c8fcbb51ce27e58cc79fc6a27527fb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53fdde3b49c83d9a3cbd9f2f9efbefcf3b82f2fa111960ae5924e9c818cdd315(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf03831b63f25ea1a0403eaadd1fbd9036d0e7001aba80950ccb6658ab717806(
    value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesPlayAudio],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e186a2b1ef179a0437ddfd4ae0f6eca9225a010c0d1c190a0b679f3c0e8e3e4(
    *,
    phone_number: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57331cb9c6069d413867ce93e466e0c1ab9e4abab3d9a67e5aa4a394dff4fca7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ab54ecaf8c1ed91aa519e07af5b72d0e7cfed9b66a102d9e11c0b00beed5e7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cf35e97d6bbfc5664a8f38870f4d775a25938b2e2fa5e4b158d016e49b7b04c(
    value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0153409442fb161b628945747122cdf8ddc6e15a3d6d3a0948bc10c7a26885f6(
    *,
    text: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a06dd4513f065ad9309d0a96051645e8a1e25667073f4ca1e04b988bc1877e2e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4129b5304583b960d5f0beec820380ae650c062c078679046d54b3e60db3a84c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f2da856a359f6e13479ee354302498446f8687051668ea56ea87c957f0b2cb(
    value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessagesText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dbb19ced0b6c9b1d22198ba4a7f0983290defd105af87f66c03662cda69e461(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0582dbdbcdfcc015af334e2c55df9c543eb7cc8aab2c8f879e6ac28e82843b26(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b0b934ff43ca7625a4f7b3d2b74223683bab64ed983cdb10e1e244620b05270(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__189b19022a0a37d65f611da92ce86132c15753dff6e3d735ffc2a5bb2f5f7d9e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bc3ed29a6fe1a6c56df7a77a6dafca943bcfc091afa8b6d48041ad775e8b814(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9f70849da3e966fdf6b96ed7433d72b3121157e46ef03cb37bcc66ac4dd2b01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeee2472db9caa2d47a89521789e8b35f36e94f69faeb5e8e3a183a96628c091(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__220977d5a118b7da09035631babbb52080bd1f81cc737ffa8743eebdfbed6d4b(
    value: typing.Optional[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64ce5b4c1ad6bc6fd3c99bb3cb134de4b9fbc58d10cb9c822cba3d1ab87681a4(
    *,
    parameter: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1009379d86a81f455f149be928b5167054ab533b589dbe561f7f79d4c5d25510(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d630eb93806d039a7a3be4015b25441367e050cb2051227e0697b8350fa2b188(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3678a2a493a46d2caed937bb0e6d6d7d7ab5f74e63263abbd8de24e174040145(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db8186aeed4322c4b8712a7e1d8ae779695931b38a479f99a2fee24571c061cf(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65ccf02e547b9c9c1c79f52b2913957dae39dd5af3cf05dc2598d8c185979bfd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23361771f23ebe9a1ed4c64c22b1f9725c28b96f39af11c1428dd0a53a053b33(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__918e7e9ba3fde7d211de3237538cae953afc374dedfa658ae13f2ece422f5bb8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b67d67b07417c3d48974e8f75da3e2985e69a745d9600461aba776c5232c103d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b65d59229d975c4b30135574d2a00ab712add1d09ac284b6f5f22b4fc3ed795(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbf8ba72500a2f738831af42f750ba19782166ea872ad100c0378e20368d07e3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GoogleDialogflowCxFlowTransitionRoutesTriggerFulfillmentSetParameterActions]],
) -> None:
    """Type checking stubs"""
    pass
