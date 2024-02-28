# NLGeoCities

NLGeoCities is a dataset containing latitude and longitude coordinates for cities in the Netherlands.

## Overview

NLGeoCities provides geographical coordinates for various cities across the Netherlands. This dataset is useful for a wide range of applications, including geographic visualizations, location-based services, and spatial analysis.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Installation

You can install NLGeoCities via pip:

```python
  pip install nl-ego-cities
```

pypi page link is here:   
(https://pypi.org/project/nl-ego-cities/)    

The documentation for NLGeoCities can be found here:      
[Document](https://nlgeocities.readthedocs.io/en/latest/)   

## Quick Start

### Get City Coordinates JSON File from NLGeoCities

To get started, you can obtain a JSON file containing city coordinates from NLGeoCities. Here's how to do it in Python:

```python
  from nl_ego_cities import city_coords

  # Get the JSON file
  cities = city_coords.city_json

  # Access city coordinates
  amsterdam_coords = cities["amsterdam"]
  print(f"Coordinates of Amsterdam: latitude: {amsterdam_coords['lat']}, longitude: {amsterdam_coords['lon']}")
```

### Processing DataFrame with get_lat_lon Function

If you have a DataFrame and want to add latitude and longitude columns using NLGeoCities, you can use the get_lat_lon function. Here's how to do it:

```python
  from nl_ego_cities.load_city_data import get_lat_lon

  # Assuming 'df' is your DataFrame with a 'city' column
  df['city_lat'], df['city_lon'] = get_lat_lon(df, 'city')
```

Note: The keys in the JSON file are lowercase.   

## JSON Data Structure
The JSON file obtained from NLGeoCities follows this structure:   

```json
  {
    "amsterdam": {
      "lat": 52.3676,
      "lon": 4.9041
    },
    "rotterdam": {
      "lat": 51.9225,
      "lon": 4.4792
    },
    ...
  }
```