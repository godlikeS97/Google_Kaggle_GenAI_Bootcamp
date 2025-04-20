import pandas as pd
import asyncio
import aiohttp
import os
from aiohttp import ClientSession
from tqdm import tqdm

# File paths
INPUT_FILE = "data/met_public_domain.csv"      # Preprocessed public domain dataset
CHECKPOINT_FILE = "data/met_with_images.csv"   # Output file with image URLs
MAX_CONCURRENT_REQUESTS = 60              # Max requests per second (API limit)
DELAY_BETWEEN_BATCHES = 1                 # Pause between batches (in seconds)

# Load data
if os.path.exists(CHECKPOINT_FILE):
    df = pd.read_csv(CHECKPOINT_FILE)
    print("✅ Resuming from checkpoint...")
else:
    raw_df = pd.read_csv("/Users/yas063/Desktop/Google_Kaggle_GenAI_Bootcamp/Capstone Project/data/Met/MetObjects.txt")
    public_domain_df = raw_df[raw_df['Is Public Domain'] == True].copy()
    public_domain_df['Primary Image URL'] = None
    df = public_domain_df
    df.to_csv(INPUT_FILE, index=False)
    print("✅ Loaded initial public domain dataset.")

# Filter rows that haven't been processed yet
pending_rows = df[df['Primary Image URL'].isna()].copy()
print(f"🚀 Number of rows to process: {len(pending_rows)}")

# Async function to fetch primary image URL
async def fetch_image_url(session: ClientSession, object_id: int, row_index: int):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    try:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return row_index, data.get("primaryImage", "")
            else:
                print(f"❌ Error: Object ID {object_id}, status code {response.status}")
                return row_index, ''
    except Exception as e:
        print(f"⚠️ Exception for Object ID {object_id}: {e}")
        return row_index, ''

# Main batch processor
async def process_all_batches():
    async with aiohttp.ClientSession() as session:
        for i in tqdm(range(0, len(pending_rows), MAX_CONCURRENT_REQUESTS)):
            batch = pending_rows.iloc[i:i+MAX_CONCURRENT_REQUESTS]
            tasks = [
                fetch_image_url(session, row['Object ID'], row.name)
                for _, row in batch.iterrows()
            ]
            results = await asyncio.gather(*tasks)

            # Update dataframe with results
            for idx, image_url in results:
                df.at[idx, 'Primary Image URL'] = image_url

            # Save progress to checkpoint
            df.to_csv(CHECKPOINT_FILE, index=False)

            # Respect rate limit
            await asyncio.sleep(DELAY_BETWEEN_BATCHES)

    print("🎉 All rows processed and saved!")

# Entry point
if __name__ == "__main__":
    asyncio.run(process_all_batches())
