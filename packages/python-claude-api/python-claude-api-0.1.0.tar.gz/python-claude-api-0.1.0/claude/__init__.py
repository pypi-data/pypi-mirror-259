# Copyright 2024 Minwoo(Daniel) Park, MIT License
from os import environ
from claude.core import Claude
from claude.constants import (
    HEADERS,
    ALLOWED_LANGUAGES,
    DEFAULT_LANGUAGE,
    REPLIT_SUPPORT_PROGRAM_LANGUAGES,
    REQUIRED_COOKIE_LIST,
)
from claude.client import GeminiClient
from claude.utils import (
    extract_links,
    upload_image,
    max_token,
    max_sentence,
)

gemini_api_key = environ.get("GEMINI_COOKIES")

__all__ = [
    "GeminiClient",
    "Gemini",
    "GeminiSession",
    "extract_links",
    "upload_image",
    "max_token",
    "max_sentence",
    "DEFAULT_LANGUAGE",
    "HEADERS",
    "ALLOWED_LANGUAGES",
    "REPLIT_SUPPORT_PROGRAM_LANGUAGES",
    "REQUIRED_COOKIE_LIST",
    "Tool",
]
__version__ = "0.1.0"
__author__ = "daniel park <parkminwoo1991@gmail.com>"
