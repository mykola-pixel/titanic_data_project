from pathlib import Path

from src.extract import extract_data
from src.transform import inspect_data, clean_data
from src.load import load_data_to_postgres

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_PATH = BASE_DIR / "data" / "processed" / "titanic_cleaned.csv"


def run_pipeline():
    print("="*50)
    print("Starting Titanic data pipeline...")
    print("="*50)
    
    # Step 1: Extract data
    df = extract_data()

    # Step 2: Inspect data
    inspect_data(df)

    # Step 3: Clean data
    df_cleaned = clean_data(df)

    # Step 4: Save cleaned data to CSV
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_cleaned.to_csv(PROCESSED_PATH, index=False)
    print(f"Cleaned data saved to {PROCESSED_PATH}")

    print("\nCleaned CSV saved!")

    # Step 5: Load cleaned data to PostgreSQL
    load_data_to_postgres(df_cleaned)

    print("\n" + "=" * 50)
    print("TITANIC PIPELINE COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    run_pipeline()

    