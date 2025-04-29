import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load processed MITRE techniques
with open("processed_mitre_data.json", "r", encoding="utf-8") as file:
    techniques = json.load(file)

# Extract descriptions
descriptions = [tech["description"] for tech in techniques]

# Convert descriptions into numerical format
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(descriptions)

# Apply KMeans clustering
num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X)

# Assign cluster numbers
for i, tech in enumerate(techniques):
    tech["cluster"] = int(clusters[i])

# Save clustered data
with open("clustered_mitre_data.json", "w", encoding="utf-8") as file:
    json.dump(techniques, file, indent=2)

print(f"Clustered {len(techniques)} techniques into {num_clusters} clusters.")
