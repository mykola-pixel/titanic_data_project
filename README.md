# Titanic Data Pipeline

A Python ETL project that extracts, cleans, and loads the Titanic dataset into a PostgreSQL database.

## Project Overview

This project demonstrates a basic ETL (Extract, Transform, Load) workflow using Python, Pandas, and PostgreSQL.

The pipeline reads raw Titanic passenger data, performs data inspection and cleaning, saves the processed dataset as a CSV file, and loads the cleaned data into PostgreSQL.

## Technologies Used

- **Python** — main programming language
- **Pandas** — data extraction, inspection, and transformation
- **PostgreSQL** — relational database for storing processed data
- **SQLAlchemy** — database connection and data loading
- **python-dotenv** — environment variable management

## Project Structure

```text
titanic_data_pipeline/
│
├── data/
│   ├── raw/
│   │   └── titanic.csv
│   └── processed/
│       └── titanic_cleaned.csv
│
├── sql/
│   ├── create_tables.sql
│   └── analysis.sql
│
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## ETL Process

### 1. Extract

- Reads the raw Titanic dataset from a CSV file.
- Checks whether the source file exists.
- Loads the data into a Pandas DataFrame.

### 2. Transform

- Inspects the dataset, data types, missing values, and duplicates.
- Removes duplicate passengers based on `PassengerId`.
- Fills missing `Age` and `Fare` values using the median.
- Fills missing `Embarked` values using the most frequent value.
- Extracts passenger deck information from the `Cabin` column.
- Extracts passenger titles from the `Name` column.
- Standardizes selected text columns.

### 3. Load

- Renames columns to follow snake_case naming conventions.
- Connects to PostgreSQL using SQLAlchemy.
- Loads the processed data into the `passengers` table.

### 4. Save Processed Data

The cleaned dataset is also saved locally:

`data/processed/titanic_cleaned.csv`

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/mykola-pixel/titanic_data_project.git
cd titanic_data_project/titanic/titanic_data_pipeline
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

For Windows, activate the environment using:

```powershell
.\.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the `titanic_data_pipeline/` directory.

Add your PostgreSQL connection settings:

```env
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=your_database
```

Replace the example values with your own PostgreSQL credentials.

**Important:** Do not commit your `.env` file or expose your database credentials. Make sure `.env` is included in `.gitignore`.

### 5. Create the database table

Before running the pipeline, make sure your PostgreSQL database and the `passengers` table have been created.

You can use the SQL script:

`sql/create_tables.sql`

## Running the Pipeline

Run the following command from the `titanic_data_pipeline/` directory:

```bash
python -m src.pipeline
```

The pipeline will:

1. Extract the raw Titanic dataset.
2. Inspect and clean the data.
3. Save the cleaned dataset as a CSV file.
4. Load the cleaned data into PostgreSQL.
5. Display the pipeline execution results.

## Pipeline Results

The pipeline successfully processes the Titanic dataset:

- **Source dataset:** 891 passenger records.
- **Cleaned dataset:** 891 passenger records.
- **Missing values after cleaning:** 0.
- **Processed data:** saved as a CSV file.
- **Database loading:** cleaned records loaded into PostgreSQL.

## SQL Analysis

The project includes SQL queries in `sql/analysis.sql` for exploring the cleaned Titanic dataset.

These queries can be used to analyze passenger survival rates and other dataset characteristics.

## Future Improvements

Possible improvements for this project:

- Add automated tests for ETL functions.
- Implement structured logging.
- Add additional data quality validation checks.
- Add Docker support for easier environment setup.
