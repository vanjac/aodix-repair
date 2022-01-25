# Aodix Repair

[Aodix](https://web.archive.org/web/20070819041559/http://www.aodix.com/pageaodixv4.html) was a music [sequencer](https://en.wikipedia.org/wiki/Music_sequencer) / [tracker](https://en.wikipedia.org/wiki/Music_tracker) program for Windows developed by Arguru Software. Unfortunately [the developer](https://en.wikipedia.org/wiki/Juan_Antonio_Arguelles_Rius) died in 2007, making v4.2.0.1 the last version of Aodix forever.

Aodix still works well on modern systems, and has a unique combination of ideas that I haven't seen in other music software. But there are also a few bugs that were never fixed. The most painful one causes certain VSTs to be corrupted when the file is saved. This results in the error message `Unable to Locate Plugin`, the loss of VST instrument settings, and possibly a crash.

I have created a [Cheat Engine](https://www.cheatengine.org/) table which patches this bug and others through code injection. I have also written a Python script which can automatically repair old corrupted project files under certain circumstances.

In the process of creating these patches, I reverse-engineered and documented the `.adx` file format, as well as the internal memory layout of the program. See `adx-spec.txt` and `memory-layout.txt`.

## Requirements

- [Aodix v4](https://web.archive.org/web/20070819041559/http://www.aodix.com/pageaodixv4.html)
- [Cheat Engine](https://www.cheatengine.org/)
- For repairing old files: [Python 3](https://www.python.org/downloads/)

## Patch instructions

- Start Aodix
- Start Cheat Engine (32-bit)
- Click the flashing button in Cheat Engine, select the Aodix process, and choose Open.
- Load the `Aodix.CT` cheat table found in this repository. After you do this once, Cheat Engine should remember and prompt you to load it the next time.
- Check the box next to "All patches" to enable all patches at once, or you can choose individual patches/categories. This should be done before loading any VSTs.

### List of patches

- Bug fixes
    - **Fix VST path bug:** Fixes a bug that causes some VSTs to save with corrupted paths, preventing them from being loaded again.
    - **Fix Bounce panel MIDI crash:** Fixes a crash triggered by MIDI input while the Bounce panel is open.
- Features
    - **Allow pre-release=0:** Allows setting the pre-release to 0
    - **Set length shortcut:** Adds a shortcut (`` ` ``/`~` key) to set the length of events to end at the cursor. All events overlapping the cursor are cut. If none are overlapping, the last event(s) before the cursor are extended.

## File repair instructions

Run the python script on the `.adx` file to repair: `python aodix-repair.py file.adx`

It will print a list of all VST paths, and whether it had to repair each of them.

**Note:** The script can only work automatically if the paths to your VST folders (in Aodix Configuration settings) contained **at least 33 characters** when the file was saved. For example: `C:\Program Files (x86)\VSTPlugins` is 33 characters long, but `C:\VST` is only 6 characters and can't be repaired by the script.
