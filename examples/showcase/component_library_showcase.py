from py_tailwind_utils import *
import macropy.activate 
import kavya as kv
kv.set_style("un")
from component_demo_boxes import (alert_box,
                                  badges_box,
                                  breadcrumbs_box,
                                  buttongroups_box,
                                  detailslist_box,
                                  dividers_box,
                                  errorpages_box,
                                  inputs_box,
                                  loginforms_box,
                                  mediaalerts_box,
                                  pagination_box,
                                  selects_box,
                                  sideMenu_box,
                                  stats_box,
                                  steps_box,
                                  tables_box,
                                  tabs_box,
                                  textarea_box,
                                  toggles_box 
                                        )
from hyperui_plugin.sideMenu import  (Simple as SimpleSideMenu,
                                      )

app = kv.load_app()
endpoint = kv.create_endpoint("hyperui_component_ui_library",
                     
         childs = [kv.HM.StackH(childs = [#WsideMenu,
                                          kv.HM.Container(childs=[alert_box,
                                                                  badges_box,
                                                                  breadcrumbs_box,
                                                                  buttongroups_box,
                                                                  detailslist_box,
                                                                  dividers_box,
                                                                  errorpages_box,
                                                                  inputs_box,
                                                                  loginforms_box,
                                                                  mediaalerts_box,
                                                                  pagination_box,
                                                                  selects_box,
                                                                  sideMenu_box,
                                                                  stats_box,
                                                                  steps_box,
                                                                  tables_box,
                                                                  tabs_box,
                                                                  textarea_box,
                                                                  toggles_box 
                                                                  ],
                                                          twsty_tags=[mr/x/auto]
                                                          )
                                          
                                          ],
                                )
                   ],
         title="HyperUI component library",
         body_classes="font-geist",
         rendering_type="MutableSSR",
         svelte_bundle_dir="ssr"
         #page_ready = on_page_ready
                              )

kv.add_route("/hyperui", endpoint)
# from starlette.testclient import TestClient
# with TestClient(app) as client:
#     # Trigger the route defined in the fixture
#     response = client.get("/hyperui")
