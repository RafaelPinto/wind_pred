from pathlib import Path

from src.data.utils import DataDownloader

dst = Path('data/external/shapefile/nws_usa_states')

# https://www.weather.gov/gis/USStates
url = 'https://www.weather.gov/source/gis/Shapefiles/County/s_11au16.zip'

descr_url = 'https://eerscmap.usgs.gov/uswtdb/assets/data/uswtdb_v3_0_1_20200514.xml'

lic = """Map services and data downloaded from the U.S. Wind Turbine
Database are free and in the public domain. There are no restrictions; however,
we request that the following acknowledgment statement be included in products
and data derived from our map services when citing, copying, or reprinting:
"Map services and data are available from U.S. Wind Turbine Database, provided
by the U.S. Geological Survey, American Wind Energy Association, and Lawrence
Berkeley National Laboratory via https://eerscmap.usgs.gov/uswtdb"."""

data = DataDownloader(url,
                      dst,
                      zipped=True,
                      descr_url=descr_url,
                      lic=lic)

data.get_descr_url()
data.write('description', 'README.xml')

data.write('license', 'LICENSE.txt')

data.get_url()
data.write('data')
