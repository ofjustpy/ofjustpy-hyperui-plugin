
import ofjustpy as oj
from html_writer.macro_module import macros, writer_ctx

def More(text=''):
    with writer_ctx:
        with Span(classes='flex items-center grow') as separator_span:
            with Span(classes='h-px flex-1 bg-black'):
                pass

            with Span(classes='shrink-0 px-6', text=f'{text}'):
                pass

            with Span(classes='h-px flex-1 bg-black'):
                pass

    return separator_span




def Blurry(text=''):
    with writer_ctx:
        with Span(classes='relative flex justify-center grow') as container_span:
            with Div(classes='absolute inset-x-0 top-1/2 h-px -translate-y-1/2 bg-transparent bg-gradient-to-r from-transparent via-gray-500 to-transparent opacity-75'):
                pass

            with Span(classes='relative z-10 bg-white px-6', text=f'{text}'):
                pass

    return container_span


def AlignLeft(text=''):
    with writer_ctx:
        with Span(classes='flex items-center grow') as separator_span:
            with Span(classes='pr-6', text=f'{text}'):
                pass

            with Span(classes='h-px flex-1 bg-black'):
                pass

    return separator_span

from html_writer.macro_module import macros, writer_ctx

def AlignRight(text=''):
    with writer_ctx:
        with Span(classes='flex items-center grow') as separator_span:
            with Span(classes='h-px flex-1 bg-black'):
                pass

            with Span(classes='pl-6', text=f'{text}'):
                pass

    return separator_span










