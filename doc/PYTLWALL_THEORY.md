---
title: PyTlWall Theory
---

# PyTlWall Theory

**Theoretical foundations of the transmission-line wall impedance model**

## Authors

- **Tatiana Rijoff** — tatiana.rijoff@gmail.com  
- **Carlo Zannini** — carlo.zannini@cern.ch  

*Copyright: CERN*

---

## Overview

This page summarizes the theoretical model implemented in **PyTlWall** for computing resistive-wall beam coupling impedance in **multilayer** vacuum chambers, and collects the key assumptions and validity limits.

---

## Background

The TLwall approach builds on the **transmission-line (TL)** analogy for layered media (planar case), extended to circular chambers through a controlled approximation, and on the **inductive bypass** concept introduced by **L. Vos** for the transverse impedance in the resistive-wall problem.

A main goal is to provide a **fast and robust** way to compute:

- longitudinal impedance
- transverse (dipolar / quadrupolar) impedance
- equivalent multilayer **surface impedance**

for **PEC / vacuum / material** boundary conditions, with optional extension to non-ultrarelativistic beams.

---

## Multilayer Wall as a Recursive Transmission Line

### Physical Model

A round chamber of radius *b* is loaded by a stack of layers (conductors/dielectrics) and terminated by a boundary condition (PEC, vacuum, or material half-space). Each layer is represented by a TL segment with its own propagation constant and characteristic impedance.

The TL equations can be applied **recursively** to any number of layers to obtain the **equivalent surface impedance** seen at the vacuum–wall interface.

> **Practical note:** In PyTlWall the same equivalent surface impedance can then be mapped to non-circular cross-sections using **Yokoya form factors** (rectangular/elliptical approximations).

### Equivalent Surface Impedance

The computation returns an equivalent surface impedance Z_s(ω) of the full multilayer stack. This is then used through the **Leontovich boundary condition** to relate tangential electric and magnetic fields at the interface, and to compute the beam coupling impedance.

---

## Applicability and TLwall Hypothesis

Transmission-line equations are exact for **planar geometries**. In circular structures they remain usable when the **attenuation of cylindrical waves** inside the wall can be neglected, so that the equivalent surface impedance is effectively independent of the incident-wave direction.

A commonly used sufficient condition is:

- **skin depth** δ ≪ b

The TLwall implementation also estimates a **maximum frequency** up to which the TL approximation is expected to remain accurate for a given configuration.

---

## Transverse Impedance and the Inductive Bypass (Vos)

For the transverse impedance, TLwall uses the **inductive bypass** concept (Vos formalism), which introduces an additional inductive contribution (often denoted L₁) to capture the transverse coupling consistently within the TL approach.

In the ultrarelativistic limit, a common constant appearing in the formalism is:

```
L₁ = μ₀ / (4π)
```

The method is extended in the code to cover the **non-ultrarelativistic** regime with improved approximations for the field radial dependence and related corrections.

---

## Impedance Types

PyTlWall computes several types of impedances:

### Base Impedances (Wall Contribution)

| Impedance | Description |
|-----------|-------------|
| **ZLong** | Longitudinal impedance |
| **ZTrans** | Transverse impedance |
| **ZDipX** | Horizontal dipolar impedance |
| **ZDipY** | Vertical dipolar impedance |
| **ZQuadX** | Horizontal quadrupolar impedance |
| **ZQuadY** | Vertical quadrupolar impedance |

### Total Impedances (Wall + Space Charge)

| Impedance | Description |
|-----------|-------------|
| **ZLongTotal** | Total longitudinal (wall + space charge) |
| **ZTransTotal** | Total transverse (wall + space charge) |
| **ZDipXTotal**, **ZDipYTotal** | Total dipolar |
| **ZQuadXTotal**, **ZQuadYTotal** | Total quadrupolar |

### Space Charge Contributions

| Impedance | Description |
|-----------|-------------|
| **ZLongDSC** | Direct space charge (longitudinal) |
| **ZLongISC** | Indirect/image space charge (longitudinal) |
| **ZTransDSC** | Direct space charge (transverse) |
| **ZTransISC** | Indirect/image space charge (transverse) |

### Surface Impedances

| Impedance | Description |
|-----------|-------------|
| **ZLongSurf** | Surface longitudinal impedance |
| **ZTransSurf** | Surface transverse impedance |

---

## Benchmarks and Reference Solutions

TLwall has been benchmarked against **ReWall** and **IW2D**.

- **IW2D** should be regarded as the reference when the highest fidelity is needed, because it solves Maxwell equations without the TL approximation.
- TLwall typically agrees well in practical cases; for some parameter sets, the validity is restricted to a limited frequency range (as per the TLwall hypothesis).

### Validation Notes

- `ZLong`, `ZTrans`, `ZLongTotal` show good agreement with IW2D
- `ZDipX`, `ZDipY`, `ZQuadX`, `ZQuadY` (wall contributions) are consistent with IW2D
- Total transverse impedances (`ZTransTotal`, `ZDipXTotal`, etc.) may show discrepancies in some configurations

---

## When TLwall is Convenient

Typical cases where TLwall is particularly attractive:

- Building an impedance model from an aperture model (many elements → many evaluations)
- Very large number of layers (e.g. metamaterial-like stacks)
- Avoiding numerical difficulties that can arise in other methods
- Simulating ideal boundary conditions or very low resistivity
- Using the computed surface impedance as an input to more complex calculations
- Including roughness effects through simple surface-impedance modifications

---

## Chamber Shapes

PyTlWall supports three chamber cross-sections:

| Shape | Description | Yokoya Factors |
|-------|-------------|----------------|
| **CIRCULAR** | Round pipe | No correction needed |
| **ELLIPTICAL** | Elliptical cross-section | Interpolated from tables |
| **RECTANGULAR** | Flat chamber | Interpolated from tables |

For non-circular chambers, **Yokoya form factors** are applied to scale the impedances computed for the equivalent circular case.

---

## References

1. L. Vos, "The transverse impedance of a cylindrical pipe with arbitrary surface impedance", CERN-AB-2003-093 (ABP), 2003.

2. N. Mounet, E. Métral, "Electromagnetic field created by a macroparticle in an infinitely long and axially symmetric multilayer beam pipe", CERN-BE-2009-039, 2009.

3. C. Zannini, "Electromagnetic Simulation of CERN Accelerator Components and Experimental Applications", PhD Thesis, EPFL, 2013.

4. N. Mounet et al., "Resistive wall impedance in elliptical multilayer vacuum chambers", *Phys. Rev. Accel. Beams* 22, 121001 (2019).

5. IW2D — Impedance Wake 2D, field-matching technique reference solver.

---

*Last updated: December 2025*
