#!/usr/bin/env python3
import numpy as np
import pandas as pd
f = pd.read_csv("2007.csv")
flight = f[['ArrDelay','Origin']][f['Origin'] == "SFO"].head(3)
print ("The 3 delayed flights")
print(flight[['ArrDelay','Origin']],"\n")

f2 = f[["Dest","Origin"]].groupby("Dest").count().sort_values(by = "Origin", ascending = False).head(3)
f2["Total"] = f2["Origin"]
print("The top 3 destinations are :","\n",f2)
