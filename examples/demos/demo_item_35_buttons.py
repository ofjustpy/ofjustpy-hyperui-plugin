import macropy.activate 
import hyperui_plugin as hui


from py_tailwind_utils import *

import kavya as kv
kv.set_style("un")
app = kv.load_app()
render_rst_btn = hui.revealHiddenStaticBorderOnHoverBordered(key="render_rst_btn",
                                                             text="Render Rst")



endpoint = kv.create_endpoint("buttons",
                              childs = [
                                  render_rst_btn
                                        ],
                              title="Side Menu",
                              svelte_bundle_dir="ssr",
                              rendering_type = "MutableSSR",
                              skeleton_data_theme = "seafoam",
                              )
kv.add_route("/", endpoint)
