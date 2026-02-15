from .api import get_recent_submissions

def run():
    submissions = get_recent_submissions()

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
    print(f"Language: {latest['lang']}")
    print(f"Submission ID: {latest['id']}")
