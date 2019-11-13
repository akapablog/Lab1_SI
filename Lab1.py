#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests as r

currency_pound = 'GBP'
currency_yen = 'JPY'
date_start = '2019-10-01'
date_end = '2019-10-31'


# 1
def get_currency(currency, date_from, date_to):
    url = "http://api.nbp.pl/api/exchangerates/rates/A/" + currency + "/" + date_from + "/" + date_to + "/"
    currency_req = r.get(url)
    currency_data = currency_req.json()
    return currency_data['rates']


# 2
rate_pound = get_currency(currency_pound, date_start, date_end)
rate_yen = get_currency(currency_yen, date_start, date_end)

# 3
dataframe_pound = pd.DataFrame.from_dict(rate_pound).head(5)
dataframe_yen = pd.DataFrame.from_dict(rate_yen).head(5)

plot_data_pound = dataframe_pound.set_index(['effectiveDate'])['mid']
plot_data_yen = dataframe_yen.set_index(['effectiveDate'])['mid']

# 4
correlation = np.corrcoef(plot_data_pound, plot_data_yen)[0][1]

# 5
plt.plot(plot_data_pound, 'r*-', plot_data_yen, 'b*-')
plt.ylim(ymin=0)
plt.title('Korelacja {} do {} = {}'.format(currency_pound, currency_yen, correlation))
plt.ylabel('PLN')
plt.xlabel('Data')
plt.legend([currency_pound, currency_yen], loc='lower right')
plt.show()
