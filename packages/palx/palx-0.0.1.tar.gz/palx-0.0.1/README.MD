# palx: Image Palette Extractor 

palx is a command-line tool and Python package that allows users to extract a color palette from an image and attach it to the image's edge. This tool is perfect for designers, artists, or anyone interested in color analysis and image manipulation.

## Features

- **Extract Color Palette**: Analyzes an image and extracts a dominant color palette.
- **Attach Palette to Image**: Adds the extracted color palette to the specified edge (top, bottom, left, or right) of the original image.
- **Customizable Options**: Allows customization of the number of colors in the palette, the position of the palette on the image, and the border width around color squares.

## Installation

To install palx, run the following command in your terminal:

```bash
pip install palx
```

## CLI Usage

To use palx from the command line, follow this syntax:
```bash
palx <image_path> [--clusters <number_of_clusters>] [--position <position>] [--border_width <width>] [--output <output_path>]
```

* image_path: Path to the input image.
* --clusters: Optional. Number of color clusters to extract (default is 5).
* --position: Optional. Position of the color palette on the image (left, right, top, bottom). Default is right.
* --border_width: Optional. Width of the border around color squares (default is 10).
* --output: Optional. Path to the output image. If not specified, the modified image will be displayed but not saved.

### Example

```bash
palx myimage.jpg --clusters 8 --position bottom --border_width 5 --output myimage_with_palette.jpg
```

This command extracts an 8-color palette from myimage.jpg, attaches it to the bottom with a border width of 5 pixels, and saves the result to myimage_with_palette.jpg.

## Python Package Usage
palx can also be used as a Python package to integrate palette extraction and attachment into your own projects.

### Extracting a Palette and Edge Length

```python
from palx import extract_palette_and_edge_length

palette, edge_length = extract_palette_and_edge_length("path/to/image.jpg", n_clusters=5)
print(palette, edge_length)
```

### Attaching the pallette to an image

```python
from palx import attach_palette

attach_palette("path/to/image.jpg", palette, "right", edge_length, border_width=10, border_color='black', output_path="path/to/output.jpg")
```

## Requirements

* Python 3.6 or higher
* Pillow
* NumPy
* scikit-learn

## License
palx is open-source software licensed under the MIT license.