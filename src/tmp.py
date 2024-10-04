from bleak import BleakClient
import asyncio

device_address = "D0:62:2C:1E:39:AE"

async def list_services(address):
    async with BleakClient(address) as client:
        if client.is_connected:
            print(f"デバイス {address} に接続しました")
            services = await client.get_services()
            for service in services:
                print(f"サービスUUID: {service.uuid}")
                for char in service.characteristics:
                    print(f"  キャラクタリスティックUUID: {char.uuid}, プロパティ: {char.properties}")

# asyncioを使って非同期関数を実行
asyncio.run(list_services(device_address))
