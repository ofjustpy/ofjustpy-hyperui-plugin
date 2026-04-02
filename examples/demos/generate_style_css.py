from twtags_safelist import get_twtags_safelist
from svelte_bundler import build_ssr_style_css
#target_module = "td_svg_components"
#target_module = "runner"
#target_module = "demo_item_17_sideMenu"
target_module = "demo_item_23_toggles"
build_ssr_style_css(target_module,
                    output_dir="./static/ssr/"
                    )
