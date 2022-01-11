import pandas as pd
import ozpy as oz
import os
import matplotlib.pyplot as plt

file_path = "/run/media/dixit/D8_HD/D/Study/Sem_3/DE/Oz_Py/make_up_demand/"

profile = pd.read_csv(os.path.join(file_path, "profile.csv"), index_col="time")


mobile = oz.fixed("mobile", 4208) # 8146 wh
com_pump = oz.fixed("com_pump", 10700)
mor_st_bulb = oz.fixed("mor_st_bulb", 3520)
mor_st_wm = oz.fixed("mor_st_wm", 7700)

data = oz.hor(oz.create(), mobile, com_pump, mor_st_wm, mor_st_bulb)

kit_ref = oz.fixed("kit_ref", 144850)
kit_tube = oz.fixed("kit_tube", 3564)
kit_bulb = oz.fixed("kit_bulb", 2387)
kit_fm = oz.fixed("kit_fm", 16500)
kit_wp = oz.fixed("kit_wp",6250)

data = oz.hor(data, kit_wp, kit_fm, kit_bulb, kit_tube, kit_ref)

li_tube = oz.fixed("li_tube", 4752)
li_bulb = oz.fixed("li_bulb", 2276)

room_tube = oz.fixed("room_tube", 792)
room_bulb = oz.fixed("room_bulb", 1060)

data = oz.hor(data, li_bulb, li_bulb, room_tube, room_bulb)

temple = oz.fixed("temple", 620)
ms_ref = oz.fixed("ms_ref", 33000)
ms_others = oz.fixed("ms_others",231)
street_light = oz.fixed("street_light", 1600)
telecom_tower = oz.fixed("telecom_tower", 4500)
shop_bulb = oz.fixed("shop_bulb", 42)
shop_ref = oz.fixed("shop_ref", 2000)
shop_fm = oz.fixed("shop_fm", 5000)
shop_tm = oz.fixed("shop_tm", 150)


data = oz.hor(data, temple, ms_ref, ms_others, street_light, telecom_tower, shop_bulb, shop_ref, shop_fm, shop_tm)

#seasonal variation
hh_pump = oz.seasonal("hh_pump", 33800)
ms_heater = oz.seasonal("ms_heater", 99000)
ki_fan = oz.seasonal("ki_fan", 10875)
li_fan = oz.seasonal("li_fan", 33825*.85)
li_ac = oz.seasonal("li_ac", 44000)
room_fan = oz.seasonal("room_fan", 51975)
shop_fan = oz.seasonal("shop_fan", 216)
 # = oz.seasonal("", )
 # = oz.seasonal("", )

data = oz.hor(data, hh_pump, ms_heater, ki_fan, li_fan, li_ac, room_fan, shop_fan)


### monthly variation
agri_pump_jan_erly = oz.monthly("agri_pump_jan_erly", 2200, "2020-12-31","2021-01-01", 15, "2021-01-16")
agri_pump_jan_late = oz.monthly("agri_pump_jan_late", 2200, "2020-01-15", "2021-01-16", 16, "2021-02-01")
agri_pump_feb = oz.monthly("agri_pump_feb", 2200, "2021-01-31", "2021-02-01", 28, "2021-03-01")
agri_pump_mar = oz.monthly("agri_pump_mar", 2200, "2021-02-28", "2021-03-01", 31, "2021-04-01")
agri_pump_apr = oz.monthly("agri_pump_apr", 2200, "2021-03-31", "2021-04-01", 30, "2021-05-01")
agri_pump_may = oz.monthly("agri_pump_may", 2200, "2021-04-30", "2021-05-01", 31, "2021-06-01")
agri_pump_jun = oz.monthly("agri_pump_jun", 2200, "2021-05-31", "2021-06-01", 30, "2021-07-01")
agri_pump_jul_erly = oz.monthly("agri_pump_jul_erly", 2200, "2021-06-30", "2021-07-01", 15, "2021-07-16")
agri_pump_jul_late = oz.monthly("agri_pump_jul_late", 2200,"2021-07-15", "2021-07-16", 16, "2021-08-01")
agri_pump_aug = oz.monthly("agri_pump_aug", 2200,"2021-07-31", "2021-08-01", 31, "2021-09-01")
agri_pump_sup = oz.monthly("agri_pump_sup", 2200,"2021-08-31", "2021-09-01", 30, "2021-10-01")
agri_pump_oct = oz.monthly("agri_pump_oct", 2200,"2021-09-30", "2021-10-01", 31, "2021-11-01")
agri_pump_nov = oz.monthly("agri_pump_nov", 2200,"2021-10-31", "2021-11-01", 30, "2021-12-01")
agri_pump_dec = oz.monthly("agri_pump_dec", 2200,"2021-11-30", "2021-12-01", 31, "2021-12-31")

