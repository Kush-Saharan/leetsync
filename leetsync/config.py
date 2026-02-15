import os
from dotenv import load_dotenv

load_dotenv()

LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
CSRFTOKEN = os.getenv("CSRFTOKEN")
LEETCODE_USERNAME = os.getenv("LEETCODE_USERNAME")


HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "x-csrftoken": CSRFTOKEN,
}

