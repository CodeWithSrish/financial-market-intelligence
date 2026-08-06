from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


class BronzeStorage:
    """
    Store raw API responses as JSON files.
    """

    def __init__(
        self,
        base_directory: str = "data/bronze",
    ) -> None:
        self.base_directory = Path(base_directory)

    def save_json(
        self,
        source: str,
        filename_prefix: str,
        data: Any,
    ) -> Path:
        """
        Save JSON to the Bronze layer.
        """

        now = datetime.utcnow()

        directory = (
            self.base_directory
            / source
            / str(now.year)
            / f"{now.month:02}"
            / f"{now.day:02}"
        )

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        filename = (
            f"{filename_prefix}_"
            f"{now:%Y%m%d_%H%M%S}.json"
        )

        file_path = directory / filename

        with open(
            file_path,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
            )

        return file_path