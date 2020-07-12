from pathlib import Path

import pickle

import geopandas as gpd

miso_states = {
    'Arkansas': 'AR',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Manitoba': 'MB',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'North Dakota': 'ND',
    'Texas': 'TX',
    'South Dakota': 'SD',
    'Wisconsin': 'WI'
}

# Drop turbines outside MISO states
uswtdb_fn = Path('data/external/geojson/uswtdb/uswtdb_v3_0_1_20200514.geojson')
assert uswtdb_fn.exists()

uswtdb = gpd.read_file(uswtdb_fn, driver='GeoJSON')
miso_uswtdb = uswtdb.loc[uswtdb.t_state.isin(miso_states.values()), :]

# Drop polygons not in contiguous states
usa_fn = Path('data/external/shapefile/nws_usa_states/s_11au16.shp')
assert usa_fn.exists()

usa = gpd.read_file(usa_fn)
not_cont = ['Alaska', 'Puerto Rico', 'Northern Marianas',
            'Virgin Islands', 'Guam', 'American Samoa', 'Hawaii']
cont_usa = usa.loc[~usa.NAME.isin(not_cont), :]

# Drop bad LON on Maryland (Maryland appears twice in this shapefile)
cont_usa = cont_usa.loc[cont_usa.LON != 0, :]

# Convert to WGS84 from NAD83
cont_usa = cont_usa.to_crs('EPSG:4326')

# Save processed files
dst = Path('data/raw/contiguous_usa')
if not dst.exists():
    dst.mkdir(parents=True)

with open(dst/'cont_usa.pickle', 'wb') as f:
    pickle.dump(cont_usa, f, pickle.HIGHEST_PROTOCOL)

with open(dst/'miso_uswtdb.pickle', 'wb') as f:
    pickle.dump(miso_uswtdb, f, pickle.HIGHEST_PROTOCOL)
