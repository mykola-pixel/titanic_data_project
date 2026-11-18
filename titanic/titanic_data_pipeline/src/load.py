import os 
from pathlib import Path

from sqlalchemy import create_engine
from dotenv import load_dotenv


base_dir = Path(__file__).resolve().parent.parent
load_dotenv(base_dir / ".env")

def load_data_to_postgres(df):
    print("\nLoading data to PostgreSQL database...")

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    connection_string = (
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    )

    engine = create_engine(connection_string)
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

    df.to_sql(
        name="passengers",
        con=engine,
        if_exists="replace",
        index=False,
        method="multi",
        chunksize=500,
    )
    
    print("Data loaded successfully to PostgreSQL database.")

    engine.dispose()
    