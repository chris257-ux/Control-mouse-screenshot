# This is a sample Python script.
import os
import time
import pyautogui

imgpath = "E:\\clqImgDataSet\\红外数据治理\\标注影像\\其他项目\\SZJC-JQ2021-000006裕和大厦外墙面砖空鼓检测lts改xmh改-wsx"

# 改ima数量num
num = 28

def click_operation():
    """点击操作"""
    #改开始数字sta=第一个存储的命名
    sta = 143
    # 1pyautogui.moveTo(444, 180)
    pyautogui.moveTo(715, 130)

    # 点击
    pyautogui.click()
    # 延迟秒
    # time.sleep(num_seconds)
    # 2 pyautogui.moveTo(673, 502)
    pyautogui.moveTo(680, 500)
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.3)
    #3 img = pyautogui.screenshot(region=[9, 198, 1425, 503])  # x,y,w,h,1434-701
    img = pyautogui.screenshot(region=[281, 150, 799, 599])
    #----------------------------------------------------------------！！！！！！！！！！！！！！！！！！！需要改第一个命名！！！！！！！！！！！！！！！！！！！！！！
    img.save(os.path.join(imgpath, str(sta) + ".jpg"))
    # 延迟秒
    time.sleep(0.05)
    for i in range(num-1):
        # 鼠标需要移动到的位置（下一个）

        # 4 pyautogui.moveTo(120, 180)
        pyautogui.moveTo(390, 130)
        pyautogui.click()

        # 鼠标需要移动到的位置(清除分析） # 715,130   390，130
        # 5 x, y = 444, 180
        x, y = 715, 130
        # duration 鼠标移动时间
        # pyautogui.moveTo(x, y, duration=num_seconds)
        # 将鼠标移动到指定位置
        pyautogui.moveTo(x, y)
        # 点击
        pyautogui.click()
        # 延迟秒
        # time.sleep(num_seconds)
        # 6 pyautogui.moveTo(673, 502)
        pyautogui.moveTo(680, 500)
        time.sleep(0.3)
        pyautogui.click()

        # 7pyautogui.moveTo(120, 80)
        pyautogui.moveTo(390, 30)
        # imgpath = "D:\\images"
        # 8 img = pyautogui.screenshot(region=[9, 198, 1425, 503])  # x,y,w,h,1434-701,(281,150)-(1080,749)
        img = pyautogui.screenshot(region=[281, 150, 799, 599])
        # ----------------------------------------------------------------！！！！！！！！！！！！！！！！！！！需要改第二个开始的命名！！！！！！！！！！！！！！！！！！！！！！
        img.save(os.path.join(imgpath, str(i + sta+1) + ".jpg"))

if __name__ == '__main__':
    time.sleep(2)
    click_operation()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

