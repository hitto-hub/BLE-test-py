from bleak import BleakClient
import asyncio

device_address = "D0:62:2C:1E:39:AE"
# 通知可能なキャラクタリスティックUUID（例として選択）
notify_characteristic_uuid = "0000005a-0000-1000-8000-00805f9b34fb"

def notification_handler(sender, data):
    print(f"通知データ (sender: {sender}): {data}")

async def enable_notifications(address, characteristic_uuid):
    async with BleakClient(address) as client:
        if client.is_connected:
            print(f"デバイス {address} に接続しました")
            
            # 通知を有効化してデータを受け取る
            await client.start_notify(characteristic_uuid, notification_handler)
            await asyncio.sleep(30)  # 30秒間通知を受け取る
            await client.stop_notify(characteristic_uuid)

# asyncioを使って非同期関数を実行
asyncio.run(enable_notifications(device_address, notify_characteristic_uuid))
