import rtmidi
import time
import threading

notePlaying = {}
noteSequence = []
def doubleNote(pitch, velocity):
    noteOn = [0x94, pitch, velocity]
    noteOff = [0x84, pitch, 0]

    currentThread = threading.get_ident()
    notePlaying[pitch] = currentThread

    time.sleep(0.2)

    if notePlaying.get(pitch) != currentThread:
        return

    outputMidi.send_message(noteOn)

    time.sleep(0.1)

    outputMidi.send_message(noteOff)
    if notePlaying.get(pitch) == currentThread:
        del notePlaying[pitch]

def message(event, data=None):
    keyPressed, a = event
    print(f"Channel: {keyPressed[0]:#X}")
    # Masking for the status of if the key was pressed or not
    status = keyPressed[0] & 0xF0
    pitch = keyPressed[1]
    velocity = keyPressed[2]

    if status == 0x90 and keyPressed[2] > 0:
        print("note on")
        print(f"velocity: {keyPressed[2]} | Pitch: {keyPressed[1]} | Channel: {keyPressed[0]:#X}" )

        if pitch in notePlaying:
            outputMidi.send_message([0x84, pitch, 0])

        threading.Thread(target=doubleNote, args=(pitch, velocity), daemon=True).start()

        print(notePlaying)

inputMidi = rtmidi.MidiIn()
outputMidi = rtmidi.MidiOut()

for i, port in enumerate(inputMidi.get_ports()):
    print(f"[{i}] {port}")
InPort = int(input("Choose available port: "))
inputMidi.open_port(InPort)

for i, port in enumerate(outputMidi.get_ports()):
    print(f"[{i}] {port}")
outPort = int(input("Choose OUTPUT port: "))

outputMidi.open_port(outPort)

inputMidi.set_callback(message)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

