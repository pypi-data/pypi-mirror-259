import os
from typing import Union

import boto3
import httpx

from hangar_sdk.config import Config


class HangarScope:
    def __init__(
        self,
        region: str,
        name: str,
        accountName: str = "default",
        roleAssumptions: list = [],
        api_key: Union[str, None] = None,
        _entity: str = None,
        endpoint: str = "https://api.tryhangar.com/controlplane",
    ):
        if api_key is None:
            self.api_key = os.environ["HANGAR_API_KEY"]
        else:
            self.api_key = api_key

        if os.environ.get("HANGAR_URL") is not None:
            self.endpoint = os.environ["HANGAR_URL"]

        self.endpoint = endpoint
        self.region = region
        self.entity = _entity
        self.name = name
        # Maintained by api key
        self.roleAssumptions = roleAssumptions
        self.resources = {}
        self.accountName = accountName

    async def deploy(self):
        if Config.mode == "invoke":
            return
        try:
            all = self.get_resources()

        except Exception:
            all = []

        to_update = []
        to_add = []
        to_delete = []

        for control_plane_resource in all:
            if control_plane_resource in self.resources.keys():
                to_update.append(self.resources.pop(control_plane_resource))
            elif control_plane_resource not in self.resources.keys():
                to_delete.append(control_plane_resource)

        for local_resource in self.resources.values():
            to_add.append(local_resource)
        for resource in to_add + to_update:
            resource._resolved = False
            resource.mode = Config.mode

        for resource in to_add + to_update:
            cr = resource._resolve()
            if cr is not None:
                await cr

        for resource in to_delete:
            self.delete_resource(resource_id=resource)

    def add_construct(self, data, force_change=False):
        payload = {
            "region": self.region,
            "version": "v1",
            "roleAssumptions": self.roleAssumptions,
            "tags": [],
            "scope": self.name,
            "accountName": self.accountName,
            "resourceId": data["resourceId"],
            **data,
            "forceChange": force_change,
        }

        # print(payload)
        try:
            if self.entity is not None:
                response = httpx.request(
                    "POST",
                    self.endpoint,
                    headers={"X-API-KEY": self.api_key},
                    json=payload,
                    timeout=20.0,
                )

            else:
                response = httpx.request(
                    "POST",
                    self.endpoint,
                    headers={"X-API-KEY": self.api_key},
                    json=payload,
                    timeout=20.0,
                )

        except httpx.ReadTimeout:
            raise Exception("Couldnt acquire lock")
        if response.status_code != 200:
            raise Exception(response.text)

        if "job_id" in response.json():
            return response.json()["job_id"]
        else:
            raise Exception(response.text)

    def get_logs(self, resource_id, path):
        res = httpx.request(
            "GET",
            self.endpoint + "/resources/" + resource_id + "/logs",
            headers={"X-API-KEY": self.api_key},
            params={"path": path},
        )

        return res.json()

    def get_state(self, resource_id):
        res = httpx.request(
            "GET",
            self.endpoint + "/state",
            headers={"X-API-KEY": self.api_key},
            params={
                "resourceId": resource_id,
            },
        )
        return res.json()

    def get_status(self, job_id):
        return httpx.request(
            "GET",
            self.endpoint + "/status",
            headers={"X-API-KEY": self.api_key},
            params={"job_id": job_id},
            timeout=httpx.Timeout(20.0),
        )

    def get_resources(self):
        r = httpx.request(
            "GET",
            f"{self.endpoint}/scopes/{self.name}/resources",
            headers={"X-API-KEY": self.api_key},
        )
        if "detail" in r.json():
            raise Exception(r.json()["detail"])

        return [resource["ResourceId"] for resource in r.json()]

    def execute_action(self, resource_id, action: str, params={}):
        payload = {
            "resourceId": resource_id,
            "action": action,
            "params": params,
        }

        if self.entity is not None:
            response = httpx.request(
                "PATCH",
                self.endpoint,
                headers={"X-API-KEY": self.api_key},
                json=payload,
                params={"entityId": self.entity},
                timeout=20.0,
            )

        else:
            response = httpx.request(
                "PATCH",
                self.endpoint,
                headers={"X-API-KEY": self.api_key},
                json=payload,
                timeout=20.0,
            )

        if response.status_code != 200:
            raise Exception(response.text)

        return response.json()

    def delete_resource(self, resource_id):
        print("Deleting resource: " + resource_id)
        return httpx.request(
            "DELETE",
            self.endpoint,
            headers={"X-API-KEY": self.api_key},
            params={"resourceId": resource_id},
        )

    def get_resource(self, resource_id):
        return httpx.request(
            "GET",
            self.endpoint + "/resources/" + resource_id,
            headers={"X-API-KEY": self.api_key},
        ).json()

    def get_boto3_session(self):
        credentials = httpx.request(
            "GET",
            self.endpoint + "/scopes/" + self.name + "/credentials",
            headers={"X-API-KEY": self.api_key},
            timeout=30.0,
        ).json()
        return boto3.Session(
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
            region_name=self.region,
        )
