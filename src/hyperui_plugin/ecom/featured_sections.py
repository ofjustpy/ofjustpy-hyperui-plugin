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
def WithProducts(section_title, section_desc, btn_text, href="", ):
    with writer_ctx:
        with Section() as root_comp:
            with Div(classes="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8"):
                with StackG(classes="gap-4 lg:grid-cols-3 lg:items-stretch", num_cols=1):
                    with StackG(classes="place-content-center rounded bg-gray-100 p-6 sm:p-8"):
                        with Div(classes="mx-auto max-w-md text-center lg:text-left"):
                            with Header():
                                with H2(classes="text-xl font-bold text-gray-900 sm:text-3xl", text=section_title):
                                    pass
                                with P(classes="mt-4 text-gray-500", text=section_desc):
                                    pass
                            with A(href="#", classes="mt-8 inline-block rounded border border-gray-900 bg-gray-900 px-12 py-3 text-sm font-medium text-white transition hover:shadow focus:outline-none focus:ring", text=btn_text):
                                pass
                    with Div(classes="lg:col-span-2 lg:py-8"):
                        with Ul(classes="grid grid-cols-2 gap-4") as display_box:

                            pass
                        pass
                    pass
                pass
            pass
        pass
    def add_product(img_src, title, desc, display_box=display_box):
        with writer_ctx:
            with Li() as product_comp:
                with A(href="#", classes="group block"):
                    with Img(src=img_src):
                        pass
                    with Div(classes="mt-3"):
                        with H3(classes="font-medium text-gray-900 group-hover:underline group-hover:underline-offset-4", text=desc):
                            pass
                        with P(classes="mt-1 text-sm text-gray-700", text="$150"):
                            pass

        display_box.components.append(product_comp)
    root_comp.add_product = add_product
                            
    return root_comp


def CollectionGrid(collection_title, collection_desc):
    with writer_ctx:
        with Section() as root_comp:
            with Div("mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8"):
                with Header(classes="text-center"):
                    with H2(classes="text-xl font-bold text-gray-900 sm:text-3xl", text=collection_title):
                        pass
                    with P(classes="mx-auto mt-4 max-w-md text-gray-500", text=collection_desc):
                        pass

                with Ul(classes="mt-8 grid grid-cols-1 gap-4 lg:grid-cols-3") as display_box:
                    pass
                pass
            pass

    def add_product(img_src, desc, btn_desc, display_box=display_box):
        with writer_ctx:
            with Li() as item_box:
                with A(href="#", classes="group relative block"):
                    with Img(src=img_src):
                        pass
                    with Div(classes="absolute inset-0 flex flex-col items-start justify-end p-6"):
                        with H3(classes="text-xl font-medium text-white", text="Casual Trainers"):
                            pass
                        with Span(classes="mt-1.5 inline-block bg-black px-5 py-3 text-xs font-medium uppercase tracking-wide text-white", text=btn_desc):
                            pass

        display_box.components.append(item_box)
    root_comp.add_product = add_product
    return root_comp
