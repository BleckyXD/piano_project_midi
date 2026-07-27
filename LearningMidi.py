# # import rtmidi
# # import time
# # out = rtmidi.MidiOut()
# #
# # ports = out.get_ports()
# #
# # print(ports)
# #
# # out.open_port(1)
# #
# # with out:
# #     note_on = [0x94, 48, 100]
# #     note_off = [0x84, 48, 0]
# #     out.send_message(note_on)
# #     time.sleep(1.0)
# #     out.send_message(note_off)
# #     time.sleep(0.1)
# #
# #
# import time
# import rtmidi
#
# out = rtmidi.MidiOut()  #  MIDI Output
# inP = rtmidi.MidiIn()
# # Obtain the different ports
# ports_dict = {k: v for (v,k) in enumerate(out.get_ports())}
#
# # Get a specific port/available port
# out.open_port(ports_dict["ARIUS-1 1"])
# inP.open_port(0)
#
# def receivedInfo(event):
#     print(event)
# with inP:
#     while True:
#         inP.set_callback(receivedInfo)
# # with out:
# #     note_on = [0x94, 48, 112]
# #     note_off = [0x84, 48, 0]
# #
# #     cc_msg = [0xB4, 3, 0]
# #     out.send_message(cc_msg)
# #     time.sleep(0.1)
# #
# #     out.send_message(note_on)
# #     time.sleep(1)
# #
# #     for cc in range(127):
# #         cc_msg = [0xB4, 3, cc]
# #         out.send_message(cc_msg)
# #         time.sleep(0.1)
# #     out.send_message(note_off)
# #     time.sleep(0.1)


import rtmidi
import time

class music:
    def __init__(self):

        self.portSelected = 0
        self.inputMidi = rtmidi.MidiIn()
        self.inputMidi.open_port(portSelected)
        self.inputMidi.set_callback(self.message)





    def message(self, event, data=None):
        keyPressed, a = event

        # Masking for the status of if the key was pressed or not
        status = keyPressed[0] & 0xF0

        if status == 0x90:
            print("note on")
        else:
            print("note off")








portSelected = int(input("Choose available port: "))

mus = music()
mus.portSelected = portSelected




try:
    input()
except KeyboardInterrupt:
    pass

