import time
import gpiod

# GPIO番号を変数に設定
gpio_num = 17

# チップの設定
chip = gpiod.Chip('gpiochip0')

# ピンの設定
line = chip.get_line(gpio_num)
line.request(consumer='my_app', type=gpiod.LINE_REQ_DIR_OUT)

try:
    while True:
        line.set_value(1)  # LED点灯
        time.sleep(1)  # 1秒間待つ
        line.set_value(0)  # LED消灯
        time.sleep(1)  # 1秒間待つ
except KeyboardInterrupt:
    pass
finally:
    line.release()