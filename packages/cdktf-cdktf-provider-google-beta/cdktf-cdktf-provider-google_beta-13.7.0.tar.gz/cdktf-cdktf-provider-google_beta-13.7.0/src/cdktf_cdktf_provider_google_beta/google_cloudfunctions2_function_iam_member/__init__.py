'''
# `google_cloudfunctions2_function_iam_member`

Refer to the Terraform Registry for docs: [`google_cloudfunctions2_function_iam_member`](https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member).
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


class GoogleCloudfunctions2FunctionIamMember(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudfunctions2FunctionIamMember.GoogleCloudfunctions2FunctionIamMember",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member google_cloudfunctions2_function_iam_member}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cloud_function: builtins.str,
        member: builtins.str,
        role: builtins.str,
        condition: typing.Optional[typing.Union["GoogleCloudfunctions2FunctionIamMemberCondition", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member google_cloudfunctions2_function_iam_member} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cloud_function: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#cloud_function GoogleCloudfunctions2FunctionIamMember#cloud_function}.
        :param member: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#member GoogleCloudfunctions2FunctionIamMember#member}.
        :param role: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#role GoogleCloudfunctions2FunctionIamMember#role}.
        :param condition: condition block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#condition GoogleCloudfunctions2FunctionIamMember#condition}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#id GoogleCloudfunctions2FunctionIamMember#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#location GoogleCloudfunctions2FunctionIamMember#location}.
        :param project: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#project GoogleCloudfunctions2FunctionIamMember#project}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8be56b211a2f319221b0691c449b0405b06f180b80b4a87ec0f88b02dc04823d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleCloudfunctions2FunctionIamMemberConfig(
            cloud_function=cloud_function,
            member=member,
            role=role,
            condition=condition,
            id=id,
            location=location,
            project=project,
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
        '''Generates CDKTF code for importing a GoogleCloudfunctions2FunctionIamMember resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the GoogleCloudfunctions2FunctionIamMember to import.
        :param import_from_id: The id of the existing GoogleCloudfunctions2FunctionIamMember that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the GoogleCloudfunctions2FunctionIamMember to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20f2bbabca0c1c2d75501344f18fb4403fced66f4ee9bab0f3cf4adddf37a37c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        *,
        expression: builtins.str,
        title: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#expression GoogleCloudfunctions2FunctionIamMember#expression}.
        :param title: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#title GoogleCloudfunctions2FunctionIamMember#title}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#description GoogleCloudfunctions2FunctionIamMember#description}.
        '''
        value = GoogleCloudfunctions2FunctionIamMemberCondition(
            expression=expression, title=title, description=description
        )

        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="condition")
    def condition(
        self,
    ) -> "GoogleCloudfunctions2FunctionIamMemberConditionOutputReference":
        return typing.cast("GoogleCloudfunctions2FunctionIamMemberConditionOutputReference", jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="cloudFunctionInput")
    def cloud_function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional["GoogleCloudfunctions2FunctionIamMemberCondition"]:
        return typing.cast(typing.Optional["GoogleCloudfunctions2FunctionIamMemberCondition"], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="memberInput")
    def member_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memberInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudFunction")
    def cloud_function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudFunction"))

    @cloud_function.setter
    def cloud_function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3408401e9010a61febc765a6b56ebddc65a020ad6d3f5d773e8d57832f3bd9ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudFunction", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c41555b0aded1488dc6a0ff10a241de5fc27b67188f1c7fb0fae78256dc280a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c03f143fff39c150119b59558c8b139f60c61396a766ee2aa73a7bf11e8a5111)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="member")
    def member(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "member"))

    @member.setter
    def member(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a00e0d7448775833c34f41d30c4d84efae56a61aa85655e745b6f9b8feb83d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "member", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e75ce5a3fa989c80b8da85e751578a86fc54a8b1d8099702138deaf2387b5e72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a49cd8e2c4dac1380b73a9a04e592d4bfb1fdc5f41005038297faeef5f932f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudfunctions2FunctionIamMember.GoogleCloudfunctions2FunctionIamMemberCondition",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "title": "title",
        "description": "description",
    },
)
class GoogleCloudfunctions2FunctionIamMemberCondition:
    def __init__(
        self,
        *,
        expression: builtins.str,
        title: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#expression GoogleCloudfunctions2FunctionIamMember#expression}.
        :param title: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#title GoogleCloudfunctions2FunctionIamMember#title}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#description GoogleCloudfunctions2FunctionIamMember#description}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed11530e8260ffa58610bce75a6b8a7755e38f741fee00b94f190c14a0296036)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "expression": expression,
            "title": title,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def expression(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#expression GoogleCloudfunctions2FunctionIamMember#expression}.'''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#title GoogleCloudfunctions2FunctionIamMember#title}.'''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#description GoogleCloudfunctions2FunctionIamMember#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudfunctions2FunctionIamMemberCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudfunctions2FunctionIamMemberConditionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudfunctions2FunctionIamMember.GoogleCloudfunctions2FunctionIamMemberConditionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ef851903554187accdde4700fdba4518c56d5ee585639fe4322a3e274f519ac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab405763aeddabf117a60f965b4f9119504909f7be5cc302d9e4a981245aeaa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93f3d269fc389a1f4e54b5e7f52caf88f2809474a531d607c80d030feef867bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07750c3aa5a69348f1fbf29840a9b70886608d6a3eeaa38ad45a5dd8862697f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleCloudfunctions2FunctionIamMemberCondition]:
        return typing.cast(typing.Optional[GoogleCloudfunctions2FunctionIamMemberCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudfunctions2FunctionIamMemberCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25c1b0c62407187063d500940fc77e51699c9d4f6c5983317238792e884cf8a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudfunctions2FunctionIamMember.GoogleCloudfunctions2FunctionIamMemberConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cloud_function": "cloudFunction",
        "member": "member",
        "role": "role",
        "condition": "condition",
        "id": "id",
        "location": "location",
        "project": "project",
    },
)
class GoogleCloudfunctions2FunctionIamMemberConfig(
    _cdktf_9a9027ec.TerraformMetaArguments,
):
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
        cloud_function: builtins.str,
        member: builtins.str,
        role: builtins.str,
        condition: typing.Optional[typing.Union[GoogleCloudfunctions2FunctionIamMemberCondition, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cloud_function: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#cloud_function GoogleCloudfunctions2FunctionIamMember#cloud_function}.
        :param member: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#member GoogleCloudfunctions2FunctionIamMember#member}.
        :param role: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#role GoogleCloudfunctions2FunctionIamMember#role}.
        :param condition: condition block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#condition GoogleCloudfunctions2FunctionIamMember#condition}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#id GoogleCloudfunctions2FunctionIamMember#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#location GoogleCloudfunctions2FunctionIamMember#location}.
        :param project: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#project GoogleCloudfunctions2FunctionIamMember#project}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(condition, dict):
            condition = GoogleCloudfunctions2FunctionIamMemberCondition(**condition)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3612c466a758876cdeaecc29b50e8236d073628c1e94207cf1292d1c7f8d58a6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cloud_function", value=cloud_function, expected_type=type_hints["cloud_function"])
            check_type(argname="argument member", value=member, expected_type=type_hints["member"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloud_function": cloud_function,
            "member": member,
            "role": role,
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
        if condition is not None:
            self._values["condition"] = condition
        if id is not None:
            self._values["id"] = id
        if location is not None:
            self._values["location"] = location
        if project is not None:
            self._values["project"] = project

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
    def cloud_function(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#cloud_function GoogleCloudfunctions2FunctionIamMember#cloud_function}.'''
        result = self._values.get("cloud_function")
        assert result is not None, "Required property 'cloud_function' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#member GoogleCloudfunctions2FunctionIamMember#member}.'''
        result = self._values.get("member")
        assert result is not None, "Required property 'member' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#role GoogleCloudfunctions2FunctionIamMember#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition(
        self,
    ) -> typing.Optional[GoogleCloudfunctions2FunctionIamMemberCondition]:
        '''condition block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#condition GoogleCloudfunctions2FunctionIamMember#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[GoogleCloudfunctions2FunctionIamMemberCondition], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#id GoogleCloudfunctions2FunctionIamMember#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#location GoogleCloudfunctions2FunctionIamMember#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/google-beta/5.18.0/docs/resources/google_cloudfunctions2_function_iam_member#project GoogleCloudfunctions2FunctionIamMember#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudfunctions2FunctionIamMemberConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GoogleCloudfunctions2FunctionIamMember",
    "GoogleCloudfunctions2FunctionIamMemberCondition",
    "GoogleCloudfunctions2FunctionIamMemberConditionOutputReference",
    "GoogleCloudfunctions2FunctionIamMemberConfig",
]

publication.publish()

def _typecheckingstub__8be56b211a2f319221b0691c449b0405b06f180b80b4a87ec0f88b02dc04823d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cloud_function: builtins.str,
    member: builtins.str,
    role: builtins.str,
    condition: typing.Optional[typing.Union[GoogleCloudfunctions2FunctionIamMemberCondition, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__20f2bbabca0c1c2d75501344f18fb4403fced66f4ee9bab0f3cf4adddf37a37c(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3408401e9010a61febc765a6b56ebddc65a020ad6d3f5d773e8d57832f3bd9ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c41555b0aded1488dc6a0ff10a241de5fc27b67188f1c7fb0fae78256dc280a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c03f143fff39c150119b59558c8b139f60c61396a766ee2aa73a7bf11e8a5111(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a00e0d7448775833c34f41d30c4d84efae56a61aa85655e745b6f9b8feb83d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e75ce5a3fa989c80b8da85e751578a86fc54a8b1d8099702138deaf2387b5e72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a49cd8e2c4dac1380b73a9a04e592d4bfb1fdc5f41005038297faeef5f932f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed11530e8260ffa58610bce75a6b8a7755e38f741fee00b94f190c14a0296036(
    *,
    expression: builtins.str,
    title: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef851903554187accdde4700fdba4518c56d5ee585639fe4322a3e274f519ac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab405763aeddabf117a60f965b4f9119504909f7be5cc302d9e4a981245aeaa9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93f3d269fc389a1f4e54b5e7f52caf88f2809474a531d607c80d030feef867bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07750c3aa5a69348f1fbf29840a9b70886608d6a3eeaa38ad45a5dd8862697f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25c1b0c62407187063d500940fc77e51699c9d4f6c5983317238792e884cf8a5(
    value: typing.Optional[GoogleCloudfunctions2FunctionIamMemberCondition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3612c466a758876cdeaecc29b50e8236d073628c1e94207cf1292d1c7f8d58a6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cloud_function: builtins.str,
    member: builtins.str,
    role: builtins.str,
    condition: typing.Optional[typing.Union[GoogleCloudfunctions2FunctionIamMemberCondition, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    project: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
