#!/bin/bash

echo "Running entrypoint.sh"
python src/generate_data.py
fastapi run src/server.py --port 80