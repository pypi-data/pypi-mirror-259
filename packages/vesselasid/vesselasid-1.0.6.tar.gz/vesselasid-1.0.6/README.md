# vesselasid

vesselasid is a python client for the [Elektron ASID protocol](http://paulus.kapsi.fi/asid_protocol.txt), which allows programming SID registers remotely using MIDI Sysex (in an ASID receiver, such as a SidStation or [Vessel](https://github.com/anarkiwi/vessel) equipped C64 runing [VAP](https://github.com/anarkiwi/vap)).

It contains extensions that allow sending arbitrary data such as machine code over Sysex, and executing code remotely, and acknowledging commands with MIDI clock. Currently only VAP implements these extensions.

# installation

## linux

```
pip3 install vesselasid
```

## macosx

1. Install [MacPorts](https://www.macports.org/install.php).
2. Install portmidi and dependencies: ```sudo port install python310 py310-pip py310-mido portmidi```
3. Install VesselASID: ```/opt/local/bin/pip-3.10 install vesselasid```
4. Test your installation:
```
% /opt/local/bin/python3.10                 
Python 3.10.13 (main, Jan  8 2024, 11:42:08) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import vesselasid
>>> import mido
>>> mido.set_backend('mido.backends.portmidi')
>>> mido.get_output_names()
['IAC Driver Bus 1']
````

# programming registers

```
MIDI_DEV = "Scarlett 2i4 USB:Scarlett 2i4 USB MIDI 1 16:0"
port = mido.open_output(MIDI_DEV)
asid = Asid(port)
asid.start()
asid.sid.voice[1].set_state(freq=2048, s=15)
asid.sid.set_state(vol=15)
asid.update() # sends all pending changes
```

# sending and running machine code

```
MIDI_DEV = "Scarlett 2i4 USB:Scarlett 2i4 USB MIDI 1 16:0"
port = mido.open_output(MIDI_DEV)
in_port = mido.open_input(MIDI_DEV) # when in_port defined, receiver will acknowledge commands with MIDI clock.
asid = Asid(port, in_port=in_port)
asid.start()
code = xa(["lda #$0f", "sta $d418"]) # Asid adds rts automatically. Code origin currently fixed to $c000.
asid.load(code)
asid.run() # does jsr $c000 remotely, sends clock when done.
```
