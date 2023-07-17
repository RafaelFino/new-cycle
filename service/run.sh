#!/bin/bash
flask --app app/main --debug run
# uvicorn app.main:app --reload --log-level trace --port 8081 --log-config ./etc/log-config.yml