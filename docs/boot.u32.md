# boot.u32 / carnevil1_9.u32

MIPS-IV executable BootROM

Likely a generic bootloader for Midway's arcade games. 

Can be disassembled with the fallowing command:

`mips-linux-gnu-objdump -D -b binary -mmips:5000`

Jumps to DIAG.EXE, which jumps back to BootROM, which jumps to GAME.EXE.