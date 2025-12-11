import tkinter as tk
import random
import threading
import time

def show_warn_tip():
    # 创建窗口
    window = tk.Tk()

    # 获取屏幕宽高
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 缩小窗口尺寸，让更多窗口能铺满屏幕
    window_width = 250   # 宽度更小
    window_height = 80   # 高度更小
    x = random.randrange(0, screen_width - window_width)
    y = random.randrange(0, screen_height - window_height)

    # 设置窗口标题和位置
    window.title("提示")
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 提示文字列表（节选，可自由添加）
    tips = [
        "愿你被世界温柔以待", "平安喜乐，万事顺心", "心中有光，生活有暖",
        "所有的美好如期而至", "愿你每天都有好心情", "岁月静好，温暖如初",
        "愿你被爱包围，被幸福环绕", "前程似锦，未来可期", "天天开心，笑口常开",
        "心想事成，美梦成真", "愿你的人生充满阳光", "温暖相伴，快乐相随",
        "岁岁年年如约而至", "愿你眼中总有光芒", "活成自己想要的模样",
        "愿你三冬暖，愿你春不寒", "愿你天天开心", "早安好心情，晚安好梦境"
    ]

    # 随机选择提示语
    tip = random.choice(tips)

    # 背景颜色列表
    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender', 'lightyellow',
        'plum', 'coral', 'bisque', 'aquamarine', 'mistyrose', 'honeydew',
        'peachpuff', 'paleturquoise', 'lavenderblush', 'oldlace', 'lemonchiffon',
        'lightcyan', 'lightgray', 'lightsalmon', 'lightseagreen',
        'lightskyblue', 'lightslategrey', 'lightsteelblue', 'lightgoldenrodyellow'
    ]

    bg = random.choice(bg_colors)

    # 调整字体大小以适应窗口
    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=("微软雅黑", 15),
        width=25,
        height=5
    ).pack()

    # 置顶显示
    window.attributes('-topmost', True)

    # 自动关闭（避免资源占用）
    window.after(6000, window.destroy)

    window.mainloop()


if __name__ == "__main__":
    # 根据屏幕大小估算需要的窗口数量
    window_count = 300  # 例如 1920x1080 下约 231 个，这里多开一些保证满屏

    # 快速创建多个窗口
    for i in range(window_count):
        t = threading.Thread(target=show_warn_tip)
        t.daemon = True
        t.start()
        time.sleep(0.01)  # 控制创建间隔

    # 保持主程序运行
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass