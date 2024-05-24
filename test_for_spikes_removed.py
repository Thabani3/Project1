import unittest
import geopandas as gpd
from shapely.geometry import Polygon
from remove_spikes import remove_spikes_from_geodataframe

class TestRemoveSpikes(unittest.TestCase):

    def setUp(self):
        # Create a GeoDataFrame with a polygon containing spikes
        self.spiky_polygon = Polygon([(0, 0), (0, 2), (1, 1), (2, 2), (2, 0)])
        self.gdf = gpd.GeoDataFrame(geometry=[self.spiky_polygon])

    def test_remove_spikes(self):
        # Apply remove_spikes_from_geodataframe function
        processed_gdf = remove_spikes_from_geodataframe(self.gdf)

        # Ensure that the resulting polygon has no more vertices than the original polygon
        original_polygon_vertices = len(self.spiky_polygon.exterior.coords)
        processed_polygon_vertices = len(processed_gdf['geometry'].iloc[0].exterior.coords)
        self.assertTrue(processed_polygon_vertices <= original_polygon_vertices,
                        "Processed polygon still contains spikes")

if __name__ == '__main__':
    unittest.main()
