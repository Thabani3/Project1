import math
import geopandas as gpd
from shapely.geometry import Polygon


def calculate_angle(p1, p2, p3):
    """
    Calculate the angle between three points (p1, p2, p3) in degrees.

    Args:
        p1 (tuple): Coordinates of the first point (x, y).
        p2 (tuple): Coordinates of the second point (x, y).
        p3 (tuple): Coordinates of the third point (x, y).

    Returns:
        float: Angle between the three points in degrees.
    """
    angle_rad = math.atan2(p3[1] - p2[1], p3[0] - p2[0]) - \
        math.atan2(p1[1] - p2[1], p1[0] - p2[0])
    angle_deg = math.degrees((angle_rad + 360) % 360)
    return angle_deg


def remove_spikes(polygon):
    """
    Remove spikes from a polygon geometry.

    Args:
        polygon (Polygon): Input polygon geometry.

    Returns:
        Polygon: Polygon geometry with spikes removed.
    """
    # Define a threshold angle for identifying spikes
    threshold_angle = 160  # Adjust as needed based on your data

    # Extract the exterior coordinates of the polygon
    coords = list(polygon.exterior.coords)

    # Initialize a list to store the filtered coordinates
    filtered_coords = []

    # Iterate through the coordinates
    for i in range(len(coords)):
        # Get three consecutive vertices
        p1 = coords[i - 1]
        p2 = coords[i]
        p3 = coords[(i + 1) % len(coords)]  # Wrap around for the last vertex

        # Calculate the angles between consecutive edges
        angle = calculate_angle(p1, p2, p3)

        # Check if the angle is below the threshold
        if angle > threshold_angle:
            filtered_coords.append(p2)

    # Check if there are enough points to form a valid polygon
    if len(filtered_coords) >= 3:
        # Create a new polygon with the filtered coordinates
        return Polygon(filtered_coords)
    else:
        # If not enough points, return an empty polygon
        return Polygon()


def remove_spikes_from_geodataframe(gdf):
    """
    Remove spikes from polygons in a GeoDataFrame.

    Args:
        gdf (GeoDataFrame): Input GeoDataFrame containing polygons.

    Returns:
        GeoDataFrame: GeoDataFrame with spikes removed from polygons.
    """
    # Apply the remove_spikes function to each polygon geometry
    gdf['geometry'] = gdf['geometry'].apply(remove_spikes)
    
    return gdf


if __name__ == "__main__":
    # Read the input GeoPackage file
    input_file = "spiky-polygons.gpkg"
    gdf = gpd.read_file(input_file)

    # Remove spikes from polygons in the GeoDataFrame
    gdf = remove_spikes_from_geodataframe(gdf)

    # Write the modified GeoDataFrame to a new GeoPackage file
    output_file = "output.gpkg"
    gdf.to_file(output_file, driver='GPKG')
