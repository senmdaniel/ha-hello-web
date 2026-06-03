import logging
from homeassistant.helpers.entity import Entity
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

# Jouw eigen EVENTS woordenboek ingebouwd in de sensor logica
EVENTS = {
    (1, 14): "12_erev_pesach",
    (1, 15): "13_pesach_1",
    (1, 16): "14_pesach_2",
    (1, 20): "15_erev_pesach_6",
    (1, 21): "16_pesach_7",
    (1, 22): "17_pesach_8",

    (3, 5): "18_erev_shavuot",
    (3, 6): "19_shavuot_1",
    (3, 7): "20_shavuot_2",

    (6, 29): "1_erev_rosh_hashanah",
    (7, 1): "2_rosh_hashanah_1",
    (7, 2): "3_rosh_hashanah_2",

    (7, 9): "4_erev_yom_kippur",
    (7, 10): "5_yom_kippur",

    (7, 14): "6_erev_sukkot",
    (7, 15): "7_sukkot_1",
    (7, 16): "8_sukkot_2",
    (7, 21): "9_erev_shemini_atzeret",
    (7, 22): "10_shemini_atzeret",
    (7, 23): "11_simchat_torah",
}

class JewishHolidaySensor(Entity):
    """Sensor die de huidige Joodse feestdag weergeeft."""

    def __init__(self, provider):
        self._name = "Zmanim Pro Joodse Feestdag"
        self._state = "Geen feestdag"
        self.provider = provider

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return f"{DOMAIN}_jewish_holiday"

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return "mdi:synagogue"

    def update(self):
        """Kijk of er vandaag een feestdag is op basis van de Joodse datum."""
        try:
            # We halen de huidige Joodse maand en dag op via jouw provider
            # PAS DIT AAN: Roep de functies aan die de cijfers (int) teruggeven
            h_month = self.provider.get_current_jewish_month() # Voorbeeld
            h_day = self.provider.get_current_jewish_day()     # Voorbeeld
            
            # Zoek de feestdag op in jouw EVENTS lijst
            holiday = EVENTS.get((h_month, h_day))
            
            if holiday:
                # Vervang eventuele underscores door spaties en maak netjes kapitaal
                self._state = holiday.split("_", 1)[-1].replace("_", " ").title()
            else:
                self._state = "Geen feestdag"
                
        except Exception as e:
            _LOGGER.error("Fout bij het ophalen van de Joodse feestdag: %s", e)
            self._state = "Fout bij berekenen"
