import unittest
from PIL import Image
from ImageReader import getHealthInfo
class MyTestCase(unittest.TestCase):
    #Tests if the health bar is above the threshold
    def test_getHealthFalse(self):
        self.assertEqual(False, getHealthInfo(Image.open("Images/dead1.png"))) #The Health bar was not read correctly

    #Tests if the health bar is below the threshold
    def test_getHealthTrue(self):
        self.assertEqual(True, getHealthInfo(Image.open("Images/dead4.png"))) #The Health bar was not read correctly

    #Tests if a health bar is visible
    def test_healthBarNotVisible(self):
        self.assertEqual(False, getHealthInfo(Image.open("Images/dead5.png"))) #Health bar recognized when it shouldn't

if __name__ == '__main__':
    unittest.main()
