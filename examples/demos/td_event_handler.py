from py_tailwind_utils import *

from html_writer.macro_module import macros, writer_ctx
import ofjustpy  as oj


def on_click(dbref, msg, to_ms):
    print("btn clicked")
    pass

app = oj.load_app()

with writer_ctx:
    with Div(classes="bg-green-100") as comp_box:
        with Button(key="abtn", classes="bg-green-100", text="Click Me", on_click=on_click):
            pass
        

endpoint = oj.create_endpoint("event handling",
                              childs = [oj.PC.Container(childs=[comp_box
                                                                ],
                                                        twsty_tags=[mr/x/auto]
                                                        )

                                        ],
                              title="Event handling"
                              )
oj.add_jproute("/", endpoint)
