
from PIL import Image, ImageEnhance, ImageFilter
import os

path_in = r"C:\Users\user\Desktop\photos"
path_out = r"C:\Users\USER\Desktop\photos1"
for filename in os.listdir(path_in):
    img = Image.open(f"{path_in}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN)
    edit = img.filter(ImageFilter.SMOOTH)
    factor = 2.0
    Enhancer = ImageEnhance.Contrast(edit)
    edit = Enhancer.enhance(factor)
    factor1 = 2.0
    obj = ImageEnhance.Brightness(edit)
    edit = obj.enhance(factor1)
    New_name = os.path.splitext(filename)[0]
    edit.save(f"{path_out}/{New_name}.jpg")


