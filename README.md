# CarnEvil Research
This repo contains all my research and scripts for reverse engineering CarnEvil by Midway Games. 

## Getting started

To access the game executable and assets you will needs CarnEvil's chd file and MAME's chdman. You will also need [these](https://forum.xentax.com/viewtopic.php?p=160064#p160064) Window's programs written by daemon1 (They never released source for these programs, but they can be easily decompiled. I plan on making python equivalents). 

1. Extract the raw disk image from chd:
    * `chdman extractraw -i carnevil.chd -o carnevil.raw`
2. Split the image into parts:
    * `.\Carnevilraw.exe carnevil.raw`
3. Extract the files from part0:
    * `.\Carnevilpart.exe part0`

## What's what
This section briefly describes the known files from ROMs and the raw hard disk image. Additional info about each file will be located in the [docs](/docs/) folder.

### ROMs
* `boot.u32` or `carnevil1_9.u32` - BootROM, not the actual game.
* `sound102.u95` - ROM for DCS Sound System chip (ADSP 2115) 

### Hard disk
Executable MIPS-IV code:
* `DIAG.EXE` - Diagnostics code ran prior to GAME.EXE. Performs hardware and CRC-based file integrity checks. Includes sound and hard drive tests, as well as gun calibration. This menu is also described in the CarnEvil Operations Manual.  
* `GAME.EXE` - Main game code. Appears to be a flat binary with code + data ordered respectively. 

Textures:
* `WMS` - Texture files. Presumably named after WMS Industries who developed arcade games at the time. 
  * Header - 1132 instances of this header, potential false-positives.
    * `00000000: 05 80 00 00 00 00 00 00 01 00 00 00 00 00 00 00  ................`

Sound:
* `BNK` - DCS audio files
  * Header - 70 instances of this header
    * `00000000: 44 43 53 20 33 2e 30           DCS 3.0`

Models:
* `ZM`, `ZM2` - Model files. Each `.ZM` and `.ZM2` files are identical. You can prove this by comparing md5 sums. The `2`s may be used as backus. The extension is never mentioned in the game binary. 
* `ZA`, `ZA2` - Animation files. Each `.ZA` and `.ZA2` files are identical. You can prove this by comparing md5 sums. The `2`s may be used as backups. The extension is never mentioned in the ga,e binary. 

Unknown: 
* `RAW` - These are considered "camera files" by the game. Perhaps these dictate the way the cameras move? 
* `RW2` - There is a matching `RW2` file for each `RAW`, they are never mentioned in the game binary and m5sums differ.
* `BIN` - DCS sound system operating system files
* `RA2` - Unknown. Only one known files with this extension, `BTOP.RA2`that has the same md5sum as its `RAW` equivalent. 
* `PTH`, `PT2` - This seem to be pathing files that dictate enemy AI movement. There is a matching `PTH` file for each `PT2`, they are never mentioned in the game binary and m5sums match.
* `AUDITS.FMT` - File written by the game that contains game statistic. Not sure what the purpose of this file is. Maybe it was interesting info back in the fay. 
* `ADJUST.FMT` - File written by the game that contains setting for difficulty, gore intensity, sound mode (mono/stereo) and more. 

Misc: 
* `FILESYS.CHK` - Contains file metadata for integrity check. File size, CRC hash etc.

