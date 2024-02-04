from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx
import ofjustpy  as oj
app = oj.load_app()


def on_click(dbref, msg, to_ms):
    ms_dbref = to_ms(dbref)
    # change background color to green-500 and font size to text-xl
    ms_dbref.add_twsty_tags(bg/green/5, fz.xl)
    pass



with writer_ctx:
    with HCCMutable_Div(classes="bg-green-100") as comp_box:
        with Mutable_Button(key="abtn", classes="bg-green-100", text="Click Me", on_click=on_click):
            pass
        

endpoint = oj.create_endpoint("Interactive_Webpage",
                     
         childs = [oj.HCCMutable.Container(childs=[comp_box
                                                                ],
                                                        twsty_tags=[mr/x/auto]
                                                        )

                                        ],
                              title="Interactive Webpage"
                              )
oj.add_jproute("/", endpoint)
