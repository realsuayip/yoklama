import asyncio
import logging
import sys

from yoklama.runner import run

if __name__ == "__main__":
    if len(sys.argv) > 2:
        logging.basicConfig(level="INFO")
    value = sys.argv[1]
    asyncio.run(run(sys.argv[1]))
