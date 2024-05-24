import unittest
import geopandas as gpd
from shapely.geometry import Polygon
from remove_spikes import remove_spikes_from_geodataframe

class TestRemoveSpikesFromGeoDataFrame(unittest.TestCase):

    def test_remove_spikes_from_geodataframe(self):
        # Create a GeoDataFrame with polygons containing spikes
        poly1 = Polygon([(0, 0), (0, 2), (1, 1), (2, 2), (2, 0)])
        poly2 = Polygon([(1, 1), (1, 3), (2, 2), (3, 3), (3, 1)])
        gdf = gpd.GeoDataFrame(geometry=[poly1, poly2])

        # Apply remove_spikes_from_geodataframe function
        processed_gdf = remove_spikes_from_geodataframe(gdf)

        # Ensure that the resulting polygons have no spikes
        for geometry in processed_gdf['geometry']:
            # Count the number of vertices in the polygon
            num_vertices = len(geometry.exterior.coords)
            # The processed polygon should have less than or equal to the original number of vertices
            self.assertTrue(num_vertices <= 4,
                            "Processed polygon still contains spikes")

if __name__ == '__main__':
    unittest.main()
