import pandas as pd
import system_sizing_py as ss
import numpy as np

# assumption
Q = 0.6


def solar_ppeak(data_frame):
    data_frame["p_peak@Q=0.6"] = data_frame.loc[:, "demand"] * Istc / (data_frame.loc[:, "global_rad"] * Q)
    data_frame.replace(np.inf, np.nan, inplace=True)
    return data_frame

# data
Eg = ss.resources.loc[:, "global_rad"]
Istc = 1000

# creating data frame
hourly_solar = ss.hor(ss.hourly_demand, Eg)
daily_solar = ss.time_division(hourly_solar, 24)
weekly_solar = ss.time_division(hourly_solar, 24 * 7)
bi_weekly_solar = ss.time_division(hourly_solar, 24 * 7 * 2)

# Calculation
hourly_solar = solar_ppeak(hourly_solar)
daily_solar = solar_ppeak(daily_solar)
weekly_solar = solar_ppeak(weekly_solar)
bi_weekly_solar = solar_ppeak(bi_weekly_solar)


if __name__ == "__main__":

    # save solar file
    # print(bi_weekly_solar)
    # output_path
    output_path = "/run/media/d8/D8_HD/D/Sem_3/Oz/output_data/system_sizing/"
    hourly_solar.to_csv(ss.path.join(output_path, "hourly_solar.csv"))
    daily_solar.to_csv(ss.path.join(output_path, "daily_solar.csv"))
    weekly_solar.to_csv(ss.path.join(output_path, "weekly_solar.csv"))
    bi_weekly_solar.to_csv(ss.path.join(output_path, "bi_weekly_solar.csv"))
