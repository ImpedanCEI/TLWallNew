# GUI — Menu Bar and Actions

The GUI provides the following top-level menus:

- **File**
- **Chamber**
- **Accelerator**
- **Help**

---

## File menu

Typical export and workspace actions:

- **Save Chamber cfg...**  
  Save the configuration of the current chamber as a `.cfg` file.

- **Save Chamber impedance...**  
  Save impedance results (text files) for the current chamber.

- **Save Chamber Complete...**  
  Save configuration + impedance files + plots for the current chamber.

- **Save All cfg...**  
  Save `.cfg` files for all chambers.

- **Save All impedances...**  
  Save impedance files for all chambers with computed data.

- **Save All Complete...**  
  Save cfg + impedance files + plots for all chambers.

- **Save Data...**  
  Export the Data table.

- **Save Plot...**  
  Export the current plot as an image.

- **Save View...**  
  Save a complete workspace ("View"): chambers, computed impedances, data table, and plot.

- **Load View...**  
  Restore a workspace previously saved as a View.

- **Exit**

---

## Chamber menu

- **New Chamber**  
  Add a new chamber with default values.

- **New Chamber with config...**  
  Create a chamber from an existing `.cfg` file.

- **Duplicate Chamber**  
  Create a copy of the currently selected chamber.

- **Select All** / **Deselect All**  
  Enable/disable impedance outputs for the current chamber (mandatory ones remain enabled).

- **Calculate**  
  Run impedance computation for the selected chamber and selected outputs.

---

## Accelerator menu

The Accelerator menu provides tools for working with multi-chamber lattice calculations.

- **Load Accelerator...**  
  Load an accelerator lattice from a directory containing:
  - `apertype2.txt` — aperture types (one per line)
  - `b_L_betax_betay.txt` — geometry and optics parameters
  - Chamber configuration files (`*.cfg`) for each aperture type

- **Impedance Selection** (submenu)  
  Configure which impedances to compute for **all chambers** at once.

  - **Select All (All Chambers)**  
    Enable all impedance outputs for every chamber.

  - **Deselect All (All Chambers)**  
    Disable non-mandatory impedances for every chamber.

  - **Base Impedances** (submenu)  
    Toggle base wall impedances:
    - `ZLong` ✓ (mandatory — always enabled)
    - `ZTrans` ✓ (mandatory — always enabled)
    - `ZDipX` ☑ (default)
    - `ZDipY` ☑ (default)
    - `ZQuadX` ☑ (default)
    - `ZQuadY` ☑ (default)

  - **Total Impedances (wall + SC)** (submenu)  
    Toggle total impedances (wall + space charge):
    - `ZLongTotal` ☑ (default)
    - `ZTransTotal`
    - `ZDipXTotal`
    - `ZDipYTotal`
    - `ZQuadXTotal`
    - `ZQuadYTotal`

  - **Surface Impedances** (submenu)  
    Toggle surface impedances:
    - `ZLongSurf`
    - `ZTransSurf`

  - **Space Charge (DSC/ISC)** (submenu)  
    Toggle space charge impedances:
    - `ZLongDSC`
    - `ZLongISC`
    - `ZTransDSC`
    - `ZTransISC`

- **Calculate All**  
  Compute impedances for all loaded chambers and create a **Total** chamber with summed impedances.

### Accelerator Workflow

1. **Load Accelerator...** → Select directory with input files
2. Chambers appear in the sidebar
3. Optionally adjust **Impedance Selection** for all chambers
4. **Calculate All** → Computes all chambers and creates Total
5. The **Total** chamber (★) appears at the top of the chamber list
6. Drag impedances to Data/Plot panels for analysis

### Notes

- Mandatory impedances (`ZLong`, `ZTrans`) are shown with ✓ and cannot be unchecked
- Default impedances are marked with ☑ and are checked on startup
- Menu checkboxes stay synchronized with the sidebar tree checkboxes
- The Total chamber is automatically recreated each time you run Calculate All

---

## Help menu

### Documentation

The Help menu opens the generated HTML documentation from `doc/html/`.

Submenus include:

- **Index** — Main documentation index
- **Pytlwall Graphical Interface** — GUI documentation pages
- **API Reference** — Module-by-module API docs
- **Examples** — Usage examples

Expected workflow:

1. Write/update Markdown sources
2. Run `build_doc`
3. Open pages from **Help → Documentation**

### About

Shows version and author information:

- Version number
- Authors: Tatiana Rijoff, Carlo Zannini
- Credits for original MATLAB implementation and Python development

---

See also: [GUI Documentation](GUI.md)
