# Aodix Repair

[Aodix](https://web.archive.org/web/20070819041559/http://www.aodix.com/pageaodixv4.html) was a music [sequencer](https://en.wikipedia.org/wiki/Music_sequencer) / [tracker](https://en.wikipedia.org/wiki/Music_tracker) program for Windows developed by Arguru Software. Unfortunately [the developer](https://en.wikipedia.org/wiki/Juan_Antonio_Arguelles_Rius) died in 2007, making v4.2.0.1 the last version of Aodix forever.

Aodix still works well on modern systems, and has a unique combination of ideas that I haven't seen in other music software. But there are also a few bugs that will never be fixed. The most painful one causes certain VSTs to be corrupted when the file is saved. This results in the error message `Unable to Locate Plugin`, the loss of VST instrument settings, and possibly a crash.

I have created a [Cheat Engine](https://www.cheatengine.org/) table which patches this bug and others through code injection. I have also written a Python script which can automatically repair old corrupted project files under certain circumstances.

In the process of creating these patches, I reverse-engineered and documented the `.adx` file format, as well as the internal memory layout of the program. See `adx-spec.txt` and `memory-layout.txt`.

## Requirements

- [Aodix v4](https://web.archive.org/web/20070819041559/http://www.aodix.com/pageaodixv4.html)
- [Cheat Engine 32-bit](https://www.cheatengine.org/)
- For repairing old files: [Python 3](https://www.python.org/downloads/)

## Patch instructions

Attach Cheat Engine to the Aodix process, load the `Aodix.CT` cheat table, and check the box next to "Bug fixes" to enable all cheats. This should be done before loading any VSTs.

### List of patches

- **Fix VST path bug:** Fixes a bug that causes some VSTs to save with corrupted paths, preventing them from being loaded again.
- **Fix Bounce panel MIDI crash:** Fixes a crash triggered by MIDI input while the Bounce panel is open.

## File repair instructions

Run the python script on the `.adx` file to repair: `python aodix-repair.py file.adx`

It will print a list of all VST paths, and whether it had to repair each of them.

**Note:** The script can only work automatically if the paths to your VST folders (in Aodix Configuration settings) contained **at least 33 characters** when the file was saved. For example: `C:\Program Files (x86)\VSTPlugins` is 33 characters long, but `C:\VST` is only 6 characters and can't be repaired by the script.
