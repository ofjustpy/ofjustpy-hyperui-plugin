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

#Note: adding max-w-md to size the images
def Simple(img_src, img_src_hover, title, sticker):
    with writer_ctx:
        with A(href="#", classes="max-w-md group block overflow-hidden") as root_comp:
            with Div(classes="relative h-96 sm:h-96"):
                with Img(src=img_src, classes="absolute inset-0 h-full w-full object-cover opacity-100 group-hover:opacity-0"):
                    pass
                with Img(src=img_src_hover, classes="absolute inset-0 h-full w-full object-cover opacity-0 group-hover:opacity-100"):
                    pass

            with Div(classes="relative bg-white pt-3"):
                with H3(classes="text-sm text-gray-700 group-hover:underline group-hover:underline-offset-4", text=title):
                    pass
                with P(classes="mt-1.5 tracking-wide text-gray-900", text=sticker):
                    pass
    return root_comp

#Note: adding max-w-md to size the images
def WithVariant(img_src, img_src_hover, desc, sticker, variant_text):
    with writer_ctx:
        with A(href="#", classes="group max-w-md block overflow-hidden") as top_component:
            with Div(classes="relative h-96 sm:h-96"):
                with Img(src=img_src, classes="absolute inset-0 h-full w-full object-cover opacity-100 group-hover:opacity-0"):
                    pass
                with Img(src=img_src_hover, classes="absolute inset-0 h-full w-full object-cover opacity-0 group-hover:opacity-100"):
                    pass

            with Div(classes="relative bg-white pt-3"):
                with H3(classes="text-sm text-gray-700 group-hover:underline group-hover:underline-offset-4", text=desc):
                    pass
                with Div(classes="mt-1.5 flex items-center justify-between text-gray-900"):
                    with P(classes="tracking-wide", text=sticker):
                        pass
                    with P(classes="text-xs uppercase tracking-wide", text=variant_text):
                        pass
    return top_component

def WithDescription(img_src, desc, desc_subtitle, price):
    with writer_ctx:
        with A(href="#", classes="group max-w-md block") as comp_box:
            with Img(src=img_src, alt="", classes="h-[350px] w-full object-cover sm:h-[450px]"):
                pass

            with Div(classes="mt-3 flex justify-between text-sm"):
                with Div():
                    with H3(classes="text-gray-900 group-hover:underline group-hover:underline-offset-4", text=desc):
                        pass

                    with P(classes="mt-1.5 max-w-[45ch] text-xs text-gray-500", text=desc_subtitle):
                        pass

                with P(classes="text-gray-900", text=price):
                    pass

    return comp_box

def ContainedWishList(key, img_src, product_name, product_price):
    with writer_ctx:
        with A(href="#", classes="max-w-md group relative block overflow-hidden") as comp_box:
            with Button(key=f"{key}_wishbtn", classes="absolute end-4 top-4 z-10 rounded-full bg-white p-1.5 text-gray-900 transition hover:text-gray-900/75"):
                with Span(classes="sr-only", text="Wishlist"):
                    pass


            with Img(src=img_src, alt="", classes="h-64 w-full object-cover transition duration-500 group-hover:scale-105 sm:h-72"):
                pass

            with Div(classes="relative border border-gray-100 bg-white p-6"):
                with Span(classes="whitespace-nowrap bg-yellow-400 px-3 py-1.5 text-xs font-medium", text="New"):
                    pass

                with H3(classes="mt-4 text-lg font-medium text-gray-900", text=product_name):
                    pass

                with P(classes="mt-1.5 text-sm text-gray-700", text=product_price):
                    pass

                with Form(key=f"{key}_form", classes="mt-4"):
                    with Button(key=f"{key}_cartbtn", classes="block w-full rounded bg-yellow-400 p-4 text-sm font-medium transition hover:scale-105", text="Add to Cart"):
                        pass

    return comp_box    
