from Profile_class import Profile
from Surf_class import Surf

user = Profile()

username = user.get_profile()

if username == "":
    print("Welcome new user. Enter your details to set up your profile.")
    new_user = Profile()
    new_user.set_up_profile()
    new_user.save_profile()

print(f"Hey {user.first_name}")

while True:
    print("How can I help you today: ")
    selection = int(input("""
    1) Check the surf
    2) Settings
    3) Quit
    
    """))
    surf = Surf(user.coordinates)
    if selection == 1:
        print(f"""Hey {user.first_name}. The surf is {surf.surf_str_entry}
        """)
    if selection == 2:
        
        confirm = input("Do you want to change your profile? write yes or no. ")
        confirm = confirm.lower()
        if confirm == 'yes':
            user.set_up_profile()
            user.save_profile()

    if selection == 3:
        break





