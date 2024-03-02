#validates a csv of external geodata sources by calling a head request to each API
import pandas as pd
import requests

#csv I used is encoded using 'windows-1252' - change encoding type if required
df = pd.read_csv('geodata_external_data.csv', encoding='windows-1252')

df_select = df[df['category'] == 'Service']

service_urls = df_select['url'].to_list()

def url_response_code(url):
    try:
        r = requests.head(url)
        return print("{} status code: {}".format(url, r.status_code))
    except requests.exceptions.RequestException as e:
        print('{} request failed: {}'.format(url, e))

for url in service_urls:
    url_response_code(url)
