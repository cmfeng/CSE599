import unittest
import urllib3
import HW4
import os

#test for remove_data
class TestRemove(unittest.TestCase):
    def test_remove(self):
        HW4.download_if_needed('http://s3.amazonaws.com/pronto-data/open_data_year_one.zip', 
                                  'open_data_year_one.zip')
        #before remove_data, data are present
        self.assertTrue(os.path.exists('open_data_year_one.zip'))
        HW4.remove_data()
        #after remove_data, data are not present
        self.assertFalse(os.path.exists('open_data_year_one.zip'))
#test for down_load_if_needed
class TestDownload(unittest.TestCase):
    def test_download(self):
        #test when data are not present
        HW4.remove_data()
        #test when the url is not valid
        with self.assertRaises(urllib3.exceptions.MaxRetryError):
            HW4.download_if_needed('http://s3.23amazonaws.com/pronto-data/open_data_year_one.zip', 
                                  'open_data_year_one.zip')
        #test when url is valid
        HW4.download_if_needed('http://s3.amazonaws.com/pronto-data/open_data_year_one.zip', 
                                  'open_data_year_one.zip')
        self.assertTrue(os.path.exists('open_data_year_one.zip'))
        #test when data are present
        out = HW4.download_if_needed('http://s3.amazonaws.com/pronto-data/open_data_year_one.zip', 
                                  'open_data_year_one.zip')
        assert out == 'open_data_year_one.zip already exists'   

#test for plot_daily_totals
class TestPlot(unittest.TestCase):
    def test_download(self):
        HW4.get_pronto_data()
        if os.path.exists('daily_totals.png'):
            os.remove('daily_totals.png')
        #before plot no png flile
        self.assertFalse(os.path.exists('daily_totals.png'))
        HW4.plot_daily_totals()
        #after plot, png file is present
        self.assertTrue(os.path.exists('daily_totals.png')) 
        

if __name__ == '__main__':
    unittest.main()