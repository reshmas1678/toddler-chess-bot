# Main entry point for toddler-chess-bot
import json
import requests

WEBHOOK_URL = "https://hooks.slack.com/services/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"

# Load lessons
with open("lessons.json") as f:
    lessons = json.load(f)

# Load current day
try:
    with open("state.txt") as f:
        day = int(f.read().strip())
except:
    day = 1

lesson = lessons[day - 1]["lesson"]

def send_slack(msg):
    requests.post(WEBHOOK_URL, json={"text": msg})

send_slack(lesson)

# increment day
with open("state.txt", "w") as f:
    f.write(str(day + 1))
