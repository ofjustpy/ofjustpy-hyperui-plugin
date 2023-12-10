from lxml import etree
from ofjustpy.SHC_types import PassiveComponents as PC
from ofjustpy.htmlcomponents import ActiveComponents as AC
from hyperui_plugin.SVGcomponents import PassiveComponents as SVGPassiveComponents
from justpy.htmlcomponents import (svg_tags,
                                   svg_tags_use,
                                   svg_presentation_attributes,
                                   svg_filter_attributes,
                                   svg_animation_attributes,
                                   svg_attr_dict
                                   )
from py_tailwind_utils import  tstr
from py_tailwind_utils.to_twsty_expr import encode_twstr

dtags = encode_twstr("block")

tag_to_passive_component = {

    'p': PC.P,
    'strong': PC.Strong
    }
tag_to_passive_div = {

    'div': PC.Div,
    'span': PC.SpanDiv,
    }

# has both text and childs
tag_to_passive_component_div = {
    'span': PC.SpanDiv,
    }

tag_to_active_component = {
    }

tag_to_active_div = {

    'button': AC.ButtonDiv,

    }

active_id_ctr = 0


    
def visit(element):
    global active_id_ctr
    twsty_tags = []
    if 'class' in element.attrib:
        print("=======================================")
        print (element.attrib['class'])
        twsty_tags = encode_twstr(element.attrib['class'])
        print("Encode decode = ", element.attrib['class'], tstr(*twsty_tags))
        del element.attrib['class']
        print("=======================================")
    #print ("entering ", element.tag, " with attribute: ", element.attrib)
    component_generator= None
    f = None
    if element.tag in tag_to_passive_component:
        component_generator = tag_to_passive_component[element.tag]
        num_children = len(element.getchildren())
        assert num_children == 0
        text = element.text

        if text:
            return component_generator(**element.attrib, text=text, twsty_tags=twsty_tags)
        else:
            return component_generator(**element.attrib, twsty_tags=twsty_tags)

    elif element.tag in tag_to_passive_component_div:
        component_generator = tag_to_passive_div[element.tag]
        f = lambda childs, text=element.text.strip(): component_generator(**element.attrib, text=text, childs=childs, twsty_tags=twsty_tags)
        
    elif element.tag in tag_to_passive_div:
        assert not element.text.strip()
        component_generator = tag_to_passive_div[element.tag]
        f = lambda childs: component_generator(**element.attrib, childs=childs, twsty_tags=twsty_tags)
            
    elif element.tag in tag_to_active_component:
        num_children = len(element.getchildren())
        assert num_children == 0
        component_generator = tag_to_active_component[element.tag]
        active_id_ctr += active_id_ctr
        if element.text:
            return component_generator(key=str(active_id_ctr), **element.attrib, text=text, twsty_tags=twsty_tags)
        else:
            return component_generator(key=str(active_id_ctr), **element.attrib)

    elif element.tag in tag_to_active_div:
        assert not element.text.strip()
        component_generator = tag_to_active_div[element.tag]
        f = lambda childs, key=str(active_id_ctr): component_generator(key=key, **element.attrib, childs = childs, twsty_tags=twsty_tags)
        active_id_ctr += active_id_ctr
        
    elif element.tag in svg_tags_use:
        tag = element.tag
        c_tag = tag[0].capitalize() + tag[1:]
        component_generator = getattr(SVGPassiveComponents, c_tag)
        f = lambda childs: component_generator(**element.attrib, childs=childs, twsty_tags=twsty_tags)
        #print("found svg component ", component_generator)
    else:
        print(element.tag, "  not found")
        assert False

    childs = [visit(_) for _ in element]
    #print ("exit ", element.tag, " with attribute: ", element.attrib)
    return f(childs=childs)

html_content = """
<p class="mt-1 text-sm text-gray-700">Your product changes have been saved.</p>
"""

# Example usage
html_content = """
<div role="alert" class="rounded-xl border border-gray-100 bg-white p-4">
  <div class="flex items-start gap-4">
    <span class="text-green-600">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="h-6 w-6"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
        />
      </svg>
    </span>

    <div class="flex-1">
      <strong class="block font-medium text-gray-900"> Changes saved </strong>

      <p class="mt-1 text-sm text-gray-700">Your product changes have been saved.</p>
    </div>

    <button class="text-gray-500 transition hover:text-gray-600">
      <span class="sr-only">Dismiss popup</span>

      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="h-6 w-6"
      >
        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
      </svg>
    </button>
  </div>
</div>
"""

# html_content = """
# <p class="mt-1 text-sm text-gray-700">Your product changes have been saved.</p>
# """
parser = etree.HTMLParser()
root = etree.fromstring(html_content, parser)
content_root_elem = root.find("./body/*[1]")

# root_hcpo: html_component python object
root_hcpo = visit(content_root_elem)


import ofjustpy as oj
app = oj.load_app()
endpoint = oj.create_endpoint("svg_demo_1",
                   childs = [root_hcpo],
                   )
oj.add_jproute("/", endpoint)

# from starlette.testclient import TestClient
# testclient = TestClient(app)
# testclient.get("/")
