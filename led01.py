import time
import gpiozero

# GPIOピン番号を指定
gpio_pin_number = 17
# 待ち時間１
wait_time1 = 0.5
# 待ち時間２
wait_time2 = 1


# LEDを指定したGPIOピンに接続
led = gpiozero.LED(gpio_pin_number)

while True:
    led.on()  # LEDを点灯
    time.sleep(wait_time2)  # 待つ
    led.off()  # LEDを消灯
    time.sleep(wait_time1)  # 待つ