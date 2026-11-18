import pandas as pd 

df = pd.read_csv("raw_2016.csv")
result = df[df["FACILITY_N"].isin(["FOOTBALL/SOCCER COMBO FLD"])]

print(len(result))

newVar = result[["PARK", "X_COORD", "Y_COORD"]].copy()
newVar = newVar.rename(columns={"PARK": "pitch_name", "X_COORD": "lng", "Y_COORD": "lat"})




newVar["id"] = range(1, len(newVar) + 1)
print(newVar.head(3))

newVar["surface_type"] = None
newVar["is_indoor"] = None
newVar["has_lights"] = None
newVar["is_free"] = None

newVar["source"] = "cpd_2016"



newVar = newVar[["id", "pitch_name", "lat", "lng", "surface_type", "is_indoor", "has_lights", "is_free", "source"]]

newVar.to_csv("data/pitches.csv", index=False)


                 









