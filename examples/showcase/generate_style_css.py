from twtags_safelist import get_twtags_safelist
from svelte_bundler import build_ssr_style_css

target_module = "component_library_showcase"
build_ssr_style_css(target_module,
                    output_dir="./static/ssr/",
                    )
