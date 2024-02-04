from hyperui_plugin.ecom.collection_cards import  (Simple,
                                                   ContentInside
                                          )

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()

acard = Simple("Small Headphones", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis quibusdam ab maiores placeat  odio id?", "https://images.unsplash.com/photo-1592921870789-04563d55041c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80")

bcard = ContentInside("Small Headphones", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis quibusdam ab maiores placeat  odio id?", "https://images.unsplash.com/photo-1592921870789-04563d55041c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80")

endpoint = oj.create_endpoint("collection_card",
                              childs = [oj.PC.Halign(acard),
                                        oj.PC.Halign(bcard)
                                        ],
                              title="Collection card"
                              )
oj.add_jproute("/", endpoint)
