from PIL import Image

# 打开图片
image_paths = ["val_batch0_labels.jpg", "val_batch2_labels.jpg"]  # 替换为你的图片路径
images = [Image.open(image_path) for image_path in image_paths]

# 定义裁剪区域
# 参数分别为左上角的 x 坐标、左上角的 y 坐标、右下角的 x 坐标、右下角的 y 坐标
crop_boxs = [(0, i*(1344//3), 1344, (i+1)*(1344//3)) for i in range(3)]  # 示例裁剪区域

# 裁剪图片
for i, image in enumerate(images):
    for j, crop_box in enumerate(crop_boxs):
        cropped_image = image.crop(crop_box)
        cropped_image.save(f"tt_{i}_{j}.png")

# 保存裁剪后的图片
# cropped_image.save("cropped_image.png")  # 保存到指定路径

# 显示裁剪后的图片
# cropped_image.show()