import os
from dotenv import load_dotenv

load_dotenv()

LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
CSRFTOKEN = os.getenv("CSRFTOKEN")
LEETCODE_USERNAME = os.getenv("LEETCODE_USERNAME")


HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://leetcode.com",
    "Content-Type": "application/json",
    "x-csrftoken": CSRFTOKEN,
}
