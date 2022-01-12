import matplotlib.pyplot as plt
import pandas as pd
import solar



# plt.hist(solar.daily_solar.iloc[:, 1], bins=30)
plt.hist(solar.hourly_solar.iloc[:, 1], bins=30)
plt.show()