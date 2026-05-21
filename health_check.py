#!/usr/bin/env python3
import sys
from datetime import datetime
import time
from anthropic import Anthropic

start_time = time.time()
timestamp = datetime.now().isoformat()

try:
    client = Anthropic()
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=10,
        messages=[
            {"role": "user", "content": "ping"}
        ]
    )

    elapsed = time.time() - start_time
    status = "OK"
    print(f"[{timestamp}] Health check: {status} (response time: {elapsed:.2f}s)")
    sys.exit(0)
except Exception as e:
    elapsed = time.time() - start_time
    status = "FAILED"
    print(f"[{timestamp}] Health check: {status} (error: {str(e)}, response time: {elapsed:.2f}s)")
    sys.exit(1)
