# from hyperui_plugin.ecom.featured_sections import  (WithProducts
#                                           )


import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()
from hyperui_plugin.ecom.featured_sections import  (WithProducts,
                                                    CollectionGrid
                                          )

collection_with_products = WithProducts("Watches", "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quas rerum quam amet provident nulla error!", "Shop All", )

collection_with_products.add_product("https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1598&q=80", "Simple Watch", "$150")

collection_with_products.add_product("https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1598&q=80", "Simple Watch", "$150")

collection_with_products.add_product("https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1598&q=80", "Simple Watch", "$150")


collection_grid = CollectionGrid("New Collection", "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Itaque praesentium cumque iure dicta incidunt est ipsam, officia dolor fugit natus?")
collection_grid.add_product("https://images.unsplash.com/photo-1618898909019-010e4e234c55?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80",
                            
                            "Casual Trainers",
                            "Shop Now")
collection_grid.add_product("https://images.unsplash.com/photo-1618898909019-010e4e234c55?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80",
                            
                            "Casual Trainers",
                            "Shop Now")

collection_grid.add_product("https://images.unsplash.com/photo-1618898909019-010e4e234c55?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80",
                            
                            "Casual Trainers",
                            "Shop Now")


endpoint = oj.create_endpoint("featured_sections",
                              childs = [collection_with_products,
                                        collection_grid
                                        ],
                              title="Featured Section Components"
                              )
oj.add_jproute("/", endpoint)
