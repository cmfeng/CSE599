import unittest
import plotxy as pl
import os
import pandas as pd

class TestPlot1(unittest.TestCase):
    def test_plot(self):
    	#deletes the pdf file if exists
    	if os.path.exists('time_id.pdf'):
    		os.remove('time_id.pdf')
    	#before plot, no pdf exists
    	self.assertFalse(os.path.exists('time_id.pdf'))
    	data = pd.read_csv('../../../open_data_year_one/2015_trip_data.csv')    
    	pl.plot_x_vs_y(data, 'trip_id', 'birthyear', 'time_id')
    	#after plot, pdf file is present
    	self.assertTrue(os.path.exists('time_id.pdf'))

class TestPlot2(unittest.TestCase):
    def test_plot(self):
        #deletes the pdf file if exists
        if os.path.exists('duration_birth.pdf'):
            os.remove('duration_birth.pdf')
        #before plot, no pdf exists
        self.assertFalse(os.path.exists('duration_birth.pdf'))
        data = pd.read_csv('../../../open_data_year_one/2015_trip_data.csv')    
        pl.plot_x_vs_y(data,  'birthyear', 'tripduration','duration_birth')
        #after plot, pdf file is present
        self.assertTrue(os.path.exists('duration_birth.pdf'))

if __name__ == '__main__':
    unittest.main()     

    
