import usb_interface
import combination_mgmt

usb = usb_interface.USBInterface()
combinations = combination_mgmt.CombinationMGMT()

old_read = None

while True:
    read = usb.get_pretty_read()
    if old_read is None:
        old_read = read
    else:
        if not read == old_read:
            if read['rlss'] == 32:
                combinations.check_combination(read)
            old_read = read
