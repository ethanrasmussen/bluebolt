import bt_discover as btd
import servo_op as sop
import json, time


# get delay time from config
with open('config.json') as f:
    data = json.load(f)
bt_delay = int(data['update_delay'])


def main_menu():
    # cmd line menu
    print("----- MENU: -----")
    print(" 1. Start Script")
    print(" 2. Edit Whitelist")
    print("-----------------")
    menu_opt = input("Please enter an option: ")
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
    print("\n\n\n\n\n\n")
    print("--- WHITELIST: ---")
    with open('whitelist.txt', 'r') as f:
        wl = f.readlines()
        line_num = 1
        for line in wl:
            print(f"{line_num} || {line}")
            line_num+=1
    print("------------------")
    print(" 1. Add Device")
    print(" 2. Delete Device")
    print(" 3. Exit to Menu")
    print("------------------")
    menu_opt = input("Please enter an option: ")
    if menu_opt == "1":
        add_bt_device()
    elif menu_opt == "2":
        remove_bt_device(wl)
    elif menu_opt == "3":
        main_menu()
    else:
        print("Improper input value. Please enter any key to try again.")
        input()
        print("\n\n\n\n\n\n")
        edit_whitelist()


def add_bt_device():
    print("\n\n\n\n\n\n")
    print("--- SCANNING NEARBY: ---")
    btd.print_nearby()
    print("------------------------")
    add_opt = input("Enter 'A' to scan again, otherwise, enter the BT address of the device you'd like to add: ")
    if add_opt == "A":
        add_bt_device()
    else:
        bt_addr = add_opt
        bt_name = input("Now, please enter the name as well: ")
    try:
        with open('whitelist.txt', 'a') as f:
            new_device = [f"\n{bt_addr} - {bt_name}"]
            f.writelines(new_device)
        print("Device added! Enter any key to return to whitelist menu.")
        input()
        edit_whitelist()
    except:
        print("Something went wrong, enter any key to return to the main menu.")
        input()
        main_menu()


def remove_bt_device(wl_lines):
    del_dev = input("Enter the number of the device you'd like to remove: ")
    try:
        wl_lines.pop(int(del_dev)-1)
        with open("whitelist.txt", 'w') as f:
            f.writelines(wl_lines)
        print("Device removed. Press any key to return to whitelist menu.")
        input()
        edit_whitelist()
    except:
        print("Something went wrong, enter any key to return to the main menu.")
        input()
        main_menu()


def run_script():
    # get deadbolt's current state
    is_locked = input("Is the deadbolt locked? (Y/N): ")
    if is_locked == "Y":
        DEADBOLT_LOCK_STATE = True
    elif is_locked == "N":
        DEADBOLT_LOCK_STATE = False
    else:
        print("Improper input. Click any key to return to the main menu.")
        input()
        print("\n\n\n\n\n\n\n")
        main_menu()
    # begin infinite script
    running = True
    print("\n\n\n\n\n\n\n")
    while running:
        try:
            print("Beginning scan...")
            if btd.check_whitelist():
                print("Whitelisted device in range!")
                if DEADBOLT_LOCK_STATE is True:
                    sop.open_bolt()
                    print("Unlocked deadbolt.")
                    DEADBOLT_LOCK_STATE = False
                    print(f"Waiting for {bt_delay} seconds...")
                    time.sleep(bt_delay)
                    print("\n\n")
            else:
                print("Whitelisted device not found or has left detectable area.")
                if DEADBOLT_LOCK_STATE is False:
                    sop.close_bolt()
                    print("Locked deadbolt.")
                    DEADBOLT_LOCK_STATE = True
                    print("\n\n")
        except KeyboardInterrupt:
            running = False



# run program
if __name__ == "__main__":
    main_menu()