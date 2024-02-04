from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
import ofjustpy as oj
from py_tailwind_utils import conc_twtags, tstr
from html_writer.macro_module import macros, writer_ctx

def Detailslist(striped=False, contained=False):
    contained_classes = ""
    if contained:
        contained_classes = "rounded-lg border border-gray-100 py-3 shadow-sm"

    with writer_ctx:
        with Div(classes=f"flow-root {contained_classes}") as comp_box:
            with Dl(classes="-my-3 divide-y divide-gray-100 text-sm") as dl_box:
                pass
            pass
        

    extra_classes = ""
    if striped:
        extra_classes="even:bg-gray-50"
    def add_item(key, value, dl_box=dl_box, **kwargs):
        
        with writer_ctx:
            with Div(classes=f"grid grid-cols-1 gap-1 py-3 {extra_classes} sm:grid-cols-3 sm:gap-4") as item_box:
                with Dt(classes="font-medium text-gray-900", text=key):
                    pass
                with Dd(classes="text-gray-700 sm:col-span-2", text=value):
                    pass

        dl_box.components.append(item_box)

    comp_box.add_item = add_item

    return comp_box



        

