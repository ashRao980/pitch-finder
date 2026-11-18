# Pitch-Finder

Find local soccer pitches in Chicago and organize pickup games.

**Status:** In development. The data pipeline is done and the API is in progress.

## Features

- [x] Cleaned dataset of 249 Chicago soccer fields (reproducible script)
- [ ] REST API to list and search pitches by location
- [ ] Distance-based search ("pitches within 5 km of me")
- [ ] Map frontend
- [ ] Pickup game organizing

## Tech Stack

- Python
- pandas (data cleaning)
- FastAPI + uvicorn (API, in progress)
- Planned: PostgreSQL + PostGIS, Leaflet, deployment

## Data

Pitch locations are seeded from the Chicago Park District facilities dataset on the [Chicago Data Portal](https://data.cityofchicago.org/), which reflects facilities as of 2016.

- `clean_pitches.py` keeps the rows where the facility is a football/soccer combo field (249 of 4,467) and writes `data/pitches.csv`.
- Columns: `id`, `pitch_name`, `lat`, `lng`, `surface_type`, `is_indoor`, `has_lights`, `is_free`, `source`.
- `surface_type`, `is_indoor`, `has_lights`, and `is_free` are intentionally empty because the source data doesn't include them. Empty means unknown, not "no".

**Limitations: Since the data is from 2016, it may not have some of the latest parks, but I'm going with the assumption that all the parks built by 2016 still exist or at least a good majority of them exist. 












