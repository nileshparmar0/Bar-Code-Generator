import barcode
from barcode.writer import ImageWriter

# Choose the barcode type (e.g., 'ean13')
EAN = barcode.get_barcode_class('ean13')

# Generate barcode with ImageWriter to save as an image
ean = EAN('3728273273111', writer=ImageWriter())

# Save the barcode as an image file
filename = ean.save('ean3_barcode')

print(f'Barcode saved as {filename}')
