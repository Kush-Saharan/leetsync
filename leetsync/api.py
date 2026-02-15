import requests
from .config import LEETCODE_SESSION, CSRFTOKEN, HEADERS, LEETCODE_USERNAME

GRAPHQL_URL = "https://leetcode.com/graphql"

def get_recent_submissions():
    query = """
    query recentSubmissions($username: String!) {
    recentSubmissionList(username: $username) {
        id
        title
        titleSlug
        statusDisplay
        lang
        timestamp
    }
    }
    """


    payload = {
        "query": query,
        "variables": {
            "username": LEETCODE_USERNAME
        }
    }


    cookies = {
        "LEETCODE_SESSION": LEETCODE_SESSION,
        "csrftoken": CSRFTOKEN
    }

    response = requests.post(
        GRAPHQL_URL,
        json=payload,
        headers=HEADERS,
        cookies=cookies
    )

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    data = response.json()
    return data["data"]["recentSubmissionList"]

def get_submission_detail(submission_id):
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
        runtime
        runtimeDisplay
        memory
        memoryDisplay
        lang {
          name
        }
        question {
          title
          titleSlug
          difficulty
          topicTags {
            name
          }
        }
      }
    }
    """

    payload = {
        "query": query,
        "variables": {
            "submissionId": int(submission_id)
        }
    }

    cookies = {
        "LEETCODE_SESSION": LEETCODE_SESSION,
        "csrftoken": CSRFTOKEN
    }

    response = requests.post(
        GRAPHQL_URL,
        json=payload,
        headers=HEADERS,
        cookies=cookies
    )

    print("Detail Status:", response.status_code)
    print("Detail Response:", response.text)

    data = response.json()
    return data["data"]["submissionDetails"]


