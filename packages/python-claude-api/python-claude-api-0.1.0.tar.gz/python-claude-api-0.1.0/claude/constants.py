# Copyright 2024 Minwoo(Daniel) Park, MIT License
import browser_cookie3


SUPPORTED_BROWSERS = [
    browser_cookie3.chrome,
    browser_cookie3.chromium,
    browser_cookie3.opera,
    browser_cookie3.opera_gx,
    browser_cookie3.brave,
    browser_cookie3.edge,
    browser_cookie3.vivaldi,
    browser_cookie3.firefox,
    browser_cookie3.librewolf,
    browser_cookie3.safari,
]

DEFAULT_LANGUAGE = "en"
TEXT_GENERATION_WEB_SERVER_PARAM = "boq_assistant-bard-web-server_20240222.09_p2"
POST_ENDPOINT = "https://gemini.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate"
HOST = "https://gemini.google.com/"
SHARE_ENDPOINT = "https://clients6.google.com/upload/drive/v3/"

IMG_UPLOAD_HEADERS = {
    "authority": "content-push.googleapis.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.7",
    "authorization": "Basic c2F2ZXM6cyNMdGhlNmxzd2F2b0RsN3J1d1U=",  # Constant Authorization Key
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "origin": "https://gemini.google.com",
    "push-id": "feeds/mcudyrk2a4khkz",  # Constant
    "referer": "https://gemini.google.com/",
    "x-goog-upload-command": "start",
    "x-goog-upload-header-content-length": "",
    "x-goog-upload-protocol": "resumable",
    "x-tenant-id": "bard-storage",
}

EXECUTE_HEADERS = {
    "Host": "gemini.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "Origin": "https://gemini.google.com",
    "Referer": "https://gemini.google.com/",
}
HEADERS = {
    "Host": "gemini.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "Origin": "https://gemini.google.com",
    "Referer": "https://gemini.google.com/",
}

SHARE_HEADERS = {
    "Alt-Used": "clients6.google.com",
    "Content-Type": 'multipart/mixed; boundary="-------314159265358979323846"',
    "Host": "clients6.google.com",
    "Origin": "https://gemini.google.com",
    "Referer": "https://gemini.google.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
}

REQUIRED_COOKIE_LIST = [
    "SIDCC",
    "__Secure-1PSID",
    "__Secure-1PSIDTS",
    "__Secure-1PSIDCC",
    "NID",
]
