import { LitElement, html } from "https://unpkg.com";
import { KosherZmanim } from "https://esm.sh";

class HaZmanimProCard extends LitElement {
  static get properties() {
    return { hass: { type: Object } };
  }

  setConfig(config) {}

  render() {
    const vandaag = new Date();

    // Exacte locatie-instellingen voor Antwerpen (overgenomen uit uw Pi-project)
    const opties = {
      date: vandaag,
      timeZoneId: "Europe/Brussels",
      latitude: 51.2194,
      longitude: 4.4025,
      elevation: 0
    };

    // Bereken alle uitgebreide Zmanim live zonder Raspberry Pi!
    const complexZmanim = KosherZmanim.getZmanimJson(opties);
    const zmanimData = complexZmanim.zmanim;

    // We bouwen exact de vertrouwde JSON-structuur op die u gewend bent
    const apiOutput = {
      status: {
        api_bron: "Home Assistant (Lovelace Engine)",
        raspberry_pi: "Uitgeschakeld & Offline",
        actieve_stad: "Antwerp",
        land: "Belgium",
        coordinaten: {
          latitude: opties.latitude,
          longitude: opties.longitude
        }
      },
      nederlandse_klok: {
        dag: vandaag.toLocaleDateString('nl-NL', { weekday: 'long' }),
        datum: vandaag.toLocaleDateString('nl-NL', { day: 'numeric', month: 'long', year: 'numeric' }),
        tijd: vandaag.toLocaleTimeString('nl-NL')
      },
      zmanim: {
        alos_hashachar: zmanimData.AlosHashachar,
        netz_hachamah_sunrise: zmanimData.Sunrise,
        sof_zman_krias_shema_mga: zmanimData.SofZmanShmaMGA,
        sof_zman_krias_shema_gra: zmanimData.SofZmanShmaGRA,
        sof_zman_tefilah_gra: zmanimData.SofZmanTfilaGRA,
        chatzos_midday: zmanimData.Chatzos,
        mincha_gedolah: zmanimData.MinchaGedolah,
        mincha_ketanah: zmanimData.MinchaKetana,
        plag_hamincha: zmanimData.PlagHamincha,
        shkias_hachamah_sunset: zmanimData.Sunset,
        tzeis_hakochavim: zmanimData.Tzeis
      }
    };

    return html`<pre style="white-space: pre-wrap; font-family: monospace; padding: 10px;">${JSON.stringify(apiOutput, null, 2)}</pre>`;
  }
}

customElements.define('pi-zmanim-card', HaZmanimProCard);
