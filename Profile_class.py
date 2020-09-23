class Profile():
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.DOB = ""
        self.city = ""
    
    def set_up_profile(self):
        name = input("Enter your first and last name: ")
        name_list = name.split(" ")
        if len(name_list) == 2:
            
            self.first_name = name_list[0]
            self.last_name = name_list[-1]
        else:
            self.first_name = name
            self.last_name = ""
        
        self.DOB = input("Enter your D.O.B in the format xx/xx/xxxx: ")
        self.city = input("Enter your city: ")
       
        
    def save_profile(self):
        with open('profile.txt', 'w') as data_file:
            data_file.write(f"Name  : {self.first_name} {self.last_name} \n"
                            f"D.O.B : {self.DOB} \n"
                            f"City  : {self.city} ")

    def get_profile(self):  
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
            return f"Name: {self.first_name} {self.last_name}, D.O.B: {self.DOB}, City: {self.city}"
        except IndexError:
            return ""
