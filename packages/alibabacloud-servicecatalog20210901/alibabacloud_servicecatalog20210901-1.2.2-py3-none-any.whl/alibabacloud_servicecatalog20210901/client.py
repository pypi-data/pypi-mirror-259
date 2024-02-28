# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_servicecatalog20210901 import models as servicecatalog_20210901_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('servicecatalog', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def approve_provisioned_product_plan_with_options(
        self,
        request: servicecatalog_20210901_models.ApproveProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ApproveProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.approval_action):
            body['ApprovalAction'] = request.approval_action
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApproveProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ApproveProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_provisioned_product_plan_with_options_async(
        self,
        request: servicecatalog_20210901_models.ApproveProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ApproveProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.approval_action):
            body['ApprovalAction'] = request.approval_action
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApproveProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ApproveProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_provisioned_product_plan(
        self,
        request: servicecatalog_20210901_models.ApproveProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.ApproveProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.approve_provisioned_product_plan_with_options(request, runtime)

    async def approve_provisioned_product_plan_async(
        self,
        request: servicecatalog_20210901_models.ApproveProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.ApproveProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_provisioned_product_plan_with_options_async(request, runtime)

    def associate_principal_with_portfolio_with_options(
        self,
        request: servicecatalog_20210901_models.AssociatePrincipalWithPortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.AssociatePrincipalWithPortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.principal_id):
            body['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            body['PrincipalType'] = request.principal_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociatePrincipalWithPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.AssociatePrincipalWithPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_principal_with_portfolio_with_options_async(
        self,
        request: servicecatalog_20210901_models.AssociatePrincipalWithPortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.AssociatePrincipalWithPortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.principal_id):
            body['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            body['PrincipalType'] = request.principal_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociatePrincipalWithPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.AssociatePrincipalWithPortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_principal_with_portfolio(
        self,
        request: servicecatalog_20210901_models.AssociatePrincipalWithPortfolioRequest,
    ) -> servicecatalog_20210901_models.AssociatePrincipalWithPortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_principal_with_portfolio_with_options(request, runtime)

    async def associate_principal_with_portfolio_async(
        self,
        request: servicecatalog_20210901_models.AssociatePrincipalWithPortfolioRequest,
    ) -> servicecatalog_20210901_models.AssociatePrincipalWithPortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_principal_with_portfolio_with_options_async(request, runtime)

    def associate_product_with_portfolio_with_options(
        self,
        request: servicecatalog_20210901_models.AssociateProductWithPortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.AssociateProductWithPortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateProductWithPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.AssociateProductWithPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_product_with_portfolio_with_options_async(
        self,
        request: servicecatalog_20210901_models.AssociateProductWithPortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.AssociateProductWithPortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateProductWithPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.AssociateProductWithPortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_product_with_portfolio(
        self,
        request: servicecatalog_20210901_models.AssociateProductWithPortfolioRequest,
    ) -> servicecatalog_20210901_models.AssociateProductWithPortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_product_with_portfolio_with_options(request, runtime)

    async def associate_product_with_portfolio_async(
        self,
        request: servicecatalog_20210901_models.AssociateProductWithPortfolioRequest,
    ) -> servicecatalog_20210901_models.AssociateProductWithPortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_product_with_portfolio_with_options_async(request, runtime)

    def associate_tag_option_with_resource_with_options(
        self,
        request: servicecatalog_20210901_models.AssociateTagOptionWithResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.AssociateTagOptionWithResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateTagOptionWithResource',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.AssociateTagOptionWithResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_tag_option_with_resource_with_options_async(
        self,
        request: servicecatalog_20210901_models.AssociateTagOptionWithResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.AssociateTagOptionWithResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateTagOptionWithResource',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.AssociateTagOptionWithResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_tag_option_with_resource(
        self,
        request: servicecatalog_20210901_models.AssociateTagOptionWithResourceRequest,
    ) -> servicecatalog_20210901_models.AssociateTagOptionWithResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_tag_option_with_resource_with_options(request, runtime)

    async def associate_tag_option_with_resource_async(
        self,
        request: servicecatalog_20210901_models.AssociateTagOptionWithResourceRequest,
    ) -> servicecatalog_20210901_models.AssociateTagOptionWithResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_tag_option_with_resource_with_options_async(request, runtime)

    def cancel_provisioned_product_plan_with_options(
        self,
        request: servicecatalog_20210901_models.CancelProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CancelProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CancelProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_provisioned_product_plan_with_options_async(
        self,
        request: servicecatalog_20210901_models.CancelProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CancelProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CancelProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_provisioned_product_plan(
        self,
        request: servicecatalog_20210901_models.CancelProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.CancelProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_provisioned_product_plan_with_options(request, runtime)

    async def cancel_provisioned_product_plan_async(
        self,
        request: servicecatalog_20210901_models.CancelProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.CancelProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_provisioned_product_plan_with_options_async(request, runtime)

    def copy_product_with_options(
        self,
        request: servicecatalog_20210901_models.CopyProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CopyProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.source_product_arn):
            body['SourceProductArn'] = request.source_product_arn
        if not UtilClient.is_unset(request.target_product_name):
            body['TargetProductName'] = request.target_product_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CopyProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_product_with_options_async(
        self,
        request: servicecatalog_20210901_models.CopyProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CopyProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.source_product_arn):
            body['SourceProductArn'] = request.source_product_arn
        if not UtilClient.is_unset(request.target_product_name):
            body['TargetProductName'] = request.target_product_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CopyProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_product(
        self,
        request: servicecatalog_20210901_models.CopyProductRequest,
    ) -> servicecatalog_20210901_models.CopyProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_product_with_options(request, runtime)

    async def copy_product_async(
        self,
        request: servicecatalog_20210901_models.CopyProductRequest,
    ) -> servicecatalog_20210901_models.CopyProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_product_with_options_async(request, runtime)

    def create_constraint_with_options(
        self,
        request: servicecatalog_20210901_models.CreateConstraintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreateConstraintResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.constraint_type):
            body['ConstraintType'] = request.constraint_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConstraint',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateConstraintResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_constraint_with_options_async(
        self,
        request: servicecatalog_20210901_models.CreateConstraintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreateConstraintResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.constraint_type):
            body['ConstraintType'] = request.constraint_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConstraint',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateConstraintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_constraint(
        self,
        request: servicecatalog_20210901_models.CreateConstraintRequest,
    ) -> servicecatalog_20210901_models.CreateConstraintResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_constraint_with_options(request, runtime)

    async def create_constraint_async(
        self,
        request: servicecatalog_20210901_models.CreateConstraintRequest,
    ) -> servicecatalog_20210901_models.CreateConstraintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_constraint_with_options_async(request, runtime)

    def create_portfolio_with_options(
        self,
        request: servicecatalog_20210901_models.CreatePortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreatePortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.portfolio_name):
            body['PortfolioName'] = request.portfolio_name
        if not UtilClient.is_unset(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreatePortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_portfolio_with_options_async(
        self,
        request: servicecatalog_20210901_models.CreatePortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreatePortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.portfolio_name):
            body['PortfolioName'] = request.portfolio_name
        if not UtilClient.is_unset(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreatePortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_portfolio(
        self,
        request: servicecatalog_20210901_models.CreatePortfolioRequest,
    ) -> servicecatalog_20210901_models.CreatePortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_portfolio_with_options(request, runtime)

    async def create_portfolio_async(
        self,
        request: servicecatalog_20210901_models.CreatePortfolioRequest,
    ) -> servicecatalog_20210901_models.CreatePortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_portfolio_with_options_async(request, runtime)

    def create_product_with_options(
        self,
        tmp_req: servicecatalog_20210901_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreateProductResponse:
        """
        Before you call the CreateProduct operation, you must call the [CreateTemplate](~~CreateTemplate~~) operation to create a template.
        
        @param tmp_req: CreateProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicecatalog_20210901_models.CreateProductShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.product_version_parameters):
            request.product_version_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_version_parameters, 'ProductVersionParameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.product_version_parameters_shrink):
            body['ProductVersionParameters'] = request.product_version_parameters_shrink
        if not UtilClient.is_unset(request.provider_name):
            body['ProviderName'] = request.provider_name
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_with_options_async(
        self,
        tmp_req: servicecatalog_20210901_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreateProductResponse:
        """
        Before you call the CreateProduct operation, you must call the [CreateTemplate](~~CreateTemplate~~) operation to create a template.
        
        @param tmp_req: CreateProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicecatalog_20210901_models.CreateProductShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.product_version_parameters):
            request.product_version_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_version_parameters, 'ProductVersionParameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.product_version_parameters_shrink):
            body['ProductVersionParameters'] = request.product_version_parameters_shrink
        if not UtilClient.is_unset(request.provider_name):
            body['ProviderName'] = request.provider_name
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product(
        self,
        request: servicecatalog_20210901_models.CreateProductRequest,
    ) -> servicecatalog_20210901_models.CreateProductResponse:
        """
        Before you call the CreateProduct operation, you must call the [CreateTemplate](~~CreateTemplate~~) operation to create a template.
        
        @param request: CreateProductRequest
        @return: CreateProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    async def create_product_async(
        self,
        request: servicecatalog_20210901_models.CreateProductRequest,
    ) -> servicecatalog_20210901_models.CreateProductResponse:
        """
        Before you call the CreateProduct operation, you must call the [CreateTemplate](~~CreateTemplate~~) operation to create a template.
        
        @param request: CreateProductRequest
        @return: CreateProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_product_with_options_async(request, runtime)

    def create_product_version_with_options(
        self,
        request: servicecatalog_20210901_models.CreateProductVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreateProductVersionResponse:
        """
        Before you call the CreateProductVersion operation, you must call the [CreateTemplate](~~CreateTemplate~~) operation to create a template.
        
        @param request: CreateProductVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.guidance):
            body['Guidance'] = request.guidance
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_name):
            body['ProductVersionName'] = request.product_version_name
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.template_url):
            body['TemplateUrl'] = request.template_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProductVersion',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_version_with_options_async(
        self,
        request: servicecatalog_20210901_models.CreateProductVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreateProductVersionResponse:
        """
        Before you call the CreateProductVersion operation, you must call the [CreateTemplate](~~CreateTemplate~~) operation to create a template.
        
        @param request: CreateProductVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.guidance):
            body['Guidance'] = request.guidance
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_name):
            body['ProductVersionName'] = request.product_version_name
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.template_url):
            body['TemplateUrl'] = request.template_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProductVersion',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product_version(
        self,
        request: servicecatalog_20210901_models.CreateProductVersionRequest,
    ) -> servicecatalog_20210901_models.CreateProductVersionResponse:
        """
        Before you call the CreateProductVersion operation, you must call the [CreateTemplate](~~CreateTemplate~~) operation to create a template.
        
        @param request: CreateProductVersionRequest
        @return: CreateProductVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_product_version_with_options(request, runtime)

    async def create_product_version_async(
        self,
        request: servicecatalog_20210901_models.CreateProductVersionRequest,
    ) -> servicecatalog_20210901_models.CreateProductVersionResponse:
        """
        Before you call the CreateProductVersion operation, you must call the [CreateTemplate](~~CreateTemplate~~) operation to create a template.
        
        @param request: CreateProductVersionRequest
        @return: CreateProductVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_product_version_with_options_async(request, runtime)

    def create_provisioned_product_plan_with_options(
        self,
        request: servicecatalog_20210901_models.CreateProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreateProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.plan_name):
            body['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.plan_type):
            body['PlanType'] = request.plan_type
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.provisioned_product_name):
            body['ProvisionedProductName'] = request.provisioned_product_name
        if not UtilClient.is_unset(request.stack_region_id):
            body['StackRegionId'] = request.stack_region_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_provisioned_product_plan_with_options_async(
        self,
        request: servicecatalog_20210901_models.CreateProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreateProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.plan_name):
            body['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.plan_type):
            body['PlanType'] = request.plan_type
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.provisioned_product_name):
            body['ProvisionedProductName'] = request.provisioned_product_name
        if not UtilClient.is_unset(request.stack_region_id):
            body['StackRegionId'] = request.stack_region_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_provisioned_product_plan(
        self,
        request: servicecatalog_20210901_models.CreateProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.CreateProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_provisioned_product_plan_with_options(request, runtime)

    async def create_provisioned_product_plan_async(
        self,
        request: servicecatalog_20210901_models.CreateProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.CreateProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_provisioned_product_plan_with_options_async(request, runtime)

    def create_tag_option_with_options(
        self,
        request: servicecatalog_20210901_models.CreateTagOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreateTagOptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_option_with_options_async(
        self,
        request: servicecatalog_20210901_models.CreateTagOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreateTagOptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateTagOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag_option(
        self,
        request: servicecatalog_20210901_models.CreateTagOptionRequest,
    ) -> servicecatalog_20210901_models.CreateTagOptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tag_option_with_options(request, runtime)

    async def create_tag_option_async(
        self,
        request: servicecatalog_20210901_models.CreateTagOptionRequest,
    ) -> servicecatalog_20210901_models.CreateTagOptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tag_option_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        request: servicecatalog_20210901_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_body):
            body['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.terraform_variables):
            body['TerraformVariables'] = request.terraform_variables
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: servicecatalog_20210901_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_body):
            body['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.terraform_variables):
            body['TerraformVariables'] = request.terraform_variables
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: servicecatalog_20210901_models.CreateTemplateRequest,
    ) -> servicecatalog_20210901_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: servicecatalog_20210901_models.CreateTemplateRequest,
    ) -> servicecatalog_20210901_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def delete_constraint_with_options(
        self,
        request: servicecatalog_20210901_models.DeleteConstraintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DeleteConstraintResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.constraint_id):
            body['ConstraintId'] = request.constraint_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConstraint',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteConstraintResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_constraint_with_options_async(
        self,
        request: servicecatalog_20210901_models.DeleteConstraintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DeleteConstraintResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.constraint_id):
            body['ConstraintId'] = request.constraint_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConstraint',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteConstraintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_constraint(
        self,
        request: servicecatalog_20210901_models.DeleteConstraintRequest,
    ) -> servicecatalog_20210901_models.DeleteConstraintResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_constraint_with_options(request, runtime)

    async def delete_constraint_async(
        self,
        request: servicecatalog_20210901_models.DeleteConstraintRequest,
    ) -> servicecatalog_20210901_models.DeleteConstraintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_constraint_with_options_async(request, runtime)

    def delete_portfolio_with_options(
        self,
        request: servicecatalog_20210901_models.DeletePortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DeletePortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeletePortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_portfolio_with_options_async(
        self,
        request: servicecatalog_20210901_models.DeletePortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DeletePortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeletePortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_portfolio(
        self,
        request: servicecatalog_20210901_models.DeletePortfolioRequest,
    ) -> servicecatalog_20210901_models.DeletePortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_portfolio_with_options(request, runtime)

    async def delete_portfolio_async(
        self,
        request: servicecatalog_20210901_models.DeletePortfolioRequest,
    ) -> servicecatalog_20210901_models.DeletePortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_portfolio_with_options_async(request, runtime)

    def delete_product_with_options(
        self,
        request: servicecatalog_20210901_models.DeleteProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DeleteProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_product_with_options_async(
        self,
        request: servicecatalog_20210901_models.DeleteProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DeleteProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_product(
        self,
        request: servicecatalog_20210901_models.DeleteProductRequest,
    ) -> servicecatalog_20210901_models.DeleteProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_product_with_options(request, runtime)

    async def delete_product_async(
        self,
        request: servicecatalog_20210901_models.DeleteProductRequest,
    ) -> servicecatalog_20210901_models.DeleteProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_product_with_options_async(request, runtime)

    def delete_product_version_with_options(
        self,
        request: servicecatalog_20210901_models.DeleteProductVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DeleteProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProductVersion',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_product_version_with_options_async(
        self,
        request: servicecatalog_20210901_models.DeleteProductVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DeleteProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProductVersion',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_product_version(
        self,
        request: servicecatalog_20210901_models.DeleteProductVersionRequest,
    ) -> servicecatalog_20210901_models.DeleteProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_product_version_with_options(request, runtime)

    async def delete_product_version_async(
        self,
        request: servicecatalog_20210901_models.DeleteProductVersionRequest,
    ) -> servicecatalog_20210901_models.DeleteProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_product_version_with_options_async(request, runtime)

    def delete_provisioned_product_plan_with_options(
        self,
        request: servicecatalog_20210901_models.DeleteProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DeleteProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_provisioned_product_plan_with_options_async(
        self,
        request: servicecatalog_20210901_models.DeleteProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DeleteProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_provisioned_product_plan(
        self,
        request: servicecatalog_20210901_models.DeleteProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.DeleteProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_provisioned_product_plan_with_options(request, runtime)

    async def delete_provisioned_product_plan_async(
        self,
        request: servicecatalog_20210901_models.DeleteProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.DeleteProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_provisioned_product_plan_with_options_async(request, runtime)

    def delete_tag_option_with_options(
        self,
        request: servicecatalog_20210901_models.DeleteTagOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DeleteTagOptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_option_with_options_async(
        self,
        request: servicecatalog_20210901_models.DeleteTagOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DeleteTagOptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteTagOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag_option(
        self,
        request: servicecatalog_20210901_models.DeleteTagOptionRequest,
    ) -> servicecatalog_20210901_models.DeleteTagOptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_option_with_options(request, runtime)

    async def delete_tag_option_async(
        self,
        request: servicecatalog_20210901_models.DeleteTagOptionRequest,
    ) -> servicecatalog_20210901_models.DeleteTagOptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_option_with_options_async(request, runtime)

    def dis_associate_tag_option_from_resource_with_options(
        self,
        request: servicecatalog_20210901_models.DisAssociateTagOptionFromResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DisAssociateTagOptionFromResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisAssociateTagOptionFromResource',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DisAssociateTagOptionFromResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def dis_associate_tag_option_from_resource_with_options_async(
        self,
        request: servicecatalog_20210901_models.DisAssociateTagOptionFromResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DisAssociateTagOptionFromResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisAssociateTagOptionFromResource',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DisAssociateTagOptionFromResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dis_associate_tag_option_from_resource(
        self,
        request: servicecatalog_20210901_models.DisAssociateTagOptionFromResourceRequest,
    ) -> servicecatalog_20210901_models.DisAssociateTagOptionFromResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.dis_associate_tag_option_from_resource_with_options(request, runtime)

    async def dis_associate_tag_option_from_resource_async(
        self,
        request: servicecatalog_20210901_models.DisAssociateTagOptionFromResourceRequest,
    ) -> servicecatalog_20210901_models.DisAssociateTagOptionFromResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dis_associate_tag_option_from_resource_with_options_async(request, runtime)

    def disassociate_principal_from_portfolio_with_options(
        self,
        request: servicecatalog_20210901_models.DisassociatePrincipalFromPortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DisassociatePrincipalFromPortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.principal_id):
            body['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            body['PrincipalType'] = request.principal_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisassociatePrincipalFromPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DisassociatePrincipalFromPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_principal_from_portfolio_with_options_async(
        self,
        request: servicecatalog_20210901_models.DisassociatePrincipalFromPortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DisassociatePrincipalFromPortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.principal_id):
            body['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            body['PrincipalType'] = request.principal_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisassociatePrincipalFromPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DisassociatePrincipalFromPortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_principal_from_portfolio(
        self,
        request: servicecatalog_20210901_models.DisassociatePrincipalFromPortfolioRequest,
    ) -> servicecatalog_20210901_models.DisassociatePrincipalFromPortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return self.disassociate_principal_from_portfolio_with_options(request, runtime)

    async def disassociate_principal_from_portfolio_async(
        self,
        request: servicecatalog_20210901_models.DisassociatePrincipalFromPortfolioRequest,
    ) -> servicecatalog_20210901_models.DisassociatePrincipalFromPortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disassociate_principal_from_portfolio_with_options_async(request, runtime)

    def disassociate_product_from_portfolio_with_options(
        self,
        request: servicecatalog_20210901_models.DisassociateProductFromPortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DisassociateProductFromPortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisassociateProductFromPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DisassociateProductFromPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_product_from_portfolio_with_options_async(
        self,
        request: servicecatalog_20210901_models.DisassociateProductFromPortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.DisassociateProductFromPortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisassociateProductFromPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DisassociateProductFromPortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_product_from_portfolio(
        self,
        request: servicecatalog_20210901_models.DisassociateProductFromPortfolioRequest,
    ) -> servicecatalog_20210901_models.DisassociateProductFromPortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return self.disassociate_product_from_portfolio_with_options(request, runtime)

    async def disassociate_product_from_portfolio_async(
        self,
        request: servicecatalog_20210901_models.DisassociateProductFromPortfolioRequest,
    ) -> servicecatalog_20210901_models.DisassociateProductFromPortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disassociate_product_from_portfolio_with_options_async(request, runtime)

    def execute_provisioned_product_plan_with_options(
        self,
        request: servicecatalog_20210901_models.ExecuteProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ExecuteProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ExecuteProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_provisioned_product_plan_with_options_async(
        self,
        request: servicecatalog_20210901_models.ExecuteProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ExecuteProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ExecuteProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_provisioned_product_plan(
        self,
        request: servicecatalog_20210901_models.ExecuteProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.ExecuteProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_provisioned_product_plan_with_options(request, runtime)

    async def execute_provisioned_product_plan_async(
        self,
        request: servicecatalog_20210901_models.ExecuteProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.ExecuteProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_provisioned_product_plan_with_options_async(request, runtime)

    def get_constraint_with_options(
        self,
        request: servicecatalog_20210901_models.GetConstraintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetConstraintResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.constraint_id):
            query['ConstraintId'] = request.constraint_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConstraint',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetConstraintResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_constraint_with_options_async(
        self,
        request: servicecatalog_20210901_models.GetConstraintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetConstraintResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.constraint_id):
            query['ConstraintId'] = request.constraint_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConstraint',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetConstraintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_constraint(
        self,
        request: servicecatalog_20210901_models.GetConstraintRequest,
    ) -> servicecatalog_20210901_models.GetConstraintResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_constraint_with_options(request, runtime)

    async def get_constraint_async(
        self,
        request: servicecatalog_20210901_models.GetConstraintRequest,
    ) -> servicecatalog_20210901_models.GetConstraintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_constraint_with_options_async(request, runtime)

    def get_portfolio_with_options(
        self,
        request: servicecatalog_20210901_models.GetPortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetPortfolioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_portfolio_with_options_async(
        self,
        request: servicecatalog_20210901_models.GetPortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetPortfolioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetPortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_portfolio(
        self,
        request: servicecatalog_20210901_models.GetPortfolioRequest,
    ) -> servicecatalog_20210901_models.GetPortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_portfolio_with_options(request, runtime)

    async def get_portfolio_async(
        self,
        request: servicecatalog_20210901_models.GetPortfolioRequest,
    ) -> servicecatalog_20210901_models.GetPortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_portfolio_with_options_async(request, runtime)

    def get_product_as_admin_with_options(
        self,
        request: servicecatalog_20210901_models.GetProductAsAdminRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetProductAsAdminResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductAsAdmin',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProductAsAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_as_admin_with_options_async(
        self,
        request: servicecatalog_20210901_models.GetProductAsAdminRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetProductAsAdminResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductAsAdmin',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProductAsAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_as_admin(
        self,
        request: servicecatalog_20210901_models.GetProductAsAdminRequest,
    ) -> servicecatalog_20210901_models.GetProductAsAdminResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_product_as_admin_with_options(request, runtime)

    async def get_product_as_admin_async(
        self,
        request: servicecatalog_20210901_models.GetProductAsAdminRequest,
    ) -> servicecatalog_20210901_models.GetProductAsAdminResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_product_as_admin_with_options_async(request, runtime)

    def get_product_as_end_user_with_options(
        self,
        request: servicecatalog_20210901_models.GetProductAsEndUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetProductAsEndUserResponse:
        """
        Make sure that you are granted the permissions to manage relevant products as a user by an administrator. For more information, see [Manage access permissions](~~405233~~).
        
        @param request: GetProductAsEndUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProductAsEndUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductAsEndUser',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProductAsEndUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_as_end_user_with_options_async(
        self,
        request: servicecatalog_20210901_models.GetProductAsEndUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetProductAsEndUserResponse:
        """
        Make sure that you are granted the permissions to manage relevant products as a user by an administrator. For more information, see [Manage access permissions](~~405233~~).
        
        @param request: GetProductAsEndUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProductAsEndUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductAsEndUser',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProductAsEndUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_as_end_user(
        self,
        request: servicecatalog_20210901_models.GetProductAsEndUserRequest,
    ) -> servicecatalog_20210901_models.GetProductAsEndUserResponse:
        """
        Make sure that you are granted the permissions to manage relevant products as a user by an administrator. For more information, see [Manage access permissions](~~405233~~).
        
        @param request: GetProductAsEndUserRequest
        @return: GetProductAsEndUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_product_as_end_user_with_options(request, runtime)

    async def get_product_as_end_user_async(
        self,
        request: servicecatalog_20210901_models.GetProductAsEndUserRequest,
    ) -> servicecatalog_20210901_models.GetProductAsEndUserResponse:
        """
        Make sure that you are granted the permissions to manage relevant products as a user by an administrator. For more information, see [Manage access permissions](~~405233~~).
        
        @param request: GetProductAsEndUserRequest
        @return: GetProductAsEndUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_product_as_end_user_with_options_async(request, runtime)

    def get_product_version_with_options(
        self,
        request: servicecatalog_20210901_models.GetProductVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetProductVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_version_id):
            query['ProductVersionId'] = request.product_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductVersion',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_version_with_options_async(
        self,
        request: servicecatalog_20210901_models.GetProductVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetProductVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_version_id):
            query['ProductVersionId'] = request.product_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductVersion',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_version(
        self,
        request: servicecatalog_20210901_models.GetProductVersionRequest,
    ) -> servicecatalog_20210901_models.GetProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_product_version_with_options(request, runtime)

    async def get_product_version_async(
        self,
        request: servicecatalog_20210901_models.GetProductVersionRequest,
    ) -> servicecatalog_20210901_models.GetProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_product_version_with_options_async(request, runtime)

    def get_provisioned_product_with_options(
        self,
        request: servicecatalog_20210901_models.GetProvisionedProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetProvisionedProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProvisionedProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProvisionedProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_provisioned_product_with_options_async(
        self,
        request: servicecatalog_20210901_models.GetProvisionedProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetProvisionedProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProvisionedProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProvisionedProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_provisioned_product(
        self,
        request: servicecatalog_20210901_models.GetProvisionedProductRequest,
    ) -> servicecatalog_20210901_models.GetProvisionedProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_provisioned_product_with_options(request, runtime)

    async def get_provisioned_product_async(
        self,
        request: servicecatalog_20210901_models.GetProvisionedProductRequest,
    ) -> servicecatalog_20210901_models.GetProvisionedProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_provisioned_product_with_options_async(request, runtime)

    def get_provisioned_product_plan_with_options(
        self,
        request: servicecatalog_20210901_models.GetProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_provisioned_product_plan_with_options_async(
        self,
        request: servicecatalog_20210901_models.GetProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_provisioned_product_plan(
        self,
        request: servicecatalog_20210901_models.GetProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.GetProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_provisioned_product_plan_with_options(request, runtime)

    async def get_provisioned_product_plan_async(
        self,
        request: servicecatalog_20210901_models.GetProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.GetProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_provisioned_product_plan_with_options_async(request, runtime)

    def get_tag_option_with_options(
        self,
        request: servicecatalog_20210901_models.GetTagOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetTagOptionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tag_option_with_options_async(
        self,
        request: servicecatalog_20210901_models.GetTagOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetTagOptionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetTagOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tag_option(
        self,
        request: servicecatalog_20210901_models.GetTagOptionRequest,
    ) -> servicecatalog_20210901_models.GetTagOptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_tag_option_with_options(request, runtime)

    async def get_tag_option_async(
        self,
        request: servicecatalog_20210901_models.GetTagOptionRequest,
    ) -> servicecatalog_20210901_models.GetTagOptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_tag_option_with_options_async(request, runtime)

    def get_task_with_options(
        self,
        request: servicecatalog_20210901_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        request: servicecatalog_20210901_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        request: servicecatalog_20210901_models.GetTaskRequest,
    ) -> servicecatalog_20210901_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: servicecatalog_20210901_models.GetTaskRequest,
    ) -> servicecatalog_20210901_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: servicecatalog_20210901_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            query['ProductVersionId'] = request.product_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: servicecatalog_20210901_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            query['ProductVersionId'] = request.product_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        request: servicecatalog_20210901_models.GetTemplateRequest,
    ) -> servicecatalog_20210901_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: servicecatalog_20210901_models.GetTemplateRequest,
    ) -> servicecatalog_20210901_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def launch_product_with_options(
        self,
        request: servicecatalog_20210901_models.LaunchProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.LaunchProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.provisioned_product_name):
            body['ProvisionedProductName'] = request.provisioned_product_name
        if not UtilClient.is_unset(request.stack_region_id):
            body['StackRegionId'] = request.stack_region_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LaunchProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.LaunchProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def launch_product_with_options_async(
        self,
        request: servicecatalog_20210901_models.LaunchProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.LaunchProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.provisioned_product_name):
            body['ProvisionedProductName'] = request.provisioned_product_name
        if not UtilClient.is_unset(request.stack_region_id):
            body['StackRegionId'] = request.stack_region_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LaunchProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.LaunchProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def launch_product(
        self,
        request: servicecatalog_20210901_models.LaunchProductRequest,
    ) -> servicecatalog_20210901_models.LaunchProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.launch_product_with_options(request, runtime)

    async def launch_product_async(
        self,
        request: servicecatalog_20210901_models.LaunchProductRequest,
    ) -> servicecatalog_20210901_models.LaunchProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.launch_product_with_options_async(request, runtime)

    def list_launch_options_with_options(
        self,
        request: servicecatalog_20210901_models.ListLaunchOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListLaunchOptionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLaunchOptions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListLaunchOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_launch_options_with_options_async(
        self,
        request: servicecatalog_20210901_models.ListLaunchOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListLaunchOptionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLaunchOptions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListLaunchOptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_launch_options(
        self,
        request: servicecatalog_20210901_models.ListLaunchOptionsRequest,
    ) -> servicecatalog_20210901_models.ListLaunchOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_launch_options_with_options(request, runtime)

    async def list_launch_options_async(
        self,
        request: servicecatalog_20210901_models.ListLaunchOptionsRequest,
    ) -> servicecatalog_20210901_models.ListLaunchOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_launch_options_with_options_async(request, runtime)

    def list_portfolios_with_options(
        self,
        request: servicecatalog_20210901_models.ListPortfoliosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListPortfoliosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPortfolios',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListPortfoliosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_portfolios_with_options_async(
        self,
        request: servicecatalog_20210901_models.ListPortfoliosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListPortfoliosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPortfolios',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListPortfoliosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_portfolios(
        self,
        request: servicecatalog_20210901_models.ListPortfoliosRequest,
    ) -> servicecatalog_20210901_models.ListPortfoliosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_portfolios_with_options(request, runtime)

    async def list_portfolios_async(
        self,
        request: servicecatalog_20210901_models.ListPortfoliosRequest,
    ) -> servicecatalog_20210901_models.ListPortfoliosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_portfolios_with_options_async(request, runtime)

    def list_principals_with_options(
        self,
        request: servicecatalog_20210901_models.ListPrincipalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListPrincipalsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrincipals',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListPrincipalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_principals_with_options_async(
        self,
        request: servicecatalog_20210901_models.ListPrincipalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListPrincipalsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrincipals',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListPrincipalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_principals(
        self,
        request: servicecatalog_20210901_models.ListPrincipalsRequest,
    ) -> servicecatalog_20210901_models.ListPrincipalsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_principals_with_options(request, runtime)

    async def list_principals_async(
        self,
        request: servicecatalog_20210901_models.ListPrincipalsRequest,
    ) -> servicecatalog_20210901_models.ListPrincipalsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_principals_with_options_async(request, runtime)

    def list_product_versions_with_options(
        self,
        request: servicecatalog_20210901_models.ListProductVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListProductVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductVersions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProductVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_versions_with_options_async(
        self,
        request: servicecatalog_20210901_models.ListProductVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListProductVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductVersions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProductVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_versions(
        self,
        request: servicecatalog_20210901_models.ListProductVersionsRequest,
    ) -> servicecatalog_20210901_models.ListProductVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_product_versions_with_options(request, runtime)

    async def list_product_versions_async(
        self,
        request: servicecatalog_20210901_models.ListProductVersionsRequest,
    ) -> servicecatalog_20210901_models.ListProductVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_product_versions_with_options_async(request, runtime)

    def list_products_as_admin_with_options(
        self,
        request: servicecatalog_20210901_models.ListProductsAsAdminRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListProductsAsAdminResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductsAsAdmin',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProductsAsAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_as_admin_with_options_async(
        self,
        request: servicecatalog_20210901_models.ListProductsAsAdminRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListProductsAsAdminResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductsAsAdmin',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProductsAsAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products_as_admin(
        self,
        request: servicecatalog_20210901_models.ListProductsAsAdminRequest,
    ) -> servicecatalog_20210901_models.ListProductsAsAdminResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_products_as_admin_with_options(request, runtime)

    async def list_products_as_admin_async(
        self,
        request: servicecatalog_20210901_models.ListProductsAsAdminRequest,
    ) -> servicecatalog_20210901_models.ListProductsAsAdminResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_products_as_admin_with_options_async(request, runtime)

    def list_products_as_end_user_with_options(
        self,
        request: servicecatalog_20210901_models.ListProductsAsEndUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListProductsAsEndUserResponse:
        """
        Make sure that you are granted the permissions to manage relevant products as a user by an administrator. For more information, see [Manage access permissions](~~405233~~).
        
        @param request: ListProductsAsEndUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsAsEndUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductsAsEndUser',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProductsAsEndUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_as_end_user_with_options_async(
        self,
        request: servicecatalog_20210901_models.ListProductsAsEndUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListProductsAsEndUserResponse:
        """
        Make sure that you are granted the permissions to manage relevant products as a user by an administrator. For more information, see [Manage access permissions](~~405233~~).
        
        @param request: ListProductsAsEndUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsAsEndUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductsAsEndUser',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProductsAsEndUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products_as_end_user(
        self,
        request: servicecatalog_20210901_models.ListProductsAsEndUserRequest,
    ) -> servicecatalog_20210901_models.ListProductsAsEndUserResponse:
        """
        Make sure that you are granted the permissions to manage relevant products as a user by an administrator. For more information, see [Manage access permissions](~~405233~~).
        
        @param request: ListProductsAsEndUserRequest
        @return: ListProductsAsEndUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_products_as_end_user_with_options(request, runtime)

    async def list_products_as_end_user_async(
        self,
        request: servicecatalog_20210901_models.ListProductsAsEndUserRequest,
    ) -> servicecatalog_20210901_models.ListProductsAsEndUserResponse:
        """
        Make sure that you are granted the permissions to manage relevant products as a user by an administrator. For more information, see [Manage access permissions](~~405233~~).
        
        @param request: ListProductsAsEndUserRequest
        @return: ListProductsAsEndUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_products_as_end_user_with_options_async(request, runtime)

    def list_provisioned_product_plan_approvers_with_options(
        self,
        request: servicecatalog_20210901_models.ListProvisionedProductPlanApproversRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListProvisionedProductPlanApproversResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionedProductPlanApprovers',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProvisionedProductPlanApproversResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_provisioned_product_plan_approvers_with_options_async(
        self,
        request: servicecatalog_20210901_models.ListProvisionedProductPlanApproversRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListProvisionedProductPlanApproversResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionedProductPlanApprovers',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProvisionedProductPlanApproversResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_provisioned_product_plan_approvers(
        self,
        request: servicecatalog_20210901_models.ListProvisionedProductPlanApproversRequest,
    ) -> servicecatalog_20210901_models.ListProvisionedProductPlanApproversResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_provisioned_product_plan_approvers_with_options(request, runtime)

    async def list_provisioned_product_plan_approvers_async(
        self,
        request: servicecatalog_20210901_models.ListProvisionedProductPlanApproversRequest,
    ) -> servicecatalog_20210901_models.ListProvisionedProductPlanApproversResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_provisioned_product_plan_approvers_with_options_async(request, runtime)

    def list_provisioned_product_plans_with_options(
        self,
        request: servicecatalog_20210901_models.ListProvisionedProductPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListProvisionedProductPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_level_filter):
            query['AccessLevelFilter'] = request.access_level_filter
        if not UtilClient.is_unset(request.approval_filter):
            query['ApprovalFilter'] = request.approval_filter
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionedProductPlans',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProvisionedProductPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_provisioned_product_plans_with_options_async(
        self,
        request: servicecatalog_20210901_models.ListProvisionedProductPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListProvisionedProductPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_level_filter):
            query['AccessLevelFilter'] = request.access_level_filter
        if not UtilClient.is_unset(request.approval_filter):
            query['ApprovalFilter'] = request.approval_filter
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionedProductPlans',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProvisionedProductPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_provisioned_product_plans(
        self,
        request: servicecatalog_20210901_models.ListProvisionedProductPlansRequest,
    ) -> servicecatalog_20210901_models.ListProvisionedProductPlansResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_provisioned_product_plans_with_options(request, runtime)

    async def list_provisioned_product_plans_async(
        self,
        request: servicecatalog_20210901_models.ListProvisionedProductPlansRequest,
    ) -> servicecatalog_20210901_models.ListProvisionedProductPlansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_provisioned_product_plans_with_options_async(request, runtime)

    def list_provisioned_products_with_options(
        self,
        request: servicecatalog_20210901_models.ListProvisionedProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListProvisionedProductsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_level_filter):
            query['AccessLevelFilter'] = request.access_level_filter
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionedProducts',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProvisionedProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_provisioned_products_with_options_async(
        self,
        request: servicecatalog_20210901_models.ListProvisionedProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListProvisionedProductsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_level_filter):
            query['AccessLevelFilter'] = request.access_level_filter
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionedProducts',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProvisionedProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_provisioned_products(
        self,
        request: servicecatalog_20210901_models.ListProvisionedProductsRequest,
    ) -> servicecatalog_20210901_models.ListProvisionedProductsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_provisioned_products_with_options(request, runtime)

    async def list_provisioned_products_async(
        self,
        request: servicecatalog_20210901_models.ListProvisionedProductsRequest,
    ) -> servicecatalog_20210901_models.ListProvisionedProductsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_provisioned_products_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> servicecatalog_20210901_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> servicecatalog_20210901_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_resources_for_tag_option_with_options(
        self,
        request: servicecatalog_20210901_models.ListResourcesForTagOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListResourcesForTagOptionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourcesForTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListResourcesForTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_for_tag_option_with_options_async(
        self,
        request: servicecatalog_20210901_models.ListResourcesForTagOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListResourcesForTagOptionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourcesForTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListResourcesForTagOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources_for_tag_option(
        self,
        request: servicecatalog_20210901_models.ListResourcesForTagOptionRequest,
    ) -> servicecatalog_20210901_models.ListResourcesForTagOptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resources_for_tag_option_with_options(request, runtime)

    async def list_resources_for_tag_option_async(
        self,
        request: servicecatalog_20210901_models.ListResourcesForTagOptionRequest,
    ) -> servicecatalog_20210901_models.ListResourcesForTagOptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resources_for_tag_option_with_options_async(request, runtime)

    def list_tag_options_with_options(
        self,
        tmp_req: servicecatalog_20210901_models.ListTagOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListTagOptionsResponse:
        UtilClient.validate_model(tmp_req)
        request = servicecatalog_20210901_models.ListTagOptionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filters):
            request.filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagOptions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListTagOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_options_with_options_async(
        self,
        tmp_req: servicecatalog_20210901_models.ListTagOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListTagOptionsResponse:
        UtilClient.validate_model(tmp_req)
        request = servicecatalog_20210901_models.ListTagOptionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filters):
            request.filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagOptions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListTagOptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_options(
        self,
        request: servicecatalog_20210901_models.ListTagOptionsRequest,
    ) -> servicecatalog_20210901_models.ListTagOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_options_with_options(request, runtime)

    async def list_tag_options_async(
        self,
        request: servicecatalog_20210901_models.ListTagOptionsRequest,
    ) -> servicecatalog_20210901_models.ListTagOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_options_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        request: servicecatalog_20210901_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        request: servicecatalog_20210901_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: servicecatalog_20210901_models.ListTasksRequest,
    ) -> servicecatalog_20210901_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: servicecatalog_20210901_models.ListTasksRequest,
    ) -> servicecatalog_20210901_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def terminate_provisioned_product_with_options(
        self,
        request: servicecatalog_20210901_models.TerminateProvisionedProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.TerminateProvisionedProductResponse:
        """
        After a product instance is terminated, the product instance is deleted from the product instance list. End users cannot manage the product instance throughout its lifecycle. Proceed with caution.
        
        @param request: TerminateProvisionedProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateProvisionedProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.provisioned_product_id):
            body['ProvisionedProductId'] = request.provisioned_product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TerminateProvisionedProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.TerminateProvisionedProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_provisioned_product_with_options_async(
        self,
        request: servicecatalog_20210901_models.TerminateProvisionedProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.TerminateProvisionedProductResponse:
        """
        After a product instance is terminated, the product instance is deleted from the product instance list. End users cannot manage the product instance throughout its lifecycle. Proceed with caution.
        
        @param request: TerminateProvisionedProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateProvisionedProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.provisioned_product_id):
            body['ProvisionedProductId'] = request.provisioned_product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TerminateProvisionedProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.TerminateProvisionedProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_provisioned_product(
        self,
        request: servicecatalog_20210901_models.TerminateProvisionedProductRequest,
    ) -> servicecatalog_20210901_models.TerminateProvisionedProductResponse:
        """
        After a product instance is terminated, the product instance is deleted from the product instance list. End users cannot manage the product instance throughout its lifecycle. Proceed with caution.
        
        @param request: TerminateProvisionedProductRequest
        @return: TerminateProvisionedProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.terminate_provisioned_product_with_options(request, runtime)

    async def terminate_provisioned_product_async(
        self,
        request: servicecatalog_20210901_models.TerminateProvisionedProductRequest,
    ) -> servicecatalog_20210901_models.TerminateProvisionedProductResponse:
        """
        After a product instance is terminated, the product instance is deleted from the product instance list. End users cannot manage the product instance throughout its lifecycle. Proceed with caution.
        
        @param request: TerminateProvisionedProductRequest
        @return: TerminateProvisionedProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.terminate_provisioned_product_with_options_async(request, runtime)

    def update_constraint_with_options(
        self,
        request: servicecatalog_20210901_models.UpdateConstraintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdateConstraintResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.constraint_id):
            body['ConstraintId'] = request.constraint_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConstraint',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateConstraintResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_constraint_with_options_async(
        self,
        request: servicecatalog_20210901_models.UpdateConstraintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdateConstraintResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.constraint_id):
            body['ConstraintId'] = request.constraint_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConstraint',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateConstraintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_constraint(
        self,
        request: servicecatalog_20210901_models.UpdateConstraintRequest,
    ) -> servicecatalog_20210901_models.UpdateConstraintResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_constraint_with_options(request, runtime)

    async def update_constraint_async(
        self,
        request: servicecatalog_20210901_models.UpdateConstraintRequest,
    ) -> servicecatalog_20210901_models.UpdateConstraintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_constraint_with_options_async(request, runtime)

    def update_portfolio_with_options(
        self,
        request: servicecatalog_20210901_models.UpdatePortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdatePortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.portfolio_name):
            body['PortfolioName'] = request.portfolio_name
        if not UtilClient.is_unset(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdatePortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_portfolio_with_options_async(
        self,
        request: servicecatalog_20210901_models.UpdatePortfolioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdatePortfolioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.portfolio_name):
            body['PortfolioName'] = request.portfolio_name
        if not UtilClient.is_unset(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdatePortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_portfolio(
        self,
        request: servicecatalog_20210901_models.UpdatePortfolioRequest,
    ) -> servicecatalog_20210901_models.UpdatePortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_portfolio_with_options(request, runtime)

    async def update_portfolio_async(
        self,
        request: servicecatalog_20210901_models.UpdatePortfolioRequest,
    ) -> servicecatalog_20210901_models.UpdatePortfolioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_portfolio_with_options_async(request, runtime)

    def update_product_with_options(
        self,
        request: servicecatalog_20210901_models.UpdateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdateProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_product_with_options_async(
        self,
        request: servicecatalog_20210901_models.UpdateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdateProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_product(
        self,
        request: servicecatalog_20210901_models.UpdateProductRequest,
    ) -> servicecatalog_20210901_models.UpdateProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_product_with_options(request, runtime)

    async def update_product_async(
        self,
        request: servicecatalog_20210901_models.UpdateProductRequest,
    ) -> servicecatalog_20210901_models.UpdateProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_product_with_options_async(request, runtime)

    def update_product_version_with_options(
        self,
        request: servicecatalog_20210901_models.UpdateProductVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdateProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.guidance):
            body['Guidance'] = request.guidance
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.product_version_name):
            body['ProductVersionName'] = request.product_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductVersion',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_product_version_with_options_async(
        self,
        request: servicecatalog_20210901_models.UpdateProductVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdateProductVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.guidance):
            body['Guidance'] = request.guidance
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.product_version_name):
            body['ProductVersionName'] = request.product_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductVersion',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_product_version(
        self,
        request: servicecatalog_20210901_models.UpdateProductVersionRequest,
    ) -> servicecatalog_20210901_models.UpdateProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_product_version_with_options(request, runtime)

    async def update_product_version_async(
        self,
        request: servicecatalog_20210901_models.UpdateProductVersionRequest,
    ) -> servicecatalog_20210901_models.UpdateProductVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_product_version_with_options_async(request, runtime)

    def update_provisioned_product_with_options(
        self,
        request: servicecatalog_20210901_models.UpdateProvisionedProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdateProvisionedProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.provisioned_product_id):
            body['ProvisionedProductId'] = request.provisioned_product_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProvisionedProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateProvisionedProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_provisioned_product_with_options_async(
        self,
        request: servicecatalog_20210901_models.UpdateProvisionedProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdateProvisionedProductResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.provisioned_product_id):
            body['ProvisionedProductId'] = request.provisioned_product_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProvisionedProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateProvisionedProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_provisioned_product(
        self,
        request: servicecatalog_20210901_models.UpdateProvisionedProductRequest,
    ) -> servicecatalog_20210901_models.UpdateProvisionedProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_provisioned_product_with_options(request, runtime)

    async def update_provisioned_product_async(
        self,
        request: servicecatalog_20210901_models.UpdateProvisionedProductRequest,
    ) -> servicecatalog_20210901_models.UpdateProvisionedProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_provisioned_product_with_options_async(request, runtime)

    def update_provisioned_product_plan_with_options(
        self,
        request: servicecatalog_20210901_models.UpdateProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdateProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_provisioned_product_plan_with_options_async(
        self,
        request: servicecatalog_20210901_models.UpdateProvisionedProductPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdateProvisionedProductPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_provisioned_product_plan(
        self,
        request: servicecatalog_20210901_models.UpdateProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.UpdateProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_provisioned_product_plan_with_options(request, runtime)

    async def update_provisioned_product_plan_async(
        self,
        request: servicecatalog_20210901_models.UpdateProvisionedProductPlanRequest,
    ) -> servicecatalog_20210901_models.UpdateProvisionedProductPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_provisioned_product_plan_with_options_async(request, runtime)

    def update_tag_option_with_options(
        self,
        request: servicecatalog_20210901_models.UpdateTagOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdateTagOptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tag_option_with_options_async(
        self,
        request: servicecatalog_20210901_models.UpdateTagOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicecatalog_20210901_models.UpdateTagOptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateTagOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tag_option(
        self,
        request: servicecatalog_20210901_models.UpdateTagOptionRequest,
    ) -> servicecatalog_20210901_models.UpdateTagOptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_tag_option_with_options(request, runtime)

    async def update_tag_option_async(
        self,
        request: servicecatalog_20210901_models.UpdateTagOptionRequest,
    ) -> servicecatalog_20210901_models.UpdateTagOptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_tag_option_with_options_async(request, runtime)
