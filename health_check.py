#!/usr/bin/env python3
import os
import time
from datetime import datetime
from anthropic import Anthropic

def health_check():
    timestamp = datetime.now().isoformat()
    start_time = time.time()

    try:
        client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

        response = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=10,
            messages=[
                {"role": "user", "content": "ping"}
            ]
        )

        response_time = time.time() - start_time

        if response.content and len(response.content) > 0:
            print(f"[{timestamp}] Health check: OK (response time: {response_time:.3f}s)")
            return True
        else:
            print(f"[{timestamp}] Health check: FAILED")
            return False
    except Exception as e:
        print(f"[{timestamp}] Health check: FAILED ({str(e)})")
        return False

if __name__ == "__main__":
    health_check()
