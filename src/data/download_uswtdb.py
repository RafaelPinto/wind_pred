from pathlib import Path

from src.data.utils import DataDownloader

dst = Path('data/external/geojson/uswtdb')

# Info: https://eerscmap.usgs.gov/uswtdb/data/
# https://eerscmap.usgs.gov/uswtdb/api-doc/
url = 'https://eerscmap.usgs.gov/uswtdb/assets/data/uswtdbGeoJSON.zip'

descr_url = 'https://www.weather.gov/gis/StateMetadata'
lic = """None. See https://www.noaa.gov/organization/information-technology/freedom-of-information-act"""

data = DataDownloader(url,
                      dst,
                      zipped=True,
                      descr_url=descr_url,
                      lic=lic)

data.get_descr_url()
data.write('description', 'README.html')

data.write('license', 'LICENSE.txt')

data.get_url()
data.write('data')
