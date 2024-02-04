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


def Card_Type_1(href, title, author, image_src, content, published_date, reading_time):
    with writer_ctx:
        with A(href=href, classes="relative block overflow-hidden rounded-lg border border-gray-100 p-4 sm:p-6 lg:p-8") as comp_box:
            with Span(classes="absolute inset-x-0 bottom-0 h-2 bg-gradient-to-r from-green-300 via-blue-500 to-purple-600"):
                pass

            with Div(classes="sm:flex sm:justify-between sm:gap-4") as header_section:
                with Div() as text_content:
                    with H3(classes="text-lg font-bold text-gray-900 sm:text-xl", text=title):
                        pass

                    with P(classes="mt-1 text-xs font-medium text-gray-600", text=f"By {author}"):
                        pass

                with Div(classes="hidden sm:block sm:shrink-0") as image_section:
                    with Img(alt="Author Image", src=image_src, classes="h-16 w-16 rounded-lg object-cover shadow-sm"):
                        pass

            with Div(classes="mt-4") as description_section:
                with P(classes="max-w-[40ch] text-sm text-gray-500", text=content):
                    pass

            with Dl(classes="mt-6 flex gap-4 sm:gap-6") as metadata_section:
                with Div(classes="flex flex-col-reverse") as published_info:
                    with Dt(classes="text-sm font-medium text-gray-600", text="Published"):
                        pass
                    with Dd(classes="text-xs text-gray-500", text=published_date):
                        pass

                with Div(classes="flex flex-col-reverse") as reading_time_info:
                    with Dt(classes="text-sm font-medium text-gray-600", text="Reading time"):
                        pass
                    with Dd(classes="text-xs text-gray-500", text=reading_time):
                        pass

    return comp_box

