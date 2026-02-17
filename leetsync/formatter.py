import os
from datetime import datetime


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
    base_folder = "leetcode"
    folder_path = os.path.join(base_folder, primary_topic)
    os.makedirs(folder_path, exist_ok=True)

    # Create file path
    filename = clean_filename(slug, extension)
    file_path = os.path.join(folder_path, filename)

    # Prevent overwrite
    if os.path.exists(file_path):
        print("File already exists. Skipping save.")
        return

    # Format file content
    content = f"""/*
Problem: {title}
Difficulty: {difficulty}
Tags: {", ".join(tags)}
Runtime: {runtime}
Memory: {memory}
Synced On: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
*/

{code}
"""

    # Write file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Saved successfully to: {file_path}")
