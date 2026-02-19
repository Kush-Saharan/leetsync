from .api import get_recent_submissions, get_submission_detail
from .formatter import save_submission
from .state_manager import load_last_synced, save_last_synced
from .git_utils import git_commit_and_push

from leetsync.ai.enhancer import enhance_solution, build_prompt


def run(enhance_mode="local"):  # enhance_mode: None | "local" | "gemini"

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

    new_submissions.reverse()

    synced_count = 0
    latest_synced_id = None

    for submission in new_submissions:
        print(f"Syncing submission {submission['id']}...")

        detail = get_submission_detail(submission["id"])
        # print(detail)


        if not detail:
            print("Failed to fetch detail, skipping.")
            continue

        if enhance_mode:
            print(f"Enhancing with AI ({enhance_mode})...")

            question = detail["question"]

            prompt = build_prompt(
                title=question["title"],
                difficulty=question["difficulty"],
                tags=[tag["name"] for tag in question["topicTags"]],
                language=detail["lang"]["name"],
                code=detail["code"]
            )

            ai_output = enhance_solution(prompt, mode=enhance_mode)

            if ai_output:
                detail["ai_explanation"] = ai_output
            else:
                print("AI enhancement failed. Saving raw solution.")

        save_submission(detail)

        latest_synced_id = submission["id"]
        synced_count += 1

    if synced_count > 0:
        save_last_synced(latest_synced_id)
        print(f"Committing {synced_count} new submissions...")
        git_commit_and_push()
