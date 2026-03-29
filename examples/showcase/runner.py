from py_tailwind_utils import *
import kavya as kv
kv.set_style("un")

from hyperui_plugin.sideMenu import  (Simple as SimpleSideMenu,
                                                )
app = kv.load_app()
sideMenu = SimpleSideMenu("HyperUI components")

with kv.uictx("tluictx") as tlctx:
    async def on_hui_comp_selected(dbref, msg, wp, request):
        target_of = wp.session_manager.target_of
        comp_deck_box_ms = target_of(tlctx.comp_deck_box)
        comp_deck_box_ms.bring_to_front(tlctx.alerts.id)
        comp_deck_box_ms.bring_to_front(f"/{dbref.value}")
        pass

    async def on_page_ready(dbref, msg, wp, request):
        target_of = wp.session_manager.target_of
        comp_deck_box_ms = target_of(tlctx.comp_deck_box)
        # there is some bug in rendering vertical menu button
        # this is a work around to reset it on page_reload
        comp_deck_box_ms.bring_to_front("/Alerts")
        pass

    sideMenu.add_flat_item("selects", "Selects", value="Selects", on_click=on_hui_comp_selected)
        
    
    pass
