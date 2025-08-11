from typing import Dict, Any, Optional
from requests import Response, request, exceptions
from requests.auth import AuthBase

class API:

    @staticmethod
    def make_api_request(
            url: str,
            http_method: str = "GET",
            json_data: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None,
            auth: Optional[AuthBase] = None,
            timeout: Optional[float] = 10.0,
            verbose: bool = False,
            **kwargs: Any
    )-> Optional[Response]:
        """A flexible API request using the requests library

        Args:
            url (str): the url of the api request
            http_method (str, optional): HTTP METHOD. Defaults to "GET".
            json_data (Optional[Dict[str, Any]], optional): body of the request as json. Defaults to None.
            params (Optional[Dict[str, Any]], optional): query parameters to add to the url. Defaults to None.
            headers (Optional[Dict[str, str]], optional): HTTP headers sent with request. Defaults to None.
            auth (Optional[AuthBase], optional): An authentication object. Defaults to None.
            timeout (Optional[float], optional): The number of seconds to wait before throwing an exception. Defaults to 10.0.
            verbose (bool, optional): Expectation of debug logs. Defaults to False.

        Returns:
            Optional[Response]: The requests response object when the request is successufl, otherwise is None
        """
        try:
            request_args: Dict[str, Any] = {}
            if json_data is not None:
                if verbose:
                    print(f"body: {json_data}")
                request_args["json"] = json_data
            if params is not None:
                if verbose:
                    print(f"query params: {params}")
                request_args["params"] = params
            if headers is not None:
                if verbose:
                    print(f"headers: {headers}")
                request_args["headers"] = headers
            if auth is not None:
                if verbose:
                    print(f"auth: {auth}")
                request_args["auth"] = auth
            if timeout is not None:
                if verbose:
                    print(f"timeout: {timeout}")
                request_args["timeout"] = timeout
            if url is not None and verbose:
                print("url: {url}")
            if http_method is not None and verbose:
                print("http_method: {http_method}")
            request_args.update(kwargs)

            response = request(http_method.upper(), url, **request_args)
            response.raise_for_status()
            return response
        except exceptions.ConnectionError as con_error:
            print(f"Conn error: {con_error}")
        except exceptions.Timeout as timeout_error:
            print(f"timeout_error: {timeout_error}")
        except exceptions.RequestException as req_err:
            print(f"req_err: {req_err}")
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")
        return None
