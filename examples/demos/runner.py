import macropy.activate
import ofjustpy as oj
oj.set_style("un")
def page_builder(key, childs, **kwargs):
    return oj.default_page_builder(key=key,
                                   childs=childs,
                                   rendering_type="SSR",
                                   head_html =  """<script src="https://cdn.tailwindcss.com"></script> """,
                                   **kwargs)

import ofjustpy as oj
with oj.PageBuilderCtx(page_builder):
    # import demo_item_1_alert_component
    # import demo_item_2_badges_component
    # import demo_item_3_breadcrumbs
    # import demo_item_4_buttongroups
    # import demo_item_5_detailslist
    # import demo_item_6_dividers
    # import demo_item_7_dropdown
    # import demo_item_8_errorpages
    # import demo_item_9_headers
    # import demo_item_10_inputs
    # import demo_item_11_login_forms
    # import demo_item_12_media_alert
    # import demo_item_13_pagination
    # import demo_item_15_radiogroups #not working
    # import demo_item_16_selects
    # import demo_item_17_sideMenu # problem with twsty_tags
    # import demo_item_18_stats
    # import demo_item_19_steps
    # import demo_item_20_tables
    # import demo_item_21_tabs
    # import demo_item_22_textareas
    import demo_item_23_toggles
    # import demo_item_24_verticalmenu
    # import demo_item_25_ecom_carts  # problem with encoding decoding text-gray-600
    # import demo_item_26_collection_cards
    # import demo_item_27_collection_filters
    # import demo_item_28_featured_sections
    # import demo_item_29_product_cards # problem with encoding decoding 
    # import demo_item_30_product_collection
    # import demo_item_31_quantity_input
    # import demo_item_32_announcements
    # import demo_item_33_banners
    # import demo_item_34_blog_cards
    # import demo_item_35_buttons
    # import demo_item_36_cards
    # import demo_item_37_cta
    # import demo_item_38_faqs
    # import demo_item_39_footers # issues with encode/decode
    # import demo_item_40_forms
    # import demo_item_41_headers # issues with encode/decode
    # import demo_item_42_popups
    # import demo_item_43_pricings
    # import demo_item_44_sections
    # import demo_item_46_testimonials





app = oj.load_app()
