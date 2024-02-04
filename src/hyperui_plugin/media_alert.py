import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow

# TODO: convert code to python dsl representation
def card(title, text, img_src, img_alt="", align = "top"):
    img = oj.PC.Img(src = img_src, alt=img_alt, twsty_tags=encode_twstr("aspect-square w-20 rounded-lg object-cover")
              )

    title = oj.PC.H3(text=title, twsty_tags=encode_twstr("text-lg/tight font-medium text-gray-900"))
    content = oj.PC.P(twsty_tags=encode_twstr("mt-0.5 text-gray-700"), text=text)
    match align:
        case "top":
            align_tw = "items-start"
        case "center":
            align_tw = "items-center"
        case "bottom":
            align_tw = "items-end"
        case "stretch":
            align_tw = "items-stretch"
        case "top-right":
            align_tw = "flex-row-reverse items-start"
        case "center-right":
            align_tw = "flex-row-reverse items-center"
        case "bottom-right":
            align_tw = "flex-row-reverse items-end"
        case "stretch-right":
            align_tw = "flex-row-reverse items-stretch"
            
            
    root = oj.PC.Div(childs = [img, oj.PC.Div(childs=[title, content])], twsty_tags=encode_twstr(f"flex {align_tw} gap-4"))
    return root

