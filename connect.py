from bleak import BleakClient

address = "デバイスのMACアドレス"
characteristic_uuid = "取得したキャラクタリスティックUUID"  # 例: "00002a37-0000-1000-8000-00805f9b34fb"

async def read_characteristic(address, characteristic_uuid):
    async with BleakClient(address) as client:
        value = await client.read_gatt_char(characteristic_uuid)
        print(f"Received data: {value}")

import asyncio
asyncio.run(read_characteristic(address, characteristic_uuid))
