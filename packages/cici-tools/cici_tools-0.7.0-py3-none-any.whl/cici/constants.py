# SPDX-FileCopyrightText: 2024 UL Research Institutes
# SPDX-License-Identifier: MIT

from pathlib import Path

BASE_DIR = Path(__file__).parent.absolute()

SCHEMA_DIR = BASE_DIR / "schema"

COMMAND_DIR = BASE_DIR / "cli"

COMMANDS = sorted(
    [path.stem for path in COMMAND_DIR.glob("*.py") if not path.stem.startswith("_")]
)

PROVIDER_DIR = BASE_DIR / "providers"

PROVIDERS = sorted(
    [path.stem for path in PROVIDER_DIR.glob("*.py") if not path.stem.startswith("_")]
    + [
        path.stem
        for path in PROVIDER_DIR.glob("*/")
        if path.is_dir() and not path.stem.startswith("_")
    ]
)

DEFAULT_PROVIDER = PROVIDERS[0]

CONFIG_DIR_NAME = ".cici"
