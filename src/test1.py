# 総なめ
from bleak import BleakClient
import asyncio

# Xiaomi Smart Band 8のMACアドレス
device_address = "D0:62:2C:1E:39:AE"
# Inspire 3 のMACアドレス
# device_address = "E4:2B:7D:0A:28:A3"

async def read_all_characteristics(address):
    async with BleakClient(address) as client:
        if client.is_connected:
            print(f"デバイス {address} に接続しました")
            
            # サービスとキャラクタリスティックを取得
            services = await client.get_services()
            for service in services:
                print(f"サービスUUID: {service.uuid}")
                for char in service.characteristics:
                    print(f"  キャラクタリスティックUUID: {char.uuid}")
                    try:
                        # キャラクタリスティックが読み取り可能か確認
                        if "read" in char.properties:
                            value = await client.read_gatt_char(char.uuid)
                            print(f"    読み取り値: {value}")
                        else:
                            print(f"    読み取り不可")
                    except Exception as e:
                        print(f"    エラー: {e}")

# asyncioを使って非同期関数を実行
asyncio.run(read_all_characteristics(device_address))
