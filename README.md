# disc-jockAI 🎵🤖  
An ML-powered DJ set generator that creates curated music sets based on a given song and set length. Whether you're hosting a party or setting the vibe for a workout, disc-jockAI ensures a seamless musical journey tailored to your preferences.

---

## Features
- **Dynamic Set Generation**: Input a song and desired set length, and generate a playlist that flows smoothly with consistent energy, BPM, and mood.
- **Spotify Integration**: Fetches track data directly from Spotify using its Web API.
- **Feature Engineering**: Utilizes audio features like BPM, energy, and danceability for precise playlist curation.
- **Interactive UI**: (Optional) Use a Streamlit-based interface for an intuitive user experience.

---

## File Structure
```plaintext
dj-set-generator/
├── data/
│   └── track_features.csv        # Optional local storage for track features
├── notebooks/
│   ├── 01_data_retrieval.ipynb   # Retrieve and cache track data from Spotify
│   ├── 02_exploration.ipynb      # EDA: Analyze BPM, energy, mood distributions
│   └── 03_model_prototype.ipynb  # Prototype sequence generation model
├── src/
│   ├── spotify_api.py            # Spotify API helper functions
│   ├── feature_engineering.py    # Feature transformations and engineering
│   └── dj_set_generator.py       # Core logic for DJ set generation
├── app/ 
│   └── streamlit_app.py          # Streamlit app for optional UI
├── requirements.txt              # Dependencies for the project
└── README.md                     # Project documentation
```