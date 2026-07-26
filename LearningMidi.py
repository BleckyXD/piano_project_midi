import rtmidi

out = rtmidi.MidiOut()

ports = out.get_ports()

print(ports)