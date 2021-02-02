import re  # 用于正则

import pytesseract
from PIL import Image  # 用于打开图片和对图片处理
import time  # 代码运行停顿
import tesserocr
img = Image.open('./yepa/data_solve/code.jpg')
new_im = img.convert("L")
# 二值化，采用阈值分割法，threshold为分割点
threshold = 140
table = []
for j in range(256):
    if j < threshold:
        table.append(0)
    else:
        table.append(1)
out = new_im.point(table, '1')

#new_im.show()
print(tesserocr.image_to_text(out))
