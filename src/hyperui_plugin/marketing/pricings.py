
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


def HighlightOption():
    with writer_ctx:
        with Div(classes="mx-auto max-w-3xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8") as comp_box:
            with Div(classes="grid grid-cols-1 gap-4 sm:grid-cols-2 sm:items-center md:gap-8"):
                with Div(classes="rounded-2xl border border-indigo-600 p-6 shadow-sm ring-1 ring-indigo-600 sm:order-last sm:px-8 lg:p-12"):
                    with Div(classes="text-center"):
                        with H2(classes="text-lg font-medium text-gray-900", text="Pro"):
                            with Span(classes="sr-only", text="Plan"):
                                pass
                            pass

                        with P(classes="mt-2 sm:mt-4"):
                            with Strong(classes="text-3xl font-bold text-gray-900 sm:text-4xl", text=" 30$ "):
                                pass

                            with Span(classes="text-sm font-medium text-gray-700", text="/month"):
                                pass

                    with Ul(classes="mt-6 space-y-2"):
                        pass

                    with A(href="#", classes="mt-8 block rounded-full border border-indigo-600 bg-indigo-600 px-12 py-3 text-center text-sm font-medium text-white hover:bg-indigo-700 hover:ring-1 hover:ring-indigo-700 focus:outline-none focus:ring active:text-indigo-500", text="Get Started"):
                        pass

                with Div(classes="rounded-2xl border border-gray-200 p-6 shadow-sm sm:px-8 lg:p-12"):
                    with Div(classes="text-center"):
                        with H2(classes="text-lg font-medium text-gray-900", text="Starter"):
                            with Span(classes="sr-only", text="Plan"):
                                pass
                            pass

                        with P(classes="mt-2 sm:mt-4"):
                            with Strong(classes="text-3xl font-bold text-gray-900 sm:text-4xl", text=" 20$ "):
                                pass

                            with Span(classes="text-sm font-medium text-gray-700", text="/month"):
                                pass

                    with Ul(classes="mt-6 space-y-2"):
                        pass

                    with A(href="#", classes="mt-8 block rounded-full border border-indigo-600 bg-white px-12 py-3 text-center text-sm font-medium text-indigo-600 hover:ring-1 hover:ring-indigo-600 focus:outline-none focus:ring active:text-indigo-500", text="Get Started"):
                        pass

    return comp_box
                
# def pricing_features():
#     for feature in ["20 users included", "5GB of storage", "Email support", "Help center access", "Phone support", "Community access"]:
#         with Li(classes="flex items-center gap-1"):
#             with Svg(xmlns="http://www.w3.org/2000/svg", fill="none", viewBox="0 0 24 24", stroke-width="1.5", stroke="currentColor", classes="h-5 w-5 text-indigo-700"):
#                 with Path(stroke-linecap="round", stroke-linejoin="round", d="M4.5 12.75l6 6 9-13.5"):
#                     pass

#             with Span(classes="text-gray-700", text=f" {feature}"):
#                 pass

# pricing_section()
