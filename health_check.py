#!/usr/bin/env python3
import time
from datetime import datetime
from anthropic import Anthropic

client = Anthropic()
timestamp = datetime.now().isoformat()
start_time = time.time()

try:
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=10,
        messages=[{"role": "user", "content": "ping"}]
    )

    response_time = time.time() - start_time
    status = "OK"
    output = f"[{timestamp}] Health check: {status} ({response_time:.3f}s)"

except Exception as e:
    response_time = time.time() - start_time
    status = "FAILED"
    output = f"[{timestamp}] Health check: {status} ({response_time:.3f}s) - {str(e)}"

print(output)
