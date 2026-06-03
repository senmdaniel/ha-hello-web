import logging
from homeassistant.helpers.entity import Entity
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class GregorianDateSensor(Entity):
    """Sensor voor de normale burgerlijke datum."""
    def __init__(self, provider):
        self._name = "Zmanim Pro Burgerlijke Datum"
        self._state = None
        self.provider = provider

    @property
    def name(self): return self._name
    @property
    def unique_id(self): return f"{DOMAIN}_gregorian_date"
    @property
    def state(self): return self._state
    @property
    def icon(self): return "mdi:calendar"

    def update(self):
        try:
            # Hier komt straks jouw eigen functie van de Pi:
            self._state = "03-06-2026" 
        except Exception as e:
            _LOGGER.error("Fout bij laden burgerlijke datum: %s", e)

class JewishDateSensor(Entity):
    """Sensor voor de Joodse / Hebreeuwse datum."""
    def __init__(self, provider):
        self._name = "Zmanim Pro Joodse Datum"
        self._state = None
        self.provider = provider

    @property
    def name(self): return self._name
    @property
    def unique_id(self): return f"{DOMAIN}_jewish_date"
    @property
    def state(self): return self._state
    @property
    def icon(self): return "mdi:calendar-star"

    def update(self):
        try:
            # Hier komt straks jouw eigen functie van de Pi:
            self._state = "3 Sivan 5786" 
        except Exception as e:
            _LOGGER.error("Fout bij berekenen Joodse datum: %s", e)
