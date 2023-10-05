# Import unit test module and final project program.
import unittest
from FinalProject import *

# Initialize testing class.
class Test(unittest.TestCase):

    # Test for correct calculation of full package.
    def test_fullPackageEstimate(self):
        price = fullPackageEstimate(1, 0, 0, "Basic", "Basic")
        self.assertEqual(price, 155)
    def test2_fullPackageEstimate(self):
        price = fullPackageEstimate(5, 1, 1, "Premium", "Advanced")
        self.assertEqual(price, 350)
    
    # Test for correct calculation of phone and internet plan.    
    def test_phoneInternetEstimate(self):
        price = phoneInternetEstimate(1, 0, 0, "Basic")
        self.assertEqual(price, 110)
    def test2_phoneInternetEstimate(self):
        price = phoneInternetEstimate(5, 1, 1, "Advanced")
        self.assertEqual(price, 260)

    # Test for correct calculation of phone and cable plan.
    def test_phoneCableEstimate(self):
        price = phoneCableEstimate(1, 0, 0, "Basic")
        self.assertEqual(price, 115)
    def test2_phoneCableEstimate(self):
        price = phoneCableEstimate(5, 1, 1, "Advanced")
        self.assertEqual(price, 280)

    # Test for correct calculation of internet and cable plan.
    def test_internetCableEstimate(self):
        price = internetCableEstimate("Basic", "Basic")
        self.assertEqual(price, 85)
    def test2_internetCableEstimate(self):
        price = internetCableEstimate("Premium", "Advanced")
        self.assertEqual(price, 145)

    # Test for correct calculation of phone plan.
    def test_familyPhonePlanEstimate(self):
        price = familyPhonePlanEstimate(1, 0, 0)
        self.assertEqual(price, 70)
    def test2_familyPhonePlanEstimate(self):
        price = familyPhonePlanEstimate(5, 1, 1)
        self.assertEqual(price, 205)

    # Test for correct calculation of internet service.
    def test_internetEstimate(self):
        price = internetEstimate("Basic")
        self.assertEqual(price, 40)
    def test2_internetEstimate(self):
        price = internetEstimate("Premium")
        self.assertEqual(price, 70)

    # Test for correct calculation of cable service.
    def test_cableEstimate(self):
        price = cableEstimate("Basic")
        self.assertEqual(price, 45)
    def test2_cableEstimate(self):
        price = cableEstimate("Advanced")
        self.assertEqual(price, 75)


# Run the test
if __name__ == '__main__':
    unittest.main()