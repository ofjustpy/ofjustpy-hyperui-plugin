from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from hyperui_plugin.progress import  (withValue, withValueCentered)
from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from time import sleep


progress_frame, update_bar = withValue("pb", 33.33)
progress_frame_ctr, update_bar_ctr = withValueCentered("pbctr", 33.33)

app = oj.load_app()
pc_values = [8.33,
                         16.66,
                         16.66,
                         20,
                         25,
                         33.33,
                         33.33,
                         40,
                         41.66,
                         50,
                         50,
                         58.33,
                         60,
                         66.66,
                         66.66,
                         75,
                         75,
                         83.33,
                         91.66,
                         100]

idx = 0
def on_btn_click(dbref, msg, to_ms):
    global  idx
    print("page rendered and now ready to display")
    update_bar(pc_values[idx], msg.page, to_ms)
    idx = idx + 1
    idx = idx%len(pc_values)

    # for i in range(0, 20):
    #     update_bar(pc_values[i], msg.page, to_ms)
    #     sleep(2)
        
    pass

progress_btn = oj.AC.Button(key="progressor", text="Click to advance the progress bar ",  on_click=on_btn_click)


def on_btn_click_ctr(dbref, msg, to_ms):
    global  idx
    print("page rendered and now ready to display")
    update_bar_ctr(pc_values[idx], msg.page, to_ms)
    idx = idx + 1
    idx = idx%len(pc_values)

    # for i in range(0, 20):
    #     update_bar(pc_values[i], msg.page, to_ms)
    #     sleep(2)
        
    pass

progress_btn_ctr = oj.AC.Button(key="progressor_ctr", text="Click to advance the progress bar ",  on_click=on_btn_click_ctr)




endpoint = oj.create_endpoint("demo_progress bar",
                              childs = [oj.HCCMutable.Container(childs=[progress_frame,
                                                                        progress_btn,
                                                                        progress_frame_ctr,
                                                                        progress_btn_ctr
                                                                        ],
                                                        twsty_tags=[mr/x/auto, space/y/8]
                                                        )
                                        ],
                              title="Demo progress bar"

                   )
oj.add_jproute("/", endpoint)
