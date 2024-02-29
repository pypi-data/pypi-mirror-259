import json
import os
from typing import Optional
import urllib
import requests
from dotenv import load_dotenv

from relari.eval.manager import eval_manager

load_dotenv()


class RelariClient:
    def __init__(self, api_key: Optional[str] = None, url="http://api.relari.ai/v1/"):
        self._api_url = url
        if api_key is None:
            self.api_key = os.getenv("RELARI_API_KEY")
        else:
            self.api_key = api_key
        if self.api_key is None:
            raise ValueError(
                "Please set the environment variable RELARI_API_KEY or pass it as an argument."
            )

        self._headers = {"X-API-Key": self.api_key, "Content-Type": "application/json"}
        self.valid = self._validate()

    def _validate(self):
        try:
            response = requests.get(
                urllib.parse.urljoin(self._api_url, "secure/auth"), headers=self._headers, timeout=10
            )
        except requests.exceptions.Timeout:
            exit("Request timed out while trying to validate API key")
        if response.status_code != 200:
            return False
        return True

    def start_remote_evaluation(self):
        if eval_manager.is_running():
            raise ValueError("Cannot save while evaluation is running")
        payload = {
            "dataset": eval_manager.dataset.data,
            "pipeline": eval_manager.pipeline.asdict(),
            "results": eval_manager.evaluation.results,
            "metadata": eval_manager.metadata,
        }
        response = requests.post(
            urllib.parse.urljoin(self._api_url, "eval"),
            headers=self._headers,
            data=json.dumps(payload),
        )
        if response.status_code != 201:
            raise Exception("Failed to save evaluation results")
        print("Evaluation task submitted successfully")
