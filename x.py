import os
# 导入模块
from app import book
from app import entodo
from app import pomodoro

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# 示例调用
def main():

    # 定义颜色：模仿苹果官网风格
    WHITE = '\033[38;5;15m'       # 白色（主要文本色）
    LIGHT_GRAY = '\033[38;5;245m' # 浅灰色（次要信息）
    GREEN = '\033[38;5;34m'       # 柔和绿色（已完成）
    ORANGE = '\033[38;5;214m'     # 柔和橙色（未完成）
    BLUE = '\033[38;5;75m'        # 蓝色（用户输入提示）
    RESET = '\033[0m'             # 重置颜色

    clear()  # 清除屏幕
    while True:
        # 提供选项
        print(f"{LIGHT_GRAY}欢迎使用英语每日任务、番茄时钟、读书记录的整合工具！{RESET}") 
        entodo.show_today_task()
        print(f"\n请选择操作：")
        print(f"{GREEN}1. 英语每日任务{RESET}")  # 柔和橙色
        print(f"{GREEN}2. 番茄时钟{RESET}")  # 柔和橙色
        print(f"{GREEN}3. 读书记录{RESET}")  # 柔和橙色
        print(f"{GREEN}4. 退出程序{RESET}")  # 柔和橙色


        choice = input(f"请输入选择 (1/2/3/4): ").strip()

        if choice == "1":
            clear()  # 清除屏幕
            # 分隔符
            print("-" * (2 * 40))
            print("运行英语每日任务中...")
            # 调用 entodo.py 中的功能
            entodo.main()
        elif choice == "2":
            clear()  # 清除屏幕
            # 分隔符
            print("-" * (2 * 40))
            print("运行番茄时钟任务中...")
            # 调用 pomodoro.py 中的功能
            pomodoro.main()
        elif choice == "3":
            clear()  # 清除屏幕
            # 分隔符
            print("-" * (2 * 40))
            print("运行读书记录任务中...")
            # 调用 book.py 中的功能
            book.main()
        elif choice == "4":
            clear()  # 清除屏幕
            print("退出程序...")
            break
        else:
            # clear()  # 清除屏幕
            # 分隔符
            print("-" * (2 * 40))
            print("无效选择，请重新输入。")

if __name__ == "__main__":
    main()
