# GUI — Sidebar

The sidebar is the left panel of the main window and provides two tabs:

- **Chambers**: manage chambers and select outputs (impedances)
- **Chamber Info**: edit the configuration parameters for the selected chamber

---

## Chambers Tab

### Add / remove chambers

- **Add chamber**: creates a new chamber with default values.
- **[Remove chamber]** (in the tree): removes the selected chamber and renumbers the remaining ones.

### Chamber tree structure

Each chamber shows a subtree of impedances organized by category:

```
★ Total: Total (sum of all chambers)    ← Gold background, bold
├── ZLong ✓                              ← Mandatory
├── ZTrans ✓                             ← Mandatory
├── ZDipX ☑                              ← Default (checked)
├── ZDipY ☑
├── ZQuadX ☑
├── ZQuadY ☑
├── ZLongTotal ☑
├── ZTransTotal ☐                        ← Not default
├── ...
└── ZTransISC ☐

Chamber 1: MyComponent                   ← Normal appearance
├── [Remove chamber]
├── ZLong ✓
├── ZTrans ✓
└── ...
```

### Impedance categories and order

Impedances are displayed in the following order:

1. **Base Impedances** (wall contribution)
   - `ZLong` (mandatory)
   - `ZTrans` (mandatory)
   - `ZDipX`, `ZDipY`
   - `ZQuadX`, `ZQuadY`

2. **Total Impedances** (wall + space charge)
   - `ZLongTotal`, `ZTransTotal`
   - `ZDipXTotal`, `ZDipYTotal`
   - `ZQuadXTotal`, `ZQuadYTotal`

3. **Surface Impedances**
   - `ZLongSurf`, `ZTransSurf`

4. **Space Charge** (DSC/ISC)
   - `ZLongDSC`, `ZLongISC`
   - `ZTransDSC`, `ZTransISC`

### Mandatory and default impedances

**Mandatory** (always enabled, cannot be deselected):
- `ZLong`
- `ZTrans`

**Default** (checked by default on new chambers):
- `ZLong`, `ZTrans` (mandatory)
- `ZLongTotal`
- `ZDipX`, `ZDipY`, `ZQuadX`, `ZQuadY`

### Child components

Each impedance has child components for drag & drop:
- `...Re` (real part)
- `...Im` (imaginary part)

---

## Total Chamber

When you load an accelerator and run **Calculate All**, a special **Total** chamber is created:

- **Visual distinction:**
  - ★ star prefix in the name
  - Gold/lemon background color
  - Bold font

- **Contents:**
  - Sum of impedances from all individual chambers
  - Same impedance selection as other chambers

- **Behavior:**
  - Cannot be manually removed
  - Automatically recreated on each **Calculate All**
  - Supports drag & drop to Data/Plot panels

---

## Drag & drop format (advanced)

Dragging from the tree provides MIME data in the form:

```
chamber_name|impedance_name
```

Examples:

- `Chamber 1|ZLongRe` — specific component
- `Chamber 1|ZLong` — base impedance (adds both Re and Im)
- `Total|ZLong` — from Total chamber

The chamber name is extracted from the tree item text, handling special cases like the ★ prefix.

---

## Chamber Info Tab

This tab edits the same information stored in a `.cfg` file, organized in collapsible sections:

- `[base_info]`
  - `component_name`
  - `chamber_shape` (CIRCULAR / ELLIPTICAL / RECTANGULAR)
  - geometry parameters (radius or horizontal/vertical semi-axes, length)
  - beta functions (`betax`, `betay`)

- `[layers_info]` and individual `[layerN]` sections
  - add/remove layers, edit thickness and material parameters

- `[boundary]`
  - boundary type and related parameters

- `[frequency_info]`
  - frequency range mode (log range) or file input mode

- `[beam_info]`
  - relativistic gamma, test beam shift, and particle mass

The GUI updates visibility of geometry fields based on the selected chamber shape.

---

## Notes

- The chamber selector (combo box) on top selects the active chamber.
- When you calculate impedances, the tree labels can display sample counts (e.g. `ZLong (N)`).
- Checkbox states in the sidebar are synchronized with the **Accelerator → Impedance Selection** menu.
