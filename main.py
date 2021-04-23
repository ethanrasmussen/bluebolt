import bt_discover as btd
import servo_op as sop


def main_menu():
    # cmd line menu
    print("----- MENU: -----")
    print(" 1. Start Script")
    print(" 2. Edit Whitelist")
    print("-----------------")
    menu_opt = input("Please enter 1 or 2: ")
    if menu_opt == "1":
        run_script()
    elif menu_opt == "2":
        edit_whitelist()
    else:
        print("Improper input value. Please enter any key to try again.")
        input()
        print("\n\n\n\n\n\n")
        main_menu()

def edit_whitelist():
    pass
def run_script():
    pass
