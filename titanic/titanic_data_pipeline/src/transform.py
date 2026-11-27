def inspect_data(df):
    print("\n--- DATA OVERVIEW ---")
    print(df.head())

    print("\n--- DATA TYPES ---")
    print(df.dtypes)

    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    print("\n--- DUPLICATES ---")
    print(df.duplicated().sum())

    print("\n--- STATISTICS ---")
    print(df.describe(include="all"))


def clean_data(df):
    print("\nStarting data cleaning...")

    df = df.copy()

    # Remove duplicate passengers
    if "PassengerId" in df.columns:
        df = df.drop_duplicates(subset=["PassengerId"])

    # Fill missing Age values with median
    if "Age" in df.columns:
        df["Age"] = df["Age"].fillna(df["Age"].median())

    # Fill missing Embarked values with mode
    if "Embarked" in df.columns:
        mode_embarked = df["Embarked"].mode()

        if not mode_embarked.empty:
            df["Embarked"] = df["Embarked"].fillna(mode_embarked[0])

    # Fill missing Fare values with median
    if "Fare" in df.columns:
        df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    # Extract Deck from Cabin
    if "Cabin" in df.columns:
        df["Deck"] = df["Cabin"].str[0]
        df["Deck"] = df["Deck"].fillna("Unknown")
        df = df.drop(columns=["Cabin"])

    # Extract Title from Name
    if "Name" in df.columns:
        df["Title"] = df["Name"].str.extract(r',\s*([^\.]*)\.')
        df = df.drop(columns=["Name"])

    # Standardize text columns without converting NaN to "nan"
    for col in ["Sex", "Embarked", "Title"]:
        if col in df.columns:
            df[col] = df[col].astype("string").str.lower().str.strip()

    df = df.dropna(how="all")

    print("\nCleaning completed!")
    print(f"Rows after cleaning: {len(df)}")
    print(f"Missing values after cleaning: {df.isnull().sum().sum()}")

    return df
