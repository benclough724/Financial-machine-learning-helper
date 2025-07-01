from pathlib import Path

# Base directory (project root)
BASE_DIR = Path(__file__).parent.parent

# dataset directories (raw and unprocessed)
DATA_DIR = BASE_DIR / "raw"
DATA_DIR = BASE_DIR / "processed"

# Data root
DATA_DIR = BASE_DIR / "data"


# dataset directories (raw and unprocessed)
RAW_DATA_DIR = DATA_DIR /"unprocessed"
PROCESSED_DATA_DIR = DATA_DIR /"processed"

