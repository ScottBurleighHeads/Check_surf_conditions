from Profile_class import Profile
from Surf_class import Surf

user = Profile()
username = user.get_profile()
if username == "":
    print("Welcome new user. Enter your details to set up your profile.")
    new_user = Profile()
    new_user.set_up_profile()
    new_user.save_profile()

print(f""" Hey {user.first_name}. The surf is {Surf().surf_str_entry}""")




