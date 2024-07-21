import barcode  # Import the main barcode library
from barcode.writer import ImageWriter  # Import ImageWriter to save barcodes as images

# Get the EAN-13 barcode class from the barcode library
EAN = barcode.get_barcode_class('ean13')

# Create an EAN-13 barcode object with a specific number
# Note: The number should be 12 digits long; the library will automatically calculate and add the 13th check digit
ean = EAN('372827327311', writer=ImageWriter())

# Save the generated barcode as an image file
# The image will be saved with the base name 'ean13_barcode' and an appropriate file extension (like .png)
filename = ean.save('ean13_barcode')

# Print the filename of the saved barcode image to confirm successful saving
print(f'Barcode saved as {filename}')
