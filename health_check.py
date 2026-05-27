#!/usr/bin/env python3
import time
from datetime import datetime
from anthropic import Anthropic

client = Anthropic()

start_time = time.time()
timestamp = datetime.now().isoformat()

try:
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=100,
        messages=[
            {"role": "user", "content": "ping"}
        ]
    )
    end_time = time.time()
    response_time = end_time - start_time
    print(f"[{timestamp}] Health check: OK (response time: {response_time:.2f}s)")
except Exception as e:
    end_time = time.time()
    response_time = end_time - start_time
    print(f"[{timestamp}] Health check: FAILED ({str(e)})")
