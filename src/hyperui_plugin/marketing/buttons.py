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



def Simple_Solid(key, label, href="#", **kwargs, ):
    with writer_ctx:
        with A(classes='inline-block rounded border border-indigo-600 bg-indigo-600 px-12 py-3 text-sm font-medium text-white hover:bg-transparent hover:text-indigo-600 focus:outline-none focus:ring active:text-indigo-500', href=href, text=label, **kwargs) as comp_box:
            pass

    return comp_box
            
def Simple_Blank(key, label, href="#", **kwargs, ):
    with writer_ctx:
        with A(classes='inline-block rounded border border-indigo-600 px-12 py-3 text-sm font-medium text-indigo-600 hover:bg-indigo-600 hover:text-white focus:outline-none focus:ring active:bg-indigo-500', href=href, text=label, **kwargs) as comp_box:
            pass

    return comp_box


def GradientBorder(key, label, href="#", **kwargs, ):
    with writer_ctx:
        with A(classes='group inline-block rounded bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500 hover:text-white focus:outline-none focus:ring active:text-opacity-75',
               extra_classes="p-[2px]",
               href=href,
               **kwargs) as comp_box:
            with Span(classes="block rounded-sm bg-white px-8 py-3 text-sm font-medium group-hover:bg-transparent", text=label):
                pass
            pass

    return comp_box

def GradientBorder_Oval(key, label, href="#", **kwargs):
    with writer_ctx:
        with A(classes='group inline-block rounded-full bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500 hover:text-white focus:outline-none focus:ring active:text-opacity-75',
               extra_classes="p-[2px]",
               href=href,
               **kwargs) as comp_box:
            with Span(classes="block rounded-sm bg-white px-8 py-3 text-sm font-medium group-hover:bg-transparent", text=label):
                pass
            pass

    return comp_box




def CurtainClose(key, label, xdir="left", href="#", **kwargs):
    match xdir:
        case "left":
            tw = "inset-y-0 left-0 w-[2px]"
        case "right":
            tw = "inset-y-0 right-0 w-[2px]"
        case "bottom":
            tw = "inset-x-0 bottom-0 h-[2px]"
        case "top":
            tw = "inset-x-0 top-0 h-[2px]"
            
        
    with writer_ctx:
        with A(classes='group relative inline-block overflow-hidden border border-indigo-600 px-8 py-3 focus:outline-none focus:ring', href=href, **kwargs) as comp_box:
            with Span(classes=f'absolute bg-indigo-600 transition-all group-hover:w-full group-active:bg-indigo-500',
                      extra=tw
                      ):
                pass

            with Span(classes='relative text-sm font-medium text-indigo-600 transition-colors group-hover:text-white',
                      text=label):
                pass

    return comp_box
