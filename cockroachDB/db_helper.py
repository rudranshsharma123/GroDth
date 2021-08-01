def get_data():
    import pandas as pd
    df = pd.read_csv('smol.csv')
    hashs = df['hash']
    number = df['number']
    cat = df['category']
    return hashs, number, cat

import psycopg2

conn = psycopg2.connect(
    database='shiny-wolf-1947.jina',
    user='test',
    password='rudranshsharma123',
    sslmode='require',
    port=26257,
    host='free-tier.gcp-us-central1.cockroachlabs.cloud',
    # options="--cluster=shiny-wolf-1947"
)