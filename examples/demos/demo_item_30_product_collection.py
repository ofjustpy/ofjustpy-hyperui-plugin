from hyperui_plugin.ecom.product_collection import  (Simple,
                                                )

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()
simple_collection = Simple("Product Collection", "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Itaque praesentium cumque iure dicta incidunt est ipsam, officia dolor fugit natus?")

# Example usage:
img_src = "https://images.unsplash.com/photo-1523381210434-271e8be1f52b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
product_name = "Basic Tee"
regular_price = "£24.00 GBP"
simple_collection.add_product(img_src, product_name, regular_price)
simple_collection.add_product(img_src, product_name, regular_price)
simple_collection.add_product(img_src, product_name, regular_price)
simple_collection.add_product(img_src, product_name, regular_price)
endpoint = oj.create_endpoint("product_collection",
                              childs = [simple_collection,

                                        ],
                              title="Product Collection"
                              )
oj.add_jproute("/", endpoint)
