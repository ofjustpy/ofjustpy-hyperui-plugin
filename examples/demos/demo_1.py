from hyperui_plugin.SVGcomponents import PassiveComponents as PC
from py_tailwind_utils import *
import ofjustpy as oj
radius = 80

all_svgs = []
for color in ['red', 'green', 'blue']:
    acircle = PC.Circle(cx='50', cy='50', r='50', fill=color)
    svg = PC.Svg(viewBox='0 0 200 200',
                 xmlns='http://www.w3.org/2000/svg',
                 width=100,
                 height=100,
                 fill="red",
                 twsty_tags= [mr/2, db.bi],
                 childs = [acircle]
                 )
    all_svgs.append(svg)
    

for radius in range(10, 51, 10):
    ellipse = PC.Ellipse(cx=50,
                         cy=50,
                         rx=radius,
                         ry=radius/2,
                         fill='teal')
    svg = PC.Svg(viewBox='0 0 200 200',
                 xmlns='http://www.w3.org/2000/svg',
                 width=100,
                 height=100,
                 fill="green", 
                 twsty_tags= [mr/2, db.bi],
                 childs = [ellipse]
                 )
    all_svgs.append(svg)
        
        
# svg = PC.Svg(viewBox='0 0 200 200',
#                             xmlns='http://www.w3.org/2000/svg',
#                             width=100,
#                             height=100,
#              twsty_tags= [mr/2, db.bi],
#                             childs = [PC.Ellipse(cx=50,
#                                                  cy=50,
#                                                  rx=radius,
#                                                  ry=radius/2,
#                                                  fill='teal'),
                                      
                                      

#                                 ]
#                             )




app = oj.load_app()
endpoint = oj.create_endpoint("svg_demo_1",
                   childs = all_svgs,
                   )
oj.add_jproute("/", endpoint)
