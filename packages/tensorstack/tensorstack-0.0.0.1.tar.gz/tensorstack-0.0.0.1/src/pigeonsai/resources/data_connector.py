# resources/data_connector.py
from __future__ import annotations

from typing import TYPE_CHECKING
from .._constants import (BASE_URL_V2)

import httpx
import os

if TYPE_CHECKING:
    from .._client import PigeonsAI


class DataConnector:
    data_connection_pri_global = None  # Class variable to store the global data_connection_pri
    train_set_pri_global = None

    def __init__(self, client: PigeonsAI):
        self.client = client

    def create_connector(
        self,
        connection_name: str,
        connection_type: str,
        db_host: str,
        db_name: str,
        db_username: str,
        db_password: str,
        db_port: int
    ):
        url = f"{BASE_URL_V2}/create-data-connector"
        headers = self.client.auth_headers
        data = {
            "conn_id": connection_name,
            "conn_type": connection_type,
            "host": db_host,
            "login": db_username,
            "password": db_password,
            "port": db_port,
            "schema": db_name
        }

        try:
            response = httpx.post(url, headers=headers, json=data)
            response.raise_for_status()
            print(
                f'\033[38;2;85;87;93mConnector creation successful:\033[0m \033[92m{response.status_code} {response.reason_phrase}\033[0m')
            result = response.json()
            DataConnector.data_connection_pri_global = result.get('res', {}).get('data_connection_pri')
            return result
        except Exception as e:
            print(response.json())
            raise e

    def create_train_set(
        self,
        type: str,
        train_set_name: str,
        file_path: str = None,
        data_connection_pri: str = None,
        table_name: str = None,
    ):

        # Use the global data_connection_pri if not provided
        if not data_connection_pri and DataConnector.data_connection_pri_global:
            data_connection_pri = DataConnector.data_connection_pri_global

        if file_path and data_connection_pri or file_path and table_name:
            raise ValueError("Only one of file or connector_details and table_name should be provided.")

        elif not file_path and not data_connection_pri and not table_name:
            raise ValueError("Either file or connector_details and table_name must be provided.")

        headers = self.client.auth_headers

        if type.lower() == 'file':
            return _prepare_data_with_file(headers=headers, train_set_name=train_set_name,
                                           file_path=file_path)
        if type.lower() == 'connection':
            result = _prepare_data_with_connector(headers=headers, train_set_name=train_set_name,
                                                  data_connection_pri=data_connection_pri, table_name=table_name)

            DataConnector.train_set_pri_global = result.get('res', {}).get('data_source_pri')

            return result

    def revision_train_set_with_file(
        self,
        train_set_pri: str,
        file_path: str,
    ):
        url = f"{BASE_URL_V2}/revision-data-source-with-file"
        headers = self.client.auth_headers
        if 'Content-Type' in headers:
            headers.pop('Content-Type')
        data = {
            'train_set_pri': train_set_pri,
        }

        try:
            with open(file_path, 'rb') as f:
                files = {'file': (file_path, f)}
                response = httpx.post(url, headers=headers, files=files, data=data)
                response.raise_for_status()
                print('Success:')
                return response.json()
        except Exception as e:
            raise e

    def revision_train_set_with_connector(
        self: str,
        train_set_pri: str,
        data_connection_pri: str,
        table_name: str,
    ):
        url = f"{BASE_URL_V2}/revision-data-source-with-connector"
        headers = self.client.auth_headers
        data = {
            'train_set_pri': train_set_pri,
            'data_connection_pri': data_connection_pri,
            'table_name': table_name,
        }

        try:
            response = httpx.post(url, headers=headers, json=data)
            response.raise_for_status()
            print('Success:')
            return response.json()
        except Exception as e:
            raise e

    def delete_train_set(
        self,
        train_set_pri: str
    ):
        """
        Sends a request to delete a data source.

        Parameters:
        - train_set_pri: int. The ID of the data source to be deleted.

        Returns:
        - A message indicating the outcome of the operation.
        """

        url = f"{BASE_URL_V2}/delete-data-source"
        data = {"train_set_pri": train_set_pri}
        headers = self.client.auth_headers

        try:
            response = httpx.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise e

    def delete_data_connector(self, data_connector_pri: str):
        """
        Sends a request to delete a data connector.

        Parameters:
        - conn_id: int. The ID of the data connector to be deleted.

        Returns:
        - A message indicating the outcome of the operation.
        """

        url = f"{BASE_URL_V2}/delete-data-connector"
        data = {"data_connector_pri": data_connector_pri}
        headers = self.client.auth_headers

        try:
            response = httpx.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise e


def _prepare_data_with_file(
    headers,
    train_set_name: str,
    file_path: str,
):
    url = f"{BASE_URL_V2}/create-data-source-with-file"

    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    if 'Content-Type' in headers:
        headers.pop('Content-Type')

    data = {
        'data_source_name': train_set_name,
        'file_name': file_name,
        'file_size': str(file_size)
    }

    try:
        with open(file_path, 'rb') as f:
            files = {'file': (file_path, f)}
            response = httpx.post(url, headers=headers, files=files, data=data)
            response.raise_for_status()  # Automatically checks for HTTP errors
        print('Success:')
        return response.json()
    except Exception as e:
        raise e


def _prepare_data_with_connector(
    train_set_name: str,
    data_connection_pri: str,
    table_name: str,
    headers,
):
    url = f"{BASE_URL_V2}/create-data-source-with-connector"
    data = {
        'data_connection_pri': data_connection_pri,
        'table_name': table_name,
        'data_source_name': train_set_name,
    }
    try:
        response = httpx.post(url, headers=headers, json=data)
        response.raise_for_status()
        print(
            f'\033[38;2;85;87;93mData source creation successful:\033[0m \033[92m{response.status_code} {response.reason_phrase}\033[0m')
        return response.json()
    except Exception as e:
        raise e
