# resources/recommender.py
from __future__ import annotations

from typing import TYPE_CHECKING
from .._constants import (BASE_URL_V2)

import httpx
import json
import warnings
from .data_connector import DataConnector

if TYPE_CHECKING:
    from .._client import PigeonsAI


class Recommender:
    def __init__(self, client: PigeonsAI):
        self.client = client
        self.vae = VAE(client)


class VAE():
    train_set_pri_global = None  # Class variable to store the global train_set_pri

    def __init__(self, client: PigeonsAI) -> None:
        self.client = client

    def train(
        self,
        custom_model_name: str,
        train_set_pri: str = None,
        n_epochs: str = None,
        batch_size: str = None,
        learn_rate: str = None,
        beta: str = None,
        verbose: str = None,
        train_prop: str = None,
        random_seed: str = None,
        latent_dims: str = None,
        hidden_dims: str = None,
        recall_at_k: str = None,
        eval_iterations: str = None,
        act_fn: str = None,
        likelihood: str = None,
        data_subset_percent: str = None,
    ):
        if not train_set_pri and DataConnector.train_set_pri_global:
            train_set_pri = DataConnector.train_set_pri_global

        if not train_set_pri:
            raise ValueError("train_set_pri must be provided")

        data = {
            'custom_model_name': custom_model_name,
            'data_source_pri': train_set_pri,
            **{k: v for k, v in locals().items() if v is not None and k not in ['self', 'custom_model_name', 'train_set_pri']}
        }

        url = BASE_URL_V2 + '/train'
        headers = self.client.auth_headers

        try:
            print(f'\033[38;2;229;192;108m    Initializing {custom_model_name} training \033[0m')

            response = httpx.post(url, headers=headers, json=data)
            response.raise_for_status()
            json_response = response.json()
            # Print status code in green
            print(f'\033[38;2;85;87;93mTraining job creation successful:\033[0m \033[92m{response.status_code} {response.reason_phrase}\033[0m')
            endpoint = json_response['res']['endpoint']
            message = json_response['res']['detail']
            
            print(f'\033[38;2;229;192;108m      {message}\033[0m')
            print(f'\033[38;2;85;87;93mEndpoint:\033[0m \033[38;2;7;102;255m{endpoint}\033[0m')
            
            return json.dumps(json_response, indent=2)
        except Exception as e:
            raise e
        

    def inference(
        self,
        user_history_ids: str,
        k: int = 10,
        model_uri: str = None,
        model_name: str = None
    ):

        if model_name and model_uri:
            warnings.warn("Both model_name and model_uri are provided. Either one of them will be used.")

        if model_name:
            model_uri = _construct_model_url(model_name=model_name, is_uri=False)
        elif not model_uri:
            raise ValueError("Either model_name or model_uri must be provided")

        model_uri = _construct_model_url(model_uri=model_uri, is_uri=True)

        headers = self.client.auth_headers
        data = {
            "history_ids": user_history_ids,
            "k": k
        }

        try:
            response = httpx.post(model_uri, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise e


def _construct_model_url(is_uri, model_name: str = None, model_uri: str = None):
    if is_uri:
        if model_uri.endswith('/'):
            model_uri = model_uri[:-1]
        return f"{model_uri}/recommend"
    return f"http://{model_name}.apps.api1.pigeonsai.cloud/recommend"
