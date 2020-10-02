# python -m unittest discover -s Tests -v
import unittest
from Surf_class import Surf

class Test_Surf(unittest.TestCase):

    @staticmethod
    def value_input(surf_size,wind_direction,wind_speed,water_temp):
        test = Surf("-26.5443222,153.0507705")
        test.surf_size = surf_size
        test.wind_direction = wind_direction
        test.wind_speed = wind_speed
        test.water_temp = water_temp
        return test
    
    def test_surf_str_entry(self):
        
        self.assertEqual(Test_Surf.value_input(0.5,"N",10,None).surf_str_entry,"pretty small with a swell of 0.5m and onshore " 
                                                                               "winds from the N. Better off going to the gym.")
        self.assertEqual(Test_Surf.value_input(0.5,"W",10,None).surf_str_entry,"pretty small with a swell of 0.5m but offshore winds "
                                                                               "from the W so probably worth a surf.")
        self.assertEqual(Test_Surf.value_input(1.5,"W",25,None).surf_str_entry,"decent swell of 1.5m and offshore winds from the W. Get out there now")
        

    def test_paddleBoard_str_entry(self):
        self.assertEqual(Test_Surf.value_input(0.5,"W",10,21).paddleBoard_str_entry,"The wind is only 10km/h and the water temp is a nice 21C. Go for a paddle board.")
        self.assertEqual(Test_Surf.value_input(1.5,"S",20,21).paddleBoard_str_entry,"Its a bit windy to go paddle boarding. The wind is 20km")
        self.assertEqual(Test_Surf.value_input(1.5,"W",10,15).paddleBoard_str_entry,"The wind is only 10km/h but the water temp is a chilly 15C. "
                                                                                    "Chuck a wetty on and go for a paddle board.")

# if __name__ == "__main__":
#   unittest.main()             # This feature will allow you to run the command in the terminal without the full command