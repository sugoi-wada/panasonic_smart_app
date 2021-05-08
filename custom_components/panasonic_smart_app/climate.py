from .entity import PanasonicClimate
from .const import DOMAIN, DEVICE_TYPE_AC, DATA_CLIENT, DATA_COORDINATOR


async def async_setup_entry(hass, entry, async_add_entities) -> bool:
    client = hass.data[DOMAIN][entry.entry_id][DATA_CLIENT]
    coordinator = hass.data[DOMAIN][entry.entry_id][DATA_COORDINATOR]
    devices = coordinator.data
    climate = []

    for device in devices:
        if int(device["Devices"][0]["DeviceType"]) == DEVICE_TYPE_AC:
            climate.append(
                PanasonicClimate(
                    client,
                    device,
                )
            )

    async_add_entities(climate, True)

    return True