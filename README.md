# Aodix File Repair

[Aodix](https://web.archive.org/web/20070819041559/http://www.aodix.com/pageaodixv4.html) was a music [sequencer](https://en.wikipedia.org/wiki/Music_sequencer) / [tracker](https://en.wikipedia.org/wiki/Music_tracker) program for Windows developed by Arguru Software. Unfortunately [the developer](https://en.wikipedia.org/wiki/Juan_Antonio_Arguelles_Rius) died in 2007, making v4.2.0.1 the last version of Aodix forever.

Aodix still works well on modern systems, and has a unique combination of ideas that I haven't seen in any other music software. But there are also a few bugs that will never be fixed. The most painful one causes certain VSTs to be corrupted when the file is saved. This results in the error message `Unable to Locate Plugin`, the loss of VST instrument settings, and possibly a crash.

I have created a [Cheat Engine](https://www.cheatengine.org/) table which patches this bug. I have also written a Python script which can automatically repair old corrupted project files under certain circumstances.

In the process of creating these patches, I also reverse-engineered and documented the `.adx` file format, as well as the internal memory layout of the program. See `adx-spec.txt` and `memory-layout.txt`.

## Requirements

- [Aodix v4](https://web.archive.org/web/20070819041559/http://www.aodix.com/pageaodixv4.html)
- [Cheat Engine 32-bit](https://www.cheatengine.org/)
- For repairing old files:
    - [Python 3](https://www.python.org/downloads/)
    - The paths to your VST folders (in Aodix Configuration settings) **must have contained at least 33 characters** when you saved the `.adx` file, in order for it to be repaired automatically.

## Patch instructions

Attach Cheat Engine to the Aodix process, load the `Aodix.CT` cheat table, and enable the "Fix VST path bug" cheat. This should be done before loading any VSTs. If it works correctly, you should now be able to save and load project files without errors.

## File repair instructions

Run the python script on the `.adx` file to repair: `python aodix-repair.py file.adx`

It will print a list of all VST paths, and whether it had to repair each of them.
