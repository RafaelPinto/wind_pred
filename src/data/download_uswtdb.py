from pathlib import Path

from src.data.utils import DataDownloader

dst_uswtdb = Path('data/external/geojson/uswtdb')

# Info: https://eerscmap.usgs.gov/uswtdb/data/
# https://eerscmap.usgs.gov/uswtdb/api-doc/
url_uswtdb = 'https://eerscmap.usgs.gov/uswtdb/assets/data/uswtdbGeoJSON.zip'

uswtdb = DataDownloader(url_uswtdb, dst_uswtdb, zipped=True)
uswtdb.write()

desc_url = 'https://www.weather.gov/gis/StateMetadata'
lic = """None. See https://www.noaa.gov/organization/information-technology/freedom-of-information-act"""
