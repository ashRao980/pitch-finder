# pitch-finder
Find local soccer pitches and organize pickup games. Built with Python, FastAPI, and PostGIS.

Status: In development 
- Data Pipeline is done 
- API is in progress 

Tech Stack
Python
pandas (data cleaning)
FastAPI + uvicorn (API, in progress)
Planned: PostgreSQL + PostGIS, Leaflet, deployment

Data
Pitch locations are seeded from the Chicago Park District facilities dataset on the Chicago Data Portal, which reflects facilities as of 2016.

clean_pitches.py keeps the rows where the facility is a football/soccer combo field (249 of 4,467) and writes data/pitches.csv.
Columns: id, pitch_name, lat, lng, surface_type, is_indoor, has_lights, is_free, source.
surface_type, is_indoor, has_lights, and is_free are intentionally empty because the source data doesn't include them. Empty means unknown, not "no".


Limitations: Since the data is from 2016, it may not have some of the latest parks, but I'm going with the assumption that all the parks built by 2016 still exist or at least a good majority of them exist. 











