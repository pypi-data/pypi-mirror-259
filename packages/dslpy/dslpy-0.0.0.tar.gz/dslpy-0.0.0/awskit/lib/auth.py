import os
import datetime
import hashlib
import hmac

from requests.auth import AuthBase
from requests.compat import urlparse


class AwsAuth(AuthBase):
    """
    AWS Authentification using AWS Signature Version 4
    """

    def __init__(self, service: str, region: str):
        """
        Parameters
        service: AWS service name
        region: AWS region name
        """

        self.service = service
        self.region = region

    def __call__(self, request):
        """
        Parameters
        request: request to be signed
        """

        now = datetime.datetime.utcnow()

        amz_date = now.strftime("%Y%m%dT%H%M%SZ")
        datestamp = now.strftime("%Y%m%d")

        url = urlparse(request.url)

        if "Host" not in request.headers:
            request.headers["Host"] = url.hostname

        if "Content-Type" not in request.headers:
            request.headers["Content-Type"] = (
                "application/x-www-form-urlencoded; charset=utf-8"
            )

        if request.method == "GET":
            payload_hash = hashlib.sha256("".encode("utf-8")).hexdigest()
        else:
            if request.body:
                if isinstance(request.body, bytes):
                    payload_hash = hashlib.sha256(request.body).hexdigest()
                else:
                    payload_hash = hashlib.sha256(
                        request.body.encode("utf-8")
                    ).hexdigest()
            else:
                payload_hash = hashlib.sha256(b"").hexdigest()

        request.headers["x-amz-content-sha256"] = payload_hash
        request.headers["X-AMZ-Date"] = amz_date

        headers_to_sign = sorted(
            (
                header
                for header in (header.lower() for header in request.headers.keys())
                if header.startswith("x-amz-") or header == "host"
            )
        )

        canonical_headers = "".join(
            (f"{header}:{request.headers[header]}\n" for header in headers_to_sign)
        )

        canonical_query_string = "&".join(
            ("=".join(t) for t in sorted((s.split("=") for s in url.query.split("&"))))
        )

        signed_headers = ";".join(headers_to_sign)

        canonical_request = (
            f"{request.method}\n"
            f"{url.path}\n"
            f"{canonical_query_string}\n"
            f"{canonical_headers}\n"
            f"{signed_headers}\n"
            f"{payload_hash}"
        )

        credential_scope = f"{datestamp}/{self.region}/{self.service}/aws4_request"

        string_to_sign = (
            "AWS4-HMAC-SHA256\n"
            f"{amz_date}\n"
            f"{credential_scope}\n"
            f"{hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()}"
        ).encode("utf-8")

        k_key = f"AWS4{os.getenv('AWS_SECRET_ACCESS_KEY')}".encode("utf-8")
        k_date = self.sign_msg(k_key, datestamp)
        k_region = self.sign_msg(k_date, self.region)
        k_service = self.sign_msg(k_region, self.service)
        k_signing = self.sign_msg(k_service, "aws4_request")
        signature = hmac.new(k_signing, string_to_sign, hashlib.sha256).hexdigest()

        request.headers["Authorization"] = (
            "AWS4-HMAC-SHA256 Credential="
            f"{os.getenv('AWS_ACCESS_KEY_ID')}/{credential_scope}, "
            f"SignedHeaders={signed_headers}, "
            f"Signature={signature}"
        )

        return request

    def sign_msg(self, key: str, msg: str) -> str:
        """
        Given a key and a message returns a hash-based message authentication code

        Parameters
        key: key to be used for encryption
        msg: message to be signed by the key
        """

        return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()
