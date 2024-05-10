from svelte_safelist_builder import get_svelte_safelist
import macropy.activate
import svelte_bundler
twtags, fontawesome_icons = get_svelte_safelist("runner")

# print (twtags)
# print (fontawesome_icons)
# #twtags = get_svelte_safelist("debug_encode_debug")


# use_shadcn = True
# use_skeleton = True

# # which components and themes to include
# skeleton_config = { 'components': [],
#                     'themes': [],

#     }

# # which font families to include
font_families = ["Geist", "Roboto"]

# # which icons of font-awesome to include
# # which ones from regular and
# # which from solid
# fontawesome_icons = []

# print (twtags)


# #twtags="w-16"
# svelte_bundler.build_bundle(twtags,
#                             font_families = font_families,
#                             fontawesome_icons = fontawesome_icons
#                             )

svelte_bundler.build_bundle_ssr (twtags,
                            )


