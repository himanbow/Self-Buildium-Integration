#!/usr/bin/env sh
set -euo pipefail

python -m my_app.jobs.processor "$@"
