from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
import ofjustpy as oj
from py_tailwind_utils import conc_twtags, tstr
from html_writer.macro_module import macros, writer_ctx

def Simple():
    with writer_ctx:
        with Div(classes="inline-flex -space-x-px overflow-hidden rounded-md border bg-white shadow-sm") as comp_box:
            pass
    def add_button(key, comp_box=comp_box, **kwargs):
        with writer_ctx:
            with Button(key=key, classes= "inline-block px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 focus:relative", **kwargs) as abtn:
                pass
        comp_box.components.append(abtn)

    comp_box.add_button = add_button
    return comp_box


def WithIcons():
    with writer_ctx:
        with Div(classes="inline-flex overflow-hidden rounded-md border bg-white shadow-sm") as comp_box:
            pass
    def add_button(key, title, icon, comp_box=comp_box, **kwargs):
        with writer_ctx:
            with Button(key=key, title=title, classes= "inline-block px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 focus:relative", **kwargs) as abtn:
                with Span(classes="sr-only", text=title):
                    pass
                pass
        abtn.components.append(icon())
        comp_box.components.append(abtn)

    comp_box.add_button = add_button
    return comp_box

