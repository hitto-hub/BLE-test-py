from bleak import BleakClient

address = "デバイスのMACアドレス"  # 例: "XX:XX:XX:XX:XX:XX"

async def discover_services(address):
    async with BleakClient(address) as client:
        # サービス一覧の取得
        services = await client.get_services()
        for service in services:
            print(f"Service: {service.uuid}")
            # 各サービスに含まれるキャラクタリスティックを表示
            for characteristic in service.characteristics:
                print(f"  Characteristic: {characteristic.uuid}, Properties: {characteristic.properties}")

import asyncio
asyncio.run(discover_services(address))
