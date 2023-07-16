#!/bin/bash
uvicorn app.main:app --reload --log-level trace --port 8081