import pandas as pd
import requests
import time

# Load the top 100 apps CSV
df_top100 = pd.read_csv('../data/download/storeappinfo.csv')
lists = df_top100['appid'].tolist()
print(f"Total appids to fetch: {len(lists)}")

# Function to fetch app details
def get_app_details(appid):
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if str(appid) in data and data[str(appid)]['success']:
            details = data[str(appid)]['data']
            details['appid'] = appid
            return details
    except Exception as e:
        print(f"Error fetching {appid}: {e}")
        return None

# List to store all fetched app details
app_details_list = []

# Loop through all appids
for i, appid in enumerate(lists, start=1):
    details = get_app_details(appid)
    if details:
        app_details_list.append(details)
        print(f"[{i}] Fetched: {details.get('name', 'Unknown')}")
    else:
        print(f"[{i}] Failed to fetch details for appid {appid}")
    time.sleep(0.2)

# Convert the list of dicts to a DataFrame
df_details = pd.DataFrame(app_details_list)

# Save the details to CSV
df_details.to_csv('../data/download/top100_app_details.csv', index=False, encoding='utf-8')

