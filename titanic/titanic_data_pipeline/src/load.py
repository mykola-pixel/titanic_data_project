import os
from pathlib import Path

from sqlalchemy import create_engine, URL
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def load_data_to_postgres(df):
    print("\nLoading data to PostgreSQL database...")

    # Get database credentials
    required_vars = ["DB_USER", "DB_PASSWORD", "DB_HOST", "DB_PORT", "DB_NAME"]

    missing_vars = [
        var for var in required_vars if not os.getenv(var)
    ]

    if missing_vars:
        raise ValueError(
            f"Missing database environment variables: {missing_vars}"
        )

    # Create database connection URL
    connection_url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME"),
    )

    # Rename columns to match PostgreSQL schema
    df = df.rename(columns={
        "PassengerId": "passenger_id",
        "Survived": "survived",
        "Pclass": "pclass",
        "Sex": "sex",
        "Age": "age",
        "SibSp": "sibsp",
        "Parch": "parch",
        "Ticket": "ticket",
        "Fare": "fare",
        "Embarked": "embarked",
        "Deck": "deck",
        "Title": "title",
    })

    engine = create_engine(connection_url)

    try:
        with engine.begin() as connection:
            # Remove old records but preserve table structure
            connection.exec_driver_sql(
                "TRUNCATE TABLE public.passengers"
            )

            # Insert new records
            df.to_sql(
                name="passengers",
                con=connection,
                schema="public",
                if_exists="append",
                index=False,
                method="multi",
                chunksize=500,
            )

        print(f"Successfully loaded {len(df)} rows into PostgreSQL.")

        return len(df)

    finally:
        engine.dispose()