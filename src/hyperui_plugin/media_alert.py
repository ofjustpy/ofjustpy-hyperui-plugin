import kavya as kv
from kavya.dsl import macros, MuCtx

from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow

# TODO: convert code to python dsl representation
def card(title, text, img_src, img_alt="", align = "top"):
    img = kv.PC.Img(src = img_src, alt=img_alt, twsty_tags=encode_twstr("aspect-square w-20 rounded-lg object-cover")
              )
    title = kv.PC.H3(text=title, twsty_tags=encode_twstr("text-lg/tight font-medium text-gray-900"))
    twsty_tags = encode_twstr("mt-0.5  w-64 border-pink-500")
    content = kv.PC.P( text=text, twsty_tags=twsty_tags)

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
            

    # TODO: bug bug bug in encode
    #twsty_tags=encode_twstr(f"flex {align_tw} gap-4")
    root = kv.PD.Div(childs = [img, kv.PD.Div(childs=[title, content])], classes=f"flex {align_tw} gap-4")
    return root

