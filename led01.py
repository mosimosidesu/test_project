import time
import gpiozero

# GPIOピン番号を指定
gpio_pin_number1 = 17
gpio_pin_number2 = 27
# 待ち時間１
wait_time1 = 0.5
# 待ち時間２
wait_time2 = 1


# LEDを指定したGPIOピンに接続
led1 = gpiozero.LED(gpio_pin_number1)
led2 = gpiozero.LED(gpio_pin_number2)

while True:
    led1.on()  # LEDを点灯
    time.sleep(wait_time1)  # 待つ
    led1.off()  # LEDを消灯
    led2.on()  # LEDを点灯
    time.sleep(wait_time1)  # 待つ
    led2.off()  # LEDを消灯
