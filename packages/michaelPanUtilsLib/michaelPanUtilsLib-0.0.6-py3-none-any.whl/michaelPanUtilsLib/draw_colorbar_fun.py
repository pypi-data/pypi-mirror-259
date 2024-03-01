# ***************************************************************
# Maintainers:
#     chuntong pan <panzhang1314@gmail.com>
# Date:
#     2024.2
# ***************************************************************
from PIL import Image, ImageDraw


# -----------------------------------------------绘制连续分段颜色条，填充色在最前面--------------------------------------------
def draw_line_part_color_bar(img_width, img_height, color_height, color_width, font_label, font_tick, test_prod,
                             test_unit, colors, text_stick, loc="for"):
    # 参数配置处理
    x1_for, y1_for, x2_for, y2_for = font_label.getbbox(test_prod)
    x1_back, y1_back, x2_back, y2_back = font_label.getbbox(test_unit)
    text_width_for = x2_for - x1_for
    text_height_for = y2_for - y1_for
    text_height_back = y2_back - y1_back
    colors_num = len(colors)
    lengths = [color_height for i in range(colors_num)]
    # 计算每个颜色段的起始位置和结束位置
    total_length = sum(lengths)
    positions = [sum(lengths[:i]) / total_length for i in range(len(lengths) + 1)]
    image = Image.new('RGBA', (img_width, img_height))
    draw = ImageDraw.Draw(image)
    # 绘制颜色块
    for i in range(len(lengths)):
        start = float(positions[i] * color_width) + (img_width - color_width) / 2
        end = float(positions[i + 1] * color_width) + (img_width - color_width) / 2
        draw.rectangle((start, 0.0, end, color_height), fill=colors[i])
    # 绘制刻度
    for i in range(colors_num):
        x = i / colors_num * color_width
        if loc == "for":  # 填充色在最前面的情况
            if i == 0:
                draw.line(
                    [(int(color_width / colors_num / 2 + int((img_width - color_width) / 2)),
                      color_height + int(color_height / 10)),
                     (int(color_width / colors_num / 2) + int((img_width - color_width) / 2),
                      color_height + 1)],
                    fill='black', width=2)
                x11, y11, x21, y21 = font_tick.getbbox(text_stick[i])
                text_width = x21 - x11
                draw.text((int(color_width / colors_num / 2) - int(text_width / 2) + int((img_width - color_width) / 2),
                           color_height + int(color_height / 10) + 1),
                          text_stick[i], fill='black', font=font_tick)
            else:
                if i == 1:  # 隔一个格显示
                    continue
                draw.line([(x + int((img_width - color_width) / 2), color_height + int(color_height / 10)),
                           (x + int((img_width - color_width) / 2), color_height + 1)], fill='black', width=2)
                x12, y12, x22, y22 = font_tick.getbbox(text_stick[i-1])
                text_width = x22 - x12
                draw.text((x - int(text_width / 2) + int((img_width - color_width) / 2),
                           color_height + int(color_height / 10) + 1), text_stick[i-1], fill='black', font=font_tick)
        elif loc == "back":  # 填充色在最后面的情况
            if i == colors_num - 1:
                draw.line(
                    [(int(color_width - color_width / colors_num / 2 + int((img_width - color_width) / 2)),
                      color_height + int(color_height / 10)),
                     (int(color_width - color_width / colors_num / 2) + int((img_width - color_width) / 2),
                      color_height + 1)],
                    fill='black', width=2)
                x11, y11, x21, y21 = font_tick.getbbox(text_stick[i-1])
                text_width = x21 - x11
                draw.text((int(color_width - color_width / colors_num / 2) - int(text_width / 2) + int(
                    (img_width - color_width) / 2),
                           color_height + int(color_height / 10) + 1),
                          text_stick[i-1], fill='black', font=font_tick)
            else:
                if i == colors_num - 2:
                    continue
                draw.line([(x + int((img_width - color_width) / 2 + (color_width / colors_num)),
                            color_height + int(color_height / 10)),
                           (x + int((img_width - color_width) / 2 + (color_width / colors_num)), color_height + 1)],
                          fill='black', width=2)
                x12, y12, x22, y22 = font_tick.getbbox(text_stick[i])
                text_width = x22 - x12
                draw.text((x - int(text_width / 2) + int((img_width - color_width) / 2 + (color_width / colors_num)),
                           color_height + int(color_height / 10) + 1), text_stick[i], fill='black', font=font_tick)
        elif loc == "all":  # 文字在色块中间的情况
            draw.line([(x + int((img_width - color_width) / 2) + int(color_width / colors_num / 2), color_height + int(color_height / 10)),
                       (x + int((img_width - color_width) / 2) + int(color_width / colors_num / 2), color_height + 1)], fill='black', width=2)
            x12, y12, x22, y22 = font_tick.getbbox(text_stick[i])
            text_width = x22 - x12
            draw.text((x - int(text_width / 2) + int((img_width - color_width) / 2) + int(color_width / colors_num / 2),
                       color_height + int(color_height / 10) + 1), text_stick[i], fill='black', font=font_tick)
        else:
            raise Exception('方法未找到，请检查配置文件')
    # 在颜色条外围添加黑色边框
    start = float(positions[0] * color_width)  + (img_width - color_width) / 2
    draw.rectangle((start, 0.0, color_width + (img_width - color_width) / 2, color_height), outline="black")
    # 绘制产品名
    draw.text((int((img_width - color_width) / 2) - text_width_for - 2,
               int((color_height - text_height_for) / 2) - 2), test_prod, fill='black', font=font_label)
    # 绘制单位
    draw.text((color_width + int((img_width - color_width) / 2) + 2,
               int((color_height - text_height_back) / 2) - 2), test_unit, fill='black', font=font_label)
    return image
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------绘制渐变颜色条-------------------------------------------------------
def draw_gradient_color_bar(img_width, img_height, color_height, color_width, font_label, font_tick, test_prod,
                            test_unit, gradients, text_stick):
    x1_for, y1_for, x2_for, y2_for = font_label.getbbox(test_prod)
    x1_back, y1_back, x2_back, y2_back = font_label.getbbox(test_unit)
    text_width_for = x2_for - x1_for
    text_height_for = y2_for - y1_for
    text_height_back = y2_back - y1_back
    image = Image.new('RGBA', (img_width, img_height))
    # 绘制颜色条
    draw = ImageDraw.Draw(image)
    x_start = int((img_width - color_width) / 2)
    j = 0
    for gradient in gradients:
        for i, color in enumerate(gradient):
            y_start, x_end = 0, x_start + color_width // (len(gradient) * len(gradients))
            y_end = color_height
            draw.rectangle((x_start, y_start, x_end, y_end), fill=color)
            x_start += color_width / (len(gradient) * len(gradients))
        colors_num = len(gradients)
        # *****************************添加刻度***********************************
        x = j / colors_num * color_width
        draw.line([(x + int((img_width - color_width) / 2),
                    color_height + int(color_height / 10)),
                   (x + int((img_width - color_width) / 2), color_height + 1)], fill='black', width=1)
        x12, y12, x22, y22 = font_tick.getbbox(text_stick[j])
        text_width = x22 - x12
        draw.text((x - int(text_width / 2) + int((img_width - color_width) / 2) + 1,
                   color_height + int(color_height / 10) + 1), text_stick[j], fill='black', font=font_tick)
        if j == colors_num - 1:  # 增加一次刻度
            draw.line([(color_width + int((img_width - color_width) / 2),
                        color_height + int(color_height / 10)),
                       (color_width + int((img_width - color_width) / 2), color_height + 1)], fill='black', width=1)
            x12, y12, x22, y22 = font_tick.getbbox(text_stick[j + 1])
            text_width = x22 - x12
            draw.text((color_width - int(text_width / 2) + int((img_width - color_width) / 2),
                       color_height + int(color_height / 10) + 1), text_stick[j + 1], fill='black', font=font_tick)
        j += 1
        # *********************************************************************
    # 在颜色条外围添加黑色边框
    start = int((img_width - color_width) / 2)
    draw.rectangle((start, 0.0, color_width + (img_width - color_width) / 2, color_height), outline="black")
    # 绘制产品名
    draw.text((int((img_width - color_width) / 2) - text_width_for - 2,
               int((color_height - text_height_for) / 2) - 2), test_prod, fill='black', font=font_label)
    # 绘制单位
    draw.text((color_width + int((img_width - color_width) / 2) + 2,
               int((color_height - text_height_back) / 2) - 2), test_unit, fill='black', font=font_label)
    return image
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------颜色渐变函数----------------------------------------------------
def gradient(color1, color2, steps):
    dr = (color2[0] - color1[0]) / steps
    dg = (color2[1] - color1[1]) / steps
    db = (color2[2] - color1[2]) / steps
    return [(int(color1[0] + i * dr), int(color1[1] + i * dg), int(color1[2] + i * db)) for i in range(steps)]
# ----------------------------------------------------------------------------------------------------------------------