import pandas as pd
import system_sizing_py as ss
import numpy as np

resources = pd.read_csv(ss.path.join("/run/media/d8/D8_HD/D/Sem_3/Oz/input_data/", "resources.csv"), index_col="time")
# data
Eg = resources.loc[:, "global_rad"]
Istc = 1000

# creating data frame
hourly_solar = pd.DataFrame(index=ss.hourly_demand.index)
hourly_solar = ss.hor(hourly_solar, ss.hourly_demand, Eg)

# Calculation
hourly_solar["p_peak@Q=0.4"] = hourly_solar.loc[:, "hourly_demand"] * Istc / (hourly_solar.loc[:, "global_rad"] * ss.Q)
hourly_solar.replace(np.inf, np.nan, inplace=True)

# hourly p_peak
# (max, min) = (253.0135, 0.0697) MWh
max_hourly_p_peak = hourly_solar.loc[:, "p_peak@Q=0.4"].max()
min_hourly_p_peak = hourly_solar.loc[:, "p_peak@Q=0.4"].min()
print(max_hourly_p_peak)
print(min_hourly_p_peak)

# daily p_peak
# (max, min) = () MWh
daily_solar = ss.time_division(hourly_solar, 24)



# save solar file
print(daily_solar)
# output_path
# output_path = "/run/media/d8/D8_HD/D/Sem_3/Oz/output_data/system_sizing/"
# hourly_solar.to_csv(ss.path.join(output_path), "hourly_solar.csv")

# def abc(name_timeslots, y, z):
#     max_p_peak = name_timeslots.loc[:, "p_peak@Q=0.4"].max()
#     min_p_peak = name_timeslots.loc[:, "p_peak@Q=0.4"].min()
#     return max_p_peak, min_p_peak
