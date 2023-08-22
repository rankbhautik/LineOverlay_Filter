from PIL import Image, ImageFilter

def apply_line_overlay_filter(image_path):
    # Open the image
    original_image = Image.open(image_path)
    
    # Convert the image to a format compatible with Core Image (RGBA)
    rgba_image = original_image.convert("RGBA")
    
    # Apply the line overlay filter
    line_overlayed_image = rgba_image.filter(ImageFilter.CONTOUR)
    
    return line_overlayed_image

# Path to your input image
input_image_path = 'your_image.png'

# Apply the line overlay filter
line_overlay_result = apply_line_overlay_filter(input_image_path)

# Show the original and line overlay images
line_overlay_result.show()
