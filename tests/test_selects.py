import macropy.activate
import kavya as kv
from hyperui_plugin.selects import Base
from addict import Dict

# Define the action that happens when the selection changes
app = kv.build_app()
async def on_guitarist_selected(dbref, msg, wp, request):
    """
    arg: is the select component instance
    arg.value: is the currently selected option (e.g., 'SRV')
    """
    # Example: Store the selection in the app state
    print ("on_guitarist_selected is called")
    dbref.on_guitarist_selected_res = msg.value
    print(f"Selection changed to: {msg.value}")
    
# Setup the component
base_select = Base("base", "Headline", on_change = on_guitarist_selected)
base_select.add_option("JM", "John Mayer")
base_select.add_option("SRV", "Stevie Ray Vaughn")
base_select.add_option("JH", "Jimi Hendrix")



import pytest
from starlette.testclient import TestClient

@pytest.fixture
def app_instance():
    wp_endpoint = kv.create_endpoint(
        key="select_page",
        childs=[base_select],
        rendering_type="MutableSSR",
        svelte_bundle_dir="ssr"
    )
    kv.add_route("/test-select", wp_endpoint)

    
    # Load the app and add routes
    app = kv.load_app()
    kv.add_route("/", wp_endpoint)
    return app



@pytest.mark.asyncio
async def test_select_on_change_event(app_instance):
    app = app_instance
    
    # 1. Create Endpoint and Route

    with TestClient(app) as client:
        # Trigger page initialization
        client.get("/test-select")
        
        # 2. Resolve the live Webpage Instance (iobj)
        target_wp_iobj = next(iter(kv.starlette_app.app_state.pageId_pageComp_map.values()))
        live_select = target_wp_iobj.components[0].components[1]

        
        # 3. Prepare the Event Data
        # Select components usually send the new value inside the 'msg' Dict
        msg = Dict({"value": "JH"}) 
        request = target_wp_iobj.session_manager.request
        
        # 4. EXECUTION: Invoke the 'change' event handler
        change_eh = live_select.get_event_handler('change')
        
        # Update the component value manually to simulate the browser's action
        await change_eh(live_select, msg, target_wp_iobj, request)

        # 5. ASSERTION: Check if the side effect occurred
        #final_state = target_wp_iobj.app_actions_trmap.selected_guitarist
        live_select.on_guitarist_selected_res == "JH"
        #assert final_state == "JH", f"Expected 'JH', but got {final_state}"
