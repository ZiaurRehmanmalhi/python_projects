from PIL import Image, ImageDraw, ImageFont

# Set the text to be converted to handwriting
text = "Hy i am zia ur Rahman in Lahore"

# Set the font to be used for handwriting
font_path = "FreeMono.ttf"
font_size = 50
font = ImageFont.truetype(font_path, font_size)

# Create an empty image and a drawing context
img = Image.new("RGB", (500, 500), "white")
draw = ImageDraw.Draw(img)

# Draw the text in handwriting
draw.text((50, 200), text, font=font, fill=(0, 0, 0))

img.save("handwriting.png")
