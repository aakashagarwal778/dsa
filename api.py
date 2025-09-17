import requests
import json
import pandas as pd
import time

# Get the full app list
app_list_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
response = requests.get(app_list_url)
apps = response.json()['applist']['apps']
print(f"Total apps found: {len(apps)}")

# Function to get app details
def get_app_details(appid):
    url = f'https://store.steampowered.com/api/appdetails?appids={appid}'
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return None
        data = response.json()
        if str(appid) in data and data[str(appid)]['success']:
            details = data[str(appid)]['data']
            # Skip non-games
            if details.get('type') != 'game':
                return None
            # Add appid for reference
            details['appid'] = appid
            return details
    except:
        return None

# Collect details for first N apps (change N if needed)
N = 5000  # You can increase this gradually
app_details_list = []
for i, app in enumerate(apps[:N], start=1):
    details = get_app_details(app['appid'])
    if details:
        app_details_list.append(details)
        print(f"[{i}] Collected: {details['name']}")
    else:
        print(f"[{i}] Skipped: {app['name']}")
    time.sleep(0.2)  # rate limit

# Save collected data (optional)
with open("steam_app_details.json", "w", encoding="utf-8") as f:
    json.dump(app_details_list, f, ensure_ascii=False, indent=2)

# Load data into pandas
df = pd.DataFrame(app_details_list)

# Filter shooter games
df['genres_list'] = df['genres'].apply(lambda x: [g['description'] for g in x] if x else [])
df['is_shooter'] = df['genres_list'].apply(lambda g: 'Shooter' in g)
df_shooters = df[df['is_shooter']].copy()

print(f"Total shooter games: {len(df_shooters)}")


#------------------------------------
# Extra: Data Analysis
#------------------------------------

# Analyze sub-genres
def extract_subgenre(genres):
    # Example sub-genres: 'Battle Royale', 'Tactical', 'Hero Shooter'
    for sub in ['Battle Royale', 'Tactical', 'Hero']:
        for g in genres:
            if sub.lower() in g.lower():
                return sub
    return 'Other'

df_shooters['subgenre'] = df_shooters['genres_list'].apply(extract_subgenre)
subgenre_counts = df_shooters['subgenre'].value_counts()
print("\nSub-genre counts:")
print(subgenre_counts)

# Leading publishers
df_shooters['publisher_name'] = df_shooters['publishers'].apply(lambda x: x[0] if x else 'Unknown')
publisher_counts = df_shooters.groupby('publisher_name').size().sort_values(ascending=False)
print("\nTop publishers by number of shooter titles:")
print(publisher_counts.head(10))

# Top shooter titles (by Metacritic score)
df_shooters['metacritic_score'] = df_shooters['metacritic'].apply(lambda x: x.get('score') if x else None)
top_shooters = df_shooters.sort_values('metacritic_score', ascending=False).head(10)
print("\nTop shooter games by Metacritic score:")
print(top_shooters[['name', 'publisher_name', 'metacritic_score', 'subgenre']])