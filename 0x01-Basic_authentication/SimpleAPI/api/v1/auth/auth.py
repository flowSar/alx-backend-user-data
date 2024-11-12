#!/usr/bin/env python3
"""Module for auth"""
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """class auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if authentication is required for a given path """
        return False

    def authorization_header(self, request=None) -> str:
        """ Returns the authorization header or None """
        return None

    def current_user(self, request=None) -> User:
        """ Returns the current user or None """
        return None
