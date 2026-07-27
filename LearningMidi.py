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

def message(event, data=None):
    keyPressed, a = event
    print(f"Channel: {keyPressed[0]:#X}")
    # Masking for the status of if the key was pressed or not
    status = keyPressed[0] & 0xF0
    pitch = keyPressed[1]
    velocity = keyPressed[2]
    noteOn = [0x94, pitch, velocity]
    noteOff = [0x84, pitch, 0]
    if status == 0x90 and keyPressed[2] > 0:
        print("note on")
        print(f"velocity: {keyPressed[2]} | Pitch: {keyPressed[1]} | Channel: {keyPressed[0]:#X}" )

        #hex 94 = 148
        #hex 84 = 132
        outputMidi.send_message(noteOn)
    else:
        print("note off")
        outputMidi.send_message(noteOff)


inputMidi = rtmidi.MidiIn()
outputMidi = rtmidi.MidiOut()

for i, port in enumerate(inputMidi.get_ports()):
    print(f"[{port}] {i}")
InPort = int(input("Choose available port: "))
inputMidi.open_port(InPort)

for i, port in enumerate(outputMidi.get_ports()):
    print(f"[{i}] {port}")
outPort = int(input("Choose OUTPUT port: "))

outputMidi.open_port(outPort)

inputMidi.set_callback(message)

try:
    input()
except KeyboardInterrupt:
    pass

