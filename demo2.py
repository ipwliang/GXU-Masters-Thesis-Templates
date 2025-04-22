from pdf2image import convert_from_path
import os

# 将 PDF 转换为图片列表
images = convert_from_path('model.pdf', dpi=300)  # dpi 可以根据需要设置图像分辨率

# 保存为 PNG 格式
# for i, image in enumerate(images):
#     image.save(f'output_page_{i + 1}.png', 'PNG')

images[0].save(os.path.join('figure', f'yolov1.png'), 'PNG')