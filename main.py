# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

from PIL import Image,ImageDraw,ImageFont
img_path = "img.jpg"
font_type = "C:\windows\Fonts\Arial.ttf"
font_size = 60

def draw_dig(n):
    text = str(n)
    img = Image.open(img_path)
    w,h = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_type,font_size)
    draw.text((w*0.9,0),text,font=font,fill="red")
    img.save("new.jpg","jpeg")



# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    draw_dig(5)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
