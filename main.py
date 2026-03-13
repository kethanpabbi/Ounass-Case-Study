import pandas as pd

df = pd.read_parquet("reco_model_data.parquet")
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nDtypes:\n", df.dtypes)
print("\nFirst 3 rows:\n", df.head(3).to_string())
print("\nNulls:\n", df.isnull().sum())
print("\nSample unique values:")
for col in df.columns:
    print(f"  {col}: {df[col].nunique()} unique —", df[col].dropna().unique()[:5])