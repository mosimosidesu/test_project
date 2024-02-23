import time
import gpiozero

# GPIOピン番号を指定
gpio_pin_number = 17

# LEDを指定したGPIOピンに接続
led = gpiozero.LED(gpio_pin_number)

while True:
    led.on()  # LEDを点灯
    time.sleep(1)  # 1秒待つ
    led.off()  # LEDを消灯
    time.sleep(1)  # 1秒待つ
