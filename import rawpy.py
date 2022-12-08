from PIL import Image

# Open the raw image
with open("image.raw", "rb") as f:
    raw_data = f.read()

# Create an image instance from the raw data
image = Image.frombytes("RGB", (width, height), raw_data)

# Save the image in JPEG format
image.save("image.jpeg", "JPEG")

