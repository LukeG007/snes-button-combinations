import usb.core

class USBInterface:
    def __init__(self):
        self.device = usb.core.find(idVendor=0x0810, idProduct=0xe501)
        self.ep = self.device[0].interfaces()[0].endpoints()[0]
        self.interface_number = self.device[0].interfaces()[0].bInterfaceNumber
        self.device.reset()
        if self.device.is_kernel_driver_active(self.interface_number):
            self.device.detach_kernel_driver(self.interface_number)
        self.device.set_configuration()
        self.eaddr = self.ep.bEndpointAddress
        self.loop_enabled = True
    def get_raw_read(self):
        read = list(self.device.read(self.eaddr, 8))
        return read
    
    def get_pretty_read(self):
        read = self.get_raw_read()
        buttons_pushed = {
            'dpad_x': read[3],
            'dpad_y': read[4],
            'letter_keys': read[5],
            'rlss': read[6]
        }
        return buttons_pushed
