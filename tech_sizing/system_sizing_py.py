import pandas as pd
from os import path

# import demand file
demand_path = "/run/media/d8/D8_HD/D/Sem_3/Oz/output_data/demand/"
hourly_demand = pd.read_csv(path.join(demand_path, "hourly_demand.csv"), index_col="time")

resources = pd.read_csv(path.join("/run/media/d8/D8_HD/D/Sem_3/Oz/input_data/", "resources.csv"), index_col="time")

# functions


def hor(*x):
    data = pd.concat(x, axis=1)
    return data


def ver(*x):
    data = pd.concat(x, axis=0)
    return data


def time_division(data_frame, hours):
    """derive specific data (i.e. daily and weekly) data from hourly data"""
    rand = []
    division = pd.DataFrame()
    for n in range(len(data_frame.columns)):
        rand.append(list())
    for m in range(len(rand)):
        for i in range(0, 8760, hours):
            rand[m].append(data_frame.iloc[i:i + hours, m].sum())
        division[data_frame.columns[m]] = rand[m]
    division.index.name = "time"
    if len(division.index) > (8760 // hours):
        division = division.drop(division.index[-1], axis=0)
    return division