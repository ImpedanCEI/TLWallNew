# PyTlWall GUI Documentation

**Qt-based configuration editor and impedance visualizer**

This section documents the graphical interface shipped with PyTlWall.  
The GUI is designed to:

- configure one or more chambers through the same `.cfg` structure used by the CLI
- compute selected impedances
- inspect results as tables and overlay plots
- export configurations, impedances, plots, and complete workspaces ("Views")
- load and calculate multi-chamber accelerator lattices

---

## Table of Contents

- [Getting Started](#getting-started)
- [Main Window Layout](#main-window-layout)
- [Sidebar](GUI_SIDEBAR.md)
- [Central Panel](#central-panel)
  - [Data Panel](GUI_DATA_PANEL.md)
  - [Plot Panel](GUI_PLOT_PANEL.md)
- [Menu Bar and Actions](GUI_MENU_BAR.md)
- [Saving and Loading Views](GUI_VIEW_IO.md)
- [Accelerator Workflow](#accelerator-workflow)
- [Tips and Troubleshooting](#tips-and-troubleshooting)

---

## Getting Started

### Launch

From the package entry points (depending on your installation):

```bash
# Recommended: Launch via the main module
python -m pytlwall --gui

# Or launch the GUI module directly
python -m pytlwall_gui

# Or use the helper script
python run_gui.py
```

If the GUI does not start, ensure the GUI dependencies are installed:

```bash
pip install pyqt5 matplotlib
```

---

## Main Window Layout

The main window is split into two areas:

- **Sidebar** (left): chamber tree + configuration editor
- **Central Panel** (right): results in **Data** and **Plot** tabs

This split is resizable via a splitter and the sidebar lists multiple chambers.

See: [Sidebar](GUI_SIDEBAR.md).

---

## Central Panel

The central panel has two tabs:

- **Data**: a table where you can collect multiple impedance components (and export them)
- **Plot**: an overlay plot view with a list of plotted items, visibility toggles, and plot settings

### Typical workflow

1. Create one or more chambers (or load an accelerator lattice).
2. Configure geometry, layers, boundary, frequency definition, and beam.
3. Choose which impedances to compute.
4. Run **Calculate** (single chamber) or **Calculate All** (accelerator).
5. Drag impedances from the chamber tree into:
   - **Data** to build custom tables
   - **Plot** to overlay curves
6. Export results or save the whole workspace as a **View**.

---

## Accelerator Workflow

The GUI supports multi-chamber accelerator calculations:

1. **Load Accelerator** (Accelerator menu)
   - Select a directory containing:
     - `apertype2.txt` (aperture types)
     - `b_L_betax_betay.txt` (geometry and optics)
     - Chamber configuration files (`*.cfg`)

2. **Configure Impedance Selection**
   - Use the **Accelerator → Impedance Selection** submenu
   - Select/deselect impedances for all chambers at once

3. **Calculate All**
   - Computes impedances for all loaded chambers
   - Creates a **Total** chamber (★) with summed impedances

4. **Analyze Results**
   - The Total chamber appears at the top of the sidebar with gold highlighting
   - Drag impedances from any chamber (including Total) to Data/Plot panels

---

## Tips and Troubleshooting

### Impedance Selection

- **Mandatory impedances:** `ZLong` and `ZTrans` are always enabled and cannot be deselected.
- **Default impedances:** The following are checked by default:
  - `ZLong`, `ZTrans` (mandatory)
  - `ZLongTotal`
  - `ZDipX`, `ZDipY`, `ZQuadX`, `ZQuadY`

### Impedance Order

Impedances are organized in categories:

1. **Base Impedances** (wall contribution): ZLong, ZTrans, ZDipX, ZDipY, ZQuadX, ZQuadY
2. **Total Impedances** (wall + space charge): ZLongTotal, ZTransTotal, ZDipXTotal, ZDipYTotal, ZQuadXTotal, ZQuadYTotal
3. **Surface Impedances**: ZLongSurf, ZTransSurf
4. **Space Charge** (DSC/ISC): ZLongDSC, ZLongISC, ZTransDSC, ZTransISC

### Drag & Drop

- Drag an impedance "base" (e.g. `ZLong`) to add both Re and Im components
- Drag a specific component (e.g. `ZLongRe`) to add only that component
- The **Total** chamber (★) supports drag & drop like any other chamber

### Plotting

- **Log scales:** When plotting in log scale, absolute values are used
- **Automatic fallback:** If data contains no positive values, the plot automatically switches to linear scale
- **Multiple curves:** Each dropped impedance gets a distinct color

### Total Chamber

- After **Calculate All**, a special "Total" chamber appears
- It's marked with ★ and has a gold background
- Contains the sum of impedances from all individual chambers
- Cannot be removed manually (recreated on each Calculate All)

### Documentation

After running `build_doc`, HTML pages are expected in `doc/html/` and accessible from the Help menu.

If you need the exact meaning of any button or setting, see the dedicated pages for each panel and menu.
