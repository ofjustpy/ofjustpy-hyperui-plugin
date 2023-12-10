from hyperui_plugin.SVGcomponents import PassiveComponents as PC
from py_tailwind_utils import *
import ofjustpy as oj

arect = PC.Rect(x='10', y='10', height="100",
                  width="100",
                  style="stroke:#ff0000; fill: #0000ff")

svg = PC.Svg(
                 xmlns='http://www.w3.org/2000/svg',
                 childs = [arect]
                 )
app = oj.load_app()
endpoint = oj.create_endpoint("svg_demo_sanity_check",
                   childs = [oj.PC.Div(childs=[svg])],
                   )
oj.add_jproute("/", endpoint)
