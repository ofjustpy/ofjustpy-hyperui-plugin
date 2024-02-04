from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin.sideMenu import  (Simple
                                          )

app = oj.load_app()
simple_sideMenu = Simple("Wiki Items")
simple_sideMenu.add_flat_item("general", "General")
simple_sideMenu.add_flat_item("more_things","More things")
teams = simple_sideMenu.add_group_item("Teams")
teams.add_flat_item("banned_users", "Banned Users")
teams.add_flat_item("calender", "Calender")


textbox = oj.PC.Prose(text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ullamcorper accumsan lacus, a condimentum orci auctor ut. Quisque et volutpat elit. Vestibulum id velit vel augue suscipit ultricies. Aenean ultricies, libero eu dignissim interdum, eros dui cursus neque, at feugiat dolor nulla nec arcu. Nam vehicula justo in tincidunt tincidunt. Vivamus accumsan urna ut fringilla commodo. Nulla facilisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse eu tincidunt orci.
Curabitur sed consequat dolor. Nullam eget urna nec nulla sodales posuere. Mauris id metus non ligula venenatis malesuada in id metus. Fusce eu urna ac justo consectetur venenatis vel sit amet libero. Sed euismod nisl vel mi ultrices, at cursus mauris volutpat. Quisque a libero felis. Curabitur laoreet, libero vel scelerisque suscipit, metus est bibendum arcu, id dapibus odio arcu nec libero. Integer convallis eget purus vel luctus. Nulla facilisi. Sed pharetra vel urna vel tempor. Integer et felis sed metus ullamcorper laoreet.

Praesent vel consectetur justo, vel blandit arcu. Vivamus cursus, libero eu tincidunt aliquet, arcu metus commodo justo, eget ultricies ligula lectus vitae lacus. Proin gravida nec metus ut rhoncus. Ut sit amet erat sit amet mi tempor rhoncus eget at neque. Integer sit amet turpis id neque bibendum cursus. Fusce quis enim euismod, suscipit justo vel, commodo mauris. Sed convallis tellus sed risus finibus efficitur. Vivamus vel elit nec odio accumsan cursus eu vel tortor. Vivamus dapibus sem id sapien dignissim cursus.

Quisque eget fermentum tortor, et congue justo. Aliquam erat volutpat. Duis malesuada eleifend orci, in vestibulum lacus suscipit et. Sed interdum laoreet nisi, at ultrices justo auctor at. Integer laoreet felis ut odio euismod eleifend. Vestibulum a feugiat elit. Integer nec fermentum mauris. Fusce bibendum, risus et malesuada ultricies, velit lacus tincidunt odio, id bibendum eros justo vel nisi. Vestibulum auctor dolor vitae sapien bibendum, in sagittis erat ultricies.

Donec eu velit quis nisi pharetra hendrerit. Nullam hendrerit auctor nisi, a euismod orci gravida nec. Proin tincidunt arcu in ligula fermentum, ut pellentesque ex efficitur. Quisque ut metus ac justo bibendum cursus nec sit amet velit. Integer vestibulum augue ut bibendum sagittis. Fusce non dapibus elit. Integer vel arcu ac quam malesuada sagittis. In hac habitasse platea dictumst. Integer elementum, erat id fermentum consequat, lacus velit rhoncus elit, eget sodales turpis elit eu ligula. Nulla facilisi.

Nam vel ullamcorper ligula. Ut suscipit bibendum turpis, vitae vestibulum mi sagittis vel. Curabitur a leo vel est ullamcorper luctus. Nunc sit amet fermentum nulla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla facilisi. Fusce tristique justo et est fermentum, in ullamcorper libero fringilla. Suspendisse potenti. Quisque vel ante nec mi tincidunt eleifend. Vivamus laoreet turpis ac nisi finibus, id efficitur quam egestas. Integer vel tellus urna. Curabitur ut purus vel tellus gravida sodales.""", twsty_tags=[W/"2/3"])

endpoint = oj.create_endpoint("sideMenu",
                              childs = [oj.HCCMutable.Container(childs = [oj.PC.StackH(childs=[simple_sideMenu, textbox])

                                                                          ])
                                        ],
                              title="Side Menu"
                              )
oj.add_jproute("/", endpoint)

