import RPi.GPIO as GPIO  # RPi.GPIOライブラリをインポート
import time              # timeライブラリをインポート

GPIO.setmode(GPIO.BCM)  # ピン番号をGPIO番号で指定することを宣言

LED_PIN = 17             # LEDが接続されているGPIOの番号。必要に応じて更可能。

GPIO.setup(LED_PIN, GPIO.OUT)  # LED_PINを出力モードに設定

try:
    while True:                 # 無限ループ
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED_PINに高電圧を出力（LED点灯）
        time.sleep(1)           # 1秒待つ

        GPIO.output(LED_PIN, GPIO.LOW)   # LED_PINに低電圧を出力（LED消灯）
        time.sleep(1)           # 1秒待つ

except KeyboardInterrupt:       # CTRL+Cが押された場合の処理
    pass                        # 何もしない

GPIO.cleanup()                  # GPIO設定をリセット