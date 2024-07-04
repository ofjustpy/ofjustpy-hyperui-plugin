import ofjustpy as oj
from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx


def wideWithIcon(href="#", text="", **kwargs):
    """
    childs, twsty_tags, and other attributes will be ignored
    """
    with writer_ctx:
        with A(classes="group flex items-center justify-between gap-4 rounded-lg border border-current px-5 py-3 text-slate-600 transition-colors hover:bg-slate-600 focus:outline-none focus:ring active:bg-slate-500", href=href) as button_box:
            with Span(classes="font-medium transition-colors group-hover:text-white", text=text):

                pass

            with Span(classes="shrink-0 rounded-full border border-text-600 bg-white p-2 group-active:border-slate-500"):
                with FontAwesomeIcon(label="faExternalLinkAlt",
                                     size="1x", 
                                     fixedWidth=True,
                                     mdi_label="open-in-new"
                                     ):
                    pass

                pass

    return button_box


def simpleAndRevealOffsetBorderOnHover(text="Download", href="#", **kwargs):
    """
    """
    
    with writer_ctx:
        with A(classes="group relative inline-block text-sm font-medium text-white focus:outline-none focus:ring", href=href, **kwargs) as button_box:
            with Span(classes="absolute inset-0 border border-red-600 group-active:border-red-500"):
                pass
            with Span(classes="block border border-red-600 bg-red-600 px-12 py-3 active:border-red-500 active:bg-red-500 group-hover:-translate-x-1 group-hover:-translate-y-1", extra_classes="transition-transform",  text=text):
                pass
        

        pass
    
    return button_box
