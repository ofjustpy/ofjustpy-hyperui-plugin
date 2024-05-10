import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow, bg, green, W, fc, gray
from html_writer.macro_module import macros, writer_ctx

def Badge(label=None, icon=None):
    with writer_ctx:
        with Div(classes='inline-flex items-center justify-center rounded-full bg-purple-100 px-2.5 py-0.5 text-purple-700') as badge_box:

            pass

    if icon:
        badge_box.components.append(icon)

    if label:
        with writer_ctx:
            with P(classes='whitespace-nowrap text-sm', text=f'{label}') as p_box:
                    pass

        badge_box.components.append(p_box)

    def add_cross_btn(key, badge_box=badge_box, **btn_kwargs):
        with writer_ctx:
            with Button(key=key, classes='-me-1 ms-1.5 inline-block rounded-full bg-purple-200 p-0.5 text-purple-700 transition hover:bg-purple-300', **btn_kwargs) as remove_button:
                with Span(classes='sr-only', text='Remove badge'):
                    pass
                with  FontAwesomeIcon(label="faCheck", fixedWidth=True, classes="w-5 h-5"):
                    pass
        badge_box.components.append(remove_button)
    
    badge_box.add_cross_btn = add_cross_btn
    return badge_box
