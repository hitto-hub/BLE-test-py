from bleak import BleakClient
import asyncio

# Xiaomi Smart Band 8のMACアドレス
device_address = "D0:62:2C:1E:39:AE"
# 通知を受け取るキャラクタリスティックのUUIDを指定（カスタムUUIDの一つを使います）
notify_characteristic_uuid = "00000003-0000-1000-8000-00805f9b34fb"  # 例としてカスタムUUID

# 通知を受け取るコールバック関数
def notification_handler(sender, data):
    print(f"通知データ (sender: {sender}): {data}")

async def enable_notifications(address):
    async with BleakClient(address) as client:
        if client.is_connected:
            print(f"デバイス {address} に接続しました")
            
            # 通知を有効化してデータを受け取る
            await client.start_notify(notify_characteristic_uuid, notification_handler)
            await asyncio.sleep(30)  # 30秒間通知を受け取る
            await client.stop_notify(notify_characteristic_uuid)

# asyncioを使って非同期関数を実行
asyncio.run(enable_notifications(device_address))
