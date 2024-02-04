import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import (conc_twtags,
                               tstr,
                               pd,
                               grow,
                               bg,
                               green,
                               W,
                               fc,
                               gray,
                               space,
                               y,
                               mr,
                               st,
                               srs,
                               ta)

from html_writer.macro_module import macros, writer_ctx

def BackgroundAccentBorder():
    with writer_ctx:
        with Div(classes="space-y-4") as comp_box:
            pass
        
    def add_faq_item(question, answer, comp_box=comp_box):
        with writer_ctx:
            with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as faq_box:
                with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 rounded-lg bg-gray-50 p-4 text-gray-900"):
                    with H2(classes="font-medium", text=question):
                        pass

                    with Icon_Plus():
                        pass
                    
                with P(classes="mt-4 px-4 leading-relaxed text-gray-700", text=answer):
                    pass
                
            pass
        comp_box.components.append(faq_box)
        return

    
    comp_box.add_faq_item = add_faq_item
    return comp_box


