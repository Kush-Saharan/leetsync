import os
from datetime import datetime
from .config import TARGET_REPO_PATH


def clean_filename(slug: str, extension: str):
    return f"{slug}.{extension}"


def save_submission(detail):
    question = detail["question"]

    title = question["title"]
    slug = question["titleSlug"]
    difficulty = question["difficulty"]
    tags = [tag["name"] for tag in question["topicTags"]]

    code = detail["code"]
    runtime = detail["runtimeDisplay"]
    memory = detail["memoryDisplay"]

    # Determine language extension
    # print("Language name:", detail["lang"]["name"])
    lang_name = detail["lang"]["name"].lower()

    if "cpp" in lang_name:
        extension = "cpp"
    elif "python" in lang_name:
        extension = "py"
    elif "java" in lang_name:
        extension = "java"
    else:
        extension = "txt"

    # Choose primary topic (first tag)
    primary_topic = tags[0] if tags else "Misc"

    # Create directory
    base_folder = TARGET_REPO_PATH
    folder_path = os.path.join(base_folder, primary_topic)
    os.makedirs(folder_path, exist_ok=True)


    # Create file path
    filename = clean_filename(slug, extension)
    file_path = os.path.join(folder_path, filename)

    # Prevent overwrite
    if os.path.exists(file_path):
        print("File already exists. Skipping save.")
        return False
    
    if extension == "py":
        comment_start = '"""'
        comment_end = '"""'
    elif extension in ["cpp", "java"]:
        comment_start = "/*"
        comment_end = "*/"
    else:
        comment_start = ""
        comment_end = ""

    ai_section = ""

    if detail.get("ai_explanation"):
        ai_section = f"""{comment_start}
Explanation:
{detail['ai_explanation']}
{comment_end}
    """

    content = f"""{comment_start}
Problem: {title}
Difficulty: {difficulty}
Tags: {", ".join(tags)}
Runtime: {runtime}
Memory: {memory}
Synced On: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
{comment_end}

{ai_section}

{code}
    """

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Saved successfully to: {file_path}")
