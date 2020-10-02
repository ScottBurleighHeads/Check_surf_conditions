from geopy.geocoders import Nominatim

class Profile():
    def __init__(self):
        
        self.first_name = None
        self.last_name = None
        self.DOB = None
        self.city = None
        self.coordinates = None
    
    @property
    def set_up_profile_name_DOB(self):
        """ This method is used to store name and DOB in the instance variables. """

        name = input("Enter your first and last name: ").title()
        name_list = name.split(" ")
        # if,else used if user only types one name.
        if len(name_list) == 2:
            self.first_name = name_list[0]
            self.last_name = name_list[-1]
        else:
            self.first_name = name
            self.last_name = ""
        # While statement used to ensure that user is putting in correct format for DOB
        while True:
            self.DOB = input("Enter your D.O.B in the format xx/xx/xxxx: ")
            if len(self.DOB) == 10 and self.DOB[2] == "/" and self.DOB[5] =="/":
                if self.DOB[:2].isnumeric() and self.DOB[3:5].isnumeric() and self.DOB[6:].isnumeric():
                    break
                else:
                    print("ERROR: Only enter the format xx/xx/xxxx where x is a number only")
            else:
                print("Please only use the format xx/xx/xxxx. Only use numbers for the x.")             
    
    @property
    def set_up_profile_address(self):
        """geopy.geocoders is used to transform the city or suburb input into longitute 
           and latitude coordinates so it can be used dynamically with the API"""
        solution = 0
        while solution != 'yes' or solution == '1': 
            
            try:
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
            except AttributeError:
                print("The program is not finding a suitable address for your input. " 
                      "I Suggest you enter the closest suburb and city with no commas and "
                      "just a space, eg: {suburb city}. ") 
    @property       
    def save_profile(self):
        """This method is used to store data in profile.txt for the user. Initially the user will
        have to enter his details but the next time the person logs in their data 
        has been saved and can be used to get up to date information."""
        with open('profile.txt', 'w') as data_file:
            data_file.write(f"Name  : {self.first_name.strip()} {self.last_name.strip()}\n"
                            f"D.O.B : {self.DOB.strip()}\n"
                            f"City  : {self.city.strip()}\n"
                            f"City coordinates: {self.coordinates.strip()}")
    @property                        
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
                self.first_name = line_1[3].strip().replace("\n","")
                self.last_name = line_1[4].strip().replace("\n","")
                self.DOB = convert(data_file)[2].strip().replace("\n","")
                self.city = data_file.readline()[8:-1].strip().replace("\n","")
                self.coordinates = convert(data_file)[2].strip().replace("\n","")
            return f"Name: {self.first_name} {self.last_name}, D.O.B: {self.DOB}, City: {self.city}"
        except IndexError:
            return ""
