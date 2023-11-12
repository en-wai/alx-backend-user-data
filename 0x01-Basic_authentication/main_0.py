#!/usr/bin/env python3
""" Main 0
"""
from api.v1.auth.auth import Auth

auth = Auth()

print(auth.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(auth.authorization_header())
print(auth.current_user())
