import rtmidi
import time
out = rtmidi.MidiOut()

ports = out.get_ports()

print(ports)

out.open_port(1)

with out:
    note_on = [0x94, 48, 100]
    note_off = [0x84, 48, 0]
    out.send_message(note_on)
    time.sleep(1.0)
    out.send_message(note_off)
    time.sleep(0.1)