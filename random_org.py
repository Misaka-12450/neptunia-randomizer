import json

import requests
import streamlit as st


class APIKeyMissingException(Exception):
    pass


class RandomOrgAPIException(Exception):
    pass


class RandomOrgRequest:
    _id: int = 0

    def __init__(self):
        self.api_url: str = "https://api.random.org/json-rpc/4/invoke"
        self.jsonrpc: str = "2.0"
        self.headers: dict = {
            "Content-Type": "application/json",
        }
        self.api_key: str | None = st.secrets.get("random_org_api_key")

    @classmethod
    def _next_id(cls) -> int:
        cls._id += 1
        return cls._id

    def generate_payload(self) -> dict:
        return {
            "jsonrpc": self.jsonrpc,
            "method": self.method,
            "params": self.params,
            "id": self.id,
        }


class GenerateIntegers(RandomOrgRequest):
    def __init__(
            self,
            min_num: int,
            max_num: int,
            n: int = 1,
            replacement: bool = True,
            base: int = 10,
            pregenerated_randomization: str | None = None,
    ) -> None:
        super().__init__()
        self.method: str = "generateIntegers"
        self.params: dict = {
            "apiKey": self.api_key,
            "n": n,
            "min": min_num,
            "max": max_num,
            "replacement": replacement,
            "base": base,
            "pregeneratedRandomization": pregenerated_randomization,
        }
        self.id: int = self._next_id()

    def post(self):
        if not self.api_key:
            raise APIKeyMissingException(
                "RANDOM.ORG API key is missing from .streamlit/secrets.toml"
            )

        try:
            response: requests.Response = requests.post(
                url=self.api_url,
                data=json.dumps(self.generate_payload()),
                headers=self.headers,
            )
            response.raise_for_status()
        except requests.RequestException as e:
            raise RandomOrgAPIException(e)

        try:
            data = response.json()
        except json.JSONDecodeError as e:
            raise RandomOrgAPIException(f"Invalid JSON response: {e}")

        if error_info := data.get("error"):
            error_message = error_info.get("message") or json.dumps(error_info)
            raise RandomOrgAPIException(error_message)

        return data.get("result", {}).get("random", {}).get("data", [])
