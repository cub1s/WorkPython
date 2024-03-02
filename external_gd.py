#this script takes a csv of external geodata sources from EOR PostGIS database and makes it into a XML loadable format in QGIS
import pandas as pd
import xml.etree.ElementTree as ET

#csv I used is encoded using 'windows-1252' - change encoding type if required
df = pd.read_csv('geodata_external_data.csv', encoding='windows-1252')

df_select = df[df['category'] == 'Service']

service_urls = df_select['url'].to_list()
service_names = df_select['name'].to_list()
url_name_dict = {service_names[i]: service_urls[i] for i in range(len(service_names))}

print('{} external data services found.'.format(len(service_names)))

a = ET.Element('qgsARCGISFEATURESERVERConnections', {'version': "1.0"})
for i, j in url_name_dict.items():
    b = ET.SubElement(a, 'arcgisfeatureserver', {'http-header:referer': '', 'authcfg': '',
                    'password': '', 'name': i, 'url': j, 
                    'username': '', 'referer': ''})

with open('geodata_external_data.xml', 'wb') as f:
    f.write('<!DOCTYPE connections>'.encode('utf-8'))
    ET.ElementTree(a).write(f, 'utf-8')