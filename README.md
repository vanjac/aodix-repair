# Aodix Repair

[Aodix](https://web.archive.org/web/20070819041559/http://www.aodix.com/pageaodixv4.html) was a music [sequencer](https://en.wikipedia.org/wiki/Music_sequencer) / [tracker](https://en.wikipedia.org/wiki/Music_tracker) program for Windows developed by Arguru Software. Unfortunately [the developer](https://en.wikipedia.org/wiki/Juan_Antonio_Arguelles_Rius) died in 2007, making v4.2.0.1 the last version of Aodix forever.

Aodix still works well on modern systems, and has a unique combination of ideas that I haven't seen in other music software. But there are also a few bugs that were never fixed. The most painful one causes certain VSTs to be corrupted when the file is saved. This results in the error message `Unable to Locate Plugin`, the loss of VST instrument settings, and possibly a crash.

I have created an unofficial patched version of Aodix which fixes this bug and others. I have also written a Python script which can automatically repair old corrupted project files under certain circumstances.

In the process of creating these patches, I reverse-engineered and documented the `.adx` file format, as well as the internal memory layout of the program. See [adx-spec.txt](https://github.com/vanjac/aodix-repair/blob/master/adx-spec.txt) and [memory-layout.txt](https://github.com/vanjac/aodix-repair/blob/master/memory-layout.txt).

## Installation instructions

You must have [Aodix v4.2.0.1](https://web.archive.org/web/20070819041559/http://www.aodix.com/pageaodixv4.html) installed already.

- Download the latest patched version of `Aodix.exe` from the [Releases page](https://github.com/vanjac/aodix-repair/releases)
- Find your Aodix installation folder (for example, `C:\Program Files (x86)\Arguru Software\Aodix`)
- Make a backup of `Aodix.exe` in the installation folder by renaming it to something like `Aodix.old.exe`
- Copy the patched version of `Aodix.exe` into the installation folder
- Start Aodix. If it worked, you should see the text "Patched Version!" in the window title bar.

## List of changes

- Bug fixes
    - **Fix VST path bug:** Fixes a bug that causes some VSTs to save with corrupted paths, preventing them from being loaded again.
    - **Fix Bounce panel MIDI crash:** Fixes a crash triggered by MIDI input while the Bounce panel is open.
- Features
    - **Set length shortcut:** Adds a shortcut (`` ` ``/`~` key) to set the length of events to end at the cursor. All events in the track overlapping the cursor are cut. If none are overlapping, the last event(s) before the cursor are extended.

## File repair instructions

If you have old files that Aodix can't read, you can use the "aodix-repair" script to repair them. You will need [Python 3](https://www.python.org/downloads/).

**Note:** The script can only work automatically if the paths to your VST folders (in Aodix Configuration settings) contained **at least 33 characters** when the file was saved. For example: `C:\Program Files (x86)\VSTPlugins` is 33 characters long, but `C:\VST` is only 6 characters and can't be repaired by the script.

In a terminal, run the python script on the `.adx` file to repair: `python aodix-repair.py file.adx`

It will print a list of all VST paths, and whether it had to repair each of them.

## Other resources

- [Archive of skins, older versions, and related software](http://www.oldschooldaw.com/forums/index.php/topic,7316.0.html)
- [Aodix undocumented features](https://github.com/vanjac/aodix-repair/blob/master/undocumented.md)

## Development information

Patches are developed using [Cheat Engine](https://www.cheatengine.org/), which allows patching the application while it's running using code injection. Development is done in the `Aodix.CT` cheat table. To patch the executable, I have created a binary patcher script `patcher.py`, which reads a list of patched memory regions from `patch.txt`.
