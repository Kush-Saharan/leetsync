from .api import get_recent_submissions, get_submission_detail
from .formatter import save_submission


def run():
    submissions = get_recent_submissions()

    if not submissions:
        print("No submissions found.")
        return

    # Sort by timestamp (descending)
    submissions = sorted(
        submissions,
        key=lambda x: int(x["timestamp"]),
        reverse=True
    )

    # Filter accepted only
    accepted = [
        s for s in submissions
        if s["statusDisplay"] == "Accepted"
    ]

    if not accepted:
        print("No accepted submissions found.")
        return

    latest = accepted[0]

    print("Latest Accepted Submission:")
    print(f"Title: {latest['title']}")
    print(f"Submission ID: {latest['id']}")
    print(f"Timestamp: {latest['timestamp']}")

    print("\nFetching full submission details...\n")

    detail = get_submission_detail(latest["id"])

    save_submission(detail)

