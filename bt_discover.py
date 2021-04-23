import bluetooth


# get all nearby bluetooth devices
def find_nearby():
    nearby_bt = bluetooth.discover_devices(lookup_names=True)
    return nearby_bt

# print formatted list of BT list
def print_nearby():
    nearby_bt = find_nearby()
    print("Found {} devices.".format(len(nearby_bt)))
    for addr, name in nearby_bt:
        print("  {} - {}".format(addr, name))

# check if whitelisted device nearby
def check_whitelist():
    # read whitelist
    with open('whitelist.txt', 'r') as f:
        wl = f.readlines()
        whitelist = []
        for item in wl:
            bt_id, name = item.strip().split(" - ")
            whitelist.append([bt_id.strip(), name.strip()])
    # compare to nearby BT devices
    nearby_bt = find_nearby()
    for device in nearby_bt:
        dev = [device[0], device[1]]
        if dev in whitelist:
            return True
    return False