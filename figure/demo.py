from PIL import Image

def resize_image(input_path, output_path, scale_factor=0.5):
    """
    将图片等比例缩小为原来的 1/4
    :param input_path: 输入图片的路径
    :param output_path: 输出图片的路径
    :param scale_factor: 缩放比例，默认为 0.25（即缩小为原来的 1/4）
    """
    # 打开图片
    with Image.open(input_path) as img:
        # 获取原始图片的宽度和高度
        width, height = img.size
        
        # 计算新的宽度和高度
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        
        # 使用高质量的缩放算法（LANCZOS）进行缩放
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # 保存缩小后的图片
        resized_img.save(output_path)

# 示例使用
input_path = "vd_0_1_9.png"  # 输入图片的路径
output_path = "vd_0_1_9.png"  # 输出图片的路径
resize_image(input_path, output_path)