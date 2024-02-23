#timeモジュールをインポート
import time

#RPi.GPIOモジュールをインポート
import RPi.GPIO as GPIO

# LED1はGPIO17
LED1=17

# 待ち時間
wait1=0.5
wait2=1

# BCM(GPIO番号)で指定する設定
GPIO.setmode(GPIO.BCM)

# GPIO17を出力モード設定
GPIO.setup(LED1, GPIO.OUT)

while True:

  # GPIO17の出力をHIGHにして、LED点灯
  GPIO.output(LED1, GPIO.HIGH)

  # 待つ
  time.sleep(wait2)

  # GPIO17の出力をLOWにして、LED点灯
  GPIO.output(LED1, GPIO.LOW)

  # 待つ
  time.sleep(wait1)
