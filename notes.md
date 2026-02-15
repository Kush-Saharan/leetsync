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

### Architecture:
CLI
 ↓
GraphQL API Call (Authenticated)
 ↓
Recent Submission List
 ↓
Filter Accepted
 ↓
Fetch Submission Details
 ↓
Format + Save File

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