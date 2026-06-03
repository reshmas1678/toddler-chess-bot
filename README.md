# Toddler Chess Bot (Slack Automation)

## What this does
- Sends daily chess lesson to Slack
- Automatically progresses day-by-day
- No manual work required

## Setup Steps

1. Create Slack webhook
2. Paste into main.py
3. Push repo to GitHub
4. Enable Actions
5. Done

## Customize
- Edit lessons.json for curriculum changes

## CMD for Test:
curl -X POST -H 'Content-type: application/json' \
--data '{"text":"🚨 Test message from Chess Bot"}' \
https://hooks.slack.com/services/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
