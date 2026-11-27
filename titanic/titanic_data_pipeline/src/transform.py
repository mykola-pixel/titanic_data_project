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

    # Drop duplicates
    df = df.copy()

    # 1.Drop duplicete passengers
    if "PassengerId" in df.columns:
        df = df.drop_duplicates(subset=["PassengerId"])

    # 2.Clean "Age"
    if "Age" in df.columns:
        df["Age"] = df["Age"].fillna(df["Age"].median())

    # 3.Clean "Embarked"
    if "Embarked" in df.columns:
        mode_embarked = df["Embarked"].mode()

        if not mode_embarked.empty:
            df["Embarked"] = df["Embarked"].fillna(mode_embarked[0])

    # 4. Clean "Fare"
    if "Fare" in df.columns:
        df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    #5. Extract Deck from Cabin
    if "Cabin" in df.columns:
        df["Deck"] = df["Cabin"].str[0]
        df["Deck"] = df["Deck"].fillna("Unknown")
        df = df.drop(columns=["Cabin"])

    # 6. Extract Title from Name
    if "Name" in df.columns:
        df["Title"] = df["Name"].str.extract(r',\s*([^\.]*)\.')
        df = df.drop(columns=["Name"])

    # 7.Normalaze text columns 
    for col in ["Sex", "Embarked", "Title"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().str.strip()

    # 8. Remove completly empty rows
    df = df.dropna(how="all")

    print("\nCleaning completed!")
    print(f"Rows after cleaning: {len(df)}")
    print(f"Missing values: {df.isnull().sum().sum()}")

    return df
