import argparse
from osgeo import gdal
import os
import math

# Define command-line arguments
parser = argparse.ArgumentParser(description='Slice rasters into individual tiles')
parser.add_argument('tile_size', type=int, help='Tile size in pixels')
parser.add_argument('zoom_level', type=int, help='Zoom level')
parser.add_argument('input_raster', type=str, help='Input raster file path')
parser.add_argument('output_folder', type=str, help='Output folder path')
args = parser.parse_args()

# Open the input raster file using GDAL
ds = gdal.Open(args.input_raster)

# Get the raster size
cols = ds.RasterXSize
rows = ds.RasterYSize

# Calculate the number of tiles in the x and y direction at the given zoom level
num_tiles_x = int(math.ceil(float(cols) / float(args.tile_size * 2 ** args.zoom_level)))
num_tiles_y = int(math.ceil(float(rows) / float(args.tile_size * 2 ** args.zoom_level)))

# Loop through each tile and extract it from the input raster
for i in range(num_tiles_x):
    for j in range(num_tiles_y):
        # Calculate the pixel coordinates of the top-left corner of the tile
        x_min = i * args.tile_size * 2 ** args.zoom_level
        y_min = j * args.tile_size * 2 ** args.zoom_level

        # Calculate the pixel coordinates of the bottom-right corner of the tile
        x_max = min((i + 1) * args.tile_size * 2 ** args.zoom_level, cols)
        y_max = min((j + 1) * args.tile_size * 2 ** args.zoom_level, rows)

        # Calculate the size of the tile in pixels
        tile_cols = x_max - x_min
        tile_rows = y_max - y_min

        # Create a new GDAL dataset for the tile
        driver = gdal.GetDriverByName("GTiff")
        tile_ds = driver.Create(os.path.join(args.output_folder, "tile_{}_{}.tif".format(i, j)), tile_cols, tile_rows, 1, ds.GetRasterBand(1).DataType)

        # Set the geotransform of the tile
        gt = list(ds.GetGeoTransform())
        gt[0] = gt[0] + x_min * gt[1]
        gt[3] = gt[3] + y_min * gt[5]
        tile_ds.SetGeoTransform(tuple(gt))

        # Set the projection of the tile
        tile_ds.SetProjection(ds.GetProjection())

        # Read the data from the input raster into the tile dataset
        data = ds.ReadAsArray(x_min, y_min, tile_cols, tile_rows)
        tile_ds.GetRasterBand(1).WriteArray(data)

        # Close the tile dataset
        tile_ds = None

# Close the input dataset
ds = None
