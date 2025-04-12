from ibm_watsonx_ai.foundation_models import get_model_specs
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import APIClient, Credentials
from Singleton import Singleton
from Logger import Logger
import os

class WatsonxClient(metaclass=Singleton):
    def __init__(self):
        self.logger = Logger('watsonx_logger', os.getenv("LOG_MISC", "DEBUG")).logger

        # Read environment variables directly
        self.wx_cloud_url = os.getenv("WATSONX_AI_HOST")
        self.wx_apikey = os.getenv("WATSONX_AI_APIKEY")
        self.project_id = os.getenv("WATSONX_AI_PROJECT_ID")
        self.space_id = os.getenv("WATSONX_AI_SPACE_ID")
        self.deployment_id = os.getenv("WATSONX_AI_DEPLOYMENT_ID")

        # Check required host and apikey env vars
        if not self.wx_cloud_url or not self.wx_apikey:
            raise ValueError("WATSONX_AI_HOST and WATSONX_AI_APIKEY environment variables must be set.")

        # Create credentials and API client directly
        self.credentials = Credentials(
            url=self.wx_cloud_url,
            api_key=self.wx_apikey
        )
        self.client = APIClient(self.credentials)

        # Check required deployment ID env var
        if not self.deployment_id:
             raise ValueError("WATSONX_AI_DEPLOYMENT_ID environment variable must be set.")

        model_data = {
            "deployment_id": self.deployment_id,
            "api_client": self.client, # Use the client created within this class
            "validate": False
        }
        if self.project_id:
            model_data['project_id'] = self.project_id
        elif self.space_id:
            model_data['space_id'] = self.space_id
        else:
            raise ValueError(
                'Either WATSONX_AI_PROJECT_ID or WATSONX_AI_SPACE_ID environment variable must be set for Watsonx AI model inference')

        self.model = ModelInference(**model_data)
        self.logger.debug("WatsonX Client successfully initialized.")

    def text_generation(self, prompt_query: str = None, params: dict = None, label: str = ""):
        self.logger.debug(f"Called text generation")

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
        self.logger.debug(f"Called text stream generation")
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
