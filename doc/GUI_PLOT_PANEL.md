# GUI — Plot Panel

The **Plot** tab provides an overlay plot of impedance curves with a control list on the right.

---

## What the Plot Panel does

- Accepts **drag & drop** of impedances from the chambers tree.
- Overlays multiple curves on the same axes.
- Provides a list to toggle visibility and edit curve labels.
- Offers plot settings (title, axis labels, and scales).
- Exports the plot to image.

---

## Drag & drop

Drop an impedance component (e.g. `ZLongRe`) or a base impedance (e.g. `ZLong`).

Each dropped item becomes a **PlotItem** with:

- chamber name (including "Total" if from the Total chamber)
- impedance base name
- component (Re / Im)
- data array and frequencies
- assigned color (automatically rotated)
- editable label

---

## Overlay control

### Visibility

Each plotted item can be shown/hidden through its checkbox in the list.

### Editable labels

Each list entry is editable: you can override the legend label without changing the underlying data.

### Remove items

Right-click on an item to access context menu options, including removal.

---

## Plot settings

Common settings include:

- **Title**: Editable plot title
- **X label**: Default "Frequency [Hz]"
- **Y label**: Default "Z [Ω]"
- **X scale**: log or linear
- **Y scale**: log or linear (plus symlog, logit, asinh options)

### Log scale behavior

When using **log scale**:

- The plot uses **absolute values** of the data
- Non-positive values are automatically masked (shown as gaps)
- If **all data points** are non-positive, the scale **automatically falls back to linear**

This prevents crashes when plotting impedances that have negative values (common for imaginary parts).

### Automatic fallback example

```
User selects: Y scale = log
Data contains: ZLongIm with negative values
Result: Plot uses |ZLongIm| for display
        If all values are ≤ 0, switches to linear scale
        Warning printed to console
```

---

## Color rotation

Each new curve receives a color from the palette:

1. Blue (#1f77b4)
2. Orange (#ff7f0e)
3. Green (#2ca02c)
4. Red (#d62728)
5. Purple (#9467bd)
6. Brown (#8c564b)
7. Pink (#e377c2)
8. Gray (#7f7f7f)
9. Yellow-green (#bcbd22)
10. Cyan (#17becf)

Colors cycle when more than 10 curves are plotted.

---

## Export

From the **File** menu:

- **Save Plot...** exports the current plot as an image file (PNG, PDF, SVG, etc.)

Plots are also exported when saving a complete **View**.

---

## Tips

- **Comparing chambers**: Drag the same impedance from multiple chambers to compare them
- **Total vs individual**: Drag from "★ Total" to see the sum alongside individual contributions
- **Log scale issues**: If a plot appears empty, try switching to linear scale — the data may have non-positive values
- **Legend positioning**: The legend automatically positions itself to minimize overlap
