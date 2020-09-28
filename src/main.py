from Profile import Profile
from Surf import Surf

user = Profile()

username = user.get_profile

if username == "":
    print("Welcome new user. Enter your details to set up your profile.")
    user.set_up_profile_name_DOB
    user.set_up_profile_address
    user.save_profile

print(f"Hey {user.first_name}")

while True:

    try:
        print("How can I help you today. Enter a number: ")
        selection = int(input("""
        1) Check the surf
        2) Settings
        3) Quit
        
        """))
        surf = Surf(user.coordinates)
        if selection == 1:
            print(f"""Hey {user.first_name}. The surf is {surf.surf_str_entry}
            """)
            if float(surf.surf_size) < 1.3:
                print(surf.paddleBoard_str_entry)
        elif selection == 2:
            
            confirm = input("Do you want to change your profile? write yes or no. ")
            confirm = confirm.lower()
            if confirm == 'yes':
                user.set_up_profile_name_DOB
                user.set_up_profile_address
                user.save_profile

        elif selection == 3:
            break
        else:
            print("Enter a number 1,2 or 3 only. ")
            
        print("Press enter to return the main menu.")
        input()
    except ValueError:
        print("Invalid input you may have entered a letter instead of a value between " 
              "1 - 3. Please try again or press 3 to quit.\n") 
    





