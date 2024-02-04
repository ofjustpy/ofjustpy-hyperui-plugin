from py_tailwind_utils import *
import ofjustpy as oj
oj.set_style("un")


from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin import errorpages

notfoundpage = errorpages.NotFoundPage()
error404page = errorpages.Error404Page()
notFoundPageWithImage = errorpages.NotFoundPageWithImage()

app = oj.load_app()
endpoint = oj.create_endpoint("demo_error_pages",
                              childs = [oj.PC.Div(childs=[notfoundpage,
                                                          error404page,
                                                          notFoundPageWithImage,
                                                          
                                                          ], twsty_tags=[space/y/4])
                                        ],
                              title="Error Pages"
                   )
oj.add_jproute("/", endpoint)

