"""
GET: data muncul jika url dijalankan lewat browser
POST: data tidak bisa diambil lewat browser, namun hanya bisa diambil berdasar permintaan dengan metode post dari form
"""

import requests
import json
import pprint

# Coba jalankan get dari link
try:
    result = requests.get('https://www.idx.co.id/umbraco/Surface/Helper/GetStockChart?indexCode=SRTG&period=1W')
    if result.status_code == 200:
        # print(result.status_code)
        # print(result.text)
        data = json.loads(result.text)
        chart_data = data['ChartData']
        # pprint.pprint(data)
        print(data['ChartData'])

        f = open('data.csv', 'w')
        f.write('#Tanggal;Value\n')

        for d in chart_data:
            tanggal = d['Date']
            value = d['Close']
            print(tanggal, ';', value)
            f.write('{};{}\n'.format(tanggal, value))
        f.close()

# Jika connection error maka....
except Exception as ex:
    print(ex)
