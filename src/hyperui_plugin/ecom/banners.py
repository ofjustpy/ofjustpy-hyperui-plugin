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

def CenteredWithAction(title, sub_title, description, button1_text, button1_link, button2_text, button2_link):
    with writer_ctx:
        with Section(classes="bg-gray-50") as comp_box:
            with Div(classes="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center"):
                with Div(classes="mx-auto max-w-xl text-center"):
                    with H1(classes="text-3xl font-extrabold sm:text-5xl", text=title):
                        with Strong(classes="font-extrabold text-red-700 sm:block", text=sub_title):
                            pass
   
                    with P(classes="mt-4 sm:text-xl/relaxed", text=description):
                        pass

                    with Div(classes="mt-8 flex flex-wrap justify-center gap-4"):
                        with A(classes="block w-full rounded bg-red-600 px-12 py-3 text-sm font-medium text-white shadow hover:bg-red-700 focus:outline-none focus:ring active:bg-red-500 sm:w-auto", href=button1_link, text=button1_text):
                            pass

                        with A(classes="block w-full rounded px-12 py-3 text-sm font-medium text-red-600 shadow hover:text-red-700 focus:outline-none focus:ring active:text-red-500 sm:w-auto", href=button2_link, text=button2_text):
                            pass
    return comp_box

def CenteredWithActionGradient(title, sub_title, description, button1_text, button1_link, button2_text, button2_link):
    with writer_ctx:
        with Section(classes="bg-gray-900 text-white") as comp_box:
            with Div(classes="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center"):
                with Div(classes="mx-auto max-w-3xl text-center"):
                    with H1(classes="bg-gradient-to-r from-green-300 via-blue-500 to-purple-600 bg-clip-text text-3xl font-extrabold text-transparent sm:text-5xl", text=title):
                        with Span(classes="sm:block", text=sub_title):
                            pass

                    with P(classes="mx-auto mt-4 max-w-xl sm:text-xl/relaxed", text=description):
                        pass

                    with Div(classes="mt-8 flex flex-wrap justify-center gap-4"):
                        with A(classes="block w-full rounded border border-blue-600 bg-blue-600 px-12 py-3 text-sm font-medium text-white hover:bg-transparent hover:text-white focus:outline-none focus:ring active:text-opacity-75 sm:w-auto", href=button1_link, text=button1_text):
                            pass

                        with A(classes="block w-full rounded border border-blue-600 px-12 py-3 text-sm font-medium text-white hover:bg-blue-600 focus:outline-none focus:ring active:bg-blue-500 sm:w-auto", href=button2_link, text=button2_text):
                            pass
    return comp_box


# def generate_forever_home_section():
#     with writer_ctx:
#         with Section(classes="relative bg-[url(https://images.unsplash.com/photo-1604014237800-1c9102c219da?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80)] bg-cover bg-center bg-no-repeat"):
#             with Div(classes="absolute inset-0 bg-white/75 sm:bg-transparent sm:from-white/95 sm:to-white/25 ltr:sm:bg-gradient-to-r rtl:sm:bg-gradient-to-l"):
#                 pass

#             with Div(classes="relative mx-auto max-w-screen-xl px-4 py-32 sm:px-6 lg:flex lg:h-screen lg:items-center lg:px-8"):
#                 with Div(classes="max-w-xl text-center ltr:sm:text-left rtl:sm:text-right"):
#                     with H1(classes="text-3xl font-extrabold sm:text-5xl", text="Let us find your"):
#                         with Strong(classes="block font-extrabold text-rose-700", text="Forever Home."):
#                             pass

#                     with P(classes="mt-4 max-w-lg sm:text-xl/relaxed", text="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nesciunt illo tenetur fuga ducimus numquam ea!"):
#                         pass

#                     with Div(classes="mt-8 flex flex-wrap gap-4 text-center"):
#                         with A(classes="block w-full rounded bg-rose-600 px-12 py-3 text-sm font-medium text-white shadow hover:bg-rose-700 focus:outline-none focus:ring active:bg-rose-500 sm:w-auto", href="#", text="Get Started"):
#                             pass

#                         with A(classes="block w-full rounded bg-white px-12 py-3 text-sm font-medium text-rose-600 shadow hover:text-rose-700 focus:outline-none focus:ring active:text-rose-500 sm:w-auto", href="#", text="Learn More"):
#                             pass



