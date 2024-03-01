import requests
import xmltodict

from lib.auth import AwsAuth


class AwsInterface:

    def __init__(self, service, version):
        self.service = service
        self.version = version

    def post(self, region: str, action: str, **kwargs) -> dict:
        """
        Creates a POST request to AWS API

        Parameters
        region: geographic location
        action: request action
        """

        return self._request("POST", region, action, **kwargs)

    def get(self, region: str, action: str, **kwargs) -> dict:
        """
        Creates a GET request to AWS API

        Parameters
        region: geographic location
        action: request action
        """

        return self._request("GET", region, action, **kwargs)

    def _request(self, method: str, region: str, action: str, **kwargs) -> dict:
        """
        Creates a request to AWS API

        Parameters
        method: request method
        region: geographic location
        action: request action
        """

        auth = AwsAuth(self.service, region)
        url = f"https://{self.service}.{region}.amazonaws.com"

        if method == "GET":
            params = self._params(action, **kwargs)
            response = requests.request(method=method, auth=auth, url=url, params=params)
            return self._parse(response)

        elif method == "POST":
            data = self._data(action, **kwargs)
            response = requests.request(method=method, auth=auth, url=url, data=data)
            return self._parse(response)

    def _parse(self, response: requests.Response) -> dict:
        """
        Returns a parsed dictionary
        """

        data = xmltodict.parse(response.text)

        if response.status_code != 200:

            print(data)

            if "Response" in data:
                raise Exception(
                    data["Response"]
                    .get("Errors", {})
                    .get("Error", {})
                    .get("Message", "")
                )

            elif "ErrorResponse" in data:
                raise Exception(
                    data["ErrorResponse"]
                    .get("Error", {})
                    .get("Message", "")
                )
            
            elif "Error" in data:
                raise Exception(
                    data["Error"].
                    get("Message", "")
                )

            raise Exception("Failed to parse error message")

        return data

    def _data(self, action: str, **kwargs) -> dict:
        """
        Returns data dictionary
        """

        data = {"Version": self.version, "Action": action}

        data.update(kwargs)

        return data

    def _params(self, action: str, **kwargs) -> str:
        """
        Returns URL query parameters
        """

        params = [f"Version={self.version}", f"Action={action}"]

        params.extend([f"{key}={value}" for key, value in kwargs.items()])

        return "&".join(params)
