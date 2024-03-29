import numpy as np
import pickle
import io

data_type = np.dtype([('productId', np.int32), ('price', np.float64)])
product_table = np.array([
    (1, 10.0),
    (2, 12.4),
    (3, 33.33),
    (4, 55),
], dtype=data_type)

print(product_table['productId'])
print(product_table[0])
print(product_table['price'][2])

# ----------------------------

file_content = """Chicago Sun 01:52
Columbus Sun 02:52
Riyadh  Sun 10:52
Copenhagen  Sun 08:52
Kuwait City Sun 10:52
Rome    Sun 08:52
Dallas  Sun 01:52
Salt Lake City  Sun 01:52
San Francisco Sun 00:52
Amsterdam Sun 08:52
Denver Sun 01:52
San Salvador Sun 01:52
Detroit Sun 02:52
Las Vegas Sun 00:52
Santiago    Sun 04:52
Anchorage Sat 23:52
Ankara Sun 10:52
Lisbon  Sun 07:52
São Paulo   Sun 05:52
Dubai   Sun 11:52
London  Sun 07:52
Seattle Sun 00:52
Dublin  Sun 07:52
Los Angeles Sun 00:52
Athens  Sun 09:52
Edmonton Sun 01:52
Madrid  Sun 08:52
Shanghai Sun 15:52
Atlanta Sun 02:52
Frankfurt   Sun 08:52
Singapore Sun 15:52
Auckland Sun 20:52
Halifax Sun 03:52
Melbourne Sun 18:52
Stockholm   Sun 08:52
Barcelona   Sun 08:52
Miami   Sun 02:52
Minneapolis Sun 01:52
Sydney Sun 18:52
Beirut  Sun 09:52
Helsinki    Sun 09:52
Montreal    Sun 02:52
Berlin  Sun 08:52
Houston Sun 01:52
Moscow  Sun 10:52
Indianapolis    Sun 02:52   
Boston  Sun 02:52
Tokyo   Sun 16:52
Brasilia Sun 05:52
Istanbul Sun 10:52
Toronto Sun 02:52
Vancouver   Sun 00:52
Brussels    Sun 08:52
Jerusalem   Sun 09:52
New Orleans Sun 01:52
Vienna  Sun 08:52
Bucharest   Sun 09:52
Johannesburg    Sun 09:52
New York    Sun 02:52
Warsaw  Sun 08:52
Budapest    Sun 08:52
Oslo    Sun 08:52
Washington DC   Sun 02:52
Ottawa  Sun 02:52
Winnipeg    Sun 01:52
Cairo   Sun 09:52
Paris   Sun 08:52
Calgary Sun 01:52
Kathmandu   Sun 13:37
Philadelphia    Sun 02:52
Zurich  Sun 08:52
Cape Town   Sun 09:52
Phoenix Sun 00:52       
Prague  Sun 08:52       
Casablanca  Sun 07:52
Reykjavik   Sun 07:52"""

data = []
for line in file_content.split('\n'):
    words = line.strip().split(' ')
    time = tuple(map(int, words[-1].split(":")))
    day = words[-2]
    city_name = ' '.join(words[:-2]).strip()
    data.append((city_name, day, time))


with open('cities_and_times.pkl', 'wb') as file:
    pickle.dump(data, file)

cities_and_times_table_datatype = np.dtype([('name', str, 20), ('day', str, 3), ('time', [('h', int), ('min', int)])])

with open('cities_and_times.pkl', 'rb') as file:
    cities_and_times_data = pickle.load(file)
    table = np.array(cities_and_times_data, dtype=cities_and_times_table_datatype)

print(table[0])
print(table[0]['name'])
print(table[0]['time']['h'])
