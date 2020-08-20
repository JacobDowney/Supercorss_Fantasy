import unittest
import moto_scraper

class GetCurrentStandingsTest(unittest.TestCase):

    def test_types(self):
        """
        Test that every rider has the correct type for each variable
        """
        standings = moto_scraper.GetCurrentStandings()
        for rider in standings:
            self.assertIsInstance(rider.get_name(), str)
            self.assertIsInstance(rider.get_number(), int)
            self.assertIsInstance(rider.get_poition(), int)
            self.assertIsInstance(rider.get_laps(), int)
            self.assertIsInstance(rider.get_gap(), float)
            self.assertIsInstance(rider.get_diff(), float)
            self.assertIsInstance(rider.get_last(), float)
            self.assertIsInstance(rider.get_best(), float)
            self.assertIsInstance(rider.get_in(), int)
            self.assertIsInstance(rider.get_active(), bool)

if __name__ == "__main__":
    unittest.main()
