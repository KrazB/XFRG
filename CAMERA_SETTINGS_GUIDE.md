# 🎛️ XFRG Camera Settings Guide

## User-Adjustable Camera Parameters

The XFRG application now includes a **Camera Settings Panel** that allows you to customize the viewing experience for different types of BIM models.

### 📍 **Location**
- **Panel Position**: Top-right corner of the application
- **Always Available**: Visible when viewing 3D models

### 🎯 **Camera Settings Explained**

#### **1. Clipping Planes**
Controls what parts of the model are visible based on distance from camera:

- **Near Plane** (0.01 - 10.0)
  - **Default**: 0.1
  - **Purpose**: Minimum distance for detail visibility
  - **Adjust Lower**: For very close detail inspection
  - **Adjust Higher**: To eliminate z-fighting on large models

- **Far Plane** (1,000 - 100,000)
  - **Default**: 50,000
  - **Purpose**: Maximum viewing distance
  - **Adjust Lower**: For smaller models (improves performance)
  - **Adjust Higher**: For very large BIM complexes

#### **2. Camera Distance Multipliers**
Controls how far the camera positions itself from models:

- **Close Distance** (1.0x - 20.0x)
  - **Default**: 5.0x
  - **Purpose**: Detailed viewing distance
  - **Adjust Lower**: For closer inspection
  - **Adjust Higher**: If models still appear too close

- **Far Distance** (1.0x - 30.0x)
  - **Default**: 8.0x
  - **Purpose**: Overview/wide viewing distance
  - **Adjust Lower**: For tighter overviews
  - **Adjust Higher**: For very wide project views

#### **3. Minimum Distance** (50 - 1,000)
- **Default**: 200
- **Purpose**: Absolute minimum camera distance
- **Adjust Higher**: For large architectural models
- **Adjust Lower**: For small mechanical components

### 🎮 **How to Use**

1. **Load your 3D model** (IFC or Fragment file)
2. **Open Camera Settings Panel** (top-right corner)
3. **Adjust sliders** to your preference
4. **Click "Apply & Refit"** to see changes immediately
5. **Use "Reset"** to return to defaults

### 🏗️ **Recommended Settings by Model Type**

#### **Small Components** (< 10m)
- Near Plane: `0.01`
- Far Plane: `5,000`
- Close Distance: `2.0x`
- Far Distance: `4.0x`
- Min Distance: `50`

#### **Single Buildings** (10-100m)
- Near Plane: `0.1` *(default)*
- Far Plane: `50,000` *(default)*
- Close Distance: `5.0x` *(default)*
- Far Distance: `8.0x` *(default)*
- Min Distance: `200` *(default)*

#### **Large Complexes** (> 100m)
- Near Plane: `1.0`
- Far Plane: `100,000`
- Close Distance: `10.0x`
- Far Distance: `20.0x`
- Min Distance: `500`

#### **Very Large Infrastructure** (> 1000m)
- Near Plane: `5.0`
- Far Plane: `100,000`
- Close Distance: `15.0x`
- Far Distance: `30.0x`
- Min Distance: `1,000`

### 🔧 **Troubleshooting**

**Models appear too close:**
- Increase Close Distance and Far Distance multipliers
- Increase Minimum Distance

**Models disappear at distance:**
- Increase Far Plane value
- Check if Far Distance is too high

**Z-fighting (flickering surfaces):**
- Increase Near Plane value
- Reduce Far Plane if very large

**Performance issues:**
- Reduce Far Plane value
- Use lower distance multipliers

### 💡 **Tips**

- **Start with defaults** and adjust incrementally
- **Use "Apply & Refit"** after each change to see results
- **Save your preferred settings** mentally for different model types
- **Reset anytime** if settings become unusable

The camera settings are designed to handle everything from small mechanical parts to entire city districts. Experiment to find what works best for your specific BIM models!
