import random
import time
import pyautogui
import os

from screen_information_judgment import locate_template_on_screen

# 自定义函数导入
import sys
sys.path.append(r'src')
import window_status

# 鼠标模拟点击函数

def click_random_point_in_ellipse(bounding_box, delay=0.2, debug=False):
    '''
    可以接受locate_template_on_screen()函数的输出，然后在其中的一点进行鼠标模拟点击操作
    '''
    if bounding_box is None:
        if debug:
            print("❌ 未找到目标区域，跳过点击")
        return

    x, y, w, h = bounding_box
    if w <= 0 or h <= 0:
        if debug:
            print("⚠️ 无效的区域尺寸")
        return

    cx, cy = x + w / 2, y + h / 2
    a, b = w / 2, h / 2

    # 生成椭圆内随机点
    for _ in range(100):  # 最多重试100次
        rx = random.uniform(-a, a)
        ry = random.uniform(-b, b)
        if (rx / a) ** 2 + (ry / b) ** 2 <= 1:
            click_x = int(cx + rx)
            click_y = int(cy + ry)
            if debug:
                print(f"🖱️ 尝试点击: ({click_x}, {click_y})")
            time.sleep(delay)  # 可选延迟
            pyautogui.moveTo(click_x, click_y)  # 显式移动（便于观察）
            pyautogui.click(click_x, click_y)
            return

    if debug:
        print("⚠️ 未能在椭圆内生成有效点击点")
# 调试
bbox = locate_template_on_screen(r'assets\screenshot_comparison_4K_100\arm\ice_ore_collector_F1.png',
                                 threshold=float(os.getenv('is_state_active_threshold', 0.8)))
click_random_point_in_ellipse(bbox)
