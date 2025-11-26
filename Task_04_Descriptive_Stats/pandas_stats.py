import pandas as pd

def analyze_with_pandas(file_path):
    print(f"\n📂 Analyzing: {file_path}")
    df = pd.read_csv(file_path)
    print("\nDescriptive Stats:")
    print(df.describe(include='all'))

    for col in df.columns:
        print(f"\nColumn: {col}")
        print("Unique values:", df[col].nunique())
        print("Most frequent:\n", df[col].value_counts().head(1))

    if 'page_id' in df.columns:
        print("\nGrouped by page_id:")
        print(df.groupby('page_id').describe())

    if 'ad_id' in df.columns:
        print("\nGrouped by page_id and ad_id:")
        print(df.groupby(['page_id', 'ad_id']).describe())

for file in ['data/facebook_ads.csv', 'data/facebook_posts.csv', 'data/twitter_posts.csv']:
    analyze_with_pandas(file)
