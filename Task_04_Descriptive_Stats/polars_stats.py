import polars as pl

def analyze_with_polars(file_path):
    print(f"\n📂 Analyzing: {file_path}")
    df = pl.read_csv(file_path)
    print("\nDescriptive Stats:")
    print(df.describe())

    if 'page_id' in df.columns:
        print("\nGrouped by page_id:")
        print(df.groupby('page_id').agg([
            pl.count().alias('count')
        ]))

    if 'ad_id' in df.columns and 'page_id' in df.columns:
        print("\nGrouped by page_id and ad_id:")
        print(df.groupby(['page_id', 'ad_id']).agg([
            pl.count().alias('count')
        ]))

for file in ['data/facebook_ads.csv', 'data/facebook_posts.csv', 'data/twitter_posts.csv']:
    analyze_with_polars(file)
