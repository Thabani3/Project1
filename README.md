# Project1

# Spike Removal Tool

## Overview

The Spike Removal Tool is a Python utility for removing spikes from polygons in GeoDataFrames. It provides a simple and efficient way to process geospatial data, particularly useful for GIS applications and spatial analysis.

## Installation

To use this tool, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/Thabani3/Project1.git
    ```

2. Navigate to the project directory:
    ```
    cd spike-removal-tool
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

Removing Spikes
python
Copy code
import geopandas as gpd

# Read input GeoPackage file
input_file = "spiky_polygons.gpkg"
gdf = gpd.read_file(input_file)

# Remove spikes from polygons
processed_gdf = remove_spikes_from_geodataframe(gdf)

# Save modified GeoDataFrame to a new GeoPackage file
output_file = "output.gpkg"
processed_gdf.to_file(output_file, driver='GPKG')
















System diagram
  +------------------+
  |       User       |
  +--------+---------+
           |
           v
  +------------------+
  | Local Environment|
  |  - Python        |
  |  - Dependencies  |
  +--------+---------+
           |
           v
  +------------------+             +------------------+
  | remove_spikes.py |<----------->|     Shapely      |
  |  - GeoPandas     |             |  (Geometric Ops) |
  +--------+---------+             +--------+---------+
           |                                ^
           v                                |
  +------------------+             +--------+---------+
  | Input GeoPackage |             |  GeoPandas       |
  |  (spiky_polygons)|             |  (Read/Write     |
  +--------+---------+             |   GeoDataFrames) |
           |
           v
  +------------------+
  | Output GeoPackage|
  |  (output.gpkg)   |
  +------------------+

  +------------------+
  | GitHub Repository|
  |  - Source Code   |
  |  - Tests         |
  |  - CI Workflow   |
  +--------+---------+
           |
           v
  +------------------+
  | GitHub Actions   |
  |  - Checkout Code |
  |  - Setup Python  |
  |  - Install Deps  |
  |  - Lint with Flake8|
  |  - Run Tests     |
  +------------------+


