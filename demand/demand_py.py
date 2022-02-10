import pandas as pd
import os

in_path = "/run/media/d8/D8_HD/D/Sem_3/Oz/decentralization/input_data/"
out_path = "/run/media/d8/D8_HD/D/Sem_3/Oz/output_data/"

# file_name = "profile.csv"

# read profile file from input_data folder
profile = pd.read_csv(os.path.join(in_path, "profile.csv"), index_col="time")


# # data file creation
def create():
    ind = pd.date_range(start="2021-01-01", end=None, periods=8760, freq="H")
    data = pd.DataFrame(index=ind)
    data.index.name = "time"
    return data


def timeslots(start_date=None, end_date=None, periods_int=None, fre=None):
    ind = pd.date_range(start=start_date, end=end_date, periods=periods_int, freq=fre)
    data = pd.DataFrame(index=ind)
    data.index.name = "time"
    return data


def hor(*x):
    data = pd.concat(x, axis=1)
    return data


def ver(*x):
    data = pd.concat(x, axis=0)
    return data


def hour(a, b, c):
    a[b] = c
    return a


def fixed(string, value):
    data = create()

    h0 = timeslots(start_date="2021-01-01 00:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h1 = timeslots(start_date="2021-01-01 01:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h2 = timeslots(start_date="2021-01-01 02:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h3 = timeslots(start_date="2021-01-01 03:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h4 = timeslots(start_date="2021-01-01 04:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h5 = timeslots(start_date="2021-01-01 05:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h6 = timeslots(start_date="2021-01-01 06:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h7 = timeslots(start_date="2021-01-01 07:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h8 = timeslots(start_date="2021-01-01 08:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h9 = timeslots(start_date="2021-01-01 09:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h10 = timeslots(start_date="2021-01-01 10:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h11 = timeslots(start_date="2021-01-01 11:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h12 = timeslots(start_date="2021-01-01 12:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h13 = timeslots(start_date="2021-01-01 13:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h14 = timeslots(start_date="2021-01-01 14:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h15 = timeslots(start_date="2021-01-01 15:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h16 = timeslots(start_date="2021-01-01 16:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h17 = timeslots(start_date="2021-01-01 17:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h18 = timeslots(start_date="2021-01-01 18:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h19 = timeslots(start_date="2021-01-01 19:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h20 = timeslots(start_date="2021-01-01 20:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h21 = timeslots(start_date="2021-01-01 21:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h22 = timeslots(start_date="2021-01-01 22:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h23 = timeslots(start_date="2021-01-01 23:00:00", end_date="2021-12-31 23:00:00", fre="D")

    a = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23]

    for i in range(len(a)):
        a[i] = hour(a[i], string, profile[string][i] * value)

    h = ver(h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22,
            h23)
    data = hor(data, h)

    return data


def seasonal(string, value):
    hh = []

    h0 = timeslots(start_date="2021-01-01 00:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h1 = timeslots(start_date="2021-01-01 01:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h2 = timeslots(start_date="2021-01-01 02:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h3 = timeslots(start_date="2021-01-01 03:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h4 = timeslots(start_date="2021-01-01 04:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h5 = timeslots(start_date="2021-01-01 05:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h6 = timeslots(start_date="2021-01-01 06:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h7 = timeslots(start_date="2021-01-01 07:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h8 = timeslots(start_date="2021-01-01 08:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h9 = timeslots(start_date="2021-01-01 09:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h10 = timeslots(start_date="2021-01-01 10:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h11 = timeslots(start_date="2021-01-01 11:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h12 = timeslots(start_date="2021-01-01 12:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h13 = timeslots(start_date="2021-01-01 13:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h14 = timeslots(start_date="2021-01-01 14:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h15 = timeslots(start_date="2021-01-01 15:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h16 = timeslots(start_date="2021-01-01 16:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h17 = timeslots(start_date="2021-01-01 17:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h18 = timeslots(start_date="2021-01-01 18:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h19 = timeslots(start_date="2021-01-01 19:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h20 = timeslots(start_date="2021-01-01 20:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h21 = timeslots(start_date="2021-01-01 21:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h22 = timeslots(start_date="2021-01-01 22:00:00", end_date="2021-12-31 23:00:00", fre="D")
    h23 = timeslots(start_date="2021-01-01 23:00:00", end_date="2021-12-31 23:00:00", fre="D")

    h = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23]

    for i in range(len(h)):
        ew = h[i].iloc[:31]
        ew = hour(ew, string, profile[string + "_w"][i] * value)
        # print(h0)
        s = h[i].iloc[31:166]
        s = hour(s, string, profile[string + "_s"][i] * value)

        # print(s)

        m = h[i].iloc[-(77 + 122):-(77)]
        m = hour(m, string, profile[string + "_m"][i] * value)

        lw = h[i].iloc[-77:]
        lw = hour(lw, string, profile[string + "_w"][i] * value)

        hh.append(ver(ew, s, m, lw))
        # h[i] = ver(ew, s, m, lw)

    hhh = hh[0]

    for i in range(1, len(hh)):
        hhh = ver(hhh, hh[i])
    # a = ver(h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23)
    data = hor(create(), hhh)

    return data


def weekly(string, value, freq="W-SUN"):
    w = []

    for i in range(24):
        if len(str(i)) == 1:
            h = timeslots(start_date="2021-01-01 0" + str(i) + ":00:00", end_date="2021-12-31 23:00:00", fre=freq)
            w.append(h)
            w[i] = hour(w[i], string, profile[string][i] * value)
            # print(w[i])

        else:
            h = timeslots(start_date="2021-01-01 " + str(i) + ":00:00", end_date="2021-12-31 23:00:00", fre=freq)
            w.append(h)
            w[i] = hour(w[i], string, profile[string][i] * value)

    ww = w[0]
    for i in range(1, len(w)):
        ww = ver(ww, w[i])

    data = hor(create(), ww)

    return data


def monthly(string, value, pre_start, start, month_value, end):
    w = []

    for i in range(24):
        if len(str(i)) == 1:
            h = timeslots(start_date=start + " 0" + str(i) + ":00:00", periods_int=month_value, fre="D")
            w.append(h)
            w[i] = hour(w[i], string, profile[string][i] * value)
        else:
            h = timeslots(start_date=start + " 0" + str(i) + ":00:00", periods_int=month_value, fre="D")
            w.append(h)
            w[i] = hour(w[i], string, profile[string][i] * value)
    if pre_start != "2020-01-31":
        e = timeslots(start_date="2021-01-01 00:00:00", end_date=pre_start + " 23:00:00", fre="H")
        e = hour(e, string, 0)
    else:
        e = pd.DataFrame()
    if end != "2021-12-31":
        extra = timeslots(start_date=end + " 00:00:00", end_date="2021-12-31 23:00:00", fre="H")
        extra = hour(extra, string, 0)
    else:
        extra = pd.DataFrame()

    ww = extra
    ww = ver(ww, e)
    for i in range(0, len(w)):
        ww = ver(ww, w[i])

    # print(ww)
    return hor(create(), ww)


def final_csv(file_name, col_name, files_path="/run/media/dixit/D8_HD/D/Study/Sem_3/DE/data/"):
    if os.path.exists(os.path.join(files_path, file_name)) is True:
        data = pd.read_csv(os.path.join(files_path, file_name), index_col=col_name)
        x = []
        y = []
        for i in list(data.index):
            i = i.lower()
            x.append(i[:3])
        for i in list(data.columns):
            y.append(i.lower())
        data.index = x
        data.columns = y
        data.index.name = col_name
        data.to_csv(os.path.join(files_path, "x.csv"), index=col_name)
        data = pd.read_csv(os.path.join(files_path, "x.csv"), index_col=col_name)
        return print(data)


def s(a):
    return a["u"] + a["m"] + a["l"]

# summer : s
# winter : w
# monsoon : m
