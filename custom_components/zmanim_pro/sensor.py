from datetime import timedelta
from homeassistant.helpers.entity import Entity

from .date_provider import DateProvider
from .sensors_data import GregorianDateSensor, JewishDateSensor
from .sensors_feestdagen import JewishHolidaySensor
from .sensors_tijden import ZmanimTimeSensor

SCAN_INTERVAL = timedelta(minutes=30)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Zet alle Zmanim Pro sensoren klaar."""
    provider = DateProvider()
    
    lijst_van_sensoren = [
        # 1. Data sensoren
        GregorianDateSensor(provider),
        JewishDateSensor(provider),
        
        # 2. Feestdagen sensor
        JewishHolidaySensor(provider),
        
        # 3. Tijden sensoren (gekoppeld aan jouw berekeningen)
        ZmanimTimeSensor(provider, "shkia", "Shkia (Zonsondergang)", "mdi:weather-sunset"),
        ZmanimTimeSensor(provider, "chatzos", "Chatzos (Middag)", "mdi:weather-sunny"),
        ZmanimTimeSensor(provider, "sof_zman_krias_shema", "Krias Shema (Grá)", "mdi:book-open-variant", "gra"),
        ZmanimTimeSensor(provider, "sof_zman_krias_shema", "Krias Shema (Magen Avraham)", "mdi:book-open-page-variant", "magen_avraham"),
        ZmanimTimeSensor(provider, "sof_zman_tefila", "Sof Zman Tefila (Grá)", "mdi:clock-outline", "gra"),
        ZmanimTimeSensor(provider, "sof_zman_tefila", "Sof Zman Tefila (Magen Avraham)", "mdi:clock-check-outline", "magen_avraham"),
        ZmanimTimeSensor(provider, "plag_hamincha", "Plag HaMincha (Grá)", "mdi:weather-sunset-down", "pla_gra"),
        ZmanimTimeSensor(provider, "plag_hamincha", "Plag HaMincha (Magen Avraham)", "mdi:weather-sunset-up", "plag_magen_avraham")
    ]
    
    async_add_entities(lijst_van_sensoren, True)
