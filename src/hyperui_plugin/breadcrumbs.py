import ofjustpy as oj
from html_writer.macro_module import macros, writer_ctx
def Simple():
    with writer_ctx:
        with Nav() as comp_box:
            with Ol(classes="flex items-center gap-1 text-sm text-gray-600") as ol_box:
                with Li():
                    with A(href="#", classes="block transition hover:text-gray-700"):
                        with Span(classes="sr-only", text="Home"):
                            pass
                        with Icon_Home():
                            pass
                        
                        pass


    def add_item(text, href="#", ol_box=ol_box, **kwargs):
        with writer_ctx:
            with Li(classes="rtl:rotate-180") as sep_box:
                with Icon_BreadcrumbSepArrow():
                    pass
        ol_box.components.append(sep_box)
        with writer_ctx:
            with Li() as label_box:
                with A(href=href,
                       classes="block transition hover:text-gray-700",
                       text=text,
                       **kwargs
                       ):
                    pass
                pass
        ol_box.components.append(label_box)
        pass

    comp_box.add_item = add_item
    return comp_box


def ChevronBackground():
    with writer_ctx:
        with Nav(classes="flex") as comp_box:
            with Ol(classes="flex overflow-hidden rounded-lg border border-gray-200 text-gray-600") as ol_box:
                with Li(classes="flex items-center"):
                    with A(href="#", classes="flex h-10 items-center gap-1.5 bg-gray-100 px-4 transition hover:text-gray-900"):
                        with Icon_Home():
                            pass
                        with Span(classes="ms-1.5 text-xs font-medium", text="Home"):
                            pass
                        
                        pass


    def add_item(text, href="#", ol_box=ol_box, **kwargs):
        with writer_ctx:
            with Li(classes="relative flex items-center") as sep_box:
                with Span(classes="absolute inset-y-0 -start-px h-10 w-4 bg-gray-100 rtl:rotate-180", extra_classes="[clip-path:_polygon(0_0,_0%_100%,_100%_50%)]"):
                    pass
                with A(href=href, classes="flex h-10 items-center bg-white pe-4 ps-8 text-xs font-medium transition hover:text-gray-900", text=text):
                    pass
        ol_box.components.append(sep_box)
    comp_box.add_item = add_item
    return comp_box