data = oz.hor(data, agri_pump_jan_erly, agri_pump_jan_late, agri_pump_feb,agri_pump_mar, agri_pump_apr, agri_pump_may, agri_pump_jun, agri_pump_jul_erly, agri_pump_jul_late, agri_pump_aug, agri_pump_sup, agri_pump_oct, agri_pump_nov, agri_pump_dec)

#weekly variation school
school_fan_M_Su = oz.fixed("school_fan_M_Su", 750)
school_tube_M_Su = oz.fixed("school_tube_M_Su", 360)
school_com_M_Su = oz.fixed("school_com_M_Su", 120)
school_tv_M_Su = oz.fixed("school_tv_M_Su", 300)
school_sat = oz.weekly("school_sat", -1350, freq="W-SAT")
school_sun = oz.weekly("school_sun", -1350, freq="W-SUN")
 # = oz.fixed("", )
 # = oz.fixed("", )

data = oz.hor(data, school_tv_M_Su, school_com_M_Su, school_tube_M_Su, school_fan_M_Su, school_sun, school_sat)

#weekly variation post_office and panchayat_office

pa_off_mon_sun = oz.fixed("pa_off_mon_sun", 201)
pa_off_sat = oz.weekly("pa_off_sat", -201, freq="W-SAT")
pa_off_sun = oz.weekly("pa_off_sun", -201, freq="W-SUN")

data = oz.hor(data,pa_off_mon_sun, pa_off_sat, pa_off_sun)

po_off_mon_sun = oz.fixed("po_off_mon_sun", 85)
po_off_sat = oz.weekly("po_off_sat", -85, freq="W-SAT")
po_off_sun = oz.weekly("po_off_sun", -85, freq="W-SUN")

data = oz.hor(data, po_off_mon_sun, po_off_sat, po_off_sun)



#weekly variation in TV

li_tv_sun = oz.weekly("li_tv_sun", 16405, freq="W-SUN")
li_tv_mon = oz.weekly("li_tv_mon", 16405, freq="W-MON")
li_tv_tue = oz.weekly("li_tv_tue", 16405, freq="W-TUE")
li_tv_wed = oz.weekly("li_tv_wed", 16405, freq="W-WED")
li_tv_thu = oz.weekly("li_tv_thu", 16405, freq="W-THU")
li_tv_fri = oz.weekly("li_tv_fri", 16405, freq="W-FRI")
li_tv_sat = oz.weekly("li_tv_sat", 16405, freq="W-SAT")

data = oz.hor(data, li_tv_sun, li_tv_mon, li_tv_tue, li_tv_wed, li_tv_thu, li_tv_fri, li_tv_sat)

# hourly demand
demand = data.sum(axis=1)

# demand profile wise
demand_data_eq = data.sum(axis=0)
demand_data_eq.index.name = "equipment"


data.to_csv(os.path.join(file_path,"oz_demand_data.csv"))
demand.to_csv(os.path.join(file_path, "oz_demand.csv"))
demand_data_eq.to_csv(os.path.join(file_path, "oz_demand_eq.csv"))
