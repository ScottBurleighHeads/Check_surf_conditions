import unittest
from src.Profile import Profile

class Test_Profile(unittest.TestCase):
    test = Profile()
    test.set_up_profile_name_DOB
    test.set_up_profile_address
    test.save_profile
    #Testing names need to be the same as the test inputs.
    def test_set_up_profile_name_DOB(self):
        
        self.assertEqual(Test_Profile.test.first_name != "", True)
        self.assertEqual(Test_Profile.test.last_name != "", True)
        self.assertEqual(Test_Profile.test.DOB != "", True)

        Test_Profile.test.first_name = "Fred"
        Test_Profile.test.last_name = "Blogs"
        Test_Profile.test.DOB = "12/23/3456"

        self.assertEqual(Test_Profile.test.first_name,'Fred')
        self.assertEqual(Test_Profile.test.last_name,'Blogs')
        self.assertEqual(Test_Profile.test.DOB,"12/23/3456")
    
    def test_set_up_profile_address(self):
        
        self.assertEqual(Test_Profile.test.city != "", True)
        self.assertEqual(Test_Profile.test.coordinates != "", True)

    def test_save_profile(self):
        
        with open('profile.txt', 'r') as data_file:
                txt = data_file.read()
        self.assertEqual(txt,f"Name  : {Test_Profile.test.first_name} {Test_Profile.test.last_name}\n"
                             f"D.O.B : {Test_Profile.test.DOB}\n"
                             f"City  : {Test_Profile.test.city}\n"
                             f"City coordinates: {Test_Profile.test.coordinates}")
        
    def test_get_profile(self):
        
        # Storing current values to test against 
        first = Test_Profile.test.first_name
        last = Test_Profile.test.last_name
        birth = Test_Profile.test.DOB
        address = Test_Profile.test.city
        coords = Test_Profile.test.coordinates
        
        # Deleting current values 
        Test_Profile.test.first_name = None
        Test_Profile.test.last_name = None
        Test_Profile.test.DOB = None
        Test_Profile.test.city = None
        Test_Profile.test.coordinates = None
        
        # Calling the function get_profile to retrieve the values 
        # from a text file.
        Test_Profile.test.get_profile.replace(" ","").replace("\n","")
        
        # Testing the values are correct
        self.assertEqual(Test_Profile.test.first_name,first)
        self.assertEqual(Test_Profile.test.last_name,last)
        self.assertEqual(Test_Profile.test.DOB,birth)
        self.assertEqual(Test_Profile.test.city,address)
        self.assertEqual(Test_Profile.test.coordinates,coords)


