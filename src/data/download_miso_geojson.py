from pathlib import Path

from src.data.utils import DataDownloader

dst_miso = Path('data/external/geojson/miso')

# MISO GeoJson from FERC GeoService
# https://hifld-geoplatform.opendata.arcgis.com/datasets/9d1099b016e5482c900d657f06f3ac80_0/geoservice
url_miso = 'https://services1.arcgis.com/Hp6G80Pky0om7QvQ/arcgis/rest/services/Independent_System_Operators/FeatureServer/0/query?where=NAME%3D%27MIDCONTINENT+INDEPENDENT+TRANSMISSION+SYSTEM+OPERATOR%2C+INC..%27'
params_miso = {
          'geometryType': 'esriGeometryEnvelope',
          'spatialRel': 'esriSpatialRelIntersects',
          'resultType': 'none',
          'distance': '0.0',
          'units': 'esriSRUnit_Meter',
          'returnGeodetic': 'false',
          'outFields': '*',
          'returnGeometry': 'true',
          'returnCentroid': 'false',
          'featureEncoding': 'esriDefault',
          'multipatchOption': 'xyFootprint',
          'applyVCSProjection': 'false',
          'returnIdsOnly': 'false',
          'returnUniqueIdsOnly': 'false',
          'returnCountOnly': 'false',
          'returnExtentOnly': 'false',
          'returnQueryGeometry': 'false',
          'returnDistinctValues': 'false',
          'cacheHint': 'false',
          'returnZ': 'false',
          'returnM': 'false',
          'returnExceededLimitFeatures': 'true',
          'sqlFormat': 'none',
          'f': 'pgeojson'
          }

# miso = DataDownloader(url_miso, dst_miso, payload=params_miso)
# miso.write('miso.geojson')

desc_url = 'https://www.arcgis.com/sharing/rest/content/items/9d1099b016e5482c900d657f06f3ac80/info/metadata/metadata.xml?format=default&output=html'
lic = """None (Public Use). Users are advised to read the data set's
metadata thoroughly to understand appropriate use and data limitations."""


