from .api import get_recent_submissions, get_submission_detail
from .formatter import save_submission
from .state_manager import load_last_synced, save_last_synced
from .git_utils import git_commit_and_push


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

    synced_count = 0   #Track successful saves

    for submission in new_submissions:
        print(f"Syncing submission {submission['id']}...")

        detail = get_submission_detail(submission["id"])

        if detail:
            save_submission(detail)
            # save_last_synced(submission["id"])
            latest_synced_id = submission["id"]
            synced_count += 1
        else:
            print("Failed to fetch detail, skipping.")

    if latest_synced_id:
        save_last_synced(latest_synced_id)
        git_commit_and_push()

    #Commit only if something was saved
    if synced_count > 0:
        print(f"Committing {synced_count} new submissions...")
        git_commit_and_push()
