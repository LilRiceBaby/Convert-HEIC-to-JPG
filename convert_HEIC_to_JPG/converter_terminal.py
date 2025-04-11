from PIL import Image
import pillow_heif  # registers HEIC support

try:
    im1 = Image.open("input.heic")
    rgb_im = im1.convert("RGB")
    rgb_im.save("output.jpg", "JPEG")
    print("Conversion successful.")
except FileNotFoundError:
    print("Error: input.heic not found.")
except Exception as e:
    print(f"Something went wrong: {e}")
