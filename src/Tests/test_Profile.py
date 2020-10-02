# python -m unittest discover -s Tests -v
import unittest
from unittest.mock import patch
from Profile_class import Profile

class Test_Profile(unittest.TestCase):
    
    def setUp(self):
        """Mock displayed below for inputs."""
        with patch("builtins.input") as input: 
            input.side_effect = ["scott malone","23/32/2332","sydney","yes"]
            self.test = Profile()
            self.test.set_up_profile_name_DOB
            self.test.set_up_profile_address
            self.test.save_profile
    #Testing names need to be the same as the test inputs.
    def test_set_up_profile_name_DOB(self):
        # Testing instance variables are not empty after initiation in setUp
        self.assertEqual(self.test.first_name != "", True)
        self.assertEqual(self.test.last_name != "", True)
        self.assertEqual(self.test.DOB != "", True)
        # Changing values in instance variables
        self.test.first_name = "Fred"
        self.test.last_name = "Blogs"
        self.test.DOB = "12/23/3456"
        # Testing the changes
        self.assertEqual(self.test.first_name,'Fred')
        self.assertEqual(self.test.last_name,'Blogs')
        self.assertEqual(self.test.DOB,"12/23/3456")
    
    def test_set_up_profile_address(self):
        # Testing inputs are not empty from the object
        self.assertEqual(self.test.city != "", True)
        self.assertEqual(self.test.coordinates != "", True)

    def test_save_profile(self):
        # opening the file and reading should return the layout printed.
        with open('profile.txt', 'r') as data_file:
                txt = data_file.read()
        self.assertEqual(txt,f"Name  : {self.test.first_name} {self.test.last_name}\n"
                             f"D.O.B : {self.test.DOB}\n"
                             f"City  : {self.test.city}\n"
                             f"City coordinates: {self.test.coordinates}")
        
    def test_get_profile(self):
        
        # Storing current values to test against 
        first = self.test.first_name
        last = self.test.last_name
        birth = self.test.DOB
        address = self.test.city
        coords = self.test.coordinates
        
        # Deleting current values 
        self.test.first_name = None
        self.test.last_name = None
        self.test.DOB = None
        self.test.city = None
        self.test.coordinates = None
        
        # Calling the function get_profile to retrieve the values 
        # from a text file.
        self.test.get_profile.replace(" ","").replace("\n","")
        
        # Testing the values are correct
        self.assertEqual(self.test.first_name,first)
        self.assertEqual(self.test.last_name,last)
        self.assertEqual(self.test.DOB,birth)
        self.assertEqual(self.test.city,address)
        self.assertEqual(self.test.coordinates,coords)


