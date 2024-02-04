import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow, bg, green, W, fc, gray, space, y

from html_writer.macro_module import macros, writer_ctx

def Simple(key, label, placeholder):
    ta = oj.AC.Textarea(key=key, rows="4", placeholder=placeholder,
                   twsty_tags=encode_twstr("mt-2 w-full rounded-lg border-gray-200 align-top shadow-sm sm:text-sm"),
                   )

    root = oj.PC.Div(childs=[oj.PC.Label(twsty_tags=encode_twstr("block text-sm font-medium text-gray-700"),
                                         text=label
                                         ),
                             ta
                             ]
                     )
    return root


# TODO: there is a stray blue mid border
# make clear functional
def ActionContained(key, label, placeholder):
    with writer_ctx:
        with Div() as comp_box:
            with Label(for_=f"for{key}", classes='sr-only', text=label):
                pass

            with Div(classes='overflow-hidden rounded-lg border border-gray-200 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600'):
                with Textarea(key=key, classes='w-full resize-none border-none align-top focus:ring-0 sm:text-sm', rows='4', placeholder=placeholder):
                    pass

                with Div(classes='flex items-center justify-end gap-2 bg-white p-3'):
                    with Button(key=f"{key}_clear_btn", type='button', classes='rounded bg-gray-200 px-3 py-1.5 text-sm font-medium text-gray-700 hover:text-gray-600', text='Clear'):
                        pass

                    with Button(key=f"{key}_add_btn",  classes='rounded bg-indigo-600 px-3 py-1.5 text-sm font-medium text-white hover:bg-indigo-700', text='Add'):
                        pass

                


    return comp_box
    
                   
                   
def WithActions(key, label, placeholder):
    
    with writer_ctx:
        with Div() as comp_box:
            with Label(for_=f'for_{key}', classes='sr-only', text=label):
                pass

            with Div(classes='overflow-hidden'):
                with Textarea(key=key, classes='w-full resize-none border-x-0 border-t-0 border-gray-200 px-0 align-top sm:text-sm', rows='4', placeholder=placeholder):
                    pass

                with Div(classes='flex items-center justify-end gap-2 py-3'):
                    with Button(key=f"Clear_{key}", classes='rounded bg-gray-200 px-3 py-1.5 text-sm font-medium text-gray-700 hover:text-gray-600', text='Clear'):
                        pass

                    with Button(key=f"Add_{key}", classes='rounded bg-indigo-600 px-3 py-1.5 text-sm font-medium text-white hover:bg-indigo-700', text='Add'):
                        pass

                
                    
    return comp_box
