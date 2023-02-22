import requests
import json

url = "https://api.bls.gov/publicAPI/v2/timeseries/data/CES0000000001"

headers = {'Content-type': 'application/json'}
data = '{"seriesid":["CES0000000001"],"startyear":"2022", "endyear":"2022", "registrationkey":"API-KEY"}'

response = requests.post(url, headers=headers, data=data)

# check if response was successful
if response.status_code == 200:
    # parse response JSON
    response_json = json.loads(response.content)

    # print the results to the console
    for series in response_json['Results']['series']:
        series_id = series['seriesID']
        for datum in series['data']:
            year = datum['year']
            period = datum['period']
            value = datum['value']
            print(f"{series_id}\t{year}-{period}\t{value}")
else:
    print("Error:", response.status_code)
