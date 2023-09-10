from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
   return {
  "slack_name": "paul",
  "current_day": "Saturday",
  "utc_time": "2023-09-10T18:19:18Z",
  "track": "backend",
  "github_file_url": "https://github.com/Benrobo/hngx-be/blob/main/s-1/app.go",
  "github_repo_url": "https://github.com/benrobo/hngx-be",
  "status_code": 200
}