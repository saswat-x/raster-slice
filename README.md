# Slicing Rasters into Individual Tiles with GDAL


This Python code is designed to slice rasters into individual tiles using the GDAL library. It allows you to specify the tile size, zoom level, input raster, and output folder as command-line arguments, and generates a set of GeoTIFF files containing the individual tiles.

## Requirements
To use this code, you need to have the following software installed:

Python 3.6 or higher
GDAL 3.0 or higher

## Installation
To install the code, simply download the slice_raster.py file and save it to a folder on your computer.

## Usage
To use the code, open a command prompt or terminal window and navigate to the folder containing the `slice_raster.py` file. Then, run the following command:

`python slice_raster.py <tile_size> <zoom_level> <input_raster> <output_folder`

Here's what each of the arguments means:

- tile_size: The size of each tile in pixels. For example, if you specify a tile size of 256, each tile will be 256x256 pixels in size.
- zoom_level: The zoom level at which to slice the raster. This determines the number of tiles that will be generated. Higher zoom levels generate more tiles, while lower zoom levels generate fewer tiles.
- input_raster: The path to the input raster file that you want to slice.
- output_folder: The path to the folder where you want to save the output tiles.

For example, to slice a raster with a tile size of 256 pixels at zoom level 10, and save the output tiles to a folder called output_tiles, you would run the following command:

`python slice_raster.py 256 10 input.tif output_tiles/`

This will generate a set of GeoTIFF files containing the individual tiles, each named according to its location in the input raster.
