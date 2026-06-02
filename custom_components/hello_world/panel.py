from homeassistant.components.frontend import add_extra_js_url

async def async_setup_panel(hass):
    hass.http.register_static_path(
        "/hello-world",
        hass.config.path("custom_components/hello_world/www"),
        cache_headers=False,
    )

    hass.components.frontend.async_register_built_in_panel(
        hass,
        component_name="iframe",
        sidebar_title="Hello World",
        sidebar_icon="mdi:web",
        frontend_url_path="hello-world",
        config={
            "url": "/hello-world/index.html"
        },
    )
