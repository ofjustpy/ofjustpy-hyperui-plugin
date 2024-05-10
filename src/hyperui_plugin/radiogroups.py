import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow, bg, green, W, fc, gray

# def SimpleStacked():
#     container = oj.PC.Fieldset(twsty_tags=encode_twstr("space-y-4"))

#     def add_item(key, left_text, right_text):
#         label = oj.PD.Label(twsty_tags=encode_twstr("flex cursor-pointer items-center justify-between rounded-lg border border-gray-100 bg-white p-4 text-sm font-medium shadow-sm hover:border-gray-200 peer-checked:border-blue-500 peer-checked:ring-1 peer-checked:ring-blue-500"),
#                     childs = [oj.PC.P(text=left_text, twsty_tags=[fc/gray/7]),
#                               oj.PC.P(text=right_text, twsty_tags=[fc/gray/9])
#                               ]
#                     )
#         # using Checkbox instead of radio
#         cbinp = oj.AC.CheckboxInput(key=key, checked=True, twsty_tags=encode_twstr(""))
#         container.components.append(oj.PD.Div(childs  = [cbinp, label]))
#     return container, add_item
        
              
from html_writer.macro_module import macros, writer_ctx

def SimpleStacked():
    with writer_ctx:
        with Fieldset(classes='space-y-4') as comp_box:
            with Legend(classes='sr-only', text='Delivery'):
                pass
            pass

    checked=True
    def add_item(key, text_left, text_right):
        nonlocal checked
        with writer_ctx:
            with Div() as cb_item:
                with CheckboxInput(key=key, classes='peer hidden', checked=checked):
                    pass

                with Label(for_='DeliveryStandard', classes='flex cursor-pointer items-center justify-between rounded-lg border border-gray-100 bg-white p-4 text-sm font-medium shadow-sm hover:border-gray-200 peer-checked:border-blue-500 peer-checked:ring-1 peer-checked:ring-blue-500'):
                    with P(classes='text-gray-700', text=text_left):
                        pass

                    with P(classes='text-gray-900', text=text_right):
                        pass

        checked=False
        comp_box.components.append(cb_item)
    comp_box.add_item = add_item
    return comp_box



# Not test yet, not in use
def Variants():
    with writer_ctx:
        with Fieldset(classes='flex flex-wrap gap-3') as comp_box:
            with Legend(classes='sr-only', text='Color'):
                pass
            pass

    checked=True
    def add_item(key, text):
        nonlocal checked
        with writer_ctx:
            with Div() as cb_item:
                with Label(key=key, classes= "flex cursor-pointer items-center justify-center rounded-md border border-gray-100 bg-white px-3 py-2 text-gray-900 hover:border-gray-200", extra_classes="has-[:checked]:border-blue-500 has-[:checked]:bg-blue-500 has-[:checked]:text-white",  ):
                    with CheckboxInput(key=f"{key}_radioinput", classes='', checked=checked):
                        pass
                    
                    with P(classes='text-sm font-medium', text=text):
                        pass



        checked=False
        comp_box.components.append(cb_item)
    comp_box.add_item = add_item
    return comp_box

