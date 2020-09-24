from geopy.geocoders import Nominatim

class Profile():
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.DOB = ""
        self.city = ""
        self.coordinates = ""
    
    def set_up_profile(self):
        """This method is used only initially while a user use's the program for the first time.
        In the main there is a control to check if profile.txt is empty"""
        name = input("Enter your first and last name: ")
        name_list = name.split(" ")
       
        if len(name_list) == 2:
            self.first_name = name_list[0]
            self.last_name = name_list[-1]
        else:
            self.first_name = name
            self.last_name = ""
        
        self.DOB = input("Enter your D.O.B in the format xx/xx/xxxx: ")
        solution = 0
       
        while solution != 'yes' or solution == '1': 
            self.city = input("Enter your address: ")
            print("\n")
            # The code below will display latitude and longitude coordinates
            # to use for the Surf_class local area.
            geolocator = Nominatim(user_agent=f"{self.first_name} {self.last_name}")
            location = geolocator.geocode(f"{self.city}")
            solution = input(f"Is the address given correct. yes or no: {location.address}: ")
            if solution == "yes":
                self.city = location.address
                self.coordinates = f"{location.latitude},{location.longitude}"
            
            else:
                print("There may have been an input error. Try again or use the next suburb." 
                      "The program only needs a suburb or city where you live.")
           
    def save_profile(self):
        """This method is used to store data in profile.txt for the user. Initially the user will
        have to enter his details but the next time the person logs in their data 
        has been saved and can be used to get up to date information."""
        with open('profile.txt', 'w') as data_file:
            data_file.write(f"Name  : {self.first_name} {self.last_name} \n"
                            f"D.O.B : {self.DOB} \n"
                            f"City  : {self.city} \n"
                            f"City coordinates: {self.coordinates}")
                            
    def get_profile(self):  
        """This method is used to retrieve the users details when executing the program. 
        The user will not have to log in again."""
        def convert(data_file):
            name_str = data_file.readline()
            name_listy = name_str.split(" ")
            return name_listy
        try:
            with open('profile.txt', 'r') as data_file:
                line_1 = convert(data_file)
                self.first_name = line_1[3]
                self.last_name = line_1[-2]
                self.DOB = convert(data_file)[-2]
                self.city = data_file.readline()[8:-1]
                self.coordinates = convert(data_file)[2]
            return f"Name: {self.first_name} {self.last_name}, D.O.B: {self.DOB}, City: {self.city}"
        except IndexError:
            return ""



