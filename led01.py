import time
import gpiozero

# LEDをGPIO18ピンに接続
led = gpiozero.LED(17)

# while True:
    led.on()  # LEDを点灯
    time.sleep(1)  # 1秒待つ
    led.off()  # LEDを消灯
    time.sleep(1)  # 1秒待つ
