from hyperui_plugin.component_builder import build_all_components
import ofjustpy as oj

for _ in build_all_components():
    print(_)
    
app = oj.load_app()
endpoint = oj.create_endpoint("hui_gallery_try1",
                   [_ for _ in build_all_components()],
                   head_html =  """<script src="https://cdn.tailwindcss.com"></script> """
                   )

oj.add_jproute("/", endpoint)
