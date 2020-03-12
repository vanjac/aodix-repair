# Aodix File Repair

[Aodix](https://web.archive.org/web/20070819041559/http://www.aodix.com/pageaodixv4.html) was a music [sequencer](https://en.wikipedia.org/wiki/Music_sequencer) / [tracker](https://en.wikipedia.org/wiki/Music_tracker) program for Windows developed by Arguru Software. Unfortunately [the developer](https://en.wikipedia.org/wiki/Juan_Antonio_Arguelles_Rius) died in 2007, making v4.2.0.1 the last version of Aodix forever.

Aodix still works well on modern systems, and has a unique combination of features that I haven't seen in any other music software. But there are also a few bugs that will never be fixed. The most painful one causes certain VSTs to be corrupted when the file is saved. This results in the error message `Unable to Locate Plugin`, the loss of VST instrument settings, and possibly a crash.

These corrupted files are easy to fix in a hex editor. I've written a Python script to automate this process.

In the process of writing the script, I also reverse-engineered and documented the `.adx` file format. See `adx-spec.txt`.

## Requirements

- [Aodix v4](https://web.archive.org/web/20070819041559/http://www.aodix.com/pageaodixv4.html)
- [Python 3](https://www.python.org/downloads/)
- The paths to your VST folders (in Aodix Configuration settings) **must contain at least 33 characters** when you save the `.adx` file, in order for it to be repaired correctly.

## Usage

Run the python script on the `.adx` file to repair: `python aodix-repair.py file.adx`

It will print a list of all VST paths, and whether it had to repair each of them.
