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

### Cura
Download the `config/Cura/Config.3mf` file. Import it into Cura (`File > Open File(s)`) and select the `Open as Project` option and `Open` at the `Summary` window.

Rename the printer (`Automated Ender 3` or similar) and ensure that `Skirt Line Count` is set to `0`, ***and*** `Skirt Height` is set to a value that will give at least 50mm (this can be found by `50/layer height`).
