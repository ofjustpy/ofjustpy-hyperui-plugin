from hyperui_plugin.hui_components import Alerts
import ofjustpy as oj

#print (Alerts)

for _ in build_all_components("Alerts"):
    print(_)
    break

hui_components.Alerts(tag, title="Changes saved", desc="Your product changes have been saved.")
app = oj.load_app()
endpoint = oj.create_endpoint("hui_gallery_try1",
                   [_ for _ in build_all_components("Alerts")],
                   head_html =  """<script src="https://cdn.tailwindcss.com"></script> """
                   )

oj.add_jproute("/", endpoint)
from addict import Dict
request = Dict()
request.session_id = "abc"
wp = endpoint(request)

