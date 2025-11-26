import csv
from collections import defaultdict, Counter
from statistics import mean, stdev

def analyze_csv(file_path):
    print(f"\n📂 Analyzing: {file_path}")
    columns = defaultdict(list)
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for col, val in row.items():
                val = val.strip()
                try:
                    columns[col].append(float(val))
                except:
                    columns[col].append(val)

    for col, values in columns.items():
        print(f"\n-- Column: {col} --")
        numeric = [v for v in values if isinstance(v, float)]
        if numeric:
            print(f"Count: {len(numeric)}")
            print(f"Mean: {mean(numeric):.2f}")
            print(f"Min: {min(numeric)}")
            print(f"Max: {max(numeric)}")
            if len(numeric) > 1:
                print(f"Std Dev: {stdev(numeric):.2f}")
        if all(isinstance(v, str) for v in values):
            counter = Counter(values)
            most_common = counter.most_common(1)[0]
            print(f"Unique: {len(counter)}")
            print(f"Most Frequent: {most_common[0]} ({most_common[1]} times)")

for file in ['data/facebook_ads.csv', 'data/facebook_posts.csv', 'data/twitter_posts.csv']:
    analyze_csv(file)
