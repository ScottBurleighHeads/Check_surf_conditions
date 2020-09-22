class Profile():
    def __init__(self,first_name,last_name,DOB,city):
        self.first_name = first_name
        self.last_name = last_name
        self.DOB = DOB
        self.city = city

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

        with open('profile.txt', 'r') as data_file:
            line_1 = convert(data_file)
            self.first_name = line_1[3]
            self.last_name = line_1[-2]
            self.DOB = convert(data_file)[-2]
            self.city = data_file.readline()[8:-1]
            
            



# scott = Profile('Scott','Malone', '24/08/1987', 'New York')
# scott.save_details()
# scott.get_details()
# print(scott.__dict__)
