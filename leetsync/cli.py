from .api import get_recent_submissions, get_submission_detail
from .formatter import save_submission
from .state_manager import load_last_synced, save_last_synced


def run():
    submissions = get_recent_submissions()

    if not submissions:
        print("No submissions found.")
        return

    submissions = sorted(
        submissions,
        key=lambda x: int(x["timestamp"]),
        reverse=True
    )

    accepted = [
        s for s in submissions
        if s["statusDisplay"] == "Accepted"
    ]

    if not accepted:
        print("No accepted submissions found.")
        return

    last_synced_id = load_last_synced()

    print("Last synced ID:", last_synced_id)

    new_submissions = []

    for submission in accepted:
        if last_synced_id and submission["id"] == str(last_synced_id):
            break
        new_submissions.append(submission)

    if not new_submissions:
        print("No new submissions to sync.")
        return

    # Reverse to sync oldest first
    new_submissions.reverse()

    for submission in new_submissions:
        print(f"Syncing submission {submission['id']}...")

        detail = get_submission_detail(submission["id"])

        if detail:
            save_submission(detail)
            save_last_synced(submission["id"])
        else:
            print("Failed to fetch detail, skipping.")
