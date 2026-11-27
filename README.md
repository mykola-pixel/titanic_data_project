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
├── test_connection.py
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

```text
data/processed/titanic_cleaned.csv
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/mykola-pixel/titanic_data_project.git
cd titanic_data_project/titanic/titanic_data_pipeline
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
```

Replace the example values with your PostgreSQL credentials.

## Running the Pipeline

Run the following command from the project root:

```bash
python -m src.pipeline
```

The pipeline will execute the extraction, transformation, and loading steps.

## Database Schema

The project includes an SQL script for creating the `passengers` table:

```text
sql/create_tables.sql
```

The table stores passenger information, including survival status, passenger class, age, fare, embarkation port, deck, and title.

## Project Goals

This project was created to practice and demonstrate:

- Building a basic ETL pipeline.
- Working with CSV datasets using Pandas.
- Handling missing and duplicate data.
- Performing data transformations and feature extraction.
- Connecting Python applications to PostgreSQL.
- Managing database credentials with environment variables.
- Organizing Python code into separate modules.

## Future Improvements

- Add automated tests for ETL functions.
- Improve logging and error handling.
- Add data quality checks.
- Improve database loading to preserve table constraints.
- Add SQL queries for data analysis.
- Add Docker support.
