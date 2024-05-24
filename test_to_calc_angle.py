import unittest
from remove_spikes import calculate_angle

class TestCalculateAngle(unittest.TestCase):

    def test_calculate_angle(self):
        # Test case 2: Obtuse angle
        angle = calculate_angle((0, 0), (0, 1), (-1, 1))
        # The expected angle for an obtuse angle might be 135 degrees
        self.assertAlmostEqual(angle, 135, delta=0.001)

if __name__ == '__main__':
    unittest.main()
