#!/usr/bin/env python3
""" Main 2
"""
from api.v1.auth.basic_auth import BasicAuth

b_auth = BasicAuth()

print(b_auth.extract_base64_authorization_header(None))
print(b_auth.extract_base64_authorization_header(89))
print(b_auth.extract_base64_authorization_header("Holberton School"))
print(b_auth.extract_base64_authorization_header("Basic Holberton"))
print(b_auth.extract_base64_authorization_header("Basic SG9sYmVydG9u"))
print(b_auth.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))
print(b_auth.extract_base64_authorization_header("Basic1234"))
