'''
# `google_dialogflow_cx_page`

Refer to the Terraform Registry for docs: [`google_dialogflow_cx_page`](https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page).
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


class DialogflowCxPage(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPage",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page google_dialogflow_cx_page}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        advanced_settings: typing.Optional[typing.Union["DialogflowCxPageAdvancedSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        entry_fulfillment: typing.Optional[typing.Union["DialogflowCxPageEntryFulfillment", typing.Dict[builtins.str, typing.Any]]] = None,
        event_handlers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEventHandlers", typing.Dict[builtins.str, typing.Any]]]]] = None,
        form: typing.Optional[typing.Union["DialogflowCxPageForm", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        language_code: typing.Optional[builtins.str] = None,
        parent: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DialogflowCxPageTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        transition_route_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        transition_routes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageTransitionRoutes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page google_dialogflow_cx_page} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: The human-readable name of the page, unique within the agent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#display_name DialogflowCxPage#display_name}
        :param advanced_settings: advanced_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#advanced_settings DialogflowCxPage#advanced_settings}
        :param entry_fulfillment: entry_fulfillment block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#entry_fulfillment DialogflowCxPage#entry_fulfillment}
        :param event_handlers: event_handlers block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#event_handlers DialogflowCxPage#event_handlers}
        :param form: form block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#form DialogflowCxPage#form}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#id DialogflowCxPage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param language_code: The language of the following fields in page:. Page.entry_fulfillment.messages Page.entry_fulfillment.conditional_cases Page.event_handlers.trigger_fulfillment.messages Page.event_handlers.trigger_fulfillment.conditional_cases Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases Page.form.parameters.fill_behavior.reprompt_event_handlers.messages Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases Page.transition_routes.trigger_fulfillment.messages Page.transition_routes.trigger_fulfillment.conditional_cases If not specified, the agent's default language is used. Many languages are supported. Note: languages must be enabled in the agent before they can be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#language_code DialogflowCxPage#language_code}
        :param parent: The flow to create a page for. Format: projects//locations//agents//flows/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parent DialogflowCxPage#parent}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#timeouts DialogflowCxPage#timeouts}
        :param transition_route_groups: Ordered list of TransitionRouteGroups associated with the page. Transition route groups must be unique within a page. If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes. If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence. Format:projects//locations//agents//flows//transitionRouteGroups/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#transition_route_groups DialogflowCxPage#transition_route_groups}
        :param transition_routes: transition_routes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#transition_routes DialogflowCxPage#transition_routes}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00b86788db75afcf01217cbd511e679f06595dd57e1056597a09befbc8f50a32)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DialogflowCxPageConfig(
            display_name=display_name,
            advanced_settings=advanced_settings,
            entry_fulfillment=entry_fulfillment,
            event_handlers=event_handlers,
            form=form,
            id=id,
            language_code=language_code,
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
        '''Generates CDKTF code for importing a DialogflowCxPage resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DialogflowCxPage to import.
        :param import_from_id: The id of the existing DialogflowCxPage that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DialogflowCxPage to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70dabc77390af26ce1af0dae01d3295e83d72d47b491fd0246e3bab431ec5ca1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAdvancedSettings")
    def put_advanced_settings(
        self,
        *,
        dtmf_settings: typing.Optional[typing.Union["DialogflowCxPageAdvancedSettingsDtmfSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dtmf_settings: dtmf_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#dtmf_settings DialogflowCxPage#dtmf_settings}
        '''
        value = DialogflowCxPageAdvancedSettings(dtmf_settings=dtmf_settings)

        return typing.cast(None, jsii.invoke(self, "putAdvancedSettings", [value]))

    @jsii.member(jsii_name="putEntryFulfillment")
    def put_entry_fulfillment(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEntryFulfillmentConditionalCases", typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEntryFulfillmentMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEntryFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        value = DialogflowCxPageEntryFulfillment(
            conditional_cases=conditional_cases,
            messages=messages,
            return_partial_responses=return_partial_responses,
            set_parameter_actions=set_parameter_actions,
            tag=tag,
            webhook=webhook,
        )

        return typing.cast(None, jsii.invoke(self, "putEntryFulfillment", [value]))

    @jsii.member(jsii_name="putEventHandlers")
    def put_event_handlers(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEventHandlers", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fb46f6fddfb632220c0d64201fa83c198ab42e08587a7ecaece5e8d4c5bea8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEventHandlers", [value]))

    @jsii.member(jsii_name="putForm")
    def put_form(
        self,
        *,
        parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParameters", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parameters DialogflowCxPage#parameters}
        '''
        value = DialogflowCxPageForm(parameters=parameters)

        return typing.cast(None, jsii.invoke(self, "putForm", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#create DialogflowCxPage#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#delete DialogflowCxPage#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#update DialogflowCxPage#update}.
        '''
        value = DialogflowCxPageTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTransitionRoutes")
    def put_transition_routes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageTransitionRoutes", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2c4a44baf7325117b478a21418fb8f6be38c5805baa6f51c89529da837056db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTransitionRoutes", [value]))

    @jsii.member(jsii_name="resetAdvancedSettings")
    def reset_advanced_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedSettings", []))

    @jsii.member(jsii_name="resetEntryFulfillment")
    def reset_entry_fulfillment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntryFulfillment", []))

    @jsii.member(jsii_name="resetEventHandlers")
    def reset_event_handlers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventHandlers", []))

    @jsii.member(jsii_name="resetForm")
    def reset_form(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForm", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLanguageCode")
    def reset_language_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLanguageCode", []))

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
    def advanced_settings(self) -> "DialogflowCxPageAdvancedSettingsOutputReference":
        return typing.cast("DialogflowCxPageAdvancedSettingsOutputReference", jsii.get(self, "advancedSettings"))

    @builtins.property
    @jsii.member(jsii_name="entryFulfillment")
    def entry_fulfillment(self) -> "DialogflowCxPageEntryFulfillmentOutputReference":
        return typing.cast("DialogflowCxPageEntryFulfillmentOutputReference", jsii.get(self, "entryFulfillment"))

    @builtins.property
    @jsii.member(jsii_name="eventHandlers")
    def event_handlers(self) -> "DialogflowCxPageEventHandlersList":
        return typing.cast("DialogflowCxPageEventHandlersList", jsii.get(self, "eventHandlers"))

    @builtins.property
    @jsii.member(jsii_name="form")
    def form(self) -> "DialogflowCxPageFormOutputReference":
        return typing.cast("DialogflowCxPageFormOutputReference", jsii.get(self, "form"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DialogflowCxPageTimeoutsOutputReference":
        return typing.cast("DialogflowCxPageTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="transitionRoutes")
    def transition_routes(self) -> "DialogflowCxPageTransitionRoutesList":
        return typing.cast("DialogflowCxPageTransitionRoutesList", jsii.get(self, "transitionRoutes"))

    @builtins.property
    @jsii.member(jsii_name="advancedSettingsInput")
    def advanced_settings_input(
        self,
    ) -> typing.Optional["DialogflowCxPageAdvancedSettings"]:
        return typing.cast(typing.Optional["DialogflowCxPageAdvancedSettings"], jsii.get(self, "advancedSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="entryFulfillmentInput")
    def entry_fulfillment_input(
        self,
    ) -> typing.Optional["DialogflowCxPageEntryFulfillment"]:
        return typing.cast(typing.Optional["DialogflowCxPageEntryFulfillment"], jsii.get(self, "entryFulfillmentInput"))

    @builtins.property
    @jsii.member(jsii_name="eventHandlersInput")
    def event_handlers_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEventHandlers"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEventHandlers"]]], jsii.get(self, "eventHandlersInput"))

    @builtins.property
    @jsii.member(jsii_name="formInput")
    def form_input(self) -> typing.Optional["DialogflowCxPageForm"]:
        return typing.cast(typing.Optional["DialogflowCxPageForm"], jsii.get(self, "formInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="languageCodeInput")
    def language_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "languageCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "DialogflowCxPageTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "DialogflowCxPageTimeouts"]], jsii.get(self, "timeoutsInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageTransitionRoutes"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageTransitionRoutes"]]], jsii.get(self, "transitionRoutesInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aceda3d155ee2d774d4b22ae88f216f4ff133b283f13db4d35f848af4e6be42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cc7c125078f31eb07da0320574b389a6b62974efe8287efbbc04039a6752930)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="languageCode")
    def language_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "languageCode"))

    @language_code.setter
    def language_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f58a8e77d7c407853b3786dae0d25eb1dae499dc05503d5e1a07dbf7a6262e38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageCode", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28d78b7c3ab6ef0892396a1958b1e536c8a95e0fb18cf05ecee6ed30d242d125)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)

    @builtins.property
    @jsii.member(jsii_name="transitionRouteGroups")
    def transition_route_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transitionRouteGroups"))

    @transition_route_groups.setter
    def transition_route_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11ebefab9cd26ab16d6738be5396da33e6d9d6b895a4efd6781900524c8307b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitionRouteGroups", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageAdvancedSettings",
    jsii_struct_bases=[],
    name_mapping={"dtmf_settings": "dtmfSettings"},
)
class DialogflowCxPageAdvancedSettings:
    def __init__(
        self,
        *,
        dtmf_settings: typing.Optional[typing.Union["DialogflowCxPageAdvancedSettingsDtmfSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dtmf_settings: dtmf_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#dtmf_settings DialogflowCxPage#dtmf_settings}
        '''
        if isinstance(dtmf_settings, dict):
            dtmf_settings = DialogflowCxPageAdvancedSettingsDtmfSettings(**dtmf_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ede6ab22672c198ad0eb08a56cdc69b984c7549f2c380101b6b26c6d89a716c6)
            check_type(argname="argument dtmf_settings", value=dtmf_settings, expected_type=type_hints["dtmf_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dtmf_settings is not None:
            self._values["dtmf_settings"] = dtmf_settings

    @builtins.property
    def dtmf_settings(
        self,
    ) -> typing.Optional["DialogflowCxPageAdvancedSettingsDtmfSettings"]:
        '''dtmf_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#dtmf_settings DialogflowCxPage#dtmf_settings}
        '''
        result = self._values.get("dtmf_settings")
        return typing.cast(typing.Optional["DialogflowCxPageAdvancedSettingsDtmfSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageAdvancedSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageAdvancedSettingsDtmfSettings",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "finish_digit": "finishDigit",
        "max_digits": "maxDigits",
    },
)
class DialogflowCxPageAdvancedSettingsDtmfSettings:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        finish_digit: typing.Optional[builtins.str] = None,
        max_digits: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: If true, incoming audio is processed for DTMF (dual tone multi frequency) events. For example, if the caller presses a button on their telephone keypad and DTMF processing is enabled, Dialogflow will detect the event (e.g. a "3" was pressed) in the incoming audio and pass the event to the bot to drive business logic (e.g. when 3 is pressed, return the account balance). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#enabled DialogflowCxPage#enabled}
        :param finish_digit: The digit that terminates a DTMF digit sequence. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#finish_digit DialogflowCxPage#finish_digit}
        :param max_digits: Max length of DTMF digits. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#max_digits DialogflowCxPage#max_digits}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dc27bcbe8f8e53a3bc08f9bd3fc80ecca9638c2dd1341048271efdd57d64128)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#enabled DialogflowCxPage#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def finish_digit(self) -> typing.Optional[builtins.str]:
        '''The digit that terminates a DTMF digit sequence.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#finish_digit DialogflowCxPage#finish_digit}
        '''
        result = self._values.get("finish_digit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_digits(self) -> typing.Optional[jsii.Number]:
        '''Max length of DTMF digits.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#max_digits DialogflowCxPage#max_digits}
        '''
        result = self._values.get("max_digits")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageAdvancedSettingsDtmfSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageAdvancedSettingsDtmfSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageAdvancedSettingsDtmfSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__381a30c71721b1169b31eac5ed44b2744dd7f862d1bb32ee6103da464e1874ba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b03718649b5cb0e240649c5f70671dae47fa71115b97cb06c5e0c945f5a7e0f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="finishDigit")
    def finish_digit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "finishDigit"))

    @finish_digit.setter
    def finish_digit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__162f3e1f727c3d53030937442e50f4a496a5abc07259f0c1d890ece0a4810dce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finishDigit", value)

    @builtins.property
    @jsii.member(jsii_name="maxDigits")
    def max_digits(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxDigits"))

    @max_digits.setter
    def max_digits(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0a69750a52b9bbf74c7baf696658177d811cae3de5339e8f04a034b092a5a0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDigits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageAdvancedSettingsDtmfSettings]:
        return typing.cast(typing.Optional[DialogflowCxPageAdvancedSettingsDtmfSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageAdvancedSettingsDtmfSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22ce22ee5dc6f10ebec9f3991740c04e8153ed65f04c87ce1f01cb99088b41af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageAdvancedSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageAdvancedSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e4cffa87c3547f58bd21b541c5133d84627a7dbc1bc3f48ae1656417dd9835c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDtmfSettings")
    def put_dtmf_settings(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        finish_digit: typing.Optional[builtins.str] = None,
        max_digits: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: If true, incoming audio is processed for DTMF (dual tone multi frequency) events. For example, if the caller presses a button on their telephone keypad and DTMF processing is enabled, Dialogflow will detect the event (e.g. a "3" was pressed) in the incoming audio and pass the event to the bot to drive business logic (e.g. when 3 is pressed, return the account balance). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#enabled DialogflowCxPage#enabled}
        :param finish_digit: The digit that terminates a DTMF digit sequence. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#finish_digit DialogflowCxPage#finish_digit}
        :param max_digits: Max length of DTMF digits. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#max_digits DialogflowCxPage#max_digits}
        '''
        value = DialogflowCxPageAdvancedSettingsDtmfSettings(
            enabled=enabled, finish_digit=finish_digit, max_digits=max_digits
        )

        return typing.cast(None, jsii.invoke(self, "putDtmfSettings", [value]))

    @jsii.member(jsii_name="resetDtmfSettings")
    def reset_dtmf_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDtmfSettings", []))

    @builtins.property
    @jsii.member(jsii_name="dtmfSettings")
    def dtmf_settings(
        self,
    ) -> DialogflowCxPageAdvancedSettingsDtmfSettingsOutputReference:
        return typing.cast(DialogflowCxPageAdvancedSettingsDtmfSettingsOutputReference, jsii.get(self, "dtmfSettings"))

    @builtins.property
    @jsii.member(jsii_name="dtmfSettingsInput")
    def dtmf_settings_input(
        self,
    ) -> typing.Optional[DialogflowCxPageAdvancedSettingsDtmfSettings]:
        return typing.cast(typing.Optional[DialogflowCxPageAdvancedSettingsDtmfSettings], jsii.get(self, "dtmfSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DialogflowCxPageAdvancedSettings]:
        return typing.cast(typing.Optional[DialogflowCxPageAdvancedSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageAdvancedSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61d7936a9ddf43a7da71bfe2901b18027a2fcdf60b33fc446ee9c19ad432fbaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageConfig",
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
        "entry_fulfillment": "entryFulfillment",
        "event_handlers": "eventHandlers",
        "form": "form",
        "id": "id",
        "language_code": "languageCode",
        "parent": "parent",
        "timeouts": "timeouts",
        "transition_route_groups": "transitionRouteGroups",
        "transition_routes": "transitionRoutes",
    },
)
class DialogflowCxPageConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        advanced_settings: typing.Optional[typing.Union[DialogflowCxPageAdvancedSettings, typing.Dict[builtins.str, typing.Any]]] = None,
        entry_fulfillment: typing.Optional[typing.Union["DialogflowCxPageEntryFulfillment", typing.Dict[builtins.str, typing.Any]]] = None,
        event_handlers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEventHandlers", typing.Dict[builtins.str, typing.Any]]]]] = None,
        form: typing.Optional[typing.Union["DialogflowCxPageForm", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        language_code: typing.Optional[builtins.str] = None,
        parent: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DialogflowCxPageTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        transition_route_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        transition_routes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageTransitionRoutes", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: The human-readable name of the page, unique within the agent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#display_name DialogflowCxPage#display_name}
        :param advanced_settings: advanced_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#advanced_settings DialogflowCxPage#advanced_settings}
        :param entry_fulfillment: entry_fulfillment block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#entry_fulfillment DialogflowCxPage#entry_fulfillment}
        :param event_handlers: event_handlers block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#event_handlers DialogflowCxPage#event_handlers}
        :param form: form block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#form DialogflowCxPage#form}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#id DialogflowCxPage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param language_code: The language of the following fields in page:. Page.entry_fulfillment.messages Page.entry_fulfillment.conditional_cases Page.event_handlers.trigger_fulfillment.messages Page.event_handlers.trigger_fulfillment.conditional_cases Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases Page.form.parameters.fill_behavior.reprompt_event_handlers.messages Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases Page.transition_routes.trigger_fulfillment.messages Page.transition_routes.trigger_fulfillment.conditional_cases If not specified, the agent's default language is used. Many languages are supported. Note: languages must be enabled in the agent before they can be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#language_code DialogflowCxPage#language_code}
        :param parent: The flow to create a page for. Format: projects//locations//agents//flows/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parent DialogflowCxPage#parent}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#timeouts DialogflowCxPage#timeouts}
        :param transition_route_groups: Ordered list of TransitionRouteGroups associated with the page. Transition route groups must be unique within a page. If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes. If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence. Format:projects//locations//agents//flows//transitionRouteGroups/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#transition_route_groups DialogflowCxPage#transition_route_groups}
        :param transition_routes: transition_routes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#transition_routes DialogflowCxPage#transition_routes}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(advanced_settings, dict):
            advanced_settings = DialogflowCxPageAdvancedSettings(**advanced_settings)
        if isinstance(entry_fulfillment, dict):
            entry_fulfillment = DialogflowCxPageEntryFulfillment(**entry_fulfillment)
        if isinstance(form, dict):
            form = DialogflowCxPageForm(**form)
        if isinstance(timeouts, dict):
            timeouts = DialogflowCxPageTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15dea158de3b8394ae860686740472a26b1661a6cdee78808233b04283785d3a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument advanced_settings", value=advanced_settings, expected_type=type_hints["advanced_settings"])
            check_type(argname="argument entry_fulfillment", value=entry_fulfillment, expected_type=type_hints["entry_fulfillment"])
            check_type(argname="argument event_handlers", value=event_handlers, expected_type=type_hints["event_handlers"])
            check_type(argname="argument form", value=form, expected_type=type_hints["form"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
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
        if entry_fulfillment is not None:
            self._values["entry_fulfillment"] = entry_fulfillment
        if event_handlers is not None:
            self._values["event_handlers"] = event_handlers
        if form is not None:
            self._values["form"] = form
        if id is not None:
            self._values["id"] = id
        if language_code is not None:
            self._values["language_code"] = language_code
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
        '''The human-readable name of the page, unique within the agent.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#display_name DialogflowCxPage#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def advanced_settings(self) -> typing.Optional[DialogflowCxPageAdvancedSettings]:
        '''advanced_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#advanced_settings DialogflowCxPage#advanced_settings}
        '''
        result = self._values.get("advanced_settings")
        return typing.cast(typing.Optional[DialogflowCxPageAdvancedSettings], result)

    @builtins.property
    def entry_fulfillment(self) -> typing.Optional["DialogflowCxPageEntryFulfillment"]:
        '''entry_fulfillment block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#entry_fulfillment DialogflowCxPage#entry_fulfillment}
        '''
        result = self._values.get("entry_fulfillment")
        return typing.cast(typing.Optional["DialogflowCxPageEntryFulfillment"], result)

    @builtins.property
    def event_handlers(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEventHandlers"]]]:
        '''event_handlers block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#event_handlers DialogflowCxPage#event_handlers}
        '''
        result = self._values.get("event_handlers")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEventHandlers"]]], result)

    @builtins.property
    def form(self) -> typing.Optional["DialogflowCxPageForm"]:
        '''form block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#form DialogflowCxPage#form}
        '''
        result = self._values.get("form")
        return typing.cast(typing.Optional["DialogflowCxPageForm"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#id DialogflowCxPage#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def language_code(self) -> typing.Optional[builtins.str]:
        '''The language of the following fields in page:.

        Page.entry_fulfillment.messages
        Page.entry_fulfillment.conditional_cases
        Page.event_handlers.trigger_fulfillment.messages
        Page.event_handlers.trigger_fulfillment.conditional_cases
        Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages
        Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases
        Page.form.parameters.fill_behavior.reprompt_event_handlers.messages
        Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases
        Page.transition_routes.trigger_fulfillment.messages
        Page.transition_routes.trigger_fulfillment.conditional_cases
        If not specified, the agent's default language is used. Many languages are supported. Note: languages must be enabled in the agent before they can be used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#language_code DialogflowCxPage#language_code}
        '''
        result = self._values.get("language_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent(self) -> typing.Optional[builtins.str]:
        '''The flow to create a page for. Format: projects//locations//agents//flows/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parent DialogflowCxPage#parent}
        '''
        result = self._values.get("parent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DialogflowCxPageTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#timeouts DialogflowCxPage#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DialogflowCxPageTimeouts"], result)

    @builtins.property
    def transition_route_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Ordered list of TransitionRouteGroups associated with the page.

        Transition route groups must be unique within a page.
        If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes.
        If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence.
        Format:projects//locations//agents//flows//transitionRouteGroups/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#transition_route_groups DialogflowCxPage#transition_route_groups}
        '''
        result = self._values.get("transition_route_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def transition_routes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageTransitionRoutes"]]]:
        '''transition_routes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#transition_routes DialogflowCxPage#transition_routes}
        '''
        result = self._values.get("transition_routes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageTransitionRoutes"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillment",
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
class DialogflowCxPageEntryFulfillment:
    def __init__(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEntryFulfillmentConditionalCases", typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEntryFulfillmentMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEntryFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71dd5966ad8a933ab4a894dbb073a900bc484ab8d156c35b52c846bd0603c4a6)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEntryFulfillmentConditionalCases"]]]:
        '''conditional_cases block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        '''
        result = self._values.get("conditional_cases")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEntryFulfillmentConditionalCases"]]], result)

    @builtins.property
    def messages(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEntryFulfillmentMessages"]]]:
        '''messages block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        '''
        result = self._values.get("messages")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEntryFulfillmentMessages"]]], result)

    @builtins.property
    def return_partial_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs.

        If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        '''
        result = self._values.get("return_partial_responses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def set_parameter_actions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEntryFulfillmentSetParameterActions"]]]:
        '''set_parameter_actions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        '''
        result = self._values.get("set_parameter_actions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEntryFulfillmentSetParameterActions"]]], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The tag used by the webhook to identify which fulfillment is being called.

        This field is required if webhook is specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook(self) -> typing.Optional[builtins.str]:
        '''The webhook to call. Format: projects//locations//agents//webhooks/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEntryFulfillment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentConditionalCases",
    jsii_struct_bases=[],
    name_mapping={"cases": "cases"},
)
class DialogflowCxPageEntryFulfillmentConditionalCases:
    def __init__(self, *, cases: typing.Optional[builtins.str] = None) -> None:
        '''
        :param cases: A JSON encoded list of cascading if-else conditions. Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored. See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#cases DialogflowCxPage#cases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41d585dc3d116965de82971528c72684a85e927c44d68a81038ea69b7f119f8a)
            check_type(argname="argument cases", value=cases, expected_type=type_hints["cases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cases is not None:
            self._values["cases"] = cases

    @builtins.property
    def cases(self) -> typing.Optional[builtins.str]:
        '''A JSON encoded list of cascading if-else conditions.

        Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored.
        See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#cases DialogflowCxPage#cases}
        '''
        result = self._values.get("cases")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEntryFulfillmentConditionalCases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEntryFulfillmentConditionalCasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentConditionalCasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d18c361d178af1f929fc21abbb6c93e795037e235b2566981a2e3d6d19f33b9d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageEntryFulfillmentConditionalCasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03e8ee129a863240770c9caeab6149676d1928c16dd220aafa9bc9fae864f07d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageEntryFulfillmentConditionalCasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffc9ac7dad5e7eabc3e774ea725f330c6250d16ff9aa3be598cfbb6f04444858)
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
            type_hints = typing.get_type_hints(_typecheckingstub__51a96b2d25253a2999b85199244f765c608871440ff03f222fca52ba0fada650)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d5afc08592983725d0cd6463f6fe0f8740aeaddcef4a55fa7370537dec6a243)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentConditionalCases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentConditionalCases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e5f19ea9f7e0ad208a668db2c77f3d9689f078e5da3595d7c973acdbdadccbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageEntryFulfillmentConditionalCasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentConditionalCasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec79794d2732ecc45da2c799893f6a112a3ceb72481aceb851b0bb910c0a2480)
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
            type_hints = typing.get_type_hints(_typecheckingstub__74a3aeb5acba7e3dc70f2aebae4704ff0bc86115cbf6397991134015b1385987)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cases", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEntryFulfillmentConditionalCases]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEntryFulfillmentConditionalCases]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEntryFulfillmentConditionalCases]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da5c278a715b2ec6b510e85dcf4cbb2951593f74d50e9b23a7f020cd55745e0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessages",
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
class DialogflowCxPageEntryFulfillmentMessages:
    def __init__(
        self,
        *,
        channel: typing.Optional[builtins.str] = None,
        conversation_success: typing.Optional[typing.Union["DialogflowCxPageEntryFulfillmentMessagesConversationSuccess", typing.Dict[builtins.str, typing.Any]]] = None,
        live_agent_handoff: typing.Optional[typing.Union["DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff", typing.Dict[builtins.str, typing.Any]]] = None,
        output_audio_text: typing.Optional[typing.Union["DialogflowCxPageEntryFulfillmentMessagesOutputAudioText", typing.Dict[builtins.str, typing.Any]]] = None,
        payload: typing.Optional[builtins.str] = None,
        play_audio: typing.Optional[typing.Union["DialogflowCxPageEntryFulfillmentMessagesPlayAudio", typing.Dict[builtins.str, typing.Any]]] = None,
        telephony_transfer_call: typing.Optional[typing.Union["DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall", typing.Dict[builtins.str, typing.Any]]] = None,
        text: typing.Optional[typing.Union["DialogflowCxPageEntryFulfillmentMessagesText", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param channel: The channel which the response is associated with. Clients can specify the channel via QueryParameters.channel, and only associated channel response will be returned. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#channel DialogflowCxPage#channel}
        :param conversation_success: conversation_success block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conversation_success DialogflowCxPage#conversation_success}
        :param live_agent_handoff: live_agent_handoff block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#live_agent_handoff DialogflowCxPage#live_agent_handoff}
        :param output_audio_text: output_audio_text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#output_audio_text DialogflowCxPage#output_audio_text}
        :param payload: A custom, platform-specific payload. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#payload DialogflowCxPage#payload}
        :param play_audio: play_audio block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#play_audio DialogflowCxPage#play_audio}
        :param telephony_transfer_call: telephony_transfer_call block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#telephony_transfer_call DialogflowCxPage#telephony_transfer_call}
        :param text: text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if isinstance(conversation_success, dict):
            conversation_success = DialogflowCxPageEntryFulfillmentMessagesConversationSuccess(**conversation_success)
        if isinstance(live_agent_handoff, dict):
            live_agent_handoff = DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff(**live_agent_handoff)
        if isinstance(output_audio_text, dict):
            output_audio_text = DialogflowCxPageEntryFulfillmentMessagesOutputAudioText(**output_audio_text)
        if isinstance(play_audio, dict):
            play_audio = DialogflowCxPageEntryFulfillmentMessagesPlayAudio(**play_audio)
        if isinstance(telephony_transfer_call, dict):
            telephony_transfer_call = DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall(**telephony_transfer_call)
        if isinstance(text, dict):
            text = DialogflowCxPageEntryFulfillmentMessagesText(**text)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49dcdce78eeddc0ea0c91912a267826414666a09fd42e6c12aabefd14ac01d58)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#channel DialogflowCxPage#channel}
        '''
        result = self._values.get("channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conversation_success(
        self,
    ) -> typing.Optional["DialogflowCxPageEntryFulfillmentMessagesConversationSuccess"]:
        '''conversation_success block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conversation_success DialogflowCxPage#conversation_success}
        '''
        result = self._values.get("conversation_success")
        return typing.cast(typing.Optional["DialogflowCxPageEntryFulfillmentMessagesConversationSuccess"], result)

    @builtins.property
    def live_agent_handoff(
        self,
    ) -> typing.Optional["DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff"]:
        '''live_agent_handoff block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#live_agent_handoff DialogflowCxPage#live_agent_handoff}
        '''
        result = self._values.get("live_agent_handoff")
        return typing.cast(typing.Optional["DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff"], result)

    @builtins.property
    def output_audio_text(
        self,
    ) -> typing.Optional["DialogflowCxPageEntryFulfillmentMessagesOutputAudioText"]:
        '''output_audio_text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#output_audio_text DialogflowCxPage#output_audio_text}
        '''
        result = self._values.get("output_audio_text")
        return typing.cast(typing.Optional["DialogflowCxPageEntryFulfillmentMessagesOutputAudioText"], result)

    @builtins.property
    def payload(self) -> typing.Optional[builtins.str]:
        '''A custom, platform-specific payload.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#payload DialogflowCxPage#payload}
        '''
        result = self._values.get("payload")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def play_audio(
        self,
    ) -> typing.Optional["DialogflowCxPageEntryFulfillmentMessagesPlayAudio"]:
        '''play_audio block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#play_audio DialogflowCxPage#play_audio}
        '''
        result = self._values.get("play_audio")
        return typing.cast(typing.Optional["DialogflowCxPageEntryFulfillmentMessagesPlayAudio"], result)

    @builtins.property
    def telephony_transfer_call(
        self,
    ) -> typing.Optional["DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall"]:
        '''telephony_transfer_call block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#telephony_transfer_call DialogflowCxPage#telephony_transfer_call}
        '''
        result = self._values.get("telephony_transfer_call")
        return typing.cast(typing.Optional["DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall"], result)

    @builtins.property
    def text(self) -> typing.Optional["DialogflowCxPageEntryFulfillmentMessagesText"]:
        '''text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional["DialogflowCxPageEntryFulfillmentMessagesText"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEntryFulfillmentMessages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesConversationSuccess",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class DialogflowCxPageEntryFulfillmentMessagesConversationSuccess:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4a589cb1b88663ef1899817b26ef8f98b20e8d574d0471c301d0cffba3dd4e6)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEntryFulfillmentMessagesConversationSuccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEntryFulfillmentMessagesConversationSuccessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesConversationSuccessOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c8d944cd5967b8535e11da8f08fd7311914c1ec0c5301049a714b0b9164d517)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f591106f876e9bb6fe5a9193ad22e7a4c21d31bc64fa8614c89b3a41f5ce74b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageEntryFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[DialogflowCxPageEntryFulfillmentMessagesConversationSuccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEntryFulfillmentMessagesConversationSuccess],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86b65a910fab838aee783af7bc580bd4f7d92e2b2afd5eae3ba600fb8b171f98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageEntryFulfillmentMessagesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5613dd1beaa1c4997bacf84707ddd469dc64ba513ea84f5c4ac9ea66c8a7ef5e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageEntryFulfillmentMessagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53cde70270348affee1882e2e525e8548831b8bc3b03c0b9e7af48627d403993)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageEntryFulfillmentMessagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0b049268bb985919745730a00796bf11fec3b1a9ad23a3d64efc1a5341d53c4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a2a5e2487adb1d43930ada8e1d15166b55fb0d6cc408b1652e516e9bef05f00)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ece63606e5d8c191695e3bcc239c17141277efbde4acd74764a2c15ac2777d7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentMessages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentMessages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79182987451d800a73bc1c3badae415bba1d3ed46a2c34fc6cbf27a2c1d0d3d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1af518f20749fd68eb9f57c02271445ed79c9fb61c5735c1016ccd32a2aba71d)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoffOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoffOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8df7cb7ddd056fdeb6d2a239386b1b334eb0eba4454c3d75c8b0474032cd3a61)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3bc1a4f84ede5c40aba6192875fde441ca1f020f6661a1dcf48a5133ccf265b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__559614559c63021e07e09edae87cf64a2b3b0b1505fa1d624f3f1bdd1767add6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesOutputAudioText",
    jsii_struct_bases=[],
    name_mapping={"ssml": "ssml", "text": "text"},
)
class DialogflowCxPageEntryFulfillmentMessagesOutputAudioText:
    def __init__(
        self,
        *,
        ssml: typing.Optional[builtins.str] = None,
        text: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__193bdaf74ac9a22e2eb8d8c7c41a54852e77637a20bb9acd6ebc6eb6b4f2c8f1)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        '''
        result = self._values.get("ssml")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def text(self) -> typing.Optional[builtins.str]:
        '''The raw text to be synthesized.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEntryFulfillmentMessagesOutputAudioText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEntryFulfillmentMessagesOutputAudioTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesOutputAudioTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__47af714731e870cc6332f67efe01c0fc73db3868b3d2a2ec72791d03c59e4d50)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae7c619be871b2c23e56301ea7e00bd39110981b1709b633c923d174b2b13578)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssml", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed475c8c4ae6606312100e1dcd8aeb0a6e031736372ec454c1fcdfede1a2abd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageEntryFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[DialogflowCxPageEntryFulfillmentMessagesOutputAudioText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEntryFulfillmentMessagesOutputAudioText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42e20a3231560ddfd90345ff896126dabdc7c0b18dbb3dc1f766c0d202775c27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageEntryFulfillmentMessagesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__978c8cc08cabca00f1aff704c0f4ca333e794550678a0521cb8c306bfd798d22)
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
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        value = DialogflowCxPageEntryFulfillmentMessagesConversationSuccess(
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
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        value = DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff(
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
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        value = DialogflowCxPageEntryFulfillmentMessagesOutputAudioText(
            ssml=ssml, text=text
        )

        return typing.cast(None, jsii.invoke(self, "putOutputAudioText", [value]))

    @jsii.member(jsii_name="putPlayAudio")
    def put_play_audio(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        value = DialogflowCxPageEntryFulfillmentMessagesPlayAudio(audio_uri=audio_uri)

        return typing.cast(None, jsii.invoke(self, "putPlayAudio", [value]))

    @jsii.member(jsii_name="putTelephonyTransferCall")
    def put_telephony_transfer_call(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        value = DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall(
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
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        value = DialogflowCxPageEntryFulfillmentMessagesText(text=text)

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
    ) -> DialogflowCxPageEntryFulfillmentMessagesConversationSuccessOutputReference:
        return typing.cast(DialogflowCxPageEntryFulfillmentMessagesConversationSuccessOutputReference, jsii.get(self, "conversationSuccess"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoffOutputReference:
        return typing.cast(DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoffOutputReference, jsii.get(self, "liveAgentHandoff"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioText")
    def output_audio_text(
        self,
    ) -> DialogflowCxPageEntryFulfillmentMessagesOutputAudioTextOutputReference:
        return typing.cast(DialogflowCxPageEntryFulfillmentMessagesOutputAudioTextOutputReference, jsii.get(self, "outputAudioText"))

    @builtins.property
    @jsii.member(jsii_name="playAudio")
    def play_audio(
        self,
    ) -> "DialogflowCxPageEntryFulfillmentMessagesPlayAudioOutputReference":
        return typing.cast("DialogflowCxPageEntryFulfillmentMessagesPlayAudioOutputReference", jsii.get(self, "playAudio"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> "DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCallOutputReference":
        return typing.cast("DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCallOutputReference", jsii.get(self, "telephonyTransferCall"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> "DialogflowCxPageEntryFulfillmentMessagesTextOutputReference":
        return typing.cast("DialogflowCxPageEntryFulfillmentMessagesTextOutputReference", jsii.get(self, "text"))

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="conversationSuccessInput")
    def conversation_success_input(
        self,
    ) -> typing.Optional[DialogflowCxPageEntryFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[DialogflowCxPageEntryFulfillmentMessagesConversationSuccess], jsii.get(self, "conversationSuccessInput"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoffInput")
    def live_agent_handoff_input(
        self,
    ) -> typing.Optional[DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "liveAgentHandoffInput"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioTextInput")
    def output_audio_text_input(
        self,
    ) -> typing.Optional[DialogflowCxPageEntryFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[DialogflowCxPageEntryFulfillmentMessagesOutputAudioText], jsii.get(self, "outputAudioTextInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadInput")
    def payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadInput"))

    @builtins.property
    @jsii.member(jsii_name="playAudioInput")
    def play_audio_input(
        self,
    ) -> typing.Optional["DialogflowCxPageEntryFulfillmentMessagesPlayAudio"]:
        return typing.cast(typing.Optional["DialogflowCxPageEntryFulfillmentMessagesPlayAudio"], jsii.get(self, "playAudioInput"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCallInput")
    def telephony_transfer_call_input(
        self,
    ) -> typing.Optional["DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall"]:
        return typing.cast(typing.Optional["DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall"], jsii.get(self, "telephonyTransferCallInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(
        self,
    ) -> typing.Optional["DialogflowCxPageEntryFulfillmentMessagesText"]:
        return typing.cast(typing.Optional["DialogflowCxPageEntryFulfillmentMessagesText"], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channel"))

    @channel.setter
    def channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9048c88fcf0bdbf04311e892010e897c134b22a199287054645ba372888e83e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="payload")
    def payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payload"))

    @payload.setter
    def payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0737bb7d2bf1ab370586e8fd5193565c739be41572fb587cfdc1966b22982e64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payload", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEntryFulfillmentMessages]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEntryFulfillmentMessages]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEntryFulfillmentMessages]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eb85a40a6a8463d7214548943b5c9b4a6e000998bf7771a4cc4d99b60541a6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesPlayAudio",
    jsii_struct_bases=[],
    name_mapping={"audio_uri": "audioUri"},
)
class DialogflowCxPageEntryFulfillmentMessagesPlayAudio:
    def __init__(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab8a645c5c6e3de3b3e18b28afae319c59913634ae339ae458dc9f365861d1e0)
            check_type(argname="argument audio_uri", value=audio_uri, expected_type=type_hints["audio_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "audio_uri": audio_uri,
        }

    @builtins.property
    def audio_uri(self) -> builtins.str:
        '''URI of the audio clip.

        Dialogflow does not impose any validation on this value. It is specific to the client that reads it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        result = self._values.get("audio_uri")
        assert result is not None, "Required property 'audio_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEntryFulfillmentMessagesPlayAudio(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEntryFulfillmentMessagesPlayAudioOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesPlayAudioOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__75a9a00557be1848acf544cd57804f2a4ad2c050104a1b1dcab41387b892feb6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f7891d3f220d986aba00f1d05f173f5c63233b436807eb0b5119f5aa2483741)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageEntryFulfillmentMessagesPlayAudio]:
        return typing.cast(typing.Optional[DialogflowCxPageEntryFulfillmentMessagesPlayAudio], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEntryFulfillmentMessagesPlayAudio],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0831571feddf981b35ca781a775b03e67acb855916885941e378c2e6d352b95f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall",
    jsii_struct_bases=[],
    name_mapping={"phone_number": "phoneNumber"},
)
class DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall:
    def __init__(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af500d65bfacaf611bc0a3d20a4dcee4edf2f2c1ec83fa1c5ab78af5066cb5d5)
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "phone_number": phone_number,
        }

    @builtins.property
    def phone_number(self) -> builtins.str:
        '''Transfer the call to a phone number in E.164 format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        result = self._values.get("phone_number")
        assert result is not None, "Required property 'phone_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCallOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCallOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad6b39b3f1f34ee5f8d0d03ad62e7f453c3b5c89393c489980d9755adaf3163f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9b85f615c8657afba54eed25b21d89f9488a7bbd9438fe43f3145f3edf16661)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall]:
        return typing.cast(typing.Optional[DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd099ead23f7f734dd83bc1343aa01c43829514773a8736c5fcf3c67bba27290)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesText",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class DialogflowCxPageEntryFulfillmentMessagesText:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2af505c57abee7200d8cb160c49ca52acbdeb6045dcf61e0299d03ae4462e2e5)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A collection of text responses.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEntryFulfillmentMessagesText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEntryFulfillmentMessagesTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentMessagesTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8661eaff956649f29f0c4634e31a442cbda0042f98ac148a7989a0a38c3134d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ab95389349952923469867e7d785dd27cc8126be5a7fb954b8921bd723e0772)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageEntryFulfillmentMessagesText]:
        return typing.cast(typing.Optional[DialogflowCxPageEntryFulfillmentMessagesText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEntryFulfillmentMessagesText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4b9d1b0c7d1369c62bedcde8087eb7e0cb0ce75d9b6d46e69ce807b8b79761f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageEntryFulfillmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cf5a596e516e17c71d09575c4630fc024c4b377f48befe7d2196de54f1ea335)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConditionalCases")
    def put_conditional_cases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEntryFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcc90f3bff330387d00e7f39c374cd2f3953e49596ff0f3fc02630bd52e2f7bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConditionalCases", [value]))

    @jsii.member(jsii_name="putMessages")
    def put_messages(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEntryFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b6ce8c3783fc7922600009c1d473f5b8d45842feaf69470d2a4327ba31acf83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessages", [value]))

    @jsii.member(jsii_name="putSetParameterActions")
    def put_set_parameter_actions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEntryFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57502e370be1f5d844f21c5be3a7c4687d452a400160fa5c97137bb4e45ccc65)
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
    def conditional_cases(self) -> DialogflowCxPageEntryFulfillmentConditionalCasesList:
        return typing.cast(DialogflowCxPageEntryFulfillmentConditionalCasesList, jsii.get(self, "conditionalCases"))

    @builtins.property
    @jsii.member(jsii_name="messages")
    def messages(self) -> DialogflowCxPageEntryFulfillmentMessagesList:
        return typing.cast(DialogflowCxPageEntryFulfillmentMessagesList, jsii.get(self, "messages"))

    @builtins.property
    @jsii.member(jsii_name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> "DialogflowCxPageEntryFulfillmentSetParameterActionsList":
        return typing.cast("DialogflowCxPageEntryFulfillmentSetParameterActionsList", jsii.get(self, "setParameterActions"))

    @builtins.property
    @jsii.member(jsii_name="conditionalCasesInput")
    def conditional_cases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentConditionalCases]]], jsii.get(self, "conditionalCasesInput"))

    @builtins.property
    @jsii.member(jsii_name="messagesInput")
    def messages_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentMessages]]], jsii.get(self, "messagesInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEntryFulfillmentSetParameterActions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEntryFulfillmentSetParameterActions"]]], jsii.get(self, "setParameterActionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__cbd86b9b7707148d069906ee7224ad618eeb0dc32bcfee1d62d3e8206537ad00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnPartialResponses", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24318a5fce06525c2d5464aa0c7964f88d07f141aec66952bf53a7f4cf11c085)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhook"))

    @webhook.setter
    def webhook(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b645a2f56947e96ce4b3003b366455c62ea637fbf309739d31fefc614ea0b21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhook", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DialogflowCxPageEntryFulfillment]:
        return typing.cast(typing.Optional[DialogflowCxPageEntryFulfillment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEntryFulfillment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10309df25d5605b800644921bf8f526cb3c9e566898cc810cd376f608db1d365)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentSetParameterActions",
    jsii_struct_bases=[],
    name_mapping={"parameter": "parameter", "value": "value"},
)
class DialogflowCxPageEntryFulfillmentSetParameterActions:
    def __init__(
        self,
        *,
        parameter: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param parameter: Display name of the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parameter DialogflowCxPage#parameter}
        :param value: The new JSON-encoded value of the parameter. A null value clears the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#value DialogflowCxPage#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__008dc86fbfe60acf8c7e060533552e76880507e7e07dd3d0983f8ad6cc18abac)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parameter DialogflowCxPage#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The new JSON-encoded value of the parameter. A null value clears the parameter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#value DialogflowCxPage#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEntryFulfillmentSetParameterActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEntryFulfillmentSetParameterActionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentSetParameterActionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3cdd468595e99ef46db7929bcb251a7e560fe4928b72161bcf7a5885ae532859)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageEntryFulfillmentSetParameterActionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f048139d4a6d7a94700cb12c28ed62c4b7ba9a47087246c5308af68b9a7c1d7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageEntryFulfillmentSetParameterActionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16f15cabb2c7e2f61c531e7a15d14596e45a2bfe6754ea2cae2e92ad6b64f3bd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c330d94d480fdaa6fd47482b25638e318cd782d41acffcf63a5296f55b41f87)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9b663fd15f365a76c6977f7eb04ae721694c608be1e45ce4a1450eb947b1dc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentSetParameterActions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentSetParameterActions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentSetParameterActions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79c8b2935763b659bb79dd483521583b5876c5b045b0b944c94f2556a3585105)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageEntryFulfillmentSetParameterActionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEntryFulfillmentSetParameterActionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c18bd735bfcb498b463c6ed802273bba27ae4dde5801c199514349a2668e2dba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ceb98c9d2d83adcf22e0e9fcba0ef4ae7cd38e7024cd766d3beb6f5fad24fd49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameter", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25e5748382338ac15293400853f0dfa7c43f83171ce8fb32be6036ca799c4397)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEntryFulfillmentSetParameterActions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEntryFulfillmentSetParameterActions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEntryFulfillmentSetParameterActions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e4689a195cb80e1ccb492b424c3d029a76f4ca24bb35064db553a362c8f81a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlers",
    jsii_struct_bases=[],
    name_mapping={
        "event": "event",
        "target_flow": "targetFlow",
        "target_page": "targetPage",
        "trigger_fulfillment": "triggerFulfillment",
    },
)
class DialogflowCxPageEventHandlers:
    def __init__(
        self,
        *,
        event: typing.Optional[builtins.str] = None,
        target_flow: typing.Optional[builtins.str] = None,
        target_page: typing.Optional[builtins.str] = None,
        trigger_fulfillment: typing.Optional[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillment", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param event: The name of the event to handle. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#event DialogflowCxPage#event}
        :param target_flow: The target flow to transition to. Format: projects//locations//agents//flows/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#target_flow DialogflowCxPage#target_flow}
        :param target_page: The target page to transition to. Format: projects//locations//agents//flows//pages/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#target_page DialogflowCxPage#target_page}
        :param trigger_fulfillment: trigger_fulfillment block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#trigger_fulfillment DialogflowCxPage#trigger_fulfillment}
        '''
        if isinstance(trigger_fulfillment, dict):
            trigger_fulfillment = DialogflowCxPageEventHandlersTriggerFulfillment(**trigger_fulfillment)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab15ae117f88b8ab8fd8faf8aec04359c52d2bb628fb3aedb74fe47fb030fea3)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#event DialogflowCxPage#event}
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_flow(self) -> typing.Optional[builtins.str]:
        '''The target flow to transition to. Format: projects//locations//agents//flows/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#target_flow DialogflowCxPage#target_flow}
        '''
        result = self._values.get("target_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_page(self) -> typing.Optional[builtins.str]:
        '''The target page to transition to. Format: projects//locations//agents//flows//pages/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#target_page DialogflowCxPage#target_page}
        '''
        result = self._values.get("target_page")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger_fulfillment(
        self,
    ) -> typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillment"]:
        '''trigger_fulfillment block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#trigger_fulfillment DialogflowCxPage#trigger_fulfillment}
        '''
        result = self._values.get("trigger_fulfillment")
        return typing.cast(typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEventHandlers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEventHandlersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f48919b767e503e9429acd9d3e0a43fef8f6804bfdf093b76df95d7974fb01ce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DialogflowCxPageEventHandlersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99fd9f7ace6de457684cd2263bcf553bccf5a4132d11b5e104fd50c38ab993c2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageEventHandlersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__704628615f089436d926563e2c4e31a8c56127f782256aaf1c6317f526c24f12)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c6c38eec91174f13ad2674fa21c807337c2d523dbb823e4e349e40ca4565700)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa978b017a1129446a73455a4aaf3915220f91390219633c8c0a5ebf7116dde8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlers]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83899170e1dcdea3831dc32fff8e1c65e55ca19c81de5d04e69f956a26356d3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageEventHandlersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c16d64c2902739d0451fc9721d989939a3db705e3abc8772178d61174e6ee240)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTriggerFulfillment")
    def put_trigger_fulfillment(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases", typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillmentMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        value = DialogflowCxPageEventHandlersTriggerFulfillment(
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
    ) -> "DialogflowCxPageEventHandlersTriggerFulfillmentOutputReference":
        return typing.cast("DialogflowCxPageEventHandlersTriggerFulfillmentOutputReference", jsii.get(self, "triggerFulfillment"))

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
    ) -> typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillment"]:
        return typing.cast(typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillment"], jsii.get(self, "triggerFulfillmentInput"))

    @builtins.property
    @jsii.member(jsii_name="event")
    def event(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "event"))

    @event.setter
    def event(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba7ddce87ad187e41cf2fb78f5cd6b91e99596c7b1e0974e078ff13f602fc460)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "event", value)

    @builtins.property
    @jsii.member(jsii_name="targetFlow")
    def target_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetFlow"))

    @target_flow.setter
    def target_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a794fd7c5be69446637ecba757d7b8f0c3dfb01006c944ea56bd7a0d33c1eda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetFlow", value)

    @builtins.property
    @jsii.member(jsii_name="targetPage")
    def target_page(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPage"))

    @target_page.setter
    def target_page(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db807ca0284018e651a6273faaa938bd71e046cb9809ed9cf754724cc8ff08f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlers]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlers]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlers]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__690a4cec683b9279070b86397597c918de83137b42754288560bb683613c7b40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillment",
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
class DialogflowCxPageEventHandlersTriggerFulfillment:
    def __init__(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases", typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillmentMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bf85d749a19598291bf90632116cb8cb83eb3f2a07c3e7ea06b5b228e5f520c)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases"]]]:
        '''conditional_cases block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        '''
        result = self._values.get("conditional_cases")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases"]]], result)

    @builtins.property
    def messages(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEventHandlersTriggerFulfillmentMessages"]]]:
        '''messages block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        '''
        result = self._values.get("messages")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEventHandlersTriggerFulfillmentMessages"]]], result)

    @builtins.property
    def return_partial_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs.

        If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        '''
        result = self._values.get("return_partial_responses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def set_parameter_actions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions"]]]:
        '''set_parameter_actions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        '''
        result = self._values.get("set_parameter_actions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions"]]], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The tag used by the webhook to identify which fulfillment is being called.

        This field is required if webhook is specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook(self) -> typing.Optional[builtins.str]:
        '''The webhook to call. Format: projects//locations//agents//webhooks/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEventHandlersTriggerFulfillment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases",
    jsii_struct_bases=[],
    name_mapping={"cases": "cases"},
)
class DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases:
    def __init__(self, *, cases: typing.Optional[builtins.str] = None) -> None:
        '''
        :param cases: A JSON encoded list of cascading if-else conditions. Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored. See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#cases DialogflowCxPage#cases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__376d46d915f41b280a077a263fed3d085e118c282b803747288126e5b7e2781d)
            check_type(argname="argument cases", value=cases, expected_type=type_hints["cases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cases is not None:
            self._values["cases"] = cases

    @builtins.property
    def cases(self) -> typing.Optional[builtins.str]:
        '''A JSON encoded list of cascading if-else conditions.

        Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored.
        See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#cases DialogflowCxPage#cases}
        '''
        result = self._values.get("cases")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__41dff1cc77a79e28e79a5c0156779a0bbfb7747192543f6a12180951ac4acb4b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daf586672edc31eef11808497d6bd13665e436947d1c98c9e1e4c0ee0217ecaa)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01eb83ee56df19bf34d5bdfd605df29554ef3dc6b472213b1cb5f99a2d6f0190)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9dec8da5d11c3ef7ffc5d49d24f650a6d108acb47ca9542e9b37544c70c2b09e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea38da542ad8b4a7c57fde79d259afd66557cdb1acdbf8c249a4a98c1619c5ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e870d5668ecdcbfa994a79f894b6a4b8dc69b7b88c89f877cb0a1b337a6b4b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b658bb5a1025911b1e5de2d943b9cde04ee802d49af1f290e618fbbcfa892d6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad4c4f88c3c8922cb35158f3cf2cbe4baec67a692c27f7074164746f909581a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cases", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b143f9c90d9da1487c71c07c4772ddae68ba73896208cc6461c2dab1c0c1f3dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessages",
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
class DialogflowCxPageEventHandlersTriggerFulfillmentMessages:
    def __init__(
        self,
        *,
        channel: typing.Optional[builtins.str] = None,
        conversation_success: typing.Optional[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess", typing.Dict[builtins.str, typing.Any]]] = None,
        live_agent_handoff: typing.Optional[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff", typing.Dict[builtins.str, typing.Any]]] = None,
        output_audio_text: typing.Optional[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText", typing.Dict[builtins.str, typing.Any]]] = None,
        payload: typing.Optional[builtins.str] = None,
        play_audio: typing.Optional[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio", typing.Dict[builtins.str, typing.Any]]] = None,
        telephony_transfer_call: typing.Optional[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall", typing.Dict[builtins.str, typing.Any]]] = None,
        text: typing.Optional[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param channel: The channel which the response is associated with. Clients can specify the channel via QueryParameters.channel, and only associated channel response will be returned. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#channel DialogflowCxPage#channel}
        :param conversation_success: conversation_success block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conversation_success DialogflowCxPage#conversation_success}
        :param live_agent_handoff: live_agent_handoff block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#live_agent_handoff DialogflowCxPage#live_agent_handoff}
        :param output_audio_text: output_audio_text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#output_audio_text DialogflowCxPage#output_audio_text}
        :param payload: A custom, platform-specific payload. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#payload DialogflowCxPage#payload}
        :param play_audio: play_audio block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#play_audio DialogflowCxPage#play_audio}
        :param telephony_transfer_call: telephony_transfer_call block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#telephony_transfer_call DialogflowCxPage#telephony_transfer_call}
        :param text: text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if isinstance(conversation_success, dict):
            conversation_success = DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess(**conversation_success)
        if isinstance(live_agent_handoff, dict):
            live_agent_handoff = DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff(**live_agent_handoff)
        if isinstance(output_audio_text, dict):
            output_audio_text = DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText(**output_audio_text)
        if isinstance(play_audio, dict):
            play_audio = DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio(**play_audio)
        if isinstance(telephony_transfer_call, dict):
            telephony_transfer_call = DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall(**telephony_transfer_call)
        if isinstance(text, dict):
            text = DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText(**text)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a679968c0dafaadba2798a1411ce95bbd5875be78731f6ecd46d11a12ed922e)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#channel DialogflowCxPage#channel}
        '''
        result = self._values.get("channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conversation_success(
        self,
    ) -> typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess"]:
        '''conversation_success block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conversation_success DialogflowCxPage#conversation_success}
        '''
        result = self._values.get("conversation_success")
        return typing.cast(typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess"], result)

    @builtins.property
    def live_agent_handoff(
        self,
    ) -> typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff"]:
        '''live_agent_handoff block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#live_agent_handoff DialogflowCxPage#live_agent_handoff}
        '''
        result = self._values.get("live_agent_handoff")
        return typing.cast(typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff"], result)

    @builtins.property
    def output_audio_text(
        self,
    ) -> typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText"]:
        '''output_audio_text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#output_audio_text DialogflowCxPage#output_audio_text}
        '''
        result = self._values.get("output_audio_text")
        return typing.cast(typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText"], result)

    @builtins.property
    def payload(self) -> typing.Optional[builtins.str]:
        '''A custom, platform-specific payload.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#payload DialogflowCxPage#payload}
        '''
        result = self._values.get("payload")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def play_audio(
        self,
    ) -> typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio"]:
        '''play_audio block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#play_audio DialogflowCxPage#play_audio}
        '''
        result = self._values.get("play_audio")
        return typing.cast(typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio"], result)

    @builtins.property
    def telephony_transfer_call(
        self,
    ) -> typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall"]:
        '''telephony_transfer_call block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#telephony_transfer_call DialogflowCxPage#telephony_transfer_call}
        '''
        result = self._values.get("telephony_transfer_call")
        return typing.cast(typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall"], result)

    @builtins.property
    def text(
        self,
    ) -> typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText"]:
        '''text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEventHandlersTriggerFulfillmentMessages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66d3776604393cf66068ec3466c5254d1e5c62a980a678f84858c1ae1935682d)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b82e9c9e4b31d07b4443b1788b23c9f2021882a8ffef4b35df4d3d9599e83c9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__996ae780b3f3289b0455b9dadaed66e529667d87c80d42514c8c69854ef001cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb0e7f666cd5fe7bd145254a8f80cf6286ceaac9fb602e64ae005175a00e903c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7054c86f78ebd73f2060ccd90e4b44d98e17035b3521570d1f87ce1a94fdf970)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41b46a1306a40dbbf9c194373c8e9db9c08762b35720cdee57b8d115fedf837a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d9004a8ad19edb50b32e3313eca72dd1806d9633b44caca9269c8562c3670cb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__45b5feef79154b39af79071966d0cfc866e728cf3f1af74dbd11bd008d36432e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b466fdf978aa50076148da2875059e5ff1c18a47c0f8b843641d9b9188de043)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentMessages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentMessages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2216f34163c046069ee6e1f70f7998905b8acd7830b52141970506a17e735e18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c8a575ddbefc9dea3ed7744844cbbbfd63555d8e6cba3db07cad82e69e4aa96)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__96fc7d0c61e49a89053b4e8cd27f5aac3842179ccee836156b55717048a9aa0e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__798ba3eaf78d35b7a739dc09bd38735a760dfdcdca5e4d64ba0fcf945d2015de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5560c3182df387dafed740a8c580bd87c7443414c99cc85ad439251920c1adee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText",
    jsii_struct_bases=[],
    name_mapping={"ssml": "ssml", "text": "text"},
)
class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText:
    def __init__(
        self,
        *,
        ssml: typing.Optional[builtins.str] = None,
        text: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d41a2c2abfb25b3f1b0a30724aa72dfbb48ee7c970dcd611866f4c47d04eb2ce)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        '''
        result = self._values.get("ssml")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def text(self) -> typing.Optional[builtins.str]:
        '''The raw text to be synthesized.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4835a111619019130dd658632c355fbec8125dcb0a102fd66d1efec86dbe65bd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b47ddf16cf9a4681bb42d6d76c58148ff264b2a6789afc9b356f8a0bff51c88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssml", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e9424bb5cf73646e5af9d43693123cf4e4fb62835edf8e7bfae07df6e01a24e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c6d1355cb9118fd4f33f6235a18a4b9379fa91edacb95c4e87fd108cf1dcc02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef85f5b2e690787853b09a1c94e44953b01462c653d948cf21e58cbb64b7089a)
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
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        value = DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess(
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
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        value = DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff(
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
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        value = DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText(
            ssml=ssml, text=text
        )

        return typing.cast(None, jsii.invoke(self, "putOutputAudioText", [value]))

    @jsii.member(jsii_name="putPlayAudio")
    def put_play_audio(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        value = DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio(
            audio_uri=audio_uri
        )

        return typing.cast(None, jsii.invoke(self, "putPlayAudio", [value]))

    @jsii.member(jsii_name="putTelephonyTransferCall")
    def put_telephony_transfer_call(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        value = DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall(
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
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        value = DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText(text=text)

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
    ) -> DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference:
        return typing.cast(DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference, jsii.get(self, "conversationSuccess"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference:
        return typing.cast(DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference, jsii.get(self, "liveAgentHandoff"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioText")
    def output_audio_text(
        self,
    ) -> DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference:
        return typing.cast(DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference, jsii.get(self, "outputAudioText"))

    @builtins.property
    @jsii.member(jsii_name="playAudio")
    def play_audio(
        self,
    ) -> "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference":
        return typing.cast("DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference", jsii.get(self, "playAudio"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference":
        return typing.cast("DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference", jsii.get(self, "telephonyTransferCall"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(
        self,
    ) -> "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTextOutputReference":
        return typing.cast("DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTextOutputReference", jsii.get(self, "text"))

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="conversationSuccessInput")
    def conversation_success_input(
        self,
    ) -> typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess], jsii.get(self, "conversationSuccessInput"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoffInput")
    def live_agent_handoff_input(
        self,
    ) -> typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "liveAgentHandoffInput"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioTextInput")
    def output_audio_text_input(
        self,
    ) -> typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText], jsii.get(self, "outputAudioTextInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadInput")
    def payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadInput"))

    @builtins.property
    @jsii.member(jsii_name="playAudioInput")
    def play_audio_input(
        self,
    ) -> typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio"]:
        return typing.cast(typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio"], jsii.get(self, "playAudioInput"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCallInput")
    def telephony_transfer_call_input(
        self,
    ) -> typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall"]:
        return typing.cast(typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall"], jsii.get(self, "telephonyTransferCallInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(
        self,
    ) -> typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText"]:
        return typing.cast(typing.Optional["DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText"], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channel"))

    @channel.setter
    def channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d28d91c12fd5fd876dd3d7e29be7c09d8c53724fb5a4cbc9ca076cccbb3b9002)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="payload")
    def payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payload"))

    @payload.setter
    def payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__760ca915fded9e8b4f6bdb0853da0a7d1978535b0e2acc471cd84d9ec17899ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payload", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlersTriggerFulfillmentMessages]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlersTriggerFulfillmentMessages]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlersTriggerFulfillmentMessages]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b76d157a5b3c0542962ab8a100180e80b9a07150a0722d17a5c8b9abb6b2e3d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio",
    jsii_struct_bases=[],
    name_mapping={"audio_uri": "audioUri"},
)
class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio:
    def __init__(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49fca395691b291967124071233db405ddde577368b9e02adeff8918e01a0b59)
            check_type(argname="argument audio_uri", value=audio_uri, expected_type=type_hints["audio_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "audio_uri": audio_uri,
        }

    @builtins.property
    def audio_uri(self) -> builtins.str:
        '''URI of the audio clip.

        Dialogflow does not impose any validation on this value. It is specific to the client that reads it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        result = self._values.get("audio_uri")
        assert result is not None, "Required property 'audio_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f8a0ee19e5efae82567c538d675740e8ea5621cca2dc2fa19d52d7cdb1ee68b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2be4c25b92f1241c18902e19f56797fac3ce1bd8297f913fce4a08d739655bb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio]:
        return typing.cast(typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55b878af9e0a713b71057f348b3f35426cfd1ce36492ec787b6f7af31defb534)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall",
    jsii_struct_bases=[],
    name_mapping={"phone_number": "phoneNumber"},
)
class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall:
    def __init__(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ca7a4a996a2144cdd7b594ff967bfb1a387f9fb8e537fc6b5e35996baf60add)
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "phone_number": phone_number,
        }

    @builtins.property
    def phone_number(self) -> builtins.str:
        '''Transfer the call to a phone number in E.164 format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        result = self._values.get("phone_number")
        assert result is not None, "Required property 'phone_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1329fc9182887bfc7ed591a4b9cc799e0862921edbdac095ad67ea749e6502c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1dd358d900bb1c4ebacd80f14509121f42abdcda7eedb4bc921e086cc6f594c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall]:
        return typing.cast(typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__539ea9a9862578e39e7917241309999bc31ff724e255274ccd23d4594080d940)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d098a2973481bf30bea7d9ee978a15fdc45eb04edfde0e74952118233cbc7db)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A collection of text responses.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5cfc7ee5d8c51fbc803270e05c369e21b710e18475b014460060664ebee4f73f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__643922a224d3ece91edd71b5ac8b58c1f5bc114b43c0a34d9039de3169c6b7cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText]:
        return typing.cast(typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afee333ce9550891355da232f661367776e3a297111c137631d8159ae8f5b151)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageEventHandlersTriggerFulfillmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__34fed25d90dd2fe7f715cda5d87e38a9e078412b6d40cfee7d1bd8c1d883ea84)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConditionalCases")
    def put_conditional_cases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bdc2d97231c9bae66248e8497f38d0e97f90ad45162618f7a41279b9aa5aa3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConditionalCases", [value]))

    @jsii.member(jsii_name="putMessages")
    def put_messages(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03a78fc11ca4858fa6baa2eef303e4ae5b5b5cfbadcfaec6727945601bc5c069)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessages", [value]))

    @jsii.member(jsii_name="putSetParameterActions")
    def put_set_parameter_actions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cc100d1b2225569d072219e4da581a99a693ddaaed2efa7620d1bc245064bc9)
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
    ) -> DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCasesList:
        return typing.cast(DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCasesList, jsii.get(self, "conditionalCases"))

    @builtins.property
    @jsii.member(jsii_name="messages")
    def messages(self) -> DialogflowCxPageEventHandlersTriggerFulfillmentMessagesList:
        return typing.cast(DialogflowCxPageEventHandlersTriggerFulfillmentMessagesList, jsii.get(self, "messages"))

    @builtins.property
    @jsii.member(jsii_name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> "DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActionsList":
        return typing.cast("DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActionsList", jsii.get(self, "setParameterActions"))

    @builtins.property
    @jsii.member(jsii_name="conditionalCasesInput")
    def conditional_cases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases]]], jsii.get(self, "conditionalCasesInput"))

    @builtins.property
    @jsii.member(jsii_name="messagesInput")
    def messages_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentMessages]]], jsii.get(self, "messagesInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions"]]], jsii.get(self, "setParameterActionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__00a61a775de73ee57b87737bc537e6786aebeba434d904c36742a04d0778b6ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnPartialResponses", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ad9ffa779c7f8ac2808b926cee623a0d8d06f23f041ea1c256f9fe8fe1785d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhook"))

    @webhook.setter
    def webhook(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf34aa83705c176cbc6d55b83c65e46418a74744a81d2c9fef9da5d83c8fcf02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhook", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillment]:
        return typing.cast(typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fef7e81fec98cd123e70949f7c0d63ef96674803c1a56ac8365c38d30e533c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions",
    jsii_struct_bases=[],
    name_mapping={"parameter": "parameter", "value": "value"},
)
class DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions:
    def __init__(
        self,
        *,
        parameter: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param parameter: Display name of the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parameter DialogflowCxPage#parameter}
        :param value: The new JSON-encoded value of the parameter. A null value clears the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#value DialogflowCxPage#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8424b4270698ae56ac5a1c9d7388ce4f62c7a18670b891c951c6a26b094101fd)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parameter DialogflowCxPage#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The new JSON-encoded value of the parameter. A null value clears the parameter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#value DialogflowCxPage#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d377d4d8e251fd3c321ae690d97c19b9dbba272574bfc827544a5bca471d42c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0214b491db8f63cebe137755ac838ecf43b3a11a68f35ccd323a676cfeae74af)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__995957ddab309cf3812e8a9d2899f9e904c5c549d4d30cf9d60b200a11a85e31)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b26fac11137ebf3bef20e553954f2b04776785ba8fa3e393d98c5ad3007aa39)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b12e6f0dd99483545752876e4fb988165e9437f6dfff90af5217b50eba0e9805)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07fcafba883209c5510d9e2bd6b86303be23fc4e9dc6fb7000074e69f644fd98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec87219ab5386789d851ba20d0e3bf72a723ec8db42f5b1e3c7f52dfd9cafa46)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5199d9249be0d4d2d00e9192ac3df829e9c53399b49836e7c8d5fe3bb8e6d20c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameter", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf78dcf17f929b3ee63250764b25255de23f57ef82ddf44eee56594312e4b8a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d7517aab5c4f80f31e00771dbfa519e2a37d038d0768baef206019917881fbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageForm",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters"},
)
class DialogflowCxPageForm:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParameters", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parameters DialogflowCxPage#parameters}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d0be360a713e2ab0a0f26268fcc80f8bb6a4ee71845eac9521c248dbfee8c7c)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parameters DialogflowCxPage#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParameters"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageForm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b38fd3c3ad7c54a2de0e9b89ad836f182b6d066d8ab0f7847df07b84b52f6b7a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParameters", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b79fcea315a89759f6bc119a67caab611421cea1ca8299c29ec078cf90e1fef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> "DialogflowCxPageFormParametersList":
        return typing.cast("DialogflowCxPageFormParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParameters"]]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DialogflowCxPageForm]:
        return typing.cast(typing.Optional[DialogflowCxPageForm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DialogflowCxPageForm]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c2d6b52f3955236b3feb7483b9f6445834a2af7ccbd3d509ed0d91a2f184de0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParameters",
    jsii_struct_bases=[],
    name_mapping={
        "advanced_settings": "advancedSettings",
        "default_value": "defaultValue",
        "display_name": "displayName",
        "entity_type": "entityType",
        "fill_behavior": "fillBehavior",
        "is_list": "isList",
        "redact": "redact",
        "required": "required",
    },
)
class DialogflowCxPageFormParameters:
    def __init__(
        self,
        *,
        advanced_settings: typing.Optional[typing.Union["DialogflowCxPageFormParametersAdvancedSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        default_value: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        entity_type: typing.Optional[builtins.str] = None,
        fill_behavior: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehavior", typing.Dict[builtins.str, typing.Any]]] = None,
        is_list: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        redact: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        required: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param advanced_settings: advanced_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#advanced_settings DialogflowCxPage#advanced_settings}
        :param default_value: The default value of an optional parameter. If the parameter is required, the default value will be ignored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#default_value DialogflowCxPage#default_value}
        :param display_name: The human-readable name of the parameter, unique within the form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#display_name DialogflowCxPage#display_name}
        :param entity_type: The entity type of the parameter. Format: projects/-/locations/-/agents/-/entityTypes/ for system entity types (for example, projects/-/locations/-/agents/-/entityTypes/sys.date), or projects//locations//agents//entityTypes/ for developer entity types. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#entity_type DialogflowCxPage#entity_type}
        :param fill_behavior: fill_behavior block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#fill_behavior DialogflowCxPage#fill_behavior}
        :param is_list: Indicates whether the parameter represents a list of values. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#is_list DialogflowCxPage#is_list}
        :param redact: Indicates whether the parameter content should be redacted in log. If redaction is enabled, the parameter content will be replaced by parameter name during logging. Note: the parameter content is subject to redaction if either parameter level redaction or entity type level redaction is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#redact DialogflowCxPage#redact}
        :param required: Indicates whether the parameter is required. Optional parameters will not trigger prompts; however, they are filled if the user specifies them. Required parameters must be filled before form filling concludes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#required DialogflowCxPage#required}
        '''
        if isinstance(advanced_settings, dict):
            advanced_settings = DialogflowCxPageFormParametersAdvancedSettings(**advanced_settings)
        if isinstance(fill_behavior, dict):
            fill_behavior = DialogflowCxPageFormParametersFillBehavior(**fill_behavior)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11c068e0f8ff01f7f7df255a459e84c9b12d07a1355c0a203b17799539ce5948)
            check_type(argname="argument advanced_settings", value=advanced_settings, expected_type=type_hints["advanced_settings"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument entity_type", value=entity_type, expected_type=type_hints["entity_type"])
            check_type(argname="argument fill_behavior", value=fill_behavior, expected_type=type_hints["fill_behavior"])
            check_type(argname="argument is_list", value=is_list, expected_type=type_hints["is_list"])
            check_type(argname="argument redact", value=redact, expected_type=type_hints["redact"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if advanced_settings is not None:
            self._values["advanced_settings"] = advanced_settings
        if default_value is not None:
            self._values["default_value"] = default_value
        if display_name is not None:
            self._values["display_name"] = display_name
        if entity_type is not None:
            self._values["entity_type"] = entity_type
        if fill_behavior is not None:
            self._values["fill_behavior"] = fill_behavior
        if is_list is not None:
            self._values["is_list"] = is_list
        if redact is not None:
            self._values["redact"] = redact
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def advanced_settings(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersAdvancedSettings"]:
        '''advanced_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#advanced_settings DialogflowCxPage#advanced_settings}
        '''
        result = self._values.get("advanced_settings")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersAdvancedSettings"], result)

    @builtins.property
    def default_value(self) -> typing.Optional[builtins.str]:
        '''The default value of an optional parameter. If the parameter is required, the default value will be ignored.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#default_value DialogflowCxPage#default_value}
        '''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The human-readable name of the parameter, unique within the form.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#display_name DialogflowCxPage#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def entity_type(self) -> typing.Optional[builtins.str]:
        '''The entity type of the parameter.

        Format: projects/-/locations/-/agents/-/entityTypes/ for system entity types (for example, projects/-/locations/-/agents/-/entityTypes/sys.date), or projects//locations//agents//entityTypes/ for developer entity types.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#entity_type DialogflowCxPage#entity_type}
        '''
        result = self._values.get("entity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fill_behavior(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehavior"]:
        '''fill_behavior block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#fill_behavior DialogflowCxPage#fill_behavior}
        '''
        result = self._values.get("fill_behavior")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehavior"], result)

    @builtins.property
    def is_list(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether the parameter represents a list of values.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#is_list DialogflowCxPage#is_list}
        '''
        result = self._values.get("is_list")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def redact(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether the parameter content should be redacted in log.

        If redaction is enabled, the parameter content will be replaced by parameter name during logging. Note: the parameter content is subject to redaction if either parameter level redaction or entity type level redaction is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#redact DialogflowCxPage#redact}
        '''
        result = self._values.get("redact")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether the parameter is required.

        Optional parameters will not trigger prompts; however, they are filled if the user specifies them.
        Required parameters must be filled before form filling concludes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#required DialogflowCxPage#required}
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersAdvancedSettings",
    jsii_struct_bases=[],
    name_mapping={"dtmf_settings": "dtmfSettings"},
)
class DialogflowCxPageFormParametersAdvancedSettings:
    def __init__(
        self,
        *,
        dtmf_settings: typing.Optional[typing.Union["DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dtmf_settings: dtmf_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#dtmf_settings DialogflowCxPage#dtmf_settings}
        '''
        if isinstance(dtmf_settings, dict):
            dtmf_settings = DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings(**dtmf_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__257dac0fbfc389e9d75eaad87d0370157950521fd7a2c7fe5dace4d5ace14ab0)
            check_type(argname="argument dtmf_settings", value=dtmf_settings, expected_type=type_hints["dtmf_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dtmf_settings is not None:
            self._values["dtmf_settings"] = dtmf_settings

    @builtins.property
    def dtmf_settings(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings"]:
        '''dtmf_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#dtmf_settings DialogflowCxPage#dtmf_settings}
        '''
        result = self._values.get("dtmf_settings")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersAdvancedSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "finish_digit": "finishDigit",
        "max_digits": "maxDigits",
    },
)
class DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        finish_digit: typing.Optional[builtins.str] = None,
        max_digits: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: If true, incoming audio is processed for DTMF (dual tone multi frequency) events. For example, if the caller presses a button on their telephone keypad and DTMF processing is enabled, Dialogflow will detect the event (e.g. a "3" was pressed) in the incoming audio and pass the event to the bot to drive business logic (e.g. when 3 is pressed, return the account balance). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#enabled DialogflowCxPage#enabled}
        :param finish_digit: The digit that terminates a DTMF digit sequence. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#finish_digit DialogflowCxPage#finish_digit}
        :param max_digits: Max length of DTMF digits. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#max_digits DialogflowCxPage#max_digits}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26a8fc021fe4f0bf6d645fe60ac419fd76551c20d194869445d2318024e9aa2f)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#enabled DialogflowCxPage#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def finish_digit(self) -> typing.Optional[builtins.str]:
        '''The digit that terminates a DTMF digit sequence.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#finish_digit DialogflowCxPage#finish_digit}
        '''
        result = self._values.get("finish_digit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_digits(self) -> typing.Optional[jsii.Number]:
        '''Max length of DTMF digits.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#max_digits DialogflowCxPage#max_digits}
        '''
        result = self._values.get("max_digits")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersAdvancedSettingsDtmfSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersAdvancedSettingsDtmfSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__63361e435c4bf67d6a07a7067ad6eb31c2a3eb8347d49a294d58550027bd312a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8738a47ac64bb0d377e9d16b4131f37ec1c5267b07565c6e57a883a9e0006691)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="finishDigit")
    def finish_digit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "finishDigit"))

    @finish_digit.setter
    def finish_digit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36c22831aa0277a89c2e1cd1e9320af5de82f9ed6db3cb96617a0384228cff35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finishDigit", value)

    @builtins.property
    @jsii.member(jsii_name="maxDigits")
    def max_digits(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxDigits"))

    @max_digits.setter
    def max_digits(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60acaadfeb22703fa9b4bd539de97e8e4fe9994425e6f8f8832d2173d90df31a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDigits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aebaaf4ad08f242e4fa79771fcb592048cf3e05f28813afd4ac26f88e90940d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersAdvancedSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersAdvancedSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d28f7a7d3210de92f2f7460e30b9630d27cb7a769a7c5591b279fe420caf9b3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDtmfSettings")
    def put_dtmf_settings(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        finish_digit: typing.Optional[builtins.str] = None,
        max_digits: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: If true, incoming audio is processed for DTMF (dual tone multi frequency) events. For example, if the caller presses a button on their telephone keypad and DTMF processing is enabled, Dialogflow will detect the event (e.g. a "3" was pressed) in the incoming audio and pass the event to the bot to drive business logic (e.g. when 3 is pressed, return the account balance). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#enabled DialogflowCxPage#enabled}
        :param finish_digit: The digit that terminates a DTMF digit sequence. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#finish_digit DialogflowCxPage#finish_digit}
        :param max_digits: Max length of DTMF digits. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#max_digits DialogflowCxPage#max_digits}
        '''
        value = DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings(
            enabled=enabled, finish_digit=finish_digit, max_digits=max_digits
        )

        return typing.cast(None, jsii.invoke(self, "putDtmfSettings", [value]))

    @jsii.member(jsii_name="resetDtmfSettings")
    def reset_dtmf_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDtmfSettings", []))

    @builtins.property
    @jsii.member(jsii_name="dtmfSettings")
    def dtmf_settings(
        self,
    ) -> DialogflowCxPageFormParametersAdvancedSettingsDtmfSettingsOutputReference:
        return typing.cast(DialogflowCxPageFormParametersAdvancedSettingsDtmfSettingsOutputReference, jsii.get(self, "dtmfSettings"))

    @builtins.property
    @jsii.member(jsii_name="dtmfSettingsInput")
    def dtmf_settings_input(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings], jsii.get(self, "dtmfSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersAdvancedSettings]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersAdvancedSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersAdvancedSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8d2d862153251a49befb095f525a28217bc719affed5dbf5433ba5e15c6c11f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehavior",
    jsii_struct_bases=[],
    name_mapping={
        "initial_prompt_fulfillment": "initialPromptFulfillment",
        "reprompt_event_handlers": "repromptEventHandlers",
    },
)
class DialogflowCxPageFormParametersFillBehavior:
    def __init__(
        self,
        *,
        initial_prompt_fulfillment: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment", typing.Dict[builtins.str, typing.Any]]] = None,
        reprompt_event_handlers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param initial_prompt_fulfillment: initial_prompt_fulfillment block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#initial_prompt_fulfillment DialogflowCxPage#initial_prompt_fulfillment}
        :param reprompt_event_handlers: reprompt_event_handlers block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#reprompt_event_handlers DialogflowCxPage#reprompt_event_handlers}
        '''
        if isinstance(initial_prompt_fulfillment, dict):
            initial_prompt_fulfillment = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment(**initial_prompt_fulfillment)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03f1251ff13a4fdb1c07b7fc4fc39ed512c7336191a6138718cc1a8d74176e5a)
            check_type(argname="argument initial_prompt_fulfillment", value=initial_prompt_fulfillment, expected_type=type_hints["initial_prompt_fulfillment"])
            check_type(argname="argument reprompt_event_handlers", value=reprompt_event_handlers, expected_type=type_hints["reprompt_event_handlers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if initial_prompt_fulfillment is not None:
            self._values["initial_prompt_fulfillment"] = initial_prompt_fulfillment
        if reprompt_event_handlers is not None:
            self._values["reprompt_event_handlers"] = reprompt_event_handlers

    @builtins.property
    def initial_prompt_fulfillment(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment"]:
        '''initial_prompt_fulfillment block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#initial_prompt_fulfillment DialogflowCxPage#initial_prompt_fulfillment}
        '''
        result = self._values.get("initial_prompt_fulfillment")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment"], result)

    @builtins.property
    def reprompt_event_handlers(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers"]]]:
        '''reprompt_event_handlers block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#reprompt_event_handlers DialogflowCxPage#reprompt_event_handlers}
        '''
        result = self._values.get("reprompt_event_handlers")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehavior(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment",
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
class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment:
    def __init__(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases", typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__692fc3e920f6f72518c79c0969c1f2eae22c21ab21da05fa77856067192cfe62)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases"]]]:
        '''conditional_cases block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        '''
        result = self._values.get("conditional_cases")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases"]]], result)

    @builtins.property
    def messages(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages"]]]:
        '''messages block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        '''
        result = self._values.get("messages")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages"]]], result)

    @builtins.property
    def return_partial_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs.

        If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        '''
        result = self._values.get("return_partial_responses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def set_parameter_actions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions"]]]:
        '''set_parameter_actions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        '''
        result = self._values.get("set_parameter_actions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions"]]], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The tag used by the webhook to identify which fulfillment is being called.

        This field is required if webhook is specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook(self) -> typing.Optional[builtins.str]:
        '''The webhook to call. Format: projects//locations//agents//webhooks/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases",
    jsii_struct_bases=[],
    name_mapping={"cases": "cases"},
)
class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases:
    def __init__(self, *, cases: typing.Optional[builtins.str] = None) -> None:
        '''
        :param cases: A JSON encoded list of cascading if-else conditions. Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored. See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#cases DialogflowCxPage#cases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e482207f5ce17bfdf97425c075711086264b23ab546b9746aa9e3fa34cf2ee3)
            check_type(argname="argument cases", value=cases, expected_type=type_hints["cases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cases is not None:
            self._values["cases"] = cases

    @builtins.property
    def cases(self) -> typing.Optional[builtins.str]:
        '''A JSON encoded list of cascading if-else conditions.

        Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored.
        See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#cases DialogflowCxPage#cases}
        '''
        result = self._values.get("cases")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__42004927783c3a78c6f21cbdeb134f0bc6d86c1a96535172b37a120d53651972)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edff3733a8c90fae1fb9a5ddb6f86c7c9eea4c06ad8243c35d63b90798e3c4b4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcca37cfc8472e9ac0d86d8d0ad730842c3ee76eea3124696c7b62f644c56618)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f3135b4e476d588273b06654456f0e0f33fce9651aae0e363b3cf0b748213e2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__becd4c2149d6c47fa7901e14e40d00044bcfd4751b02daa964fdfbb9bd976605)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__885f1ba4506a3efe3b40de89ab166274df3c972e199d1d52f61e82a80e64c9a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0eb7295d07ab3ffbf76e7f5e7e4c18df3ef46e5900148608b9f28fa54de85709)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2913f0ff72993e6c777498482b49c4d5929b143e84939d521f1e50b3b839db91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cases", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10916fdb82b858832a874eadd5870e4d232afae349dea9bbc4615a58008d8e4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages",
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
class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages:
    def __init__(
        self,
        *,
        channel: typing.Optional[builtins.str] = None,
        conversation_success: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess", typing.Dict[builtins.str, typing.Any]]] = None,
        live_agent_handoff: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff", typing.Dict[builtins.str, typing.Any]]] = None,
        output_audio_text: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText", typing.Dict[builtins.str, typing.Any]]] = None,
        payload: typing.Optional[builtins.str] = None,
        play_audio: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio", typing.Dict[builtins.str, typing.Any]]] = None,
        telephony_transfer_call: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall", typing.Dict[builtins.str, typing.Any]]] = None,
        text: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param channel: The channel which the response is associated with. Clients can specify the channel via QueryParameters.channel, and only associated channel response will be returned. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#channel DialogflowCxPage#channel}
        :param conversation_success: conversation_success block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conversation_success DialogflowCxPage#conversation_success}
        :param live_agent_handoff: live_agent_handoff block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#live_agent_handoff DialogflowCxPage#live_agent_handoff}
        :param output_audio_text: output_audio_text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#output_audio_text DialogflowCxPage#output_audio_text}
        :param payload: A custom, platform-specific payload. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#payload DialogflowCxPage#payload}
        :param play_audio: play_audio block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#play_audio DialogflowCxPage#play_audio}
        :param telephony_transfer_call: telephony_transfer_call block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#telephony_transfer_call DialogflowCxPage#telephony_transfer_call}
        :param text: text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if isinstance(conversation_success, dict):
            conversation_success = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess(**conversation_success)
        if isinstance(live_agent_handoff, dict):
            live_agent_handoff = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff(**live_agent_handoff)
        if isinstance(output_audio_text, dict):
            output_audio_text = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText(**output_audio_text)
        if isinstance(play_audio, dict):
            play_audio = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio(**play_audio)
        if isinstance(telephony_transfer_call, dict):
            telephony_transfer_call = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall(**telephony_transfer_call)
        if isinstance(text, dict):
            text = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText(**text)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18271e61c8b487d74b047575b27fc5cc83eb6f06928e148932d80004d5d0cbdc)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#channel DialogflowCxPage#channel}
        '''
        result = self._values.get("channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conversation_success(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess"]:
        '''conversation_success block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conversation_success DialogflowCxPage#conversation_success}
        '''
        result = self._values.get("conversation_success")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess"], result)

    @builtins.property
    def live_agent_handoff(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff"]:
        '''live_agent_handoff block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#live_agent_handoff DialogflowCxPage#live_agent_handoff}
        '''
        result = self._values.get("live_agent_handoff")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff"], result)

    @builtins.property
    def output_audio_text(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText"]:
        '''output_audio_text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#output_audio_text DialogflowCxPage#output_audio_text}
        '''
        result = self._values.get("output_audio_text")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText"], result)

    @builtins.property
    def payload(self) -> typing.Optional[builtins.str]:
        '''A custom, platform-specific payload.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#payload DialogflowCxPage#payload}
        '''
        result = self._values.get("payload")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def play_audio(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio"]:
        '''play_audio block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#play_audio DialogflowCxPage#play_audio}
        '''
        result = self._values.get("play_audio")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio"], result)

    @builtins.property
    def telephony_transfer_call(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall"]:
        '''telephony_transfer_call block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#telephony_transfer_call DialogflowCxPage#telephony_transfer_call}
        '''
        result = self._values.get("telephony_transfer_call")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall"], result)

    @builtins.property
    def text(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText"]:
        '''text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc510bad6ccc125383ff53d636cf742088a99ff42d945d40c4de9ceec5574636)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccessOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__66300a5157d0334db33b338f035f710df70058144ff9eea5349a850a299d7d1d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f76f4ba1123c4fd070a5411b2f868c223fa7265c37e76163c65cafb05397deaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5257c755211ef5c530ab788314dbea9fcf98afc3f739fcd8252f891dc73f530e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__18e2c51fff5e58dbbb67d0c6c56555da7413ac65a018d861ef057e7718dcbe52)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b43331be443702fb1badc2a95cf0ba44db05d18c0330e6e74132deab53a10aa0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdcad1a707e7f604e1a8e60f1d2788a96d50980895b608abf43d38c4d87681f7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f48ad33f05bab3d1f294d76b83ad1cab1ce46d3b284d2368503a15585daeba5d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8644b12fcbcfe524e8c5d09fb6dd54be8ed0a7c46be0b2202df7449fec8fda82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36354e4b63c8039e10e203a3303de95849563b933dc23a07074b19bba1b484a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec5d6aa875fe82b0c1b312fed8ef6db0c55a8f5db6d76185bf5222b1c2174bec)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoffOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoffOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__093ef6329b98c85838601b3257ce2f56f7239e26fba9c0dc4f0634f96355bf8d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f47c94adddb2d089eacd89fe409d570e7adc51b91e310a74fef83d54ae953d60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f9197edcb7adcae9f12c2b4087e54f8b7af6c366531f2dc3da3448ec40cf1eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText",
    jsii_struct_bases=[],
    name_mapping={"ssml": "ssml", "text": "text"},
)
class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText:
    def __init__(
        self,
        *,
        ssml: typing.Optional[builtins.str] = None,
        text: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd7a2efb0b3fc8b68679ee6954385f03e7cbea23b0847e0ed95a4591eb6505d5)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        '''
        result = self._values.get("ssml")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def text(self) -> typing.Optional[builtins.str]:
        '''The raw text to be synthesized.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__90f13dd6fb779a8cb4fcf084bdaefaa5955e78a6c0b66e60aee88cf63c13cad3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c8ae52ae0d03cf27805018ec5631f1572de6270f3bb5e01fba8c1442e45a0006)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssml", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4db3619e30fa969f4f6ec92f74e63b300509ac6c9317b386404a9e37e4172a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3865fe4dff04e4c1b261c431fc44ed6d4ec511d3500037507be2f13d628dccb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b708a36e4e3dd47b9ce1fe06462ec9dd2e00e673093818461240100026be31f)
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
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess(
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
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff(
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
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText(
            ssml=ssml, text=text
        )

        return typing.cast(None, jsii.invoke(self, "putOutputAudioText", [value]))

    @jsii.member(jsii_name="putPlayAudio")
    def put_play_audio(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio(
            audio_uri=audio_uri
        )

        return typing.cast(None, jsii.invoke(self, "putPlayAudio", [value]))

    @jsii.member(jsii_name="putTelephonyTransferCall")
    def put_telephony_transfer_call(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall(
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
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText(
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
    ) -> DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccessOutputReference:
        return typing.cast(DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccessOutputReference, jsii.get(self, "conversationSuccess"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoffOutputReference:
        return typing.cast(DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoffOutputReference, jsii.get(self, "liveAgentHandoff"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioText")
    def output_audio_text(
        self,
    ) -> DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioTextOutputReference:
        return typing.cast(DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioTextOutputReference, jsii.get(self, "outputAudioText"))

    @builtins.property
    @jsii.member(jsii_name="playAudio")
    def play_audio(
        self,
    ) -> "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudioOutputReference":
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudioOutputReference", jsii.get(self, "playAudio"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCallOutputReference":
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCallOutputReference", jsii.get(self, "telephonyTransferCall"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(
        self,
    ) -> "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTextOutputReference":
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTextOutputReference", jsii.get(self, "text"))

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="conversationSuccessInput")
    def conversation_success_input(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess], jsii.get(self, "conversationSuccessInput"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoffInput")
    def live_agent_handoff_input(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "liveAgentHandoffInput"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioTextInput")
    def output_audio_text_input(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText], jsii.get(self, "outputAudioTextInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadInput")
    def payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadInput"))

    @builtins.property
    @jsii.member(jsii_name="playAudioInput")
    def play_audio_input(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio"]:
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio"], jsii.get(self, "playAudioInput"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCallInput")
    def telephony_transfer_call_input(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall"]:
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall"], jsii.get(self, "telephonyTransferCallInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText"]:
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText"], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channel"))

    @channel.setter
    def channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e5bb98280f1f65bc051ccd2f405cd89ae5c5b7a945eabdcb27925e047464d94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="payload")
    def payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payload"))

    @payload.setter
    def payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__586d8d6dafddf87599f983391662e22bcaca903ed23879158f2250c855cb8b4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payload", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2325a86ea9d5ffc2424cc86ad5e694992ca3928e98f3136a1a904fc2d9813a86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio",
    jsii_struct_bases=[],
    name_mapping={"audio_uri": "audioUri"},
)
class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio:
    def __init__(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__111e9595e9d9cea9fe99291727304cd80bb1505494e03bc9609aeeb092eb1673)
            check_type(argname="argument audio_uri", value=audio_uri, expected_type=type_hints["audio_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "audio_uri": audio_uri,
        }

    @builtins.property
    def audio_uri(self) -> builtins.str:
        '''URI of the audio clip.

        Dialogflow does not impose any validation on this value. It is specific to the client that reads it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        result = self._values.get("audio_uri")
        assert result is not None, "Required property 'audio_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudioOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudioOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__284f6347054ff0400cadfa05eaa25294d75cc11ab485ec0307bb25dd2ff285f6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__73816c880c734daedb30c92249e182a5ac862a284e356256f421dad47a22b9e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e319a4ee8f34e77ca756180711f1ba4461e76c534c2da922e2d4b722f84273ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall",
    jsii_struct_bases=[],
    name_mapping={"phone_number": "phoneNumber"},
)
class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall:
    def __init__(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aa4839e97b2f271ea666b3e239d459997941d574e178d95fa92ecf4eab2fc18)
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "phone_number": phone_number,
        }

    @builtins.property
    def phone_number(self) -> builtins.str:
        '''Transfer the call to a phone number in E.164 format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        result = self._values.get("phone_number")
        assert result is not None, "Required property 'phone_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCallOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCallOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__40321bc113550e70eedd00d2474781035a5adb2dd7fce00d0d8029b708a88424)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b5ec8262685e09fc18273137a6eb882aab7ba48ce1e4a8a88517c1bcfb7e894)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ddba0b5e425d5ffdf5f99604b0373587477797cca4048e88fde0e626df83b00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6697996e7afbaa35fc7858b33c1854be7d09b753f5d12a9fd567381649ebe89c)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A collection of text responses.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__004eec1626ed78aee03936571543bb6052d26797ea60b31eac008a4f117ddbce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9210dbcccc3d5dfdb02ee1f8ef308c71670d00cd118bfa248dff0fdb1b513a9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec5b918444a4be722f549a0295a510427a91c089cf00090bb1c65c2316aa4d62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ad6fe5fd835894bf08d025aafa3eec11548d7da007d2b236233179ef68212bf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConditionalCases")
    def put_conditional_cases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4f5a2b54c3794853e12c7d0d697702a41fd1fbaea36bdb79c9c11c5948f414f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConditionalCases", [value]))

    @jsii.member(jsii_name="putMessages")
    def put_messages(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b66ab45c6ae2c7886d743e05ca4b6d3aae605968012cd9b1c891127399137d57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessages", [value]))

    @jsii.member(jsii_name="putSetParameterActions")
    def put_set_parameter_actions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc286ca59c71eb354298c70830be416d0110b91f1af3ff2d393d16ee3174ca5c)
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
    ) -> DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCasesList:
        return typing.cast(DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCasesList, jsii.get(self, "conditionalCases"))

    @builtins.property
    @jsii.member(jsii_name="messages")
    def messages(
        self,
    ) -> DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList:
        return typing.cast(DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList, jsii.get(self, "messages"))

    @builtins.property
    @jsii.member(jsii_name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActionsList":
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActionsList", jsii.get(self, "setParameterActions"))

    @builtins.property
    @jsii.member(jsii_name="conditionalCasesInput")
    def conditional_cases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases]]], jsii.get(self, "conditionalCasesInput"))

    @builtins.property
    @jsii.member(jsii_name="messagesInput")
    def messages_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]]], jsii.get(self, "messagesInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions"]]], jsii.get(self, "setParameterActionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__ff7279d1f08a550166b6872555b738238e84a97c8e1e9cddaaa15f856a4558ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnPartialResponses", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a93af7e0b48aeb42185e0460a56bcac4c51d164d328f553c0f29c7faadebff18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhook"))

    @webhook.setter
    def webhook(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__691945a3b51db8dd5b44ca8f88f98e3aa3e9b23a03cdb8b65f46b3274d0940bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhook", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e88cac18cffbca1731f7a49420c57092254b6df424a56069cf1dde9c8e67a71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions",
    jsii_struct_bases=[],
    name_mapping={"parameter": "parameter", "value": "value"},
)
class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions:
    def __init__(
        self,
        *,
        parameter: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param parameter: Display name of the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parameter DialogflowCxPage#parameter}
        :param value: The new JSON-encoded value of the parameter. A null value clears the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#value DialogflowCxPage#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2f8d250084b41386398fc1417fc29bfb5af84ba5f4796207a63be51789147a4)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parameter DialogflowCxPage#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The new JSON-encoded value of the parameter. A null value clears the parameter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#value DialogflowCxPage#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c67cf06d134313049c76013252917a7f73ae250ae6cfed6a99f07a414b8274d7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__706e9dc1ba13269555a5ae5f2f94c2b320dbd8270accbacbb12caa1c0bfbe697)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cdb831e8055b45e952afd4fbda53a1190b37868d2f4014ad14437619a0797bc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c01ef0905f8d63e6c5d1cec0d66a5fae641b83c50aeada6c5c499ba0a4d21d16)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e817803c6dfc6174a2ce6ddcb05ef44e65b8a42c71f47e36d2536afcecd487b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5eb89c9cf6e67383187d704bc4a2cffdb911344cf765c410019a246cb36159d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__63bbc22365018e711310f749fe1396b2ca8c882bccae4b38851afcab01e16115)
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
            type_hints = typing.get_type_hints(_typecheckingstub__86b697e9fa06554bb640ae9fc8efc8b1758c3d3022af205fecc7a5df3312aa91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameter", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7c6d1ca91636bbabbc773d365514a6ff3ce1c7cd6e3cbba98683db6de080565)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4c3ab9eec035875c59d21ae5a86ad6cbce87f116b6eab0778fc91e609e602b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersFillBehaviorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3066229f7bb71408e9f43905b352f3bfecbfaccbf8c68b3952fd982b0e3034d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInitialPromptFulfillment")
    def put_initial_prompt_fulfillment(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment(
            conditional_cases=conditional_cases,
            messages=messages,
            return_partial_responses=return_partial_responses,
            set_parameter_actions=set_parameter_actions,
            tag=tag,
            webhook=webhook,
        )

        return typing.cast(None, jsii.invoke(self, "putInitialPromptFulfillment", [value]))

    @jsii.member(jsii_name="putRepromptEventHandlers")
    def put_reprompt_event_handlers(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf14005a1ef873c9a1029e000520121e99a1328f8605cc64c42953784d572127)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRepromptEventHandlers", [value]))

    @jsii.member(jsii_name="resetInitialPromptFulfillment")
    def reset_initial_prompt_fulfillment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialPromptFulfillment", []))

    @jsii.member(jsii_name="resetRepromptEventHandlers")
    def reset_reprompt_event_handlers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepromptEventHandlers", []))

    @builtins.property
    @jsii.member(jsii_name="initialPromptFulfillment")
    def initial_prompt_fulfillment(
        self,
    ) -> DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference:
        return typing.cast(DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference, jsii.get(self, "initialPromptFulfillment"))

    @builtins.property
    @jsii.member(jsii_name="repromptEventHandlers")
    def reprompt_event_handlers(
        self,
    ) -> "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersList":
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersList", jsii.get(self, "repromptEventHandlers"))

    @builtins.property
    @jsii.member(jsii_name="initialPromptFulfillmentInput")
    def initial_prompt_fulfillment_input(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment], jsii.get(self, "initialPromptFulfillmentInput"))

    @builtins.property
    @jsii.member(jsii_name="repromptEventHandlersInput")
    def reprompt_event_handlers_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers"]]], jsii.get(self, "repromptEventHandlersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehavior]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehavior], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehavior],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c79d3cf49994812c2d7fa11adeb0a6396ef7c7f318c105321023a445071a6d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers",
    jsii_struct_bases=[],
    name_mapping={
        "event": "event",
        "target_flow": "targetFlow",
        "target_page": "targetPage",
        "trigger_fulfillment": "triggerFulfillment",
    },
)
class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers:
    def __init__(
        self,
        *,
        event: typing.Optional[builtins.str] = None,
        target_flow: typing.Optional[builtins.str] = None,
        target_page: typing.Optional[builtins.str] = None,
        trigger_fulfillment: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param event: The name of the event to handle. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#event DialogflowCxPage#event}
        :param target_flow: The target flow to transition to. Format: projects//locations//agents//flows/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#target_flow DialogflowCxPage#target_flow}
        :param target_page: The target page to transition to. Format: projects//locations//agents//flows//pages/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#target_page DialogflowCxPage#target_page}
        :param trigger_fulfillment: trigger_fulfillment block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#trigger_fulfillment DialogflowCxPage#trigger_fulfillment}
        '''
        if isinstance(trigger_fulfillment, dict):
            trigger_fulfillment = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment(**trigger_fulfillment)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c6f4c393d49a4134fc2cdb09be3c8bc5768c7f7188376f88dc60af512acbfcc)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#event DialogflowCxPage#event}
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_flow(self) -> typing.Optional[builtins.str]:
        '''The target flow to transition to. Format: projects//locations//agents//flows/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#target_flow DialogflowCxPage#target_flow}
        '''
        result = self._values.get("target_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_page(self) -> typing.Optional[builtins.str]:
        '''The target page to transition to. Format: projects//locations//agents//flows//pages/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#target_page DialogflowCxPage#target_page}
        '''
        result = self._values.get("target_page")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger_fulfillment(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment"]:
        '''trigger_fulfillment block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#trigger_fulfillment DialogflowCxPage#trigger_fulfillment}
        '''
        result = self._values.get("trigger_fulfillment")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__67f84d9f7ae2c2ed1be16c1bd39d0e4f0bcebc24ebe1d32a7e9dcd4b8bb91c12)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__982b28218fda86b4b0a53c4eb1f1e994f8dd7d09b953b13cdfa5697e4ad28000)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05d2531e1fb36427be61894bce079e6027fb5a80b78d30375b5a1846b2bfd424)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7034ea0b8e63cb16eb19d1f69d9b653c8293d6a902f087dcc6b5a06553a97312)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b763c9cfccdb62fa7e75a2b210b8e857dcd06c33bb5bcb92d9e1e9d444d62854)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aae0a28ec12afb8a41c96dcf893faeb71d91a8d34f858a13464f445652e33c23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2e17e7ac3202b945ef66eaa6a7d8b517a9feba10a4cbec879301bc38ea5b374)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTriggerFulfillment")
    def put_trigger_fulfillment(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases", typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment(
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
    ) -> "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentOutputReference":
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentOutputReference", jsii.get(self, "triggerFulfillment"))

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
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment"]:
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment"], jsii.get(self, "triggerFulfillmentInput"))

    @builtins.property
    @jsii.member(jsii_name="event")
    def event(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "event"))

    @event.setter
    def event(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f76b24efebc6caaf1c60d3e25d0f212a5b2fea545bc437a1e968d7492e66c496)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "event", value)

    @builtins.property
    @jsii.member(jsii_name="targetFlow")
    def target_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetFlow"))

    @target_flow.setter
    def target_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74abcc5d487b5606c3b615c155de774723291ac247b3e3cd8d82115bca320c50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetFlow", value)

    @builtins.property
    @jsii.member(jsii_name="targetPage")
    def target_page(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPage"))

    @target_page.setter
    def target_page(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e4ff25111b065da35542b55a99b2dffb206031d3139d5a99f2f18d8248d10f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5012074a6c766ce917a80b54d5767965b6c0e228ba48ff587536981d86d645e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment",
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
class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment:
    def __init__(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases", typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23a2f9247a15b225c9aeed35e0047e1672a3f98ae21acf9b14fd336f113c7e6f)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases"]]]:
        '''conditional_cases block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        '''
        result = self._values.get("conditional_cases")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases"]]], result)

    @builtins.property
    def messages(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages"]]]:
        '''messages block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        '''
        result = self._values.get("messages")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages"]]], result)

    @builtins.property
    def return_partial_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs.

        If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        '''
        result = self._values.get("return_partial_responses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def set_parameter_actions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions"]]]:
        '''set_parameter_actions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        '''
        result = self._values.get("set_parameter_actions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions"]]], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The tag used by the webhook to identify which fulfillment is being called.

        This field is required if webhook is specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook(self) -> typing.Optional[builtins.str]:
        '''The webhook to call. Format: projects//locations//agents//webhooks/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases",
    jsii_struct_bases=[],
    name_mapping={"cases": "cases"},
)
class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases:
    def __init__(self, *, cases: typing.Optional[builtins.str] = None) -> None:
        '''
        :param cases: A JSON encoded list of cascading if-else conditions. Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored. See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#cases DialogflowCxPage#cases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81849e2f2275e16ae439e717051e89bcb7e653815fb68b8723368eef16c00317)
            check_type(argname="argument cases", value=cases, expected_type=type_hints["cases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cases is not None:
            self._values["cases"] = cases

    @builtins.property
    def cases(self) -> typing.Optional[builtins.str]:
        '''A JSON encoded list of cascading if-else conditions.

        Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored.
        See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#cases DialogflowCxPage#cases}
        '''
        result = self._values.get("cases")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1834c8c2a0879684e096601ae2f2a0b9ede11b8b987c86877097aaa0fe9cadb4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eed9bb7a923db26e226cdd2d63c9de7182a084595f1da4c11d5d32a11f14626)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__504f915c36d2a6f7fe94cc1f745f80a06474a893b45323245b2422e2398f7ec1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2217529a3314041e080b9aac552baf74a6a069fed0aa52f66de472cd5de111f6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__130990475d5c3685ee87257f252d76d02d24ea5e960dd62377a2cc32fa5b4502)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ce252b4046b702d4c7647bac535588666f34bdf356107f990065d16d8fe8cd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f1ebdd741a9a298823d667e63ac9b68bbb84a2380d0268c0f386b41f43d83e3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__303f486ff7a76f1949d67fa3e1de71ecc1dced82ad86c0381e49f57543f8fef2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cases", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3ca79bb4ff4c672c6d86e6d2a837563ac3295325689f7aa2d93291c1d31ebe3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages",
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
class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages:
    def __init__(
        self,
        *,
        channel: typing.Optional[builtins.str] = None,
        conversation_success: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess", typing.Dict[builtins.str, typing.Any]]] = None,
        live_agent_handoff: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff", typing.Dict[builtins.str, typing.Any]]] = None,
        output_audio_text: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText", typing.Dict[builtins.str, typing.Any]]] = None,
        payload: typing.Optional[builtins.str] = None,
        play_audio: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio", typing.Dict[builtins.str, typing.Any]]] = None,
        telephony_transfer_call: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall", typing.Dict[builtins.str, typing.Any]]] = None,
        text: typing.Optional[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param channel: The channel which the response is associated with. Clients can specify the channel via QueryParameters.channel, and only associated channel response will be returned. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#channel DialogflowCxPage#channel}
        :param conversation_success: conversation_success block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conversation_success DialogflowCxPage#conversation_success}
        :param live_agent_handoff: live_agent_handoff block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#live_agent_handoff DialogflowCxPage#live_agent_handoff}
        :param output_audio_text: output_audio_text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#output_audio_text DialogflowCxPage#output_audio_text}
        :param payload: A custom, platform-specific payload. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#payload DialogflowCxPage#payload}
        :param play_audio: play_audio block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#play_audio DialogflowCxPage#play_audio}
        :param telephony_transfer_call: telephony_transfer_call block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#telephony_transfer_call DialogflowCxPage#telephony_transfer_call}
        :param text: text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if isinstance(conversation_success, dict):
            conversation_success = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess(**conversation_success)
        if isinstance(live_agent_handoff, dict):
            live_agent_handoff = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff(**live_agent_handoff)
        if isinstance(output_audio_text, dict):
            output_audio_text = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText(**output_audio_text)
        if isinstance(play_audio, dict):
            play_audio = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio(**play_audio)
        if isinstance(telephony_transfer_call, dict):
            telephony_transfer_call = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall(**telephony_transfer_call)
        if isinstance(text, dict):
            text = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText(**text)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93fb2db8ee7a9fbb5d9d8722cf434834340388c4375497da67779d9bcf87fc46)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#channel DialogflowCxPage#channel}
        '''
        result = self._values.get("channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conversation_success(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess"]:
        '''conversation_success block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conversation_success DialogflowCxPage#conversation_success}
        '''
        result = self._values.get("conversation_success")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess"], result)

    @builtins.property
    def live_agent_handoff(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff"]:
        '''live_agent_handoff block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#live_agent_handoff DialogflowCxPage#live_agent_handoff}
        '''
        result = self._values.get("live_agent_handoff")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff"], result)

    @builtins.property
    def output_audio_text(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText"]:
        '''output_audio_text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#output_audio_text DialogflowCxPage#output_audio_text}
        '''
        result = self._values.get("output_audio_text")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText"], result)

    @builtins.property
    def payload(self) -> typing.Optional[builtins.str]:
        '''A custom, platform-specific payload.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#payload DialogflowCxPage#payload}
        '''
        result = self._values.get("payload")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def play_audio(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio"]:
        '''play_audio block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#play_audio DialogflowCxPage#play_audio}
        '''
        result = self._values.get("play_audio")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio"], result)

    @builtins.property
    def telephony_transfer_call(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall"]:
        '''telephony_transfer_call block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#telephony_transfer_call DialogflowCxPage#telephony_transfer_call}
        '''
        result = self._values.get("telephony_transfer_call")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall"], result)

    @builtins.property
    def text(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText"]:
        '''text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__749602d06cb6937ec1ac7c38f71919593f78a9f81e1a295ad6c8437ce8539f86)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f33496ffd59cdf604c411ce8f4fb224b14e90b42c9991680db5739416b7de8a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef79c0a0a92ad9419c0c5f53eb8c9f1ea347ee79c241ce2ef4785167229601b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1959513ae1d16c7e48f4680a90da304896f3a07c0da6dd037e8216f6e9219f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__328e98988bcd8dfb728651e66b072748a7e3c26f1268d829aaf8023209f963bb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a6b431cc86d866d738b25a3041f6f19b7bf1d257f5a72454906da24e2fcdaf3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b5fbd64a91a3f8a0c115b7cef84bb402cd838c5b70199e999ce8b2e9a61158d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9774ae7ed17e84b4adaf3cce096993a11334fd522d234cc43ed9936dbde64b10)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0da302874c27567e281f8a57a9ec100c564ed90b7b271361bae4a48d89cd199f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc3194f2bb63b8194e9405fd3f96a7c76f244131ca92983acfbc60907bbbab68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6208f60cdee1ec1d059f52b7a1a552c3aa97719c80ec991c759208e39b34e8e4)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__be31bec1d45e141d5e59ba188e28872b0393fa21ddee18757553c3a6aa493a0d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f14af29ecdf5545d34416d32e5d89bc6ab8a0623284d0caab66196f0605850b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acdcb6103d46600b17cf66e9c0d2eaf002d01c93e1d16f153db54486ee39e041)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText",
    jsii_struct_bases=[],
    name_mapping={"ssml": "ssml", "text": "text"},
)
class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText:
    def __init__(
        self,
        *,
        ssml: typing.Optional[builtins.str] = None,
        text: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7f5e3d583137cf5ffdbd07bf0aa2289f5ac4e070470d1f93a8c0a929c5d357f)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        '''
        result = self._values.get("ssml")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def text(self) -> typing.Optional[builtins.str]:
        '''The raw text to be synthesized.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__359fde6aab2ee46515ae43bbc1e0426220d817db6b663c27e96bbc46baa890ba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d1f96503d07bea7b230a96c7e5441d13e824207a5ef4e9ee627b4a21f364ce7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssml", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b23c840a914fd8997a23abced560393e18a6635125a8d01b4620043fa9baa80e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82aae2679358ec43bbe1426cfebaa57e341aa71459f22cf856badd0abb83e1c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9b60872e0413605ba3d3384ece4c2b33466e9404a373508c86aaeeae4d73295)
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
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess(
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
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff(
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
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText(
            ssml=ssml, text=text
        )

        return typing.cast(None, jsii.invoke(self, "putOutputAudioText", [value]))

    @jsii.member(jsii_name="putPlayAudio")
    def put_play_audio(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio(
            audio_uri=audio_uri
        )

        return typing.cast(None, jsii.invoke(self, "putPlayAudio", [value]))

    @jsii.member(jsii_name="putTelephonyTransferCall")
    def put_telephony_transfer_call(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall(
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
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        value = DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText(
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
    ) -> DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference:
        return typing.cast(DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference, jsii.get(self, "conversationSuccess"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference:
        return typing.cast(DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference, jsii.get(self, "liveAgentHandoff"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioText")
    def output_audio_text(
        self,
    ) -> DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference:
        return typing.cast(DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference, jsii.get(self, "outputAudioText"))

    @builtins.property
    @jsii.member(jsii_name="playAudio")
    def play_audio(
        self,
    ) -> "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference":
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference", jsii.get(self, "playAudio"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference":
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference", jsii.get(self, "telephonyTransferCall"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(
        self,
    ) -> "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTextOutputReference":
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTextOutputReference", jsii.get(self, "text"))

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="conversationSuccessInput")
    def conversation_success_input(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess], jsii.get(self, "conversationSuccessInput"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoffInput")
    def live_agent_handoff_input(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "liveAgentHandoffInput"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioTextInput")
    def output_audio_text_input(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText], jsii.get(self, "outputAudioTextInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadInput")
    def payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadInput"))

    @builtins.property
    @jsii.member(jsii_name="playAudioInput")
    def play_audio_input(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio"]:
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio"], jsii.get(self, "playAudioInput"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCallInput")
    def telephony_transfer_call_input(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall"]:
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall"], jsii.get(self, "telephonyTransferCallInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(
        self,
    ) -> typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText"]:
        return typing.cast(typing.Optional["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText"], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channel"))

    @channel.setter
    def channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b686276781abcb5befab9c44aa3a1321eb50ab749761f13f0d52d96c0e19821b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="payload")
    def payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payload"))

    @payload.setter
    def payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fdb67d59f5eb75f7cecc0eb87b589cba7fe15c4f6d08cabcdb1f1b7a3416377)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payload", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc7de8fceeb5489b48b0adfecb995a0967a781eb58937b507210ce35bee005f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio",
    jsii_struct_bases=[],
    name_mapping={"audio_uri": "audioUri"},
)
class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio:
    def __init__(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fead30325e1ae4827ecc8c98fabfc2d6ae173c8794d226407d3b6e638770c8b5)
            check_type(argname="argument audio_uri", value=audio_uri, expected_type=type_hints["audio_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "audio_uri": audio_uri,
        }

    @builtins.property
    def audio_uri(self) -> builtins.str:
        '''URI of the audio clip.

        Dialogflow does not impose any validation on this value. It is specific to the client that reads it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        result = self._values.get("audio_uri")
        assert result is not None, "Required property 'audio_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__22c8fc4cd991b99ca63ca5035057e950db1fdea9ce4eba61ec15d1adddd561a6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a2e1f004cb9abc09d69b2c6a95fd768236ad1b43ed73bde8968eed0f6eea400)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7522b41c37b92317d985216292ffdf0f92ccdd085c364195d71a2890a4ec191)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall",
    jsii_struct_bases=[],
    name_mapping={"phone_number": "phoneNumber"},
)
class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall:
    def __init__(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c72605d1f13aabe9951226594e81aa5a36c4e7ea0186f7e1e695111129ebc9d)
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "phone_number": phone_number,
        }

    @builtins.property
    def phone_number(self) -> builtins.str:
        '''Transfer the call to a phone number in E.164 format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        result = self._values.get("phone_number")
        assert result is not None, "Required property 'phone_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb81dfed5fcaccfc83c340243f71e86a26e36ea398c3dd4c565a2c569746d181)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3265d96159f4218d366d6694a14c987dd147140cef678432958bdd3c34f6247f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7af95c9c45b051cc215fa1fc6fa7727e5bd8f5757f7109af0177c54f92dddb3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41a0efa64aa0a4660eebe1feff25627ec5d21e7e776e8a55124de8575831f369)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A collection of text responses.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cdbe4e4e0d1830c1032487feb64ac8850447fd15d8b12e34d5f82606d6f99d50)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a96c8078208faaf675ef926648a37e0ef16f4f45e4bc56080892de5328ee799)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50a2af4b8e1b1b951d62759c1952fab5e4ef1bea1842dfe42f86c940b0844afa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__78b4aa7a1074440da3c1128aacf1477a22cfbabf3265fc17591f49d05dea1264)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConditionalCases")
    def put_conditional_cases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91eb77888d0ba8188b452f1cc946ab9e009e4ea97236270e59bf8e1c17c366fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConditionalCases", [value]))

    @jsii.member(jsii_name="putMessages")
    def put_messages(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7938300b7f69f7581fc68ba230a7ca60005ce3cab73c6eeb1665d8cd3fee41e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessages", [value]))

    @jsii.member(jsii_name="putSetParameterActions")
    def put_set_parameter_actions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47905912712f1a4946e37a7b95f87bd69d5f0494c61907e64b4a6329d316fdc6)
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
    ) -> DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCasesList:
        return typing.cast(DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCasesList, jsii.get(self, "conditionalCases"))

    @builtins.property
    @jsii.member(jsii_name="messages")
    def messages(
        self,
    ) -> DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesList:
        return typing.cast(DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesList, jsii.get(self, "messages"))

    @builtins.property
    @jsii.member(jsii_name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActionsList":
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActionsList", jsii.get(self, "setParameterActions"))

    @builtins.property
    @jsii.member(jsii_name="conditionalCasesInput")
    def conditional_cases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases]]], jsii.get(self, "conditionalCasesInput"))

    @builtins.property
    @jsii.member(jsii_name="messagesInput")
    def messages_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages]]], jsii.get(self, "messagesInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions"]]], jsii.get(self, "setParameterActionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__9e74bae246dc19e9eec2fca2f562abfed4eaffe5a121d2a5329ed3deb919be23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnPartialResponses", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ae89e61e81cc890511924e9676e1073e758d937c2b278813a5b4fa05c4cfb62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhook"))

    @webhook.setter
    def webhook(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0aeb815c3edb2d28fec446c2395dac8746c9aaf79042830cbe4730a12aa89ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhook", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd88a253effbd5ed96cb9039cd66cf0580e3cdc795cb0f58d3e20cc33bd2bb32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions",
    jsii_struct_bases=[],
    name_mapping={"parameter": "parameter", "value": "value"},
)
class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions:
    def __init__(
        self,
        *,
        parameter: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param parameter: Display name of the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parameter DialogflowCxPage#parameter}
        :param value: The new JSON-encoded value of the parameter. A null value clears the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#value DialogflowCxPage#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87ccd17d2816cd632b1a300960f7e835be028001289b71c5935650b9d539732b)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parameter DialogflowCxPage#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The new JSON-encoded value of the parameter. A null value clears the parameter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#value DialogflowCxPage#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__01868519dcf3981d6042e75371f353b6c17c38892b668ca47bde248881dc004c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__690a5d6aa323f8b98c36f1539b63dace9a656c2597768dbb5557b76f675e34ae)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c5ed138a85653b0c4fd70b7350c6fc90a56be6a9c63295c060612c9b1c257cf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ce72bf4e059cd4f14a9a540925c750aac56d1d3732c95f9cc5158c6100b0353)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6fed3e839dca404f9b6ee7ee5f2a692da2b3a010e72f01983305eb69b1d4756)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05fd57adb5eaea3986428a682ebdd971c7d91d33d17a378f10fdcd4335504f91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e396f8b57cdcc47b9b8427a9f37fc7e9c936ed7fc6a09a444b4406b974f10c4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ccb64ba78fd2248dd53321282e556ecad6fe1bc175d2d6b88686154934aa2bfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameter", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e572498d708d4844d816a4c70940cb68e9d91ea6bc4961463d041851c807ca5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d7197c3dd547cd08c9f24aab2b32639c914506fa2c78b8edb603e1cbaf39806)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__65ab0bd7e69cea4c0bcc2d18e83ad155e5ce49bb9ed29faf85496981a9fb1d3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageFormParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac4826b540914b797b342f0f40616d9e0bdcc07e4a7d503069051ebda41bfc9a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageFormParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0833af22ad182769bd2a385b2e1163c1d47db93b68021becec42d74e3413e52c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__13eb2fa37e8520a9e60db6f7aeb02af6803d37a33408fee7c34962a1867944e5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8252559b74bba55fdf07c1122d2b7c3f0138e97c5f449de6e9294758f2ba2dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParameters]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParameters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84168b6727bed5f577334b6278adb82bc93d535162150a4b9e97043172cf769c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageFormParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageFormParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__96b0622b63bf8976f6ddb697fe0277da020f18e377aa4e07e8d1458151e2172a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAdvancedSettings")
    def put_advanced_settings(
        self,
        *,
        dtmf_settings: typing.Optional[typing.Union[DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dtmf_settings: dtmf_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#dtmf_settings DialogflowCxPage#dtmf_settings}
        '''
        value = DialogflowCxPageFormParametersAdvancedSettings(
            dtmf_settings=dtmf_settings
        )

        return typing.cast(None, jsii.invoke(self, "putAdvancedSettings", [value]))

    @jsii.member(jsii_name="putFillBehavior")
    def put_fill_behavior(
        self,
        *,
        initial_prompt_fulfillment: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment, typing.Dict[builtins.str, typing.Any]]] = None,
        reprompt_event_handlers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param initial_prompt_fulfillment: initial_prompt_fulfillment block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#initial_prompt_fulfillment DialogflowCxPage#initial_prompt_fulfillment}
        :param reprompt_event_handlers: reprompt_event_handlers block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#reprompt_event_handlers DialogflowCxPage#reprompt_event_handlers}
        '''
        value = DialogflowCxPageFormParametersFillBehavior(
            initial_prompt_fulfillment=initial_prompt_fulfillment,
            reprompt_event_handlers=reprompt_event_handlers,
        )

        return typing.cast(None, jsii.invoke(self, "putFillBehavior", [value]))

    @jsii.member(jsii_name="resetAdvancedSettings")
    def reset_advanced_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedSettings", []))

    @jsii.member(jsii_name="resetDefaultValue")
    def reset_default_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultValue", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetEntityType")
    def reset_entity_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntityType", []))

    @jsii.member(jsii_name="resetFillBehavior")
    def reset_fill_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFillBehavior", []))

    @jsii.member(jsii_name="resetIsList")
    def reset_is_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsList", []))

    @jsii.member(jsii_name="resetRedact")
    def reset_redact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedact", []))

    @jsii.member(jsii_name="resetRequired")
    def reset_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequired", []))

    @builtins.property
    @jsii.member(jsii_name="advancedSettings")
    def advanced_settings(
        self,
    ) -> DialogflowCxPageFormParametersAdvancedSettingsOutputReference:
        return typing.cast(DialogflowCxPageFormParametersAdvancedSettingsOutputReference, jsii.get(self, "advancedSettings"))

    @builtins.property
    @jsii.member(jsii_name="fillBehavior")
    def fill_behavior(
        self,
    ) -> DialogflowCxPageFormParametersFillBehaviorOutputReference:
        return typing.cast(DialogflowCxPageFormParametersFillBehaviorOutputReference, jsii.get(self, "fillBehavior"))

    @builtins.property
    @jsii.member(jsii_name="advancedSettingsInput")
    def advanced_settings_input(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersAdvancedSettings]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersAdvancedSettings], jsii.get(self, "advancedSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultValueInput")
    def default_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultValueInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="entityTypeInput")
    def entity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="fillBehaviorInput")
    def fill_behavior_input(
        self,
    ) -> typing.Optional[DialogflowCxPageFormParametersFillBehavior]:
        return typing.cast(typing.Optional[DialogflowCxPageFormParametersFillBehavior], jsii.get(self, "fillBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="isListInput")
    def is_list_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isListInput"))

    @builtins.property
    @jsii.member(jsii_name="redactInput")
    def redact_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "redactInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d03faf4d56d23635247ab5f9732ab85a8d0c72b60991be57ea60f854de6aae4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__992a2cff1d737740167aa4dc345f902ad2d3e6444bf14dd4a9470198b42acb76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="entityType")
    def entity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entityType"))

    @entity_type.setter
    def entity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d855713b9bc360962424d57f242ad4e7db238b5b32ebc9fd2f80e78c2abe8345)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityType", value)

    @builtins.property
    @jsii.member(jsii_name="isList")
    def is_list(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isList"))

    @is_list.setter
    def is_list(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__090feb3efde0d92df93cc4dffdd8ae9a1a845026ba35259732ffc393d60a938c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isList", value)

    @builtins.property
    @jsii.member(jsii_name="redact")
    def redact(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "redact"))

    @redact.setter
    def redact(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39fa322492de6d0066f52f6db7696836bb0a2026eeac0281cfe98b401439f990)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redact", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__783421a7873f243c8974cd21cf7ec3298e09ee47f7d6e979ea824d0d33485b73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParameters]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParameters]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParameters]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45f63f6efa57f41d57dc8f7c55c6a185253a2ce1dca840d65f5a02f986d9108e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DialogflowCxPageTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#create DialogflowCxPage#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#delete DialogflowCxPage#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#update DialogflowCxPage#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e19156a49b1e0987ceb69d743e69217491db69c64a86751513a4ce9e2ae312)
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
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#create DialogflowCxPage#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#delete DialogflowCxPage#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#update DialogflowCxPage#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__873e29e32e378d5b33dd9389659e3cf173adaac21d3d6341095e7c00790a44cf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ef2204dbf7dddaae7255015ad7298c5bb3e3aa69c0572b3d148fa3a54a4c737)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72e884773b7fbebac1a12b7401d637462235ec24edbc8dee9a1491d84a0a5dfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a41bae19acacf19f12d8883f3c033c21b9bfbb619503800c51d344a2f64f877d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ec1ac3c4aeaa8b59fec413b264b067aa053747243884dc9c0a5cb3554de84b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutes",
    jsii_struct_bases=[],
    name_mapping={
        "condition": "condition",
        "intent": "intent",
        "target_flow": "targetFlow",
        "target_page": "targetPage",
        "trigger_fulfillment": "triggerFulfillment",
    },
)
class DialogflowCxPageTransitionRoutes:
    def __init__(
        self,
        *,
        condition: typing.Optional[builtins.str] = None,
        intent: typing.Optional[builtins.str] = None,
        target_flow: typing.Optional[builtins.str] = None,
        target_page: typing.Optional[builtins.str] = None,
        trigger_fulfillment: typing.Optional[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillment", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition: The condition to evaluate against form parameters or session parameters. At least one of intent or condition must be specified. When both intent and condition are specified, the transition can only happen when both are fulfilled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#condition DialogflowCxPage#condition}
        :param intent: The unique identifier of an Intent. Format: projects//locations//agents//intents/. Indicates that the transition can only happen when the given intent is matched. At least one of intent or condition must be specified. When both intent and condition are specified, the transition can only happen when both are fulfilled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#intent DialogflowCxPage#intent}
        :param target_flow: The target flow to transition to. Format: projects//locations//agents//flows/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#target_flow DialogflowCxPage#target_flow}
        :param target_page: The target page to transition to. Format: projects//locations//agents//flows//pages/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#target_page DialogflowCxPage#target_page}
        :param trigger_fulfillment: trigger_fulfillment block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#trigger_fulfillment DialogflowCxPage#trigger_fulfillment}
        '''
        if isinstance(trigger_fulfillment, dict):
            trigger_fulfillment = DialogflowCxPageTransitionRoutesTriggerFulfillment(**trigger_fulfillment)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b3435eb1a146fc63d7e6d293889fda573b9bff719bbdaf59bcea81e6eb98ada)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#condition DialogflowCxPage#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def intent(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an Intent.

        Format: projects//locations//agents//intents/. Indicates that the transition can only happen when the given intent is matched. At least one of intent or condition must be specified. When both intent and condition are specified, the transition can only happen when both are fulfilled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#intent DialogflowCxPage#intent}
        '''
        result = self._values.get("intent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_flow(self) -> typing.Optional[builtins.str]:
        '''The target flow to transition to. Format: projects//locations//agents//flows/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#target_flow DialogflowCxPage#target_flow}
        '''
        result = self._values.get("target_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_page(self) -> typing.Optional[builtins.str]:
        '''The target page to transition to. Format: projects//locations//agents//flows//pages/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#target_page DialogflowCxPage#target_page}
        '''
        result = self._values.get("target_page")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger_fulfillment(
        self,
    ) -> typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillment"]:
        '''trigger_fulfillment block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#trigger_fulfillment DialogflowCxPage#trigger_fulfillment}
        '''
        result = self._values.get("trigger_fulfillment")
        return typing.cast(typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageTransitionRoutes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageTransitionRoutesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__46540ff2c84fd09076c73342fc2d46e8921d558b6467a3480fe739931316229c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageTransitionRoutesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__420cfb1c1d7d8a3f16df38b019c07f6e16ff52d4b02fce439fc40849c3f88016)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageTransitionRoutesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f766fda6b99326a90062090b50c4727f7dc8112e39bb9e97183f4b6b0b16ee9a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac225f06b4ab414b3a6e1c08609ba41b53514d64de8383291fa16935d1fe6ab9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eff84c7dbd08cae100d48c3311bdfb9656ccc831e5a228dbf46289293b406c6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__229959eb3cf663c0698ef2d689a22acf6500524bed95056a6193672bb0c61897)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageTransitionRoutesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__afc47d02f9f9d8ebc69fd9923e29bf79b568299e87607085c7a27ae4e590e182)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTriggerFulfillment")
    def put_trigger_fulfillment(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases", typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        value = DialogflowCxPageTransitionRoutesTriggerFulfillment(
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
    ) -> "DialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference":
        return typing.cast("DialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference", jsii.get(self, "triggerFulfillment"))

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
    ) -> typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillment"]:
        return typing.cast(typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillment"], jsii.get(self, "triggerFulfillmentInput"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "condition"))

    @condition.setter
    def condition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81b1922418924023773fbc449810d4ef493bd61400797e8ad1551b413ec17828)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "condition", value)

    @builtins.property
    @jsii.member(jsii_name="intent")
    def intent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intent"))

    @intent.setter
    def intent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21fdf4b07d988386a65511fe0e5004026924601205333cc64e43a2ae971d9f23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intent", value)

    @builtins.property
    @jsii.member(jsii_name="targetFlow")
    def target_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetFlow"))

    @target_flow.setter
    def target_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d03f3404f145c76c35aaeec4040f93ab4f0a9a36a4ef5f5042de6dd5297938a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetFlow", value)

    @builtins.property
    @jsii.member(jsii_name="targetPage")
    def target_page(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPage"))

    @target_page.setter
    def target_page(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b3ec57a6c3ff8f466bafe8de6cef29b823cd402c47449dd4e7329552596f81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutes]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutes]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutes]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__901c8134c279bcafdc495edf34345f816d9c3e8d155df607743f510c7b686dad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillment",
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
class DialogflowCxPageTransitionRoutesTriggerFulfillment:
    def __init__(
        self,
        *,
        conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases", typing.Dict[builtins.str, typing.Any]]]]] = None,
        messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditional_cases: conditional_cases block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        :param messages: messages block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        :param set_parameter_actions: set_parameter_actions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a97a872305ddc645dd18929371877893606a6c501a3b834ec0f824adf60e91fd)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases"]]]:
        '''conditional_cases block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conditional_cases DialogflowCxPage#conditional_cases}
        '''
        result = self._values.get("conditional_cases")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases"]]], result)

    @builtins.property
    def messages(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages"]]]:
        '''messages block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#messages DialogflowCxPage#messages}
        '''
        result = self._values.get("messages")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages"]]], result)

    @builtins.property
    def return_partial_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs.

        If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#return_partial_responses DialogflowCxPage#return_partial_responses}
        '''
        result = self._values.get("return_partial_responses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def set_parameter_actions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions"]]]:
        '''set_parameter_actions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#set_parameter_actions DialogflowCxPage#set_parameter_actions}
        '''
        result = self._values.get("set_parameter_actions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions"]]], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The tag used by the webhook to identify which fulfillment is being called.

        This field is required if webhook is specified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#tag DialogflowCxPage#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook(self) -> typing.Optional[builtins.str]:
        '''The webhook to call. Format: projects//locations//agents//webhooks/.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#webhook DialogflowCxPage#webhook}
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageTransitionRoutesTriggerFulfillment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases",
    jsii_struct_bases=[],
    name_mapping={"cases": "cases"},
)
class DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases:
    def __init__(self, *, cases: typing.Optional[builtins.str] = None) -> None:
        '''
        :param cases: A JSON encoded list of cascading if-else conditions. Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored. See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#cases DialogflowCxPage#cases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b83c74829229872c98e1ed0124487bb8f099acc8be3aeac4f2f7b0714d3f52bc)
            check_type(argname="argument cases", value=cases, expected_type=type_hints["cases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cases is not None:
            self._values["cases"] = cases

    @builtins.property
    def cases(self) -> typing.Optional[builtins.str]:
        '''A JSON encoded list of cascading if-else conditions.

        Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored.
        See `Case <https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment#case>`_ for the schema.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#cases DialogflowCxPage#cases}
        '''
        result = self._values.get("cases")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5aa345ac5a14a6e5cb16548a021a00aab77e5e606c661d422ab6a3a88d08ef1f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a7610c085480b0d0fe22f43be49b7532ddb825fc19d5d99f4bb3d08a61bb992)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d4bf90eba61a3faceab2f07fb101f79f9e8a7bf029ff71ebb98c242251c1b12)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc80c33362ce64203f02455d41fecc2ce22f8081736a73d95d2111efb80ef714)
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
            type_hints = typing.get_type_hints(_typecheckingstub__024ae6c4c6f027c4da2fb483653fbc8c31103904180d6814f53810e206d6c843)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bef7503cd21d754c517f750e11ac63d24f2008c5798e798695fa29392bef498)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e3b2e2bb60d9a064c4312ad69cce01233415a67208e4bd4f63f9e0ad9e4661b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__930c10cd5d7407117c22ff89dc142813d8c98597f4f904d478dc93f0eaea6568)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cases", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abb09bf9e873adda2818a285a138676f94d67bad486530cc4b4fe747f3a69cb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages",
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
class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages:
    def __init__(
        self,
        *,
        channel: typing.Optional[builtins.str] = None,
        conversation_success: typing.Optional[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess", typing.Dict[builtins.str, typing.Any]]] = None,
        live_agent_handoff: typing.Optional[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff", typing.Dict[builtins.str, typing.Any]]] = None,
        output_audio_text: typing.Optional[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText", typing.Dict[builtins.str, typing.Any]]] = None,
        payload: typing.Optional[builtins.str] = None,
        play_audio: typing.Optional[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio", typing.Dict[builtins.str, typing.Any]]] = None,
        telephony_transfer_call: typing.Optional[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall", typing.Dict[builtins.str, typing.Any]]] = None,
        text: typing.Optional[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param channel: The channel which the response is associated with. Clients can specify the channel via QueryParameters.channel, and only associated channel response will be returned. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#channel DialogflowCxPage#channel}
        :param conversation_success: conversation_success block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conversation_success DialogflowCxPage#conversation_success}
        :param live_agent_handoff: live_agent_handoff block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#live_agent_handoff DialogflowCxPage#live_agent_handoff}
        :param output_audio_text: output_audio_text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#output_audio_text DialogflowCxPage#output_audio_text}
        :param payload: A custom, platform-specific payload. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#payload DialogflowCxPage#payload}
        :param play_audio: play_audio block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#play_audio DialogflowCxPage#play_audio}
        :param telephony_transfer_call: telephony_transfer_call block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#telephony_transfer_call DialogflowCxPage#telephony_transfer_call}
        :param text: text block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if isinstance(conversation_success, dict):
            conversation_success = DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess(**conversation_success)
        if isinstance(live_agent_handoff, dict):
            live_agent_handoff = DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff(**live_agent_handoff)
        if isinstance(output_audio_text, dict):
            output_audio_text = DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText(**output_audio_text)
        if isinstance(play_audio, dict):
            play_audio = DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio(**play_audio)
        if isinstance(telephony_transfer_call, dict):
            telephony_transfer_call = DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall(**telephony_transfer_call)
        if isinstance(text, dict):
            text = DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText(**text)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d22ce8934a9bca258cd2e799d597ad03bfd47a02e609a93611e4fb345e4c184)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#channel DialogflowCxPage#channel}
        '''
        result = self._values.get("channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conversation_success(
        self,
    ) -> typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess"]:
        '''conversation_success block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#conversation_success DialogflowCxPage#conversation_success}
        '''
        result = self._values.get("conversation_success")
        return typing.cast(typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess"], result)

    @builtins.property
    def live_agent_handoff(
        self,
    ) -> typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff"]:
        '''live_agent_handoff block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#live_agent_handoff DialogflowCxPage#live_agent_handoff}
        '''
        result = self._values.get("live_agent_handoff")
        return typing.cast(typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff"], result)

    @builtins.property
    def output_audio_text(
        self,
    ) -> typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText"]:
        '''output_audio_text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#output_audio_text DialogflowCxPage#output_audio_text}
        '''
        result = self._values.get("output_audio_text")
        return typing.cast(typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText"], result)

    @builtins.property
    def payload(self) -> typing.Optional[builtins.str]:
        '''A custom, platform-specific payload.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#payload DialogflowCxPage#payload}
        '''
        result = self._values.get("payload")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def play_audio(
        self,
    ) -> typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio"]:
        '''play_audio block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#play_audio DialogflowCxPage#play_audio}
        '''
        result = self._values.get("play_audio")
        return typing.cast(typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio"], result)

    @builtins.property
    def telephony_transfer_call(
        self,
    ) -> typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall"]:
        '''telephony_transfer_call block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#telephony_transfer_call DialogflowCxPage#telephony_transfer_call}
        '''
        result = self._values.get("telephony_transfer_call")
        return typing.cast(typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall"], result)

    @builtins.property
    def text(
        self,
    ) -> typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText"]:
        '''text block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0af7c427fa2f7ff2969025807f3153756f8bb0024db2ba1e9cba182e67d5314)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccessOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__930d5f3b6c3ab578c61388c5490f17c7c04281bff6aac2de1677cc5fd5bffaa7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__350aeee9e821543de6c80b6debeb1b69ea1ff5bd10686933524edbae13c34ba0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__015255b21ec1d2a3363df5ece2cd59398fedcb7e0be7b53a57753f05006bf326)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9f3c16e44c20f2d8ddb6385f99619d0fde68b0adfac481c54a84f08a9ea11584)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4615fbd30bdeb1460c3590d248c3297ba150d054b3e0df2f02a555dc6e95ad2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73a00feb449934341e9412bd11fe0f6181c04b222923c77197165d0dd87d5ae8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__429b3b07aafdbac74649dc0514e678a98d3e0132419e0e84500804847749aa72)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70a8ff8286f97e9b2de1883e5cc2f78fc193ca81c6eb8095fb30aa7e2a67a4a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afed3854e9dbe53ea3ac9c2e35933b29acc40c3a173d9d02fbc0c869dd3d3c2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff:
    def __init__(self, *, metadata: typing.Optional[builtins.str] = None) -> None:
        '''
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__415a0ba89f2c3f9a528509d439e875ccdf09c2b3af4e4c9e8fc65134d8ead551)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''Custom metadata. Dialogflow doesn't impose any structure on this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoffOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoffOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c4011edc221b767e57fe6f6f03541dcdc02b50b074bfc0fdf93f23400cd5db29)
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
            type_hints = typing.get_type_hints(_typecheckingstub__64e94bd10599c1306157f7107cd96fb20ce56078c3e5d57e01b380c69d7a87f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee55b6d3a077b4bd8bad07148690afbf23537b8278000798b43688a1aad6453c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText",
    jsii_struct_bases=[],
    name_mapping={"ssml": "ssml", "text": "text"},
)
class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText:
    def __init__(
        self,
        *,
        ssml: typing.Optional[builtins.str] = None,
        text: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e56430df76cb33cff7367f84097006c77f5add1c6017331d1455bfc7b37bad1f)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        '''
        result = self._values.get("ssml")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def text(self) -> typing.Optional[builtins.str]:
        '''The raw text to be synthesized.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__432aca8f9a9673c83a85d5160db3c62f0cc52996da38878d3e17a20462ca5f14)
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
            type_hints = typing.get_type_hints(_typecheckingstub__63bcdfa0e0b407a140081ef2d3520144d2ac2614f4f9292b50431d3f83818370)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssml", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d847f5dbcc6b8f571733d8ca573503ca8d1668dad1e95db90393463c88db11a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e3370bf506fd143c3a29f0848a629344b39470971e235e4186b753917227c03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d48e4c11699dd3ec0d5b6c0026e486e289be2713bd6e974d25756eaf7580cedb)
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
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        value = DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess(
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
        :param metadata: Custom metadata. Dialogflow doesn't impose any structure on this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#metadata DialogflowCxPage#metadata}
        '''
        value = DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff(
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
        :param ssml: The SSML text to be synthesized. For more information, see SSML. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#ssml DialogflowCxPage#ssml}
        :param text: The raw text to be synthesized. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        value = DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText(
            ssml=ssml, text=text
        )

        return typing.cast(None, jsii.invoke(self, "putOutputAudioText", [value]))

    @jsii.member(jsii_name="putPlayAudio")
    def put_play_audio(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        value = DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio(
            audio_uri=audio_uri
        )

        return typing.cast(None, jsii.invoke(self, "putPlayAudio", [value]))

    @jsii.member(jsii_name="putTelephonyTransferCall")
    def put_telephony_transfer_call(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        value = DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall(
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
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        value = DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText(
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
    ) -> DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccessOutputReference:
        return typing.cast(DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccessOutputReference, jsii.get(self, "conversationSuccess"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoffOutputReference:
        return typing.cast(DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoffOutputReference, jsii.get(self, "liveAgentHandoff"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioText")
    def output_audio_text(
        self,
    ) -> DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioTextOutputReference:
        return typing.cast(DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioTextOutputReference, jsii.get(self, "outputAudioText"))

    @builtins.property
    @jsii.member(jsii_name="playAudio")
    def play_audio(
        self,
    ) -> "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudioOutputReference":
        return typing.cast("DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudioOutputReference", jsii.get(self, "playAudio"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCallOutputReference":
        return typing.cast("DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCallOutputReference", jsii.get(self, "telephonyTransferCall"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(
        self,
    ) -> "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTextOutputReference":
        return typing.cast("DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTextOutputReference", jsii.get(self, "text"))

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="conversationSuccessInput")
    def conversation_success_input(
        self,
    ) -> typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess]:
        return typing.cast(typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess], jsii.get(self, "conversationSuccessInput"))

    @builtins.property
    @jsii.member(jsii_name="liveAgentHandoffInput")
    def live_agent_handoff_input(
        self,
    ) -> typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff]:
        return typing.cast(typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff], jsii.get(self, "liveAgentHandoffInput"))

    @builtins.property
    @jsii.member(jsii_name="outputAudioTextInput")
    def output_audio_text_input(
        self,
    ) -> typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText]:
        return typing.cast(typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText], jsii.get(self, "outputAudioTextInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadInput")
    def payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadInput"))

    @builtins.property
    @jsii.member(jsii_name="playAudioInput")
    def play_audio_input(
        self,
    ) -> typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio"]:
        return typing.cast(typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio"], jsii.get(self, "playAudioInput"))

    @builtins.property
    @jsii.member(jsii_name="telephonyTransferCallInput")
    def telephony_transfer_call_input(
        self,
    ) -> typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall"]:
        return typing.cast(typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall"], jsii.get(self, "telephonyTransferCallInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(
        self,
    ) -> typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText"]:
        return typing.cast(typing.Optional["DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText"], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channel"))

    @channel.setter
    def channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a04e56e7efbf26c27ee4321d19fb2710174d0bb7927906a2b5619af0063b70d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="payload")
    def payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payload"))

    @payload.setter
    def payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__209fbd7fbb7c10c95c190697977508fa1bd297818a5e5640ac41c04f5c01a503)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payload", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1cb45f4bf1cd472528176699250fcee8b0f5a955ba125bfa79abeea5fa89d2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio",
    jsii_struct_bases=[],
    name_mapping={"audio_uri": "audioUri"},
)
class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio:
    def __init__(self, *, audio_uri: builtins.str) -> None:
        '''
        :param audio_uri: URI of the audio clip. Dialogflow does not impose any validation on this value. It is specific to the client that reads it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32fa8953e5eddde87dfce36af9d4ab29166121ed6bc1c3e7496e958f708df679)
            check_type(argname="argument audio_uri", value=audio_uri, expected_type=type_hints["audio_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "audio_uri": audio_uri,
        }

    @builtins.property
    def audio_uri(self) -> builtins.str:
        '''URI of the audio clip.

        Dialogflow does not impose any validation on this value. It is specific to the client that reads it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#audio_uri DialogflowCxPage#audio_uri}
        '''
        result = self._values.get("audio_uri")
        assert result is not None, "Required property 'audio_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudioOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudioOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c965306e4cf9e1fc56b546e90fe5a80f1e72e882b29283d5982cdeaec4c6ad9e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ed0960649e88ad149dc23c065920b0063b59c0562d7d7b079441d2cad72c9f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio]:
        return typing.cast(typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74b0321ee8864f2b4bd390f004a8a0b4f59145a39c0810d504ad0e60fc6cfd2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall",
    jsii_struct_bases=[],
    name_mapping={"phone_number": "phoneNumber"},
)
class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall:
    def __init__(self, *, phone_number: builtins.str) -> None:
        '''
        :param phone_number: Transfer the call to a phone number in E.164 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18617bd321e91cf3e474fcacecf34e74c11f24f22253feef6e6aa8209e2f7ce7)
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "phone_number": phone_number,
        }

    @builtins.property
    def phone_number(self) -> builtins.str:
        '''Transfer the call to a phone number in E.164 format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#phone_number DialogflowCxPage#phone_number}
        '''
        result = self._values.get("phone_number")
        assert result is not None, "Required property 'phone_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCallOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCallOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c6571dce2f4b6961e83287498c65d3d669113de231eb97785181a8eb37f0a9e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e52321f156071788c83ecb9d80faf1cef37bca72aadf831ff716a8725ed3e19d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall]:
        return typing.cast(typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3341ad650af3e72408c6d15b9ab6ec59a6c27de9ab6bbae93bc8fff81d6c5c76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f229b0f5398de9819fbd94bb7660e0408e42120b4e82942a08f7d9c65e803c6d)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A collection of text responses.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#text DialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc51c1fb7863a377441c47262a5331aea1b9b88b333fbd70e94e7dd867ddc150)
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
            type_hints = typing.get_type_hints(_typecheckingstub__165d58e126c7aa73b28c066cb408a8072687b8bcb5cbad62af23f964ec1c121e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText]:
        return typing.cast(typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bdf78eb3543e05aea0d5bfaa26a3fdad6a2a3e85dae6491af398873654c0c32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea3cbb3620ed0939e38dd92bfbc402432c69c4cb5070257496ec76f3c829a1d5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConditionalCases")
    def put_conditional_cases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eba185bb89fd5d4b237a02894814867363b6cf4efd1ed2e80a7d6455c221658b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConditionalCases", [value]))

    @jsii.member(jsii_name="putMessages")
    def put_messages(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afc61086a8fbba8d92206d0954fbc4f1d1a51effc040cd201616cf2781d9fc5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessages", [value]))

    @jsii.member(jsii_name="putSetParameterActions")
    def put_set_parameter_actions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a97c828ef785e306b959769cf0abd5bff3855e47167acc526c7062700fb217a5)
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
    ) -> DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCasesList:
        return typing.cast(DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCasesList, jsii.get(self, "conditionalCases"))

    @builtins.property
    @jsii.member(jsii_name="messages")
    def messages(
        self,
    ) -> DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList:
        return typing.cast(DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList, jsii.get(self, "messages"))

    @builtins.property
    @jsii.member(jsii_name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> "DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActionsList":
        return typing.cast("DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActionsList", jsii.get(self, "setParameterActions"))

    @builtins.property
    @jsii.member(jsii_name="conditionalCasesInput")
    def conditional_cases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases]]], jsii.get(self, "conditionalCasesInput"))

    @builtins.property
    @jsii.member(jsii_name="messagesInput")
    def messages_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]]], jsii.get(self, "messagesInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions"]]], jsii.get(self, "setParameterActionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__73e78df8164162d3a9b1c90492b27437ea1b2046668d42b69b65f4e859e5a94e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnPartialResponses", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__065f9fba4af77da30a2390a4ee81b0c8800d9a7e2f719a842e28f641aeed787c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhook"))

    @webhook.setter
    def webhook(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4abb4351a647581ea5289ae8ec97df80be83a4be2af41c807c181a628615aafc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhook", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillment]:
        return typing.cast(typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efeb2c980b86abe8e81f39af0ccbf811a86ef1a5a125b02df0dae781123c219c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions",
    jsii_struct_bases=[],
    name_mapping={"parameter": "parameter", "value": "value"},
)
class DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions:
    def __init__(
        self,
        *,
        parameter: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param parameter: Display name of the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parameter DialogflowCxPage#parameter}
        :param value: The new JSON-encoded value of the parameter. A null value clears the parameter. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#value DialogflowCxPage#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5700713004cb59bc56318b50c1f1c2e38227de5d1bed214451756c09499d80bc)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#parameter DialogflowCxPage#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The new JSON-encoded value of the parameter. A null value clears the parameter.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google/5.18.0/docs/resources/dialogflow_cx_page#value DialogflowCxPage#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a63f10442a94fe29974836ae6e074b79e6d33a760e96881c98d71cfea448d3ba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e6f871bac10ceda742a7ff34a4fe369f8c946170603ecc788e7d9e35d319a99)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__651680b31c489a095ecc088d4aa782a7a592d4ded848d0ac6fdb370b5a13c6a9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__15dfa29b966f38c5d30fbc83de90ca80ca43a11ab9e1bb956761e45c6d1a2a09)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af16ff9540168099ee7b3fba27147e14b4d3436a2cb47de71b8a855113f66706)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__090d868f4df589ff8b89499036054048b393093d9e00bcb483a42b27d0b86673)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.dialogflowCxPage.DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2437932259c5600d5ba7f6db4dbb6d2e6fa3bbc43bf88696d14499f3b5c33faa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2246f085b14f333434cadf3de2ff822e8f37ccf82678c91de9e041f4d8da79cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameter", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__828e0c9fde17f7d9c613caa4b458316fde1c417c34872a34d19c60b28f24b4ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__172053e84a993940c6bd929fca2ce3c97dd5ef61b607e2416c41ce74b2767b6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DialogflowCxPage",
    "DialogflowCxPageAdvancedSettings",
    "DialogflowCxPageAdvancedSettingsDtmfSettings",
    "DialogflowCxPageAdvancedSettingsDtmfSettingsOutputReference",
    "DialogflowCxPageAdvancedSettingsOutputReference",
    "DialogflowCxPageConfig",
    "DialogflowCxPageEntryFulfillment",
    "DialogflowCxPageEntryFulfillmentConditionalCases",
    "DialogflowCxPageEntryFulfillmentConditionalCasesList",
    "DialogflowCxPageEntryFulfillmentConditionalCasesOutputReference",
    "DialogflowCxPageEntryFulfillmentMessages",
    "DialogflowCxPageEntryFulfillmentMessagesConversationSuccess",
    "DialogflowCxPageEntryFulfillmentMessagesConversationSuccessOutputReference",
    "DialogflowCxPageEntryFulfillmentMessagesList",
    "DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff",
    "DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoffOutputReference",
    "DialogflowCxPageEntryFulfillmentMessagesOutputAudioText",
    "DialogflowCxPageEntryFulfillmentMessagesOutputAudioTextOutputReference",
    "DialogflowCxPageEntryFulfillmentMessagesOutputReference",
    "DialogflowCxPageEntryFulfillmentMessagesPlayAudio",
    "DialogflowCxPageEntryFulfillmentMessagesPlayAudioOutputReference",
    "DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall",
    "DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCallOutputReference",
    "DialogflowCxPageEntryFulfillmentMessagesText",
    "DialogflowCxPageEntryFulfillmentMessagesTextOutputReference",
    "DialogflowCxPageEntryFulfillmentOutputReference",
    "DialogflowCxPageEntryFulfillmentSetParameterActions",
    "DialogflowCxPageEntryFulfillmentSetParameterActionsList",
    "DialogflowCxPageEntryFulfillmentSetParameterActionsOutputReference",
    "DialogflowCxPageEventHandlers",
    "DialogflowCxPageEventHandlersList",
    "DialogflowCxPageEventHandlersOutputReference",
    "DialogflowCxPageEventHandlersTriggerFulfillment",
    "DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases",
    "DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCasesList",
    "DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCasesOutputReference",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessages",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesList",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputReference",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText",
    "DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTextOutputReference",
    "DialogflowCxPageEventHandlersTriggerFulfillmentOutputReference",
    "DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions",
    "DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActionsList",
    "DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActionsOutputReference",
    "DialogflowCxPageForm",
    "DialogflowCxPageFormOutputReference",
    "DialogflowCxPageFormParameters",
    "DialogflowCxPageFormParametersAdvancedSettings",
    "DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings",
    "DialogflowCxPageFormParametersAdvancedSettingsDtmfSettingsOutputReference",
    "DialogflowCxPageFormParametersAdvancedSettingsOutputReference",
    "DialogflowCxPageFormParametersFillBehavior",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCasesList",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCasesOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccessOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoffOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioTextOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudioOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCallOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTextOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActionsList",
    "DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActionsOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersList",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCasesList",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCasesOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccessOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesList",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoffOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioTextOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudioOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCallOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTextOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentOutputReference",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActionsList",
    "DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActionsOutputReference",
    "DialogflowCxPageFormParametersList",
    "DialogflowCxPageFormParametersOutputReference",
    "DialogflowCxPageTimeouts",
    "DialogflowCxPageTimeoutsOutputReference",
    "DialogflowCxPageTransitionRoutes",
    "DialogflowCxPageTransitionRoutesList",
    "DialogflowCxPageTransitionRoutesOutputReference",
    "DialogflowCxPageTransitionRoutesTriggerFulfillment",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCasesList",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCasesOutputReference",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccessOutputReference",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoffOutputReference",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioTextOutputReference",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputReference",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudioOutputReference",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCallOutputReference",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTextOutputReference",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActionsList",
    "DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActionsOutputReference",
]

publication.publish()

def _typecheckingstub__00b86788db75afcf01217cbd511e679f06595dd57e1056597a09befbc8f50a32(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    display_name: builtins.str,
    advanced_settings: typing.Optional[typing.Union[DialogflowCxPageAdvancedSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    entry_fulfillment: typing.Optional[typing.Union[DialogflowCxPageEntryFulfillment, typing.Dict[builtins.str, typing.Any]]] = None,
    event_handlers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEventHandlers, typing.Dict[builtins.str, typing.Any]]]]] = None,
    form: typing.Optional[typing.Union[DialogflowCxPageForm, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    language_code: typing.Optional[builtins.str] = None,
    parent: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DialogflowCxPageTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    transition_route_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    transition_routes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageTransitionRoutes, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__70dabc77390af26ce1af0dae01d3295e83d72d47b491fd0246e3bab431ec5ca1(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fb46f6fddfb632220c0d64201fa83c198ab42e08587a7ecaece5e8d4c5bea8b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEventHandlers, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c4a44baf7325117b478a21418fb8f6be38c5805baa6f51c89529da837056db(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageTransitionRoutes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aceda3d155ee2d774d4b22ae88f216f4ff133b283f13db4d35f848af4e6be42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc7c125078f31eb07da0320574b389a6b62974efe8287efbbc04039a6752930(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f58a8e77d7c407853b3786dae0d25eb1dae499dc05503d5e1a07dbf7a6262e38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28d78b7c3ab6ef0892396a1958b1e536c8a95e0fb18cf05ecee6ed30d242d125(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ebefab9cd26ab16d6738be5396da33e6d9d6b895a4efd6781900524c8307b1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ede6ab22672c198ad0eb08a56cdc69b984c7549f2c380101b6b26c6d89a716c6(
    *,
    dtmf_settings: typing.Optional[typing.Union[DialogflowCxPageAdvancedSettingsDtmfSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dc27bcbe8f8e53a3bc08f9bd3fc80ecca9638c2dd1341048271efdd57d64128(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    finish_digit: typing.Optional[builtins.str] = None,
    max_digits: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__381a30c71721b1169b31eac5ed44b2744dd7f862d1bb32ee6103da464e1874ba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b03718649b5cb0e240649c5f70671dae47fa71115b97cb06c5e0c945f5a7e0f7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__162f3e1f727c3d53030937442e50f4a496a5abc07259f0c1d890ece0a4810dce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0a69750a52b9bbf74c7baf696658177d811cae3de5339e8f04a034b092a5a0d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22ce22ee5dc6f10ebec9f3991740c04e8153ed65f04c87ce1f01cb99088b41af(
    value: typing.Optional[DialogflowCxPageAdvancedSettingsDtmfSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e4cffa87c3547f58bd21b541c5133d84627a7dbc1bc3f48ae1656417dd9835c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61d7936a9ddf43a7da71bfe2901b18027a2fcdf60b33fc446ee9c19ad432fbaa(
    value: typing.Optional[DialogflowCxPageAdvancedSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15dea158de3b8394ae860686740472a26b1661a6cdee78808233b04283785d3a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    display_name: builtins.str,
    advanced_settings: typing.Optional[typing.Union[DialogflowCxPageAdvancedSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    entry_fulfillment: typing.Optional[typing.Union[DialogflowCxPageEntryFulfillment, typing.Dict[builtins.str, typing.Any]]] = None,
    event_handlers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEventHandlers, typing.Dict[builtins.str, typing.Any]]]]] = None,
    form: typing.Optional[typing.Union[DialogflowCxPageForm, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    language_code: typing.Optional[builtins.str] = None,
    parent: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DialogflowCxPageTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    transition_route_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    transition_routes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageTransitionRoutes, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71dd5966ad8a933ab4a894dbb073a900bc484ab8d156c35b52c846bd0603c4a6(
    *,
    conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEntryFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]]] = None,
    messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEntryFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]]] = None,
    return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEntryFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tag: typing.Optional[builtins.str] = None,
    webhook: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41d585dc3d116965de82971528c72684a85e927c44d68a81038ea69b7f119f8a(
    *,
    cases: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d18c361d178af1f929fc21abbb6c93e795037e235b2566981a2e3d6d19f33b9d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e8ee129a863240770c9caeab6149676d1928c16dd220aafa9bc9fae864f07d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffc9ac7dad5e7eabc3e774ea725f330c6250d16ff9aa3be598cfbb6f04444858(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51a96b2d25253a2999b85199244f765c608871440ff03f222fca52ba0fada650(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5afc08592983725d0cd6463f6fe0f8740aeaddcef4a55fa7370537dec6a243(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e5f19ea9f7e0ad208a668db2c77f3d9689f078e5da3595d7c973acdbdadccbc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentConditionalCases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec79794d2732ecc45da2c799893f6a112a3ceb72481aceb851b0bb910c0a2480(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74a3aeb5acba7e3dc70f2aebae4704ff0bc86115cbf6397991134015b1385987(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da5c278a715b2ec6b510e85dcf4cbb2951593f74d50e9b23a7f020cd55745e0d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEntryFulfillmentConditionalCases]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49dcdce78eeddc0ea0c91912a267826414666a09fd42e6c12aabefd14ac01d58(
    *,
    channel: typing.Optional[builtins.str] = None,
    conversation_success: typing.Optional[typing.Union[DialogflowCxPageEntryFulfillmentMessagesConversationSuccess, typing.Dict[builtins.str, typing.Any]]] = None,
    live_agent_handoff: typing.Optional[typing.Union[DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff, typing.Dict[builtins.str, typing.Any]]] = None,
    output_audio_text: typing.Optional[typing.Union[DialogflowCxPageEntryFulfillmentMessagesOutputAudioText, typing.Dict[builtins.str, typing.Any]]] = None,
    payload: typing.Optional[builtins.str] = None,
    play_audio: typing.Optional[typing.Union[DialogflowCxPageEntryFulfillmentMessagesPlayAudio, typing.Dict[builtins.str, typing.Any]]] = None,
    telephony_transfer_call: typing.Optional[typing.Union[DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall, typing.Dict[builtins.str, typing.Any]]] = None,
    text: typing.Optional[typing.Union[DialogflowCxPageEntryFulfillmentMessagesText, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4a589cb1b88663ef1899817b26ef8f98b20e8d574d0471c301d0cffba3dd4e6(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c8d944cd5967b8535e11da8f08fd7311914c1ec0c5301049a714b0b9164d517(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f591106f876e9bb6fe5a9193ad22e7a4c21d31bc64fa8614c89b3a41f5ce74b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86b65a910fab838aee783af7bc580bd4f7d92e2b2afd5eae3ba600fb8b171f98(
    value: typing.Optional[DialogflowCxPageEntryFulfillmentMessagesConversationSuccess],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5613dd1beaa1c4997bacf84707ddd469dc64ba513ea84f5c4ac9ea66c8a7ef5e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53cde70270348affee1882e2e525e8548831b8bc3b03c0b9e7af48627d403993(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0b049268bb985919745730a00796bf11fec3b1a9ad23a3d64efc1a5341d53c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a2a5e2487adb1d43930ada8e1d15166b55fb0d6cc408b1652e516e9bef05f00(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ece63606e5d8c191695e3bcc239c17141277efbde4acd74764a2c15ac2777d7f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79182987451d800a73bc1c3badae415bba1d3ed46a2c34fc6cbf27a2c1d0d3d6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentMessages]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1af518f20749fd68eb9f57c02271445ed79c9fb61c5735c1016ccd32a2aba71d(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8df7cb7ddd056fdeb6d2a239386b1b334eb0eba4454c3d75c8b0474032cd3a61(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3bc1a4f84ede5c40aba6192875fde441ca1f020f6661a1dcf48a5133ccf265b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__559614559c63021e07e09edae87cf64a2b3b0b1505fa1d624f3f1bdd1767add6(
    value: typing.Optional[DialogflowCxPageEntryFulfillmentMessagesLiveAgentHandoff],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__193bdaf74ac9a22e2eb8d8c7c41a54852e77637a20bb9acd6ebc6eb6b4f2c8f1(
    *,
    ssml: typing.Optional[builtins.str] = None,
    text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47af714731e870cc6332f67efe01c0fc73db3868b3d2a2ec72791d03c59e4d50(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae7c619be871b2c23e56301ea7e00bd39110981b1709b633c923d174b2b13578(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed475c8c4ae6606312100e1dcd8aeb0a6e031736372ec454c1fcdfede1a2abd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42e20a3231560ddfd90345ff896126dabdc7c0b18dbb3dc1f766c0d202775c27(
    value: typing.Optional[DialogflowCxPageEntryFulfillmentMessagesOutputAudioText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__978c8cc08cabca00f1aff704c0f4ca333e794550678a0521cb8c306bfd798d22(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9048c88fcf0bdbf04311e892010e897c134b22a199287054645ba372888e83e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0737bb7d2bf1ab370586e8fd5193565c739be41572fb587cfdc1966b22982e64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eb85a40a6a8463d7214548943b5c9b4a6e000998bf7771a4cc4d99b60541a6f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEntryFulfillmentMessages]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab8a645c5c6e3de3b3e18b28afae319c59913634ae339ae458dc9f365861d1e0(
    *,
    audio_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75a9a00557be1848acf544cd57804f2a4ad2c050104a1b1dcab41387b892feb6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f7891d3f220d986aba00f1d05f173f5c63233b436807eb0b5119f5aa2483741(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0831571feddf981b35ca781a775b03e67acb855916885941e378c2e6d352b95f(
    value: typing.Optional[DialogflowCxPageEntryFulfillmentMessagesPlayAudio],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af500d65bfacaf611bc0a3d20a4dcee4edf2f2c1ec83fa1c5ab78af5066cb5d5(
    *,
    phone_number: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad6b39b3f1f34ee5f8d0d03ad62e7f453c3b5c89393c489980d9755adaf3163f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b85f615c8657afba54eed25b21d89f9488a7bbd9438fe43f3145f3edf16661(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd099ead23f7f734dd83bc1343aa01c43829514773a8736c5fcf3c67bba27290(
    value: typing.Optional[DialogflowCxPageEntryFulfillmentMessagesTelephonyTransferCall],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2af505c57abee7200d8cb160c49ca52acbdeb6045dcf61e0299d03ae4462e2e5(
    *,
    text: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8661eaff956649f29f0c4634e31a442cbda0042f98ac148a7989a0a38c3134d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ab95389349952923469867e7d785dd27cc8126be5a7fb954b8921bd723e0772(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4b9d1b0c7d1369c62bedcde8087eb7e0cb0ce75d9b6d46e69ce807b8b79761f(
    value: typing.Optional[DialogflowCxPageEntryFulfillmentMessagesText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cf5a596e516e17c71d09575c4630fc024c4b377f48befe7d2196de54f1ea335(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcc90f3bff330387d00e7f39c374cd2f3953e49596ff0f3fc02630bd52e2f7bf(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEntryFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b6ce8c3783fc7922600009c1d473f5b8d45842feaf69470d2a4327ba31acf83(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEntryFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57502e370be1f5d844f21c5be3a7c4687d452a400160fa5c97137bb4e45ccc65(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEntryFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbd86b9b7707148d069906ee7224ad618eeb0dc32bcfee1d62d3e8206537ad00(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24318a5fce06525c2d5464aa0c7964f88d07f141aec66952bf53a7f4cf11c085(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b645a2f56947e96ce4b3003b366455c62ea637fbf309739d31fefc614ea0b21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10309df25d5605b800644921bf8f526cb3c9e566898cc810cd376f608db1d365(
    value: typing.Optional[DialogflowCxPageEntryFulfillment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__008dc86fbfe60acf8c7e060533552e76880507e7e07dd3d0983f8ad6cc18abac(
    *,
    parameter: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cdd468595e99ef46db7929bcb251a7e560fe4928b72161bcf7a5885ae532859(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f048139d4a6d7a94700cb12c28ed62c4b7ba9a47087246c5308af68b9a7c1d7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16f15cabb2c7e2f61c531e7a15d14596e45a2bfe6754ea2cae2e92ad6b64f3bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c330d94d480fdaa6fd47482b25638e318cd782d41acffcf63a5296f55b41f87(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9b663fd15f365a76c6977f7eb04ae721694c608be1e45ce4a1450eb947b1dc2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79c8b2935763b659bb79dd483521583b5876c5b045b0b944c94f2556a3585105(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEntryFulfillmentSetParameterActions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c18bd735bfcb498b463c6ed802273bba27ae4dde5801c199514349a2668e2dba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceb98c9d2d83adcf22e0e9fcba0ef4ae7cd38e7024cd766d3beb6f5fad24fd49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25e5748382338ac15293400853f0dfa7c43f83171ce8fb32be6036ca799c4397(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e4689a195cb80e1ccb492b424c3d029a76f4ca24bb35064db553a362c8f81a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEntryFulfillmentSetParameterActions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab15ae117f88b8ab8fd8faf8aec04359c52d2bb628fb3aedb74fe47fb030fea3(
    *,
    event: typing.Optional[builtins.str] = None,
    target_flow: typing.Optional[builtins.str] = None,
    target_page: typing.Optional[builtins.str] = None,
    trigger_fulfillment: typing.Optional[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillment, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f48919b767e503e9429acd9d3e0a43fef8f6804bfdf093b76df95d7974fb01ce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99fd9f7ace6de457684cd2263bcf553bccf5a4132d11b5e104fd50c38ab993c2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__704628615f089436d926563e2c4e31a8c56127f782256aaf1c6317f526c24f12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c6c38eec91174f13ad2674fa21c807337c2d523dbb823e4e349e40ca4565700(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa978b017a1129446a73455a4aaf3915220f91390219633c8c0a5ebf7116dde8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83899170e1dcdea3831dc32fff8e1c65e55ca19c81de5d04e69f956a26356d3a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlers]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c16d64c2902739d0451fc9721d989939a3db705e3abc8772178d61174e6ee240(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba7ddce87ad187e41cf2fb78f5cd6b91e99596c7b1e0974e078ff13f602fc460(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a794fd7c5be69446637ecba757d7b8f0c3dfb01006c944ea56bd7a0d33c1eda(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db807ca0284018e651a6273faaa938bd71e046cb9809ed9cf754724cc8ff08f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__690a4cec683b9279070b86397597c918de83137b42754288560bb683613c7b40(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlers]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bf85d749a19598291bf90632116cb8cb83eb3f2a07c3e7ea06b5b228e5f520c(
    *,
    conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]]] = None,
    messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]]] = None,
    return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tag: typing.Optional[builtins.str] = None,
    webhook: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__376d46d915f41b280a077a263fed3d085e118c282b803747288126e5b7e2781d(
    *,
    cases: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41dff1cc77a79e28e79a5c0156779a0bbfb7747192543f6a12180951ac4acb4b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf586672edc31eef11808497d6bd13665e436947d1c98c9e1e4c0ee0217ecaa(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01eb83ee56df19bf34d5bdfd605df29554ef3dc6b472213b1cb5f99a2d6f0190(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dec8da5d11c3ef7ffc5d49d24f650a6d108acb47ca9542e9b37544c70c2b09e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea38da542ad8b4a7c57fde79d259afd66557cdb1acdbf8c249a4a98c1619c5ae(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e870d5668ecdcbfa994a79f894b6a4b8dc69b7b88c89f877cb0a1b337a6b4b5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b658bb5a1025911b1e5de2d943b9cde04ee802d49af1f290e618fbbcfa892d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad4c4f88c3c8922cb35158f3cf2cbe4baec67a692c27f7074164746f909581a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b143f9c90d9da1487c71c07c4772ddae68ba73896208cc6461c2dab1c0c1f3dc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a679968c0dafaadba2798a1411ce95bbd5875be78731f6ecd46d11a12ed922e(
    *,
    channel: typing.Optional[builtins.str] = None,
    conversation_success: typing.Optional[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess, typing.Dict[builtins.str, typing.Any]]] = None,
    live_agent_handoff: typing.Optional[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff, typing.Dict[builtins.str, typing.Any]]] = None,
    output_audio_text: typing.Optional[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText, typing.Dict[builtins.str, typing.Any]]] = None,
    payload: typing.Optional[builtins.str] = None,
    play_audio: typing.Optional[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio, typing.Dict[builtins.str, typing.Any]]] = None,
    telephony_transfer_call: typing.Optional[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall, typing.Dict[builtins.str, typing.Any]]] = None,
    text: typing.Optional[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66d3776604393cf66068ec3466c5254d1e5c62a980a678f84858c1ae1935682d(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b82e9c9e4b31d07b4443b1788b23c9f2021882a8ffef4b35df4d3d9599e83c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__996ae780b3f3289b0455b9dadaed66e529667d87c80d42514c8c69854ef001cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb0e7f666cd5fe7bd145254a8f80cf6286ceaac9fb602e64ae005175a00e903c(
    value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesConversationSuccess],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7054c86f78ebd73f2060ccd90e4b44d98e17035b3521570d1f87ce1a94fdf970(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b46a1306a40dbbf9c194373c8e9db9c08762b35720cdee57b8d115fedf837a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d9004a8ad19edb50b32e3313eca72dd1806d9633b44caca9269c8562c3670cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45b5feef79154b39af79071966d0cfc866e728cf3f1af74dbd11bd008d36432e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b466fdf978aa50076148da2875059e5ff1c18a47c0f8b843641d9b9188de043(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2216f34163c046069ee6e1f70f7998905b8acd7830b52141970506a17e735e18(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentMessages]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c8a575ddbefc9dea3ed7744844cbbbfd63555d8e6cba3db07cad82e69e4aa96(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96fc7d0c61e49a89053b4e8cd27f5aac3842179ccee836156b55717048a9aa0e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__798ba3eaf78d35b7a739dc09bd38735a760dfdcdca5e4d64ba0fcf945d2015de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5560c3182df387dafed740a8c580bd87c7443414c99cc85ad439251920c1adee(
    value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d41a2c2abfb25b3f1b0a30724aa72dfbb48ee7c970dcd611866f4c47d04eb2ce(
    *,
    ssml: typing.Optional[builtins.str] = None,
    text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4835a111619019130dd658632c355fbec8125dcb0a102fd66d1efec86dbe65bd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b47ddf16cf9a4681bb42d6d76c58148ff264b2a6789afc9b356f8a0bff51c88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e9424bb5cf73646e5af9d43693123cf4e4fb62835edf8e7bfae07df6e01a24e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c6d1355cb9118fd4f33f6235a18a4b9379fa91edacb95c4e87fd108cf1dcc02(
    value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputAudioText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef85f5b2e690787853b09a1c94e44953b01462c653d948cf21e58cbb64b7089a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d28d91c12fd5fd876dd3d7e29be7c09d8c53724fb5a4cbc9ca076cccbb3b9002(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__760ca915fded9e8b4f6bdb0853da0a7d1978535b0e2acc471cd84d9ec17899ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b76d157a5b3c0542962ab8a100180e80b9a07150a0722d17a5c8b9abb6b2e3d3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlersTriggerFulfillmentMessages]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49fca395691b291967124071233db405ddde577368b9e02adeff8918e01a0b59(
    *,
    audio_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f8a0ee19e5efae82567c538d675740e8ea5621cca2dc2fa19d52d7cdb1ee68b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2be4c25b92f1241c18902e19f56797fac3ce1bd8297f913fce4a08d739655bb7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55b878af9e0a713b71057f348b3f35426cfd1ce36492ec787b6f7af31defb534(
    value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesPlayAudio],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca7a4a996a2144cdd7b594ff967bfb1a387f9fb8e537fc6b5e35996baf60add(
    *,
    phone_number: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1329fc9182887bfc7ed591a4b9cc799e0862921edbdac095ad67ea749e6502c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dd358d900bb1c4ebacd80f14509121f42abdcda7eedb4bc921e086cc6f594c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__539ea9a9862578e39e7917241309999bc31ff724e255274ccd23d4594080d940(
    value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d098a2973481bf30bea7d9ee978a15fdc45eb04edfde0e74952118233cbc7db(
    *,
    text: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cfc7ee5d8c51fbc803270e05c369e21b710e18475b014460060664ebee4f73f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__643922a224d3ece91edd71b5ac8b58c1f5bc114b43c0a34d9039de3169c6b7cd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afee333ce9550891355da232f661367776e3a297111c137631d8159ae8f5b151(
    value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillmentMessagesText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34fed25d90dd2fe7f715cda5d87e38a9e078412b6d40cfee7d1bd8c1d883ea84(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bdc2d97231c9bae66248e8497f38d0e97f90ad45162618f7a41279b9aa5aa3a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03a78fc11ca4858fa6baa2eef303e4ae5b5b5cfbadcfaec6727945601bc5c069(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc100d1b2225569d072219e4da581a99a693ddaaed2efa7620d1bc245064bc9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00a61a775de73ee57b87737bc537e6786aebeba434d904c36742a04d0778b6ba(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ad9ffa779c7f8ac2808b926cee623a0d8d06f23f041ea1c256f9fe8fe1785d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf34aa83705c176cbc6d55b83c65e46418a74744a81d2c9fef9da5d83c8fcf02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fef7e81fec98cd123e70949f7c0d63ef96674803c1a56ac8365c38d30e533c2(
    value: typing.Optional[DialogflowCxPageEventHandlersTriggerFulfillment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8424b4270698ae56ac5a1c9d7388ce4f62c7a18670b891c951c6a26b094101fd(
    *,
    parameter: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d377d4d8e251fd3c321ae690d97c19b9dbba272574bfc827544a5bca471d42c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0214b491db8f63cebe137755ac838ecf43b3a11a68f35ccd323a676cfeae74af(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__995957ddab309cf3812e8a9d2899f9e904c5c549d4d30cf9d60b200a11a85e31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b26fac11137ebf3bef20e553954f2b04776785ba8fa3e393d98c5ad3007aa39(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b12e6f0dd99483545752876e4fb988165e9437f6dfff90af5217b50eba0e9805(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07fcafba883209c5510d9e2bd6b86303be23fc4e9dc6fb7000074e69f644fd98(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec87219ab5386789d851ba20d0e3bf72a723ec8db42f5b1e3c7f52dfd9cafa46(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5199d9249be0d4d2d00e9192ac3df829e9c53399b49836e7c8d5fe3bb8e6d20c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf78dcf17f929b3ee63250764b25255de23f57ef82ddf44eee56594312e4b8a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d7517aab5c4f80f31e00771dbfa519e2a37d038d0768baef206019917881fbf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageEventHandlersTriggerFulfillmentSetParameterActions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d0be360a713e2ab0a0f26268fcc80f8bb6a4ee71845eac9521c248dbfee8c7c(
    *,
    parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParameters, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b38fd3c3ad7c54a2de0e9b89ad836f182b6d066d8ab0f7847df07b84b52f6b7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b79fcea315a89759f6bc119a67caab611421cea1ca8299c29ec078cf90e1fef(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParameters, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c2d6b52f3955236b3feb7483b9f6445834a2af7ccbd3d509ed0d91a2f184de0(
    value: typing.Optional[DialogflowCxPageForm],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11c068e0f8ff01f7f7df255a459e84c9b12d07a1355c0a203b17799539ce5948(
    *,
    advanced_settings: typing.Optional[typing.Union[DialogflowCxPageFormParametersAdvancedSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    default_value: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    entity_type: typing.Optional[builtins.str] = None,
    fill_behavior: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
    is_list: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    redact: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    required: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__257dac0fbfc389e9d75eaad87d0370157950521fd7a2c7fe5dace4d5ace14ab0(
    *,
    dtmf_settings: typing.Optional[typing.Union[DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26a8fc021fe4f0bf6d645fe60ac419fd76551c20d194869445d2318024e9aa2f(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    finish_digit: typing.Optional[builtins.str] = None,
    max_digits: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63361e435c4bf67d6a07a7067ad6eb31c2a3eb8347d49a294d58550027bd312a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8738a47ac64bb0d377e9d16b4131f37ec1c5267b07565c6e57a883a9e0006691(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36c22831aa0277a89c2e1cd1e9320af5de82f9ed6db3cb96617a0384228cff35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60acaadfeb22703fa9b4bd539de97e8e4fe9994425e6f8f8832d2173d90df31a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aebaaf4ad08f242e4fa79771fcb592048cf3e05f28813afd4ac26f88e90940d(
    value: typing.Optional[DialogflowCxPageFormParametersAdvancedSettingsDtmfSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d28f7a7d3210de92f2f7460e30b9630d27cb7a769a7c5591b279fe420caf9b3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8d2d862153251a49befb095f525a28217bc719affed5dbf5433ba5e15c6c11f(
    value: typing.Optional[DialogflowCxPageFormParametersAdvancedSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03f1251ff13a4fdb1c07b7fc4fc39ed512c7336191a6138718cc1a8d74176e5a(
    *,
    initial_prompt_fulfillment: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment, typing.Dict[builtins.str, typing.Any]]] = None,
    reprompt_event_handlers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__692fc3e920f6f72518c79c0969c1f2eae22c21ab21da05fa77856067192cfe62(
    *,
    conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]]] = None,
    messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]]] = None,
    return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tag: typing.Optional[builtins.str] = None,
    webhook: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e482207f5ce17bfdf97425c075711086264b23ab546b9746aa9e3fa34cf2ee3(
    *,
    cases: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42004927783c3a78c6f21cbdeb134f0bc6d86c1a96535172b37a120d53651972(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edff3733a8c90fae1fb9a5ddb6f86c7c9eea4c06ad8243c35d63b90798e3c4b4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcca37cfc8472e9ac0d86d8d0ad730842c3ee76eea3124696c7b62f644c56618(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f3135b4e476d588273b06654456f0e0f33fce9651aae0e363b3cf0b748213e2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__becd4c2149d6c47fa7901e14e40d00044bcfd4751b02daa964fdfbb9bd976605(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__885f1ba4506a3efe3b40de89ab166274df3c972e199d1d52f61e82a80e64c9a3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eb7295d07ab3ffbf76e7f5e7e4c18df3ef46e5900148608b9f28fa54de85709(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2913f0ff72993e6c777498482b49c4d5929b143e84939d521f1e50b3b839db91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10916fdb82b858832a874eadd5870e4d232afae349dea9bbc4615a58008d8e4a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18271e61c8b487d74b047575b27fc5cc83eb6f06928e148932d80004d5d0cbdc(
    *,
    channel: typing.Optional[builtins.str] = None,
    conversation_success: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess, typing.Dict[builtins.str, typing.Any]]] = None,
    live_agent_handoff: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff, typing.Dict[builtins.str, typing.Any]]] = None,
    output_audio_text: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText, typing.Dict[builtins.str, typing.Any]]] = None,
    payload: typing.Optional[builtins.str] = None,
    play_audio: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio, typing.Dict[builtins.str, typing.Any]]] = None,
    telephony_transfer_call: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall, typing.Dict[builtins.str, typing.Any]]] = None,
    text: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc510bad6ccc125383ff53d636cf742088a99ff42d945d40c4de9ceec5574636(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66300a5157d0334db33b338f035f710df70058144ff9eea5349a850a299d7d1d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f76f4ba1123c4fd070a5411b2f868c223fa7265c37e76163c65cafb05397deaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5257c755211ef5c530ab788314dbea9fcf98afc3f739fcd8252f891dc73f530e(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesConversationSuccess],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18e2c51fff5e58dbbb67d0c6c56555da7413ac65a018d861ef057e7718dcbe52(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b43331be443702fb1badc2a95cf0ba44db05d18c0330e6e74132deab53a10aa0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdcad1a707e7f604e1a8e60f1d2788a96d50980895b608abf43d38c4d87681f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f48ad33f05bab3d1f294d76b83ad1cab1ce46d3b284d2368503a15585daeba5d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8644b12fcbcfe524e8c5d09fb6dd54be8ed0a7c46be0b2202df7449fec8fda82(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36354e4b63c8039e10e203a3303de95849563b933dc23a07074b19bba1b484a2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec5d6aa875fe82b0c1b312fed8ef6db0c55a8f5db6d76185bf5222b1c2174bec(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__093ef6329b98c85838601b3257ce2f56f7239e26fba9c0dc4f0634f96355bf8d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f47c94adddb2d089eacd89fe409d570e7adc51b91e310a74fef83d54ae953d60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f9197edcb7adcae9f12c2b4087e54f8b7af6c366531f2dc3da3448ec40cf1eb(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesLiveAgentHandoff],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd7a2efb0b3fc8b68679ee6954385f03e7cbea23b0847e0ed95a4591eb6505d5(
    *,
    ssml: typing.Optional[builtins.str] = None,
    text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90f13dd6fb779a8cb4fcf084bdaefaa5955e78a6c0b66e60aee88cf63c13cad3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8ae52ae0d03cf27805018ec5631f1572de6270f3bb5e01fba8c1442e45a0006(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4db3619e30fa969f4f6ec92f74e63b300509ac6c9317b386404a9e37e4172a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3865fe4dff04e4c1b261c431fc44ed6d4ec511d3500037507be2f13d628dccb0(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputAudioText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b708a36e4e3dd47b9ce1fe06462ec9dd2e00e673093818461240100026be31f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e5bb98280f1f65bc051ccd2f405cd89ae5c5b7a945eabdcb27925e047464d94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__586d8d6dafddf87599f983391662e22bcaca903ed23879158f2250c855cb8b4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2325a86ea9d5ffc2424cc86ad5e694992ca3928e98f3136a1a904fc2d9813a86(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__111e9595e9d9cea9fe99291727304cd80bb1505494e03bc9609aeeb092eb1673(
    *,
    audio_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__284f6347054ff0400cadfa05eaa25294d75cc11ab485ec0307bb25dd2ff285f6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73816c880c734daedb30c92249e182a5ac862a284e356256f421dad47a22b9e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e319a4ee8f34e77ca756180711f1ba4461e76c534c2da922e2d4b722f84273ea(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesPlayAudio],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aa4839e97b2f271ea666b3e239d459997941d574e178d95fa92ecf4eab2fc18(
    *,
    phone_number: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40321bc113550e70eedd00d2474781035a5adb2dd7fce00d0d8029b708a88424(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b5ec8262685e09fc18273137a6eb882aab7ba48ce1e4a8a88517c1bcfb7e894(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ddba0b5e425d5ffdf5f99604b0373587477797cca4048e88fde0e626df83b00(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTelephonyTransferCall],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6697996e7afbaa35fc7858b33c1854be7d09b753f5d12a9fd567381649ebe89c(
    *,
    text: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__004eec1626ed78aee03936571543bb6052d26797ea60b31eac008a4f117ddbce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9210dbcccc3d5dfdb02ee1f8ef308c71670d00cd118bfa248dff0fdb1b513a9a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec5b918444a4be722f549a0295a510427a91c089cf00090bb1c65c2316aa4d62(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad6fe5fd835894bf08d025aafa3eec11548d7da007d2b236233179ef68212bf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4f5a2b54c3794853e12c7d0d697702a41fd1fbaea36bdb79c9c11c5948f414f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b66ab45c6ae2c7886d743e05ca4b6d3aae605968012cd9b1c891127399137d57(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc286ca59c71eb354298c70830be416d0110b91f1af3ff2d393d16ee3174ca5c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff7279d1f08a550166b6872555b738238e84a97c8e1e9cddaaa15f856a4558ab(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a93af7e0b48aeb42185e0460a56bcac4c51d164d328f553c0f29c7faadebff18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__691945a3b51db8dd5b44ca8f88f98e3aa3e9b23a03cdb8b65f46b3274d0940bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e88cac18cffbca1731f7a49420c57092254b6df424a56069cf1dde9c8e67a71(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2f8d250084b41386398fc1417fc29bfb5af84ba5f4796207a63be51789147a4(
    *,
    parameter: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c67cf06d134313049c76013252917a7f73ae250ae6cfed6a99f07a414b8274d7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__706e9dc1ba13269555a5ae5f2f94c2b320dbd8270accbacbb12caa1c0bfbe697(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cdb831e8055b45e952afd4fbda53a1190b37868d2f4014ad14437619a0797bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01ef0905f8d63e6c5d1cec0d66a5fae641b83c50aeada6c5c499ba0a4d21d16(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e817803c6dfc6174a2ce6ddcb05ef44e65b8a42c71f47e36d2536afcecd487b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5eb89c9cf6e67383187d704bc4a2cffdb911344cf765c410019a246cb36159d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63bbc22365018e711310f749fe1396b2ca8c882bccae4b38851afcab01e16115(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86b697e9fa06554bb640ae9fc8efc8b1758c3d3022af205fecc7a5df3312aa91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7c6d1ca91636bbabbc773d365514a6ff3ce1c7cd6e3cbba98683db6de080565(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4c3ab9eec035875c59d21ae5a86ad6cbce87f116b6eab0778fc91e609e602b3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentSetParameterActions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3066229f7bb71408e9f43905b352f3bfecbfaccbf8c68b3952fd982b0e3034d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf14005a1ef873c9a1029e000520121e99a1328f8605cc64c42953784d572127(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c79d3cf49994812c2d7fa11adeb0a6396ef7c7f318c105321023a445071a6d7(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehavior],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c6f4c393d49a4134fc2cdb09be3c8bc5768c7f7188376f88dc60af512acbfcc(
    *,
    event: typing.Optional[builtins.str] = None,
    target_flow: typing.Optional[builtins.str] = None,
    target_page: typing.Optional[builtins.str] = None,
    trigger_fulfillment: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67f84d9f7ae2c2ed1be16c1bd39d0e4f0bcebc24ebe1d32a7e9dcd4b8bb91c12(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__982b28218fda86b4b0a53c4eb1f1e994f8dd7d09b953b13cdfa5697e4ad28000(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05d2531e1fb36427be61894bce079e6027fb5a80b78d30375b5a1846b2bfd424(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7034ea0b8e63cb16eb19d1f69d9b653c8293d6a902f087dcc6b5a06553a97312(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b763c9cfccdb62fa7e75a2b210b8e857dcd06c33bb5bcb92d9e1e9d444d62854(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aae0a28ec12afb8a41c96dcf893faeb71d91a8d34f858a13464f445652e33c23(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2e17e7ac3202b945ef66eaa6a7d8b517a9feba10a4cbec879301bc38ea5b374(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f76b24efebc6caaf1c60d3e25d0f212a5b2fea545bc437a1e968d7492e66c496(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74abcc5d487b5606c3b615c155de774723291ac247b3e3cd8d82115bca320c50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4ff25111b065da35542b55a99b2dffb206031d3139d5a99f2f18d8248d10f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5012074a6c766ce917a80b54d5767965b6c0e228ba48ff587536981d86d645e8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlers]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23a2f9247a15b225c9aeed35e0047e1672a3f98ae21acf9b14fd336f113c7e6f(
    *,
    conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]]] = None,
    messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]]] = None,
    return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tag: typing.Optional[builtins.str] = None,
    webhook: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81849e2f2275e16ae439e717051e89bcb7e653815fb68b8723368eef16c00317(
    *,
    cases: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1834c8c2a0879684e096601ae2f2a0b9ede11b8b987c86877097aaa0fe9cadb4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eed9bb7a923db26e226cdd2d63c9de7182a084595f1da4c11d5d32a11f14626(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__504f915c36d2a6f7fe94cc1f745f80a06474a893b45323245b2422e2398f7ec1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2217529a3314041e080b9aac552baf74a6a069fed0aa52f66de472cd5de111f6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__130990475d5c3685ee87257f252d76d02d24ea5e960dd62377a2cc32fa5b4502(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ce252b4046b702d4c7647bac535588666f34bdf356107f990065d16d8fe8cd6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f1ebdd741a9a298823d667e63ac9b68bbb84a2380d0268c0f386b41f43d83e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__303f486ff7a76f1949d67fa3e1de71ecc1dced82ad86c0381e49f57543f8fef2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3ca79bb4ff4c672c6d86e6d2a837563ac3295325689f7aa2d93291c1d31ebe3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93fb2db8ee7a9fbb5d9d8722cf434834340388c4375497da67779d9bcf87fc46(
    *,
    channel: typing.Optional[builtins.str] = None,
    conversation_success: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess, typing.Dict[builtins.str, typing.Any]]] = None,
    live_agent_handoff: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff, typing.Dict[builtins.str, typing.Any]]] = None,
    output_audio_text: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText, typing.Dict[builtins.str, typing.Any]]] = None,
    payload: typing.Optional[builtins.str] = None,
    play_audio: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio, typing.Dict[builtins.str, typing.Any]]] = None,
    telephony_transfer_call: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall, typing.Dict[builtins.str, typing.Any]]] = None,
    text: typing.Optional[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__749602d06cb6937ec1ac7c38f71919593f78a9f81e1a295ad6c8437ce8539f86(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f33496ffd59cdf604c411ce8f4fb224b14e90b42c9991680db5739416b7de8a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef79c0a0a92ad9419c0c5f53eb8c9f1ea347ee79c241ce2ef4785167229601b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1959513ae1d16c7e48f4680a90da304896f3a07c0da6dd037e8216f6e9219f9(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesConversationSuccess],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__328e98988bcd8dfb728651e66b072748a7e3c26f1268d829aaf8023209f963bb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a6b431cc86d866d738b25a3041f6f19b7bf1d257f5a72454906da24e2fcdaf3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b5fbd64a91a3f8a0c115b7cef84bb402cd838c5b70199e999ce8b2e9a61158d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9774ae7ed17e84b4adaf3cce096993a11334fd522d234cc43ed9936dbde64b10(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0da302874c27567e281f8a57a9ec100c564ed90b7b271361bae4a48d89cd199f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc3194f2bb63b8194e9405fd3f96a7c76f244131ca92983acfbc60907bbbab68(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6208f60cdee1ec1d059f52b7a1a552c3aa97719c80ec991c759208e39b34e8e4(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be31bec1d45e141d5e59ba188e28872b0393fa21ddee18757553c3a6aa493a0d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f14af29ecdf5545d34416d32e5d89bc6ab8a0623284d0caab66196f0605850b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acdcb6103d46600b17cf66e9c0d2eaf002d01c93e1d16f153db54486ee39e041(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesLiveAgentHandoff],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7f5e3d583137cf5ffdbd07bf0aa2289f5ac4e070470d1f93a8c0a929c5d357f(
    *,
    ssml: typing.Optional[builtins.str] = None,
    text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__359fde6aab2ee46515ae43bbc1e0426220d817db6b663c27e96bbc46baa890ba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d1f96503d07bea7b230a96c7e5441d13e824207a5ef4e9ee627b4a21f364ce7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b23c840a914fd8997a23abced560393e18a6635125a8d01b4620043fa9baa80e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82aae2679358ec43bbe1426cfebaa57e341aa71459f22cf856badd0abb83e1c4(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesOutputAudioText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b60872e0413605ba3d3384ece4c2b33466e9404a373508c86aaeeae4d73295(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b686276781abcb5befab9c44aa3a1321eb50ab749761f13f0d52d96c0e19821b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fdb67d59f5eb75f7cecc0eb87b589cba7fe15c4f6d08cabcdb1f1b7a3416377(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc7de8fceeb5489b48b0adfecb995a0967a781eb58937b507210ce35bee005f6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fead30325e1ae4827ecc8c98fabfc2d6ae173c8794d226407d3b6e638770c8b5(
    *,
    audio_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22c8fc4cd991b99ca63ca5035057e950db1fdea9ce4eba61ec15d1adddd561a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a2e1f004cb9abc09d69b2c6a95fd768236ad1b43ed73bde8968eed0f6eea400(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7522b41c37b92317d985216292ffdf0f92ccdd085c364195d71a2890a4ec191(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesPlayAudio],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c72605d1f13aabe9951226594e81aa5a36c4e7ea0186f7e1e695111129ebc9d(
    *,
    phone_number: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb81dfed5fcaccfc83c340243f71e86a26e36ea398c3dd4c565a2c569746d181(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3265d96159f4218d366d6694a14c987dd147140cef678432958bdd3c34f6247f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7af95c9c45b051cc215fa1fc6fa7727e5bd8f5757f7109af0177c54f92dddb3f(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesTelephonyTransferCall],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41a0efa64aa0a4660eebe1feff25627ec5d21e7e776e8a55124de8575831f369(
    *,
    text: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdbe4e4e0d1830c1032487feb64ac8850447fd15d8b12e34d5f82606d6f99d50(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a96c8078208faaf675ef926648a37e0ef16f4f45e4bc56080892de5328ee799(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50a2af4b8e1b1b951d62759c1952fab5e4ef1bea1842dfe42f86c940b0844afa(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessagesText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78b4aa7a1074440da3c1128aacf1477a22cfbabf3265fc17591f49d05dea1264(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91eb77888d0ba8188b452f1cc946ab9e009e4ea97236270e59bf8e1c17c366fa(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7938300b7f69f7581fc68ba230a7ca60005ce3cab73c6eeb1665d8cd3fee41e2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47905912712f1a4946e37a7b95f87bd69d5f0494c61907e64b4a6329d316fdc6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e74bae246dc19e9eec2fca2f562abfed4eaffe5a121d2a5329ed3deb919be23(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ae89e61e81cc890511924e9676e1073e758d937c2b278813a5b4fa05c4cfb62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0aeb815c3edb2d28fec446c2395dac8746c9aaf79042830cbe4730a12aa89ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd88a253effbd5ed96cb9039cd66cf0580e3cdc795cb0f58d3e20cc33bd2bb32(
    value: typing.Optional[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87ccd17d2816cd632b1a300960f7e835be028001289b71c5935650b9d539732b(
    *,
    parameter: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01868519dcf3981d6042e75371f353b6c17c38892b668ca47bde248881dc004c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__690a5d6aa323f8b98c36f1539b63dace9a656c2597768dbb5557b76f675e34ae(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c5ed138a85653b0c4fd70b7350c6fc90a56be6a9c63295c060612c9b1c257cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ce72bf4e059cd4f14a9a540925c750aac56d1d3732c95f9cc5158c6100b0353(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6fed3e839dca404f9b6ee7ee5f2a692da2b3a010e72f01983305eb69b1d4756(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05fd57adb5eaea3986428a682ebdd971c7d91d33d17a378f10fdcd4335504f91(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e396f8b57cdcc47b9b8427a9f37fc7e9c936ed7fc6a09a444b4406b974f10c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccb64ba78fd2248dd53321282e556ecad6fe1bc175d2d6b88686154934aa2bfa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e572498d708d4844d816a4c70940cb68e9d91ea6bc4961463d041851c807ca5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d7197c3dd547cd08c9f24aab2b32639c914506fa2c78b8edb603e1cbaf39806(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParametersFillBehaviorRepromptEventHandlersTriggerFulfillmentSetParameterActions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65ab0bd7e69cea4c0bcc2d18e83ad155e5ce49bb9ed29faf85496981a9fb1d3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac4826b540914b797b342f0f40616d9e0bdcc07e4a7d503069051ebda41bfc9a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0833af22ad182769bd2a385b2e1163c1d47db93b68021becec42d74e3413e52c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13eb2fa37e8520a9e60db6f7aeb02af6803d37a33408fee7c34962a1867944e5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8252559b74bba55fdf07c1122d2b7c3f0138e97c5f449de6e9294758f2ba2dd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84168b6727bed5f577334b6278adb82bc93d535162150a4b9e97043172cf769c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageFormParameters]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96b0622b63bf8976f6ddb697fe0277da020f18e377aa4e07e8d1458151e2172a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d03faf4d56d23635247ab5f9732ab85a8d0c72b60991be57ea60f854de6aae4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__992a2cff1d737740167aa4dc345f902ad2d3e6444bf14dd4a9470198b42acb76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d855713b9bc360962424d57f242ad4e7db238b5b32ebc9fd2f80e78c2abe8345(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__090feb3efde0d92df93cc4dffdd8ae9a1a845026ba35259732ffc393d60a938c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39fa322492de6d0066f52f6db7696836bb0a2026eeac0281cfe98b401439f990(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__783421a7873f243c8974cd21cf7ec3298e09ee47f7d6e979ea824d0d33485b73(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45f63f6efa57f41d57dc8f7c55c6a185253a2ce1dca840d65f5a02f986d9108e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageFormParameters]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e19156a49b1e0987ceb69d743e69217491db69c64a86751513a4ce9e2ae312(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__873e29e32e378d5b33dd9389659e3cf173adaac21d3d6341095e7c00790a44cf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ef2204dbf7dddaae7255015ad7298c5bb3e3aa69c0572b3d148fa3a54a4c737(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72e884773b7fbebac1a12b7401d637462235ec24edbc8dee9a1491d84a0a5dfa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a41bae19acacf19f12d8883f3c033c21b9bfbb619503800c51d344a2f64f877d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ec1ac3c4aeaa8b59fec413b264b067aa053747243884dc9c0a5cb3554de84b1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTimeouts]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b3435eb1a146fc63d7e6d293889fda573b9bff719bbdaf59bcea81e6eb98ada(
    *,
    condition: typing.Optional[builtins.str] = None,
    intent: typing.Optional[builtins.str] = None,
    target_flow: typing.Optional[builtins.str] = None,
    target_page: typing.Optional[builtins.str] = None,
    trigger_fulfillment: typing.Optional[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillment, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46540ff2c84fd09076c73342fc2d46e8921d558b6467a3480fe739931316229c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__420cfb1c1d7d8a3f16df38b019c07f6e16ff52d4b02fce439fc40849c3f88016(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f766fda6b99326a90062090b50c4727f7dc8112e39bb9e97183f4b6b0b16ee9a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac225f06b4ab414b3a6e1c08609ba41b53514d64de8383291fa16935d1fe6ab9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eff84c7dbd08cae100d48c3311bdfb9656ccc831e5a228dbf46289293b406c6b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__229959eb3cf663c0698ef2d689a22acf6500524bed95056a6193672bb0c61897(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afc47d02f9f9d8ebc69fd9923e29bf79b568299e87607085c7a27ae4e590e182(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81b1922418924023773fbc449810d4ef493bd61400797e8ad1551b413ec17828(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21fdf4b07d988386a65511fe0e5004026924601205333cc64e43a2ae971d9f23(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d03f3404f145c76c35aaeec4040f93ab4f0a9a36a4ef5f5042de6dd5297938a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b3ec57a6c3ff8f466bafe8de6cef29b823cd402c47449dd4e7329552596f81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__901c8134c279bcafdc495edf34345f816d9c3e8d155df607743f510c7b686dad(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutes]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a97a872305ddc645dd18929371877893606a6c501a3b834ec0f824adf60e91fd(
    *,
    conditional_cases: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]]] = None,
    messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]]] = None,
    return_partial_responses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    set_parameter_actions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tag: typing.Optional[builtins.str] = None,
    webhook: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b83c74829229872c98e1ed0124487bb8f099acc8be3aeac4f2f7b0714d3f52bc(
    *,
    cases: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa345ac5a14a6e5cb16548a021a00aab77e5e606c661d422ab6a3a88d08ef1f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a7610c085480b0d0fe22f43be49b7532ddb825fc19d5d99f4bb3d08a61bb992(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d4bf90eba61a3faceab2f07fb101f79f9e8a7bf029ff71ebb98c242251c1b12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc80c33362ce64203f02455d41fecc2ce22f8081736a73d95d2111efb80ef714(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__024ae6c4c6f027c4da2fb483653fbc8c31103904180d6814f53810e206d6c843(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bef7503cd21d754c517f750e11ac63d24f2008c5798e798695fa29392bef498(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e3b2e2bb60d9a064c4312ad69cce01233415a67208e4bd4f63f9e0ad9e4661b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__930c10cd5d7407117c22ff89dc142813d8c98597f4f904d478dc93f0eaea6568(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abb09bf9e873adda2818a285a138676f94d67bad486530cc4b4fe747f3a69cb4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d22ce8934a9bca258cd2e799d597ad03bfd47a02e609a93611e4fb345e4c184(
    *,
    channel: typing.Optional[builtins.str] = None,
    conversation_success: typing.Optional[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess, typing.Dict[builtins.str, typing.Any]]] = None,
    live_agent_handoff: typing.Optional[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff, typing.Dict[builtins.str, typing.Any]]] = None,
    output_audio_text: typing.Optional[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText, typing.Dict[builtins.str, typing.Any]]] = None,
    payload: typing.Optional[builtins.str] = None,
    play_audio: typing.Optional[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio, typing.Dict[builtins.str, typing.Any]]] = None,
    telephony_transfer_call: typing.Optional[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall, typing.Dict[builtins.str, typing.Any]]] = None,
    text: typing.Optional[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0af7c427fa2f7ff2969025807f3153756f8bb0024db2ba1e9cba182e67d5314(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__930d5f3b6c3ab578c61388c5490f17c7c04281bff6aac2de1677cc5fd5bffaa7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__350aeee9e821543de6c80b6debeb1b69ea1ff5bd10686933524edbae13c34ba0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__015255b21ec1d2a3363df5ece2cd59398fedcb7e0be7b53a57753f05006bf326(
    value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesConversationSuccess],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f3c16e44c20f2d8ddb6385f99619d0fde68b0adfac481c54a84f08a9ea11584(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4615fbd30bdeb1460c3590d248c3297ba150d054b3e0df2f02a555dc6e95ad2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73a00feb449934341e9412bd11fe0f6181c04b222923c77197165d0dd87d5ae8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429b3b07aafdbac74649dc0514e678a98d3e0132419e0e84500804847749aa72(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a8ff8286f97e9b2de1883e5cc2f78fc193ca81c6eb8095fb30aa7e2a67a4a6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afed3854e9dbe53ea3ac9c2e35933b29acc40c3a173d9d02fbc0c869dd3d3c2a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__415a0ba89f2c3f9a528509d439e875ccdf09c2b3af4e4c9e8fc65134d8ead551(
    *,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4011edc221b767e57fe6f6f03541dcdc02b50b074bfc0fdf93f23400cd5db29(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64e94bd10599c1306157f7107cd96fb20ce56078c3e5d57e01b380c69d7a87f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee55b6d3a077b4bd8bad07148690afbf23537b8278000798b43688a1aad6453c(
    value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesLiveAgentHandoff],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e56430df76cb33cff7367f84097006c77f5add1c6017331d1455bfc7b37bad1f(
    *,
    ssml: typing.Optional[builtins.str] = None,
    text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__432aca8f9a9673c83a85d5160db3c62f0cc52996da38878d3e17a20462ca5f14(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63bcdfa0e0b407a140081ef2d3520144d2ac2614f4f9292b50431d3f83818370(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d847f5dbcc6b8f571733d8ca573503ca8d1668dad1e95db90393463c88db11a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e3370bf506fd143c3a29f0848a629344b39470971e235e4186b753917227c03(
    value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputAudioText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d48e4c11699dd3ec0d5b6c0026e486e289be2713bd6e974d25756eaf7580cedb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a04e56e7efbf26c27ee4321d19fb2710174d0bb7927906a2b5619af0063b70d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__209fbd7fbb7c10c95c190697977508fa1bd297818a5e5640ac41c04f5c01a503(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1cb45f4bf1cd472528176699250fcee8b0f5a955ba125bfa79abeea5fa89d2e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32fa8953e5eddde87dfce36af9d4ab29166121ed6bc1c3e7496e958f708df679(
    *,
    audio_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c965306e4cf9e1fc56b546e90fe5a80f1e72e882b29283d5982cdeaec4c6ad9e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ed0960649e88ad149dc23c065920b0063b59c0562d7d7b079441d2cad72c9f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74b0321ee8864f2b4bd390f004a8a0b4f59145a39c0810d504ad0e60fc6cfd2e(
    value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesPlayAudio],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18617bd321e91cf3e474fcacecf34e74c11f24f22253feef6e6aa8209e2f7ce7(
    *,
    phone_number: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c6571dce2f4b6961e83287498c65d3d669113de231eb97785181a8eb37f0a9e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e52321f156071788c83ecb9d80faf1cef37bca72aadf831ff716a8725ed3e19d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3341ad650af3e72408c6d15b9ab6ec59a6c27de9ab6bbae93bc8fff81d6c5c76(
    value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTelephonyTransferCall],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f229b0f5398de9819fbd94bb7660e0408e42120b4e82942a08f7d9c65e803c6d(
    *,
    text: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc51c1fb7863a377441c47262a5331aea1b9b88b333fbd70e94e7dd867ddc150(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__165d58e126c7aa73b28c066cb408a8072687b8bcb5cbad62af23f964ec1c121e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bdf78eb3543e05aea0d5bfaa26a3fdad6a2a3e85dae6491af398873654c0c32(
    value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea3cbb3620ed0939e38dd92bfbc402432c69c4cb5070257496ec76f3c829a1d5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eba185bb89fd5d4b237a02894814867363b6cf4efd1ed2e80a7d6455c221658b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentConditionalCases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afc61086a8fbba8d92206d0954fbc4f1d1a51effc040cd201616cf2781d9fc5a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentMessages, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a97c828ef785e306b959769cf0abd5bff3855e47167acc526c7062700fb217a5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73e78df8164162d3a9b1c90492b27437ea1b2046668d42b69b65f4e859e5a94e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__065f9fba4af77da30a2390a4ee81b0c8800d9a7e2f719a842e28f641aeed787c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4abb4351a647581ea5289ae8ec97df80be83a4be2af41c807c181a628615aafc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efeb2c980b86abe8e81f39af0ccbf811a86ef1a5a125b02df0dae781123c219c(
    value: typing.Optional[DialogflowCxPageTransitionRoutesTriggerFulfillment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5700713004cb59bc56318b50c1f1c2e38227de5d1bed214451756c09499d80bc(
    *,
    parameter: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a63f10442a94fe29974836ae6e074b79e6d33a760e96881c98d71cfea448d3ba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e6f871bac10ceda742a7ff34a4fe369f8c946170603ecc788e7d9e35d319a99(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__651680b31c489a095ecc088d4aa782a7a592d4ded848d0ac6fdb370b5a13c6a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15dfa29b966f38c5d30fbc83de90ca80ca43a11ab9e1bb956761e45c6d1a2a09(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af16ff9540168099ee7b3fba27147e14b4d3436a2cb47de71b8a855113f66706(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__090d868f4df589ff8b89499036054048b393093d9e00bcb483a42b27d0b86673(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2437932259c5600d5ba7f6db4dbb6d2e6fa3bbc43bf88696d14499f3b5c33faa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2246f085b14f333434cadf3de2ff822e8f37ccf82678c91de9e041f4d8da79cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__828e0c9fde17f7d9c613caa4b458316fde1c417c34872a34d19c60b28f24b4ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__172053e84a993940c6bd929fca2ce3c97dd5ef61b607e2416c41ce74b2767b6a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DialogflowCxPageTransitionRoutesTriggerFulfillmentSetParameterActions]],
) -> None:
    """Type checking stubs"""
    pass
