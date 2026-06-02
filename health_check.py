#!/usr/bin/env python3
import time
from datetime import datetime
from anthropic import Anthropic

def health_check():
    timestamp = datetime.now().isoformat()
    start_time = time.time()

    try:
        client = Anthropic()
        response = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=10,
            messages=[{"role": "user", "content": "ping"}]
        )
        elapsed = time.time() - start_time
        status = "OK"
        print(f"[{timestamp}] Health check: {status} ({elapsed:.2f}s)")
        return True
    except Exception as e:
        elapsed = time.time() - start_time
        status = "FAILED"
        print(f"[{timestamp}] Health check: {status} ({elapsed:.2f}s) - {str(e)}")
        return False

if __name__ == "__main__":
    health_check()
