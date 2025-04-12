from ibm_watsonx_ai.foundation_models import get_model_specs
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import APIClient, Credentials

import os

class WatsonxConfig:
    apikey = os.getenv("WATSONX_AI_APIKEY")
    url = os.getenv("WATSONX_AI_HOST")

    # provide one of these
    project_id = os.getenv("WATSONX_AI_PROJECT_ID")
    space_id = os.getenv("WATSONX_AI_SPACE_ID")

    deployment_id = os.getenv("WATSONX_AI_DEPLOYMENT_ID")

class WatsonxAPIClient(metaclass=Singleton):
    def __init__(self, watsonxconfig: WatsonxConfig):
        self.wx_cloud_url = watsonxconfig.url
        self.wx_apikey = watsonxconfig.apikey

        self.credentials = Credentials(
            url=self.wx_cloud_url,
            api_key=self.wx_apikey
        )

        self.client = APIClient(self.credentials)


class WatsonxClient(metaclass=Singleton):
    def __init__(self, watsonxconfig: WatsonxConfig):

        self.logger = Logger('watsonx_logger', LogConfig.misc_level).logger

        self.wx_cloud_url = watsonxconfig.url
        self.wx_apikey = watsonxconfig.apikey

        self.client = WatsonxAPIClient(watsonxconfig).client

        # one of these two is required
        self.project_id = watsonxconfig.project_id
        self.space_id = watsonxconfig.space_id

        self.deployment_id = watsonxconfig.deployment_id

        model_data = {
            "deployment_id": self.deployment_id,
            "api_client": self.client,
            "validate": False
        }
        if self.project_id:
            model_data['project_id'] = self.project_id
        elif self.space_id:
            model_data['space_id'] = self.space_id
        else:
            raise Exception(
                'Project ID or Space ID required for Watsonx AI model inference')

        self.model = ModelInference(**model_data)
        self.logger.debug("WatsonX Client successfully initialized.")

    def text_generation(self, prompt_query: str = None, params: dict = None, label: str = ""):
        self.logger.debug(
            f"Called text generation")

        response = None
        tries = 3
        # retry in case WX dies
        while tries > 0:
            try:
                response = self.model.generate_text(
                    prompt=prompt_query, params=params)
                tries = -1
                self.logger.debug(f"generated ok {response}")
            except:
                self.logger.error(f"Failed generation")
                tries -= 1
        return response

    def text_generation_stream(self, prompt_query: str = None, params: dict = None):
        self.logger.debug(
            f"Called text stream generation")
        response = None
        tries = 3
        # retry in case WX dies
        while tries > 0:
            try:
                response = self.model.generate_text_stream(
                    prompt=prompt_query, params=params)
                tries = -1
            except:
                self.logger.warning(f"Failed stream generation")
                tries -= 1
        return response

    def tokenize(self, prompt):
        self.logger.debug(f"Tokenizing")
        tokenized_response = self.model.tokenize(prompt=prompt)
        return tokenized_response["result"]["token_count"]

    def list_models(self):
        models_list = get_model_specs(url=self.wx_cloud_url)
        self.logger.debug(f"Available models: {models_list}")
        return models_list

    def get_model_detail(self):
        model_detail = get_model_specs(
            url=self.wx_cloud_url, model_id=self.model_id)
        self.logger.debug(f"Model details: {model_detail}")
        return model_detail
