from Profile_class import Profile

user = Profile()
username = user.get_profile()
if username == "":
    print("Welcome new user. Enter your details to set up your profile.")
    new_user = Profile()
    new_user.set_up_profile()
    new_user.save_profile()

print(user.first_name)


