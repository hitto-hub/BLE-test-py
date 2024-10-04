from bleak import BleakScanner
import asyncio

# 非同期関数を定義
async def run():
    # BLEデバイスをスキャンし、発見したデバイスのリストを取得
    devices = await BleakScanner.discover(return_adv=True)
    
    # 発見したデバイスを1つずつループし、デバイス情報を表示
    for d, adv in devices.values():
        print(f"デバイスのMACアドレス: {d.address}")
        if adv.local_name:
            print(f"デバイス名: {adv.local_name}")
        if adv.service_uuids:
            print(f"サービスUUID: {adv.service_uuids}")
        print(f"RSSI: {adv.rssi}")
        print("-----------------------------")

# asyncioを使って非同期関数を実行
asyncio.run(run())
