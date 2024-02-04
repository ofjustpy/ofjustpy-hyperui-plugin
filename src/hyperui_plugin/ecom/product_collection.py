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

def Simple (title, desc, align_desc = "left"):
    """
    align_desc: left or centered
    """
    desc_align_twsty = ""
    if align_desc == "center":
        desc_align_twsty = "mx-auto"
    with writer_ctx:
        with Section() as comp_box:
            with Div(classes="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8"):
                with Header():
                    with H2(classes="text-xl font-bold text-gray-900 sm:text-3xl", text=title):
                        pass

                    with P(classes=f"{desc_align_twsty} mt-4 max-w-md text-gray-500", text=desc):
                        pass

                with Ul(classes="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4") as item_container:
                    pass

    def add_product(img_src, product_name, regular_price, item_container=item_container):
        
        with writer_ctx:
            with Li() as item_box:
                with A(href="#", classes="group block overflow-hidden"):
                    with Img(src=img_src, alt="", classes="h-80 w-full object-cover transition duration-500 group-hover:scale-105 sm:h-96"):
                        pass

                    with Div(classes="relative bg-white pt-3"):
                        with H3(classes="text-xs text-gray-700 group-hover:underline group-hover:underline-offset-4", text=product_name):
                            pass

                        with P(classes="mt-2"):
                            with Span(classes="sr-only", text="Regular Price"):
                                pass

                            with Span(classes="tracking-wider text-gray-900", text=regular_price):
                                pass

        item_container.components.append(item_box)
    comp_box.add_product = add_product
    return comp_box


#TODO: fix it later
# def FeaturePanel(label):
#     """
#     Like Availablity, etc
    
#     """
#     # Availability details
#     with writer_ctx:
#         with Details(classes='overflow-hidden rounded border border-gray-300', extra_classes="[&_summary::-webkit-details-marker]:hidden"):
#             with Summary(classes='flex cursor-pointer items-center justify-between gap-2 p-4 text-gray-900 transition'):
#                 with Span(classes='text-sm font-medium', text=label):
#                     pass
#                 with Span(classes='transition group-open:-rotate-180'):
                    
#                     pass

#             with Div(classes='border-t border-gray-200 bg-white'):
#                 with Header(classes='flex items-center justify-between p-4'):
#                     with Span(classes='text-sm text-gray-700', text=' 0 Selected '):
#                         pass
#                     with Button(classes='text-sm text-gray-900 underline underline-offset-4', text='Reset', key='reset_button_availability'):
#                         pass

#                 with Ul(classes='space-y-1 border-t border-gray-200 p-4') as ul_box:
#                     # Add list items as needed
#                     pass
            

#     def add_filter_clause(key, label):
#         """
#         Checkbox showing filter clause
#         """
#         with writer_ctx:
#             with Li() as filter_clause_box:
#                 with Label(for_='FilterOutOfStock', classes='inline-flex items-center gap-2'):
#                     with CheckboxInput(key=key, classes='h-5 w-5 rounded border-gray-300'):
#                         pass

#                     with Span(classes='text-sm font-medium text-gray-700', text=label):
#                         pass
                
#         ul_box.components.append(filter_clause_box)
        
