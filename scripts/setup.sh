#!/bin/bash
set -euo pipefail
echo "Setting up CI/CD Pipeline Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
