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


def Simple(image_url, date, title, content, link):
    with writer_ctx:
        with Article(classes="overflow-hidden rounded-lg shadow transition hover:shadow-lg") as comp_box:
            with Img(src=image_url, alt="Office", classes="h-56 w-full object-cover"):
                pass

            with Div(classes="bg-white p-4 sm:p-6"):
                with Time(classes="block text-xs text-gray-500", datetime=date, text=date):
                    pass

                with A(href=link):
                    with H3(classes="mt-0.5 text-lg text-gray-900", text=title):
                        pass

                with P(classes="mt-2 line-clamp-3 text-sm/relaxed text-gray-500", text=content):
                    pass

    return comp_box

def Floating(image_url, alt_text, title, content, link):
    
    with writer_ctx:
        with Article(classes="group") as comp_box:
            with Img(src=image_url, alt=alt_text, classes="h-56 w-full rounded-xl object-cover shadow-xl transition "):
                pass

            with Div(classes="p-4"):
                with A(href=link):
                    with H3(classes="text-lg font-medium text-gray-900", text=title):
                        pass

                with P(classes="mt-2 line-clamp-3 text-sm/relaxed text-gray-500", text=content):
                    pass

    return comp_box

def Bordered(image_url, alt_text, title, content, link):
    with writer_ctx:
        with Article(classes="overflow-hidden rounded-lg border border-gray-100 bg-white shadow-sm") as comp_box:
            with Img(src=image_url, alt=alt_text, classes="h-56 w-full object-cover"):
                pass

            with Div(classes="p-4 sm:p-6"):
                with A(href=link):
                    with H3(classes="text-lg font-medium text-gray-900", text=title):
                        pass

                with P(classes="mt-2 line-clamp-3 text-sm/relaxed text-gray-500", text=content):
                    pass

                with A(href="#" , classes="group mt-4 inline-flex items-center gap-1 text-sm font-medium text-blue-600", text="Find out more"):

                    with Span(classes="block transition-all group-hover:ms-0.5 rtl:rotate-180", aria_hidden="true", text="→"):
                        pass

    return comp_box


def GradientBorder(date, title, tags):
    with writer_ctx:
        with Article(classes="hover:animate-background rounded-xl bg-gradient-to-r from-green-300 via-blue-500 to-purple-600 p-0.5 shadow-xl transition  hover:shadow-sm ") as comp_box:
            with Div(classes="rounded-3xl bg-white p-4 !pt-20 sm:p-6"):
                with Time(classes="block text-xs text-gray-500", datetime=date, text=date):
                    pass

                with A(href="#"):
                    with H3(classes="mt-0.5 text-lg font-medium text-gray-900", text=title):
                        pass
                with Div(classes="mt-4 flex flex-wrap gap-1"):
                    with Span(classes="whitespace-nowrap rounded-full bg-purple-100 px-2.5 py-0.5 text-xs text-purple-600", text="Snippet"):
                        pass

                    with Span(classes="whitespace-nowrap rounded-full bg-purple-100 px-2.5 py-0.5 text-xs text-purple-600", text="JavaScript"):
                        pass
                    pass

    

    return comp_box

# Example usage:
