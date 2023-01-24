# To download MODIS data from the NASA Earthdata Search portal (https://search.earthdata.nasa.gov/search) using Python, you can use the requests library to make HTTP requests to the portal's API and the json library to parse the JSON response.

# Here's an example script that shows how to search for MODIS data products and download the URLs of the data files:


import requests
import json

# Set the parameters for the API call
search_url = 'https://search.earthdata.nasa.gov/search'
params = {'q': 'MODIS', 'format': 'json'}

# Make the API call and parse the JSON response
response = requests.get(search_url, params=params)
data = json.loads(response.text)

# Print the URLs of the data files
for item in data['feed']['entry']:
    print(item['link'][0]['href'])
# This script will search for all MODIS data products in the JSON format and print the URLs of the data files.
# You can then use these URLs to download the data files using the requests library or other libraries such as urllib or wget.

# If you need to filter your search by date, you can use the begin_date and end_date parameters.


params = {'q': 'MODIS', 'format': 'json', 'begin_date': '2022-01-01', 'end_date': '2022-12-31'}

# This will only return the records that match with the specified dates.

# Remember to add the http or https to the links before download

# Please let me know if you have any further questions or need help with anything else.


# You can filter the search results for specific MODIS products by including the product's short name in the q parameter of the API call.
# For example, you can use "MOD13Q1" to search for the "MODIS/Terra Vegetation Indices 16-Day L3 Global 250m SIN Grid V006" product.

# Here's an example script that shows how to search for a specific MODIS product and download the URLs of the data files:


import requests
import json

# Set the parameters for the API call
search_url = 'https://search.earthdata.nasa.gov/search'
params = {'q': 'MOD13Q1', 'format': 'json'}

# Make the API call and parse the JSON response
response = requests.get(search_url, params=params)
data = json.loads(response.text)

# Print the URLs of the data files
for item in data['feed']['entry']:
    print(item['link'][0]['href'])
# This script will search for the MOD13Q1 product in the JSON format and print the URLs of the data files.

# You can also use the product parameter to filter the results, for example:


params = {'q': 'MODIS', 'format': 'json', 'product': 'MOD13Q1'}
# You can find the short names of other MODIS products on the NASA Earthdata Search portal by searching for "MODIS" and then looking at the "Short Name" field of the product's metadata.

# Keep in mind that the API returns a maximum of 1000 records per request

# you can filter the search results for specific MODIS tiles by including the tile's horizontal and vertical coordinates in the q parameter of the API call.
# For example, you can use "h10v05" to search for the tile at horizontal coordinate 10 and vertical coordinate 5.

# Here's an example script that shows how to search for a specific MODIS tile and download the URLs of the data files:


import requests
import json

# Set the parameters for the API call
search_url = 'https://search.earthdata.nasa.gov/search'
params = {'q': 'MOD13Q1+AND+h10v05', 'format': 'json'}

# Make the API call and parse the JSON response
response = requests.get(search_url, params=params)
data = json.loads(response.text)

# Print the URLs of the data files
for item in data['feed']['entry']:
    print(item['link'][0]['href'])
# This script will search for the MOD13Q1 product in the JSON format and the tile h10v05 and print the URLs of the data files.

# You can also use the tile parameter to filter the results, for example:


params = {'q': 'MODIS', 'format': 'json', 'tile': 'h10v05'}
# Keep in mind that some tiles may not have data available for certain dates or products, you can use the date range and product filter to ensure that you are retrieving the data you need.










# you can combine all the parameters in one script to filter the search results by date, MODIS product, and tile, and download the URLs of the data files.
# Here's an example script that shows how to do this:

import requests
import json

# Set the parameters for the API call
search_url = 'https://search.earthdata.nasa.gov/search'
params = {'q': 'MOD13Q1+AND+h10v05+AND+begin_date:2022-01-01+AND+end_date:2022-12-31', 'format': 'json'}

# Make the API call and parse the JSON response
response = requests.get(search_url, params=params)
data = json.loads(response.text)

# Print the URLs of the data files
for item in data['feed']['entry']:
    print(item['link'][0]['href'])
# This script will search for the MOD13Q1 product in the JSON format, the tile h10v05 and the date range from 2022-01-01 to 2022-12-31 and print the URLs of the data files.

# You can then use these URLs to download the data files using the requests library or other libraries such as urllib or wget.

# You can also use the product, tile, begin_date and end_date parameters to filter the results, for example:

params = {'q': 'MODIS', 'format': 'json', 'product': 'MOD13Q1', 'tile': 'h10v05', 'begin_date': '2022-01-01', 'end_date': '2022-12-31'}
# Keep in mind that the API returns a maximum of 1000 records per request, so you may need to use the start parameter to retrieve all records if your search returns more than 1000 records.


# example of how to download the data files using the urllib library:

import urllib.request

for item in data['feed']['entry']:
    url = item['link'][0]['href']
    filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, filename)
# This script will iterate over the URLs of the data files obtained from the search, and use the urllib.request.urlretrieve() function to download each file. The first argument is the URL of the file and the second one is the name of the file to be saved in the local directory.

# You can also use the wget library to download the files by running the command !pip install wget in your command line or terminal and then:


import wget

for item in data['feed']['entry']:
    url = item['link'][0]['href']
    wget.download(url)
# This script will iterate over the URLs of the data files obtained from the search, and use the wget.download() function to download each file.


# here's an example of how to download the data files using the urllib library:

import urllib.request

for item in data['feed']['entry']:
    url = item['link'][0]['href']
    filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, filename)
# This script will iterate over the URLs of the data files obtained from the search, and use the urllib.request.urlretrieve() function to download each file. The first argument is the URL of the file and the second one is the name of the file to be saved in the local directory.

# You can also use the wget library to download the files by running the command !pip install wget in your command line or terminal and then:

import wget

for item in data['feed']['entry']:
    url = item['link'][0]['href']
    wget.download(url)
# This script will iterate over the URLs of the data files obtained from the search, and use the wget.download() function to download each file.

# Keep in mind that the data files can be very large and the download may take a long time, it is recommended to use the tqdm library to show a progress bar while the files are downloading.

# The tqdm library can be used to show a progress bar while the files are downloading. Here's an example of how to use it with the urllib library:

from tqdm import tqdm

for item in tqdm(data['feed']['entry']):
    url = item['link'][0]['href']
    filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, filename, reporthook=tqdm.update_to)
# You can also use tqdm when using the wget library like this:

from tqdm import tqdm

for item in tqdm(data['feed']['entry']):
    url = item['link'][0]['href']
    filename = url.split('/')[-1]
    wget.download(url, bar=tqdm)
# This script will iterate over the URLs of the data files obtained from the search, and use the urllib.request.urlretrieve() or wget.download() functions to download each file, while tqdm will show a progress bar to indicate the progress of the download.

# The reporthook parameter passed to urllib.request.urlretrieve() function is used to update the progress bar, and the bar parameter passed to wget.download() function is used to display the progress bar.





