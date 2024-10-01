# 必要なライブラリ`bleak`からBleakScannerクラスをインポート
from bleak import BleakScanner

# runという非同期関数を定義
async def run():
    # BLEデバイスをスキャンし、発見したデバイスのリストを取得
    devices = await BleakScanner.discover()
    # 発見したデバイスを1つずつループし、デバイス情報を表示
    for d in devices:
        print(d)

# Pythonの非同期処理ライブラリ`asyncio`をインポート
import asyncio
# asyncioを使って非同期関数runを実行
asyncio.run(run())
