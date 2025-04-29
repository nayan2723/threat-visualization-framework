# Threat Intelligence Visualization Framework 🛡️📊

This project aims to simplify the understanding of cyber threats by **clustering and visualizing** attack techniques from the **MITRE ATT&CK** and **NIST** frameworks.

We built an **interactive dashboard** using Python libraries like **Dash**, **Plotly**, and **NetworkX**, allowing cybersecurity professionals and students to explore threat data more intuitively.

---

## 📌 Features

- 📥 **Fetch and Process Data** from MITRE ATT&CK & NIST
- 🔢 **Vectorize Descriptions** using TF-IDF
- 🤖 **Apply KMeans Clustering** on similar threat techniques
- 📊 **3D Scatter Plot** to visualize clusters
- 🌐 **Network Graph** to show interconnections
- 🔎 **Dropdown Filtering** to explore specific threat groups
- ⚡ **Interactive Dash App** running locally

---

## 🧠 Tech Stack

- Python 3  
- Dash  
- Plotly  
- Pandas  
- Scikit-Learn  
- NetworkX  
- JSON & CSV data formats  
- Kali Linux / Windows (compatible)

---

## 📂 Project Structure

```
├── app.py                       # Main Dash dashboard
├── cluster_mitre_data.py       # KMeans clustering script
├── clustered_mitre_data.json   # Output with cluster labels
├── fetch_nist_data.py          # NIST data fetcher (optional)
├── mitre_data.json             # Raw MITRE data
├── nist_data.csv               # NIST threat dataset
├── process_mitre_data.py       # Data cleaning & preparation
├── processed_mitre_data.json   # Cleaned MITRE data
```

---

## 🚀 How to Run

1. Clone the repo:

```bash
git clone https://github.com/nayan2723/threat-visualization-framework.git
cd threat-visualization-framework
```

2. Install the dependencies:

```bash
pip install dash plotly pandas scikit-learn networkx
```

3. Run the dashboard:

```bash
python app.py
```

4. Open your browser and go to:  
   [http://127.0.0.1:8050/](http://127.0.0.1:8050/)




   :)
