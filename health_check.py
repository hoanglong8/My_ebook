#!/usr/bin/env python3
import os
import sys
import time
from datetime import datetime
from anthropic import Anthropic

def health_check():
    timestamp = datetime.now().isoformat()
    start_time = time.time()

    try:
        client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

        message = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=10,
            messages=[
                {"role": "user", "content": "ping"}
            ]
        )

        response_time = time.time() - start_time
        status = "OK"

    except Exception as e:
        response_time = time.time() - start_time
        status = f"FAILED: {str(e)}"

    # Output the result
    if status == "OK":
        print(f"[{timestamp}] Health check: OK (response time: {response_time:.2f}s)")
        sys.exit(0)
    else:
        print(f"[{timestamp}] Health check: FAILED (response time: {response_time:.2f}s)")
        print(f"Error: {status}")
        sys.exit(1)

if __name__ == "__main__":
    health_check()
