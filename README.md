# 2024-summer-internship
Files and documentation for automating a print smallholding.

## Slicer Profiles
There are slicer profiles available for PrusaSlicer (recommended) and Cura. 

These files change the start and end GCode of the printer.

### PrusaSlicer
Download the `config/PS/config.ini` file. Import it into PrusaSlicer (`File > Import > Import Config`) and save it as `Automated Ender 3` or a similarly useful name.

#### Print Settings
The only print setting which must not be changed is `Loops (minimum)` in `Skirt and Brim`. No skirt should be printed. If in doubt, use a draft shield:
1. `Loops (minimum)`: `2`
2. `Draft shield`: `Enabled`
