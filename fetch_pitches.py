import requests
import csv

Overpass_URL = "https://overpass.kumi.systems/api/interpreter"
Overpass_Query = """

[out:json][timeout:30];
(

    node["leisure" = "pitch"]["sport" = "soccer"](41.64, -87.94, 41.83, -87.73);
    way["leisure" = "pitch"]["sport" = "soccer"](41.64, -87.94, 41.83, -87.73);

);
out center;
"""

headers = {
    "User-Agent": "PitchFinderApp/1.0 (academic project)"
}


response = requests.post(Overpass_URL, data = {"data": Overpass_Query}, headers = headers, timeout = 45)
response.raise_for_status()
result = response.json()


print("Number of soccer pitches found:", len(result['elements']))


