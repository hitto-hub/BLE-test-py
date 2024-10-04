# キャラクタリスティックUUID全表示
from bleak import BleakClient
import asyncio

# Xiaomi Smart Band 8のMACアドレス
device_address = "D0:62:2C:1E:39:AE"
# Inspire 3
# device_address = "E4:2B:7D:0A:28:A3"

# 非同期関数を定義
async def connect_and_get_data(address):
    async with BleakClient(address) as client:
        # 接続が確立したか確認
        if client.is_connected:
            print(f"デバイス {address} に接続しました")

            # サービスを取得
            services = await client.get_services()
            print("サービスの一覧:")
            for service in services:
                print(f"  サービスUUID: {service.uuid}")
                for char in service.characteristics:
                    print(f"    キャラクタリスティックUUID: {char.uuid}")
            
            # 必要に応じてキャラクタリスティックを読み取る
            # 心拍数などのデータを読み取る場合、適切なUUIDを指定
            # data = await client.read_gatt_char(characteristic_uuid)
            # print(f"データ: {data}")

# asyncioを使って非同期関数を実行
asyncio.run(connect_and_get_data(device_address))
