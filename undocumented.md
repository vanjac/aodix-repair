# Aodix Undocumented Features

## Event Syntaxes

- **Note channels:** Contrary to the help file, the second byte in a note event is not unused. It is the MIDI channel number (minus 1).
- **Tempo syntax:** `Tmp TT FF 00 00`
    - TT = Integer part of tempo
    - FF = Fractional part / 256

## Keyboard Shortcuts

- Ctrl + I: Interpolate
- Ctrl + R: Randomize
