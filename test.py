import rtmidi

midiin = rtmidi.MidiIn()
ports = midiin.get_ports()

for i, port in enumerate(ports):
    print(f"[{i}] {port}")