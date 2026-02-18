import subprocess
from .config import TARGET_REPO_PATH

def git_commit_and_push():
    subprocess.run(["git", "add", "."], cwd=TARGET_REPO_PATH)

    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=TARGET_REPO_PATH
    )

    if result.returncode != 0:
        subprocess.run(
            ["git", "commit", "-m", "chore: sync new LeetCode submissions"],
            cwd=TARGET_REPO_PATH
        )
        subprocess.run(["git", "push"], cwd=TARGET_REPO_PATH)
