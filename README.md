# 2024-summer-internship
Files and documentation for automating a print smallholding.

## Slicer Profiles
There are slicer profiles available for PrusaSlicer (recommended) and Cura.

These files change the start and end GCode of the printer.

### PrusaSlicer
Copy the text in `config/PS/start-gcode.txt` into the `Start G-code` box in the `Printers` tab of PrusaSlicer, **replacing the current contents.** Do the same for `config/PS/end-gcode.txt` into the `End G-code` box. Save this as a new printer, named `Automated Ender 3`.

#### Print Settings
The only print setting which must be changed is `Loops (minimum)` in `Skirt and Brim`, which should be set to 0. No skirt should be printed. If in doubt, use a draft shield:
1. `Loops (minimum)`: `2`
2. `Draft shield`: `Enabled`

### Cura
Add a new Ender 3 named `Automated Ender 3`. Click `Machine settings` and copy the text in `config/Cura/start-gcode.txt` into the `Start G-code` box, **replacing the current contents.** Do the same for `config/Cura/end-gcode.txt` into the `End G-code` box and save.

#### Print Settings
Ensure that `Skirt Line Count` is set to `0`, ***and*** `Skirt Height` is set to a value that will give at least 50mm (this can be found by `50/layer height`).
