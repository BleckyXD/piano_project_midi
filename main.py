import rtmidi

# Note number to name mapping
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def note_to_name(note_number):
    octave = (note_number // 12) - 1
    name = NOTE_NAMES[note_number % 12]
    return f"{name}{octave}"

def on_message(event, data=None):
    message, delta_time = event
    status = message[0] & 0xF0  # strip channel

    if status == 0x90 and message[2] > 0:  # Note On (velocity > 0)
        note = message[1]
        velocity = message[2]
        print(f"▶ {note_to_name(note):4s}  (MIDI {note})  vel={velocity}")
    elif status == 0x80 or (status == 0x90 and message[2] == 0):  # Note Off
        note = message[1]
        print(f"  {note_to_name(note):4s}  released")

midiin = rtmidi.MidiIn()

# List and pick a port
ports = midiin.get_ports()
if not ports:
    print("No MIDI devices found!")
    exit()

print("Available ports:")
for i, port in enumerate(ports):
    print(f"  [{i}] {port}")

port_index = int(input("Select port number: "))
midiin.open_port(port_index)
midiin.set_callback(on_message)

print("\nPlaying... (Ctrl+C to stop)\n")
try:
    input()
except KeyboardInterrupt:
    pass

del midiin