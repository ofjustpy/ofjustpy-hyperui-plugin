from hyperui_plugin.SVGcomponents import PassiveComponents
from py_tailwind_utils import *

print(PassiveComponents.View)

view = PassiveComponents.View()
print (view.html_tag)

print (mr/2)
svg = PassiveComponents.Svg(viewBox='0 0 100 100',
                            xmlns='http://www.w3.org/2000/svg',
                            width=100,
                            height=100,
                            twsty_tags= [mr/2, db.bi]
                            )

print (svg.domDict)
print (svg.attrs)


