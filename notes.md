Built an authenticated CLI tool that reverse-engineers LeetCode’s GraphQL API to automatically fetch and sync accepted submissions with structured metadata.

### Basic structure for the project:

User
  ↓
CLI Tool (Python)
  ↓
LeetCode GraphQL (Authenticated)
  ↓
Fetch latest AC submission
  ↓
Parse metadata (title, difficulty, tags)
  ↓
Generate structured file
  ↓
Update stats JSON
  ↓
Git commit & push

## Goal:
Build a CLI tool that:
- Authenticates with LeetCode
- Fetches latest Accepted submission
- Retrieves exact submitted code
- Extracts metadata (difficulty, tags, runtime, memory)
- Saves formatted solution locally

### Data flow:
CLI
  ↓
requests.post()
  ↓
GraphQL endpoint
  ↓
LeetCode internal backend
  ↓
Database
  ↓
Response JSON
  ↓
Your script parses
  ↓
Save file locally


### Problem:
Leetcode doesnt provide a public api

### Solution:
We authenticate using:
- LEETCODE_SESSION cookie
- csrftoken

save it in .env(locally saved)
load it using python dotenv(library used to access that data)

headers required:
HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "x-csrftoken": CSRFTOKEN,
}
Without x-csrftoken, requests fail.

### Used GraphQL integration
endpoint: https://leetcode.com/graphql

## Used two queries 
### Fetch Recent Submissions
we did:
- Sorted explicitly by timestamp.
- Filtered statusDisplay == "Accepted".

### Fetch Submission Details
Important findings(from errors based on wrong data input datatypes):
- submissionId must be Int!
- statusDisplay does NOT exist in SubmissionDetailsNode
- Use runtimeDisplay and memoryDisplay


### Errors encountereed:
- Missing required username
- Wrong type (String! vs Int!)
- Deprecated field (statusDisplay)

Solved by printing(response.status_code and response.text)

-> Till commit 2

### Formatter

Responsibilities:
- Detect language - map to extension
- Choose primary topic from topicTags
- Create folder if not exists
- Generate filename from titleSlug
- Format solution with metadata header

### Added Incremental Sync Engine

Algorithm:
- Fetch all recent submissions
- Sort by timestamp descending
- Filter accepted only
- Compare against last_synced_id
- Collect newer submissions
- Reverse order (sync oldest first)
- Save files
- Update state

We reverse to fetch the latest first

## Project structure now:

CLI
  ↓
Fetch recent submissions
  ↓
Filter Accepted
  ↓
Compare with .synced.json
  ↓
Fetch details via GraphQL
  ↓
Format file
  ↓
Save
  ↓
Update state


-> Till commit 4

### Git Automation Layer

In a repository made for leetcode solutions:
git add .
git diff --cached --quiet
if changes:
    git commit
    git push

## Project structure now:

User
  ↓
CLI Tool (Python)
  ↓
LeetCode GraphQL (Authenticated)
  ↓
Fetch recent submissions
  ↓
Filter Accepted
  ↓
Fetch submission details
  ↓
Parse metadata
  ↓
Generate structured file
  ↓
Update state (.synced.json)
  ↓
Git commit & push

-> Till commit 5

### AI-augmented solution archiver

Goal:
AI generates:
- Explanation
- Approach
- Time/Space complexity
- Proper main() driver (if needed)
- Merge AI output into formatted file

Example format of sending to any AI:

You are given a LeetCode solution.

Title: Two Sum
Difficulty: Easy
Tags: Array, Hash Table

Code:
<code_here>

Generate:
1. Clear explanation of approach
2. Time and space complexity
3. A working main function (in same language)
4. Format in markdown-style comment block

## Project architecture now:
CLI
  ↓
Fetch submission details (GraphQL)
  ↓
Build AI prompt
  ↓
AI backend (Local Ollama / Gemini)
  ↓
Inject explanation into detail object
  ↓
Formatter embeds explanation inside code file
  ↓
Git commit

Primary Backend: Ollama (Local LLM)
model used:deepseek-coder
AI endpoint:http://localhost:11434/api/generate

Advantages:
- Fully local
- No API cost
- No quota limits
- No internet dependency
- Private inference

Optional Backend: Gemini (Cloud)
- Using official google-genai SDK.
However:
- Free tier quota often limited to 0
- Requires billing attachment
- Not default backend

