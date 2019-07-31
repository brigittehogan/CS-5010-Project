from query3_project_code import *
import unittest
import pandas as pd

#creating a test dataframe for my unittests

data = [[11, 1], [2,2], [3,3], [4,4],[5,5],[6,6],[15,7],[8,8],[9,9],[10,10],[11,11],[12,12],[13,13],[14,14],[15,15],[16,16],[17,17],[18,18],[19,19],[20,20],[21,21]]
dftest1 = pd.DataFrame(data, columns = ['quality', 'alcohol'])

class TestAlcohol(unittest.TestCase):
    #creating class for a test dataframe
    
    def test_high_ext(self):
        test95 = Alcohol.high_extremes(dftest1, 'alcohol')
        self.assertEqual(test95,20)
    
    def test_low_ext(self):
        test05 = Alcohol.low_extremes(dftest1, 'alcohol')
        self.assertEqual(test05,2)
    
    def test_alc_high(self):
        test112 = Alcohol.alcohol_high(dftest1)
        data12 = [[21,21]]
        expectedf12 = pd.DataFrame(data12, columns = ['quality', 'alcohol'])
        self.assertEqual(test112.iat[0,1], expectedf12.iat[0,1])
        
    def test_alc_high2(self):
        test112 = Alcohol.alcohol_high(dftest1)
        data12 = [[21,21]]
        expectedf12 = pd.DataFrame(data12, columns = ['quality', 'alcohol'])
        self.assertEqual(test112.iat[0,0], expectedf12.iat[0,0])
    
    def test_alc_low(self):
        test220 = Alcohol.alcohol_low(dftest1)
        data220 = [[11,1]]
        expected220 = pd.DataFrame(data220, columns = ['quality', 'alcohol'])
        self.assertEqual(test220.iat[0,0],expected220.iat[0,0])

    def test_alc_norm(self):
        data13 = [[2,2], [3,3]]
        expectedf13 = pd.DataFrame(data13, columns = ['quality', 'alcohol'])
        test113 = Alcohol.alcohol_hohum(dftest1)
        self.assertEqual(test113.iat[1,1], expectedf13.iat[1,1])
    
    def test_alc_norm2(self):
        data14 = [[2,2], [3,3]]
        expectedf14 = pd.DataFrame(data14, columns = ['quality', 'alcohol'])
        test114 = Alcohol.alcohol_hohum(dftest1)
        self.assertEqual(test114.iat[0,0], expectedf14.iat[0,0])

    def test_low_q(self):
        data15 = [[11,1]]
        expectedf15 = pd.DataFrame(data15, columns = ['quality', 'alcohol'])
        test115 = Alcohol.low_quality(dftest1, 10)
        self.assertEqual(test115.iat[0,0], expectedf15.iat[0,0])
    
    def test_high_q(self):
        data16 = [[21,21]]
        expectedf16 = pd.DataFrame(data16, columns = ['quality', 'alcohol'])
        test116 = Alcohol.high_quality(dftest1, 10)
        self.assertEqual(test116.iat[0,0], expectedf16.iat[0,0])

    def test_hohum2(self):
        data17 = [[15,7]]
        expectedf17 = pd.DataFrame(data17, columns = ['quality', 'alcohol'])
        test117 = Alcohol.alcohol_hohum2(dftest1, 10)
        self.assertEqual(test117.iat[0,0],expectedf17.iat[0,0])
    
if __name__ == '__main__':
    unittest.main()

