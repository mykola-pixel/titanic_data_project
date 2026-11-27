import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw" / "titanic.csv"


def extract_data():
    print("\nExtracting Titanic dataset...")

    if not RAW_DATA_DIR.exists():
        raise FileNotFoundError(
            f"Raw data file not found at {RAW_DATA_DIR}"
        )

    df = pd.read_csv(RAW_DATA_DIR)

    print(f"Extracted {len(df)} rows and {len(df.columns)} columns.")

    return df