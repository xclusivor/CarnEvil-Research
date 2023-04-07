# CarnEvil Research
This repo contains all my research and scripts for reverse engineering CarnEvil by Midway Games. 

## Getting started
## What's what
This section briefly describes the known files from ROMs and the raw hard disk image.

### ROMs
* `boot.u32` or `carnevil1_9.u32` - BootROM, not the actual game.
* `sound102.u95` - ROM for DCS Sound System chip (ADSP 2115) 

### Hard disk
Executable MIPS-IV code:
* `DIAG.EXE` - Diagnostics code ran prior to GAME.EXE. Performs hardware and CRC-based file integrity checks. 
* `GAME.EXE` - Main game code. Appears to be a flat binary with code + data ordered respectively. 

Textures:
* `WMS` - Texture files. Presumably named after WMS Industries who developed arcade games at the time. 
  * Header - 1132 instances of this header, potential false-positives.
    * `00000000: 05 80 00 00 00 00 00 00 01 00 00 00 00 00 00 00  ................`

Sound:
* `BNK` - DCS audio files
  * Header - 70 instances of this header
    * `00000000: 44 43 53 20 33 2e 30                             DCS 3.0`

Models:
* `ZA`, `ZM2`

Misc: 
* `FILESYS.CHK` - Contains file metadata for integrity check. File size, CRC hash etc.

Unknown: 
* `RAW` - I suspect these are the games FMVs
* `BIN`, `RA2`, `FMT`, `RW2`, `PTH`, `PT2`