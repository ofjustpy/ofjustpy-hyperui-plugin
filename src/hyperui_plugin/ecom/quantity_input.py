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

# Quantity input section
def Simple(key):
    with writer_ctx:
        
        with Div(classes="max-w-md") as comp_box:
            with Label(for_='Quantity', classes='sr-only'):
                pass

            with Div(classes='flex items-center gap-1'):
                with Button(key=key, classes='h-10 w-10 leading-10 text-gray-600 transition hover:opacity-75', text='−'):
                    pass

                with TextInput(type='number', key=f"inp_{key}", placeholder='1', value='1', classes='h-10 w-24 rounded border-gray-200 sm:text-sm'):
                    pass

                with Button(key=f"inc_{key}", classes='h-10 w-10 leading-10 text-gray-600 transition hover:opacity-75', text='+'):
                    pass
    return comp_box


# TODO: figure out how not to strecth the div containing 
# have fixed width with max-w-md
def Contained(key):
    with writer_ctx:
        with Div(classes="max-w-md") as comp_box:
            with Label(for_='Quantity', classes='sr-only'):
                pass

            with Div(classes='flex items-center rounded border border-gray-200'):
                with Button(key=f"dec_{key}", classes='h-10 w-10 leading-10 text-gray-600 transition hover:opacity-75', text='−'):
                    pass

                with TextInput(type='number',  value='1', placeholder='1',  classes='h-10 w-16 border-transparent text-center  sm:text-sm', key=f"{key}_quantity_input", extra_classes="[-moz-appearance:_textfield] [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:m-0 [&::-webkit-outer-spin-button]:appearance-none", ):
                    pass

                with Button(key="inc_{key}", classes='h-10 w-10 leading-10 text-gray-600 transition hover:opacity-75', text='+'):
                    pass

    return comp_box
