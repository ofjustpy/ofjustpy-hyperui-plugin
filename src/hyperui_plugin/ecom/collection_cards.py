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

# TODO: we need to figure out how to use relative
def Simple(title, para, img_src, alt="", ):
    with writer_ctx:
        with A(href="#", classes="group block") as tlb:
            with Div(classes="relative h-80 sm:h-96"):
                with Img(src=img_src,
                         alt=alt,
                         classes="absolute inset-0 h-full w-full object-cover opacity-100 group-hover:opacity-0"):
                    pass
                with Img(src=img_src,
                         alt=alt,
                         classes="absolute inset-0 h-full w-full object-cover opacity-0 group-hover:opacity-100"):
                    pass

            
            with Div(classes="mt-3"):
                with H3(classes="text-sm text-gray-700 group-hover:underline group-hover:underline-offset-4", text=title):
                    pass
                with P(classes="mt-1.5 max-w-24 text-xs text-gray-500",
                       text=para):
                    pass
                    
    return tlb
# TODO: we need to figure out how to use relative with A classesj
def ContentInside(title, para, img_src, alt="#"):
    with writer_ctx:
        with A(href="#", classes="group w-1/3 block") as tlb:
            with Div(classes="relative", extra_classes="h-[350px] sm:h-[450px]"):
                with Img(src=img_src,
                         alt=alt,
                         classes="absolute inset-0 h-full w-full object-cover opacity-100 group-hover:opacity-0"):
                    pass
                with Img(src=img_src,
                         alt=alt,
                         classes="absolute inset-0 h-full w-full object-cover opacity-0 group-hover:opacity-100"):
                    pass

            
            with Div(classes="absolute inset-0 flex flex-col items-start justify-end p-6"):
                with H3(classes="text-xl font-medium text-white", text=title):
                    pass
                with P(classes="mt-1.5 max-w-24 text-xs text-gray-500",
                       text=para):
                    pass
                    
    return tlb

