### single band to multiband
from osgeo import gdal

# List of single band raster files
single_band_files = ["file1.tif", "file2.tif", "file3.tif"]

# Output multiband raster file
output_file = "output.tif"

# Open first single band file
ds = gdal.Open(single_band_files[0])

# Get the number of rows and columns
rows = ds.RasterYSize
cols = ds.RasterXSize

# Get the projection and geographic transformation
projection = ds.GetProjection()
geo_transform = ds.GetGeoTransform()

# Create the output multiband raster
driver = gdal.GetDriverByName("GTiff")
multiband_ds = driver.Create(output_file, cols, rows, len(single_band_files), gdal.GDT_Byte)
multiband_ds.SetProjection(projection)
multiband_ds.SetGeoTransform(geo_transform)

# Add the single band files to the output multiband raster
for i, file in enumerate(single_band_files):
    ds = gdal.Open(file)
    band = ds.GetRasterBand(1)
    multiband_ds.GetRasterBand(i+1).WriteArray(band.ReadAsArray())

# Close the datasets
ds = None
multiband_ds = None

# You can change the format of the output file by change the driver format, in 
# this case is "GTiff" and also you can change the data type of the output using 
# gdal.GDT_Byte, to the data type that you need.

# The single_band_files list should contain the path and file names of the single 
# band raster files that you want to combine.
# The output_file variable should contain the path and file name of the output 
# multiband raster file.
# The code uses the gdal.Open() function to open the first single band file and 
# gets the number of rows and columns, projection, and geographic transformation 
# from it. These values will be used to create the output multiband raster file.
# The gdal.GetDriverByName() function is used to get the driver for the output 
# file format, in this case "GTiff"
# The driver.Create() function is used to create the output multiband raster file, 
# with the number of bands specified as the fourth argument, in this case len(single_band_files)
# The multiband_ds.SetProjection() and multiband_ds.SetGeoTransform() functions 
# are used to set the projection and geographic transformation of the output file.
# The code then loops through the single_band_files list and adds each single 
# band file to the output multiband raster file using the gdal.Open() function 
# to open the file, the ds.GetRasterBand(1) function to get the first band, and 
# the multiband_ds.GetRasterBand(i+1).WriteArray() function to write the data to 
# the corresponding band in the output file.
# Finally, the code closes the datasets using ds = None and multiband_ds = None 
# to ensure that the file handles are properly closed and the data is saved.



### Multiband to single band
from osgeo import gdal

# Input multiband raster file
input_file = "input.tif"

# Open the input multiband raster
ds = gdal.Open(input_file)

# Get the number of bands
bands = ds.RasterCount

# Loop through each band
for i in range(1, bands + 1):
    band = ds.GetRasterBand(i)
    # Create the output single band file name
    output_file = "band" + str(i) + ".tif"
    # Create the output single band raster
    driver = gdal.GetDriverByName("GTiff")
    single_band_ds = driver.Create(output_file, ds.RasterXSize, ds.RasterYSize, 1, band.DataType)
    single_band_ds.SetProjection(ds.GetProjection())
    single_band_ds.SetGeoTransform(ds.GetGeoTransform())
    single_band_ds.GetRasterBand(1).WriteArray(band.ReadAsArray())
    single_band_ds = None

# Close the input multiband raster
ds = None

# The input_file variable should contain the path and file name of the input 
# multiband raster file.
# The code uses the gdal.Open() function to open the input multiband file, and 
# gets the number of bands using the ds.RasterCount property.
# The code then loops through each band using the range(1, bands + 1) function,
#  and for each band:
# it creates the output file name using the "band" + str(i) + ".tif" format
# it creates the output single band raster using the gdal.GetDriverByName() 
# function to get the driver for the output file format, in this case "GTiff" 
# and the driver.Create() function to create the output file with 1 band, and 
# the same data type of the input band.
# it sets the projection and geographic transformation of the output file using 
# single_band_ds.SetProjection(ds.GetProjection()) and single_band_ds.SetGeoTransform(ds.GetGeoTransform())
# it writes the data of the current band to the output file using 
# single_band_ds.GetRasterBand(1).WriteArray(band.ReadAsArray())
# it closes the dataset using single_band_ds = None
# Finally, the code closes the input multiband raster using ds = None to 
# ensure that the file handles are properly closed and the data is saved.
# Same as the previous example, make sure you have gdal library installed 
# in your environment, if not you can install it via pip by running "pip install gdal"