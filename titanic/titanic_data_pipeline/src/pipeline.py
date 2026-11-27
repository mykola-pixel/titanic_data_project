from pathlib import Path

from src.extract import extract_data
from src.transform import inspect_data, clean_data
from src.load import load_data_to_postgres

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_PATH = BASE_DIR / "data" / "processed" / "titanic_cleaned.csv"


def run_pipeline():
    print("\n" + "=" * 50)
    print("STARTING TITANIC DATA PIPELINE")
    print("=" * 50)

    try:
        # Step 1: Extract
        df = extract_data()

        # Step 2: Inspect
        inspect_data(df)

        # Step 3: Transform
        df_cleaned = clean_data(df)

        # Step 4: Save processed data
        PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
        df_cleaned.to_csv(PROCESSED_PATH, index=False)

        print(f"\nCleaned data saved to: {PROCESSED_PATH}")

        # Step 5: Load
        rows_loaded = load_data_to_postgres(df_cleaned)

        print("\n" + "=" * 50)
        print("TITANIC PIPELINE COMPLETED SUCCESSFULLY")
        print(f"Total rows loaded: {rows_loaded}")
        print("=" * 50)

        return rows_loaded

    except Exception as error:
        print("\nPIPELINE FAILED!")
        print(f"Error: {error}")
        raise


if __name__ == "__main__":
    run_pipeline()
    