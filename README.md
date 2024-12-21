# disc-jockAI
ML model to build "DJ Sets" based off a given song and Set Length


## Breakdown of the file structure
dj-set-generator/
├── data/
│   └── track_features.csv        # optional local storage of features
├── notebooks/
│   ├── 01_data_retrieval.ipynb   # gathering track info, caching to local
│   ├── 02_exploration.ipynb      # EDA, distribution of BPM, energy, etc.
│   └── 03_model_prototype.ipynb  # building the sequence generation logic
├── src/
│   ├── spotify_api.py            # helper functions to get data from Spotify
│   ├── feature_engineering.py    # any transformations or additional feats
│   └── dj_set_generator.py       # main script to generate the set
├── app/ 
│   └── streamlit_app.py          # optional Streamlit UI
├── requirements.txt
└── README.md
