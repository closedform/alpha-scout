#!/usr/bin/env bash
#
# generate_prompt.sh CONFIG_PATH [OUTPUT_PATH]
# Populates the alpha discovery template with values from a config file.

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 path/to/config.env [output-path]" >&2
  exit 1
fi

CONFIG_PATH="$1"
OUTPUT_OVERRIDE="${2:-}"

if [[ ! -f "$CONFIG_PATH" ]]; then
  echo "Config file not found: ${CONFIG_PATH}" >&2
  exit 1
fi

# Load config variables as exported environment vars
set -o allexport
# shellcheck disable=SC1090
source "${CONFIG_PATH}"
set +o allexport

PROMPT_TEMPLATE="${PROMPT_TEMPLATE:-content/prompts/alpha-discovery-report.md}"
OUTPUT_DIR="${OUTPUT_DIR:-content/reports}"
CONFIG_TITLE="${CONFIG_TITLE:-$(basename "${CONFIG_PATH}")}"

if [[ ! -f "${PROMPT_TEMPLATE}" ]]; then
  echo "Prompt template not found: ${PROMPT_TEMPLATE}" >&2
  exit 1
fi

today="$(date +%Y%m%d)"

if [[ -z "${OUTPUT_OVERRIDE}" ]]; then
  if [[ -n "${OUTPUT_BASENAME:-}" ]]; then
    base="${OUTPUT_BASENAME}"
  else
    # slugify the title for the filename
    base="$(echo "${CONFIG_TITLE}" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | tr -s '-')"
    base="${base#-}"
    base="${base%-}"
    [[ -z "${base}" ]] && base="prompt"
  fi
  OUTPUT_PATH="${OUTPUT_DIR}/${today}-${base}.md"
else
  OUTPUT_PATH="${OUTPUT_OVERRIDE}"
fi

mkdir -p "$(dirname "${OUTPUT_PATH}")"

header="### ${today} ${CONFIG_TITLE}"

python3 - "${PROMPT_TEMPLATE}" "${OUTPUT_PATH}" "${header}" <<'PY'
import os
import re
import sys
from pathlib import Path

template_path = Path(sys.argv[1])
output_path = Path(sys.argv[2])
header_line = sys.argv[3]

text = template_path.read_text()
env = os.environ.copy()

pattern = re.compile(r"\{([A-Za-z0-9_]+)\}")
missing = set()

def replace(match: re.Match) -> str:
    key = match.group(1)
    value = env.get(key)
    if value is None:
        missing.add(key)
        return match.group(0)
    return value

body = pattern.sub(replace, text)

output_path.write_text(f"{header_line}\n\n{body}")

if missing:
    sys.stderr.write(
        "Warning: missing values for {}\n".format(", ".join(sorted(missing)))
    )
PY

echo "Wrote prompt to ${OUTPUT_PATH}"
