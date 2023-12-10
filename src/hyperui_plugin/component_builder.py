"""
from hyperui repo, parse the html and build all the components
"""

from lxml import etree
from pathlib import Path
import frontmatter
import ofjustpy as oj
from ofjustpy.SHC_types import PassiveComponents as PC
from ofjustpy.htmlcomponents import ActiveComponents as AC
from ofjustpy.htmlcomponents import ActiveDivs as AD
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

tag_to_passive_component = {
    'p': PC.P,
    'strong': PC.Strong,
    'h1': PC.H1,
    'h2': PC.H2,
    'h3': PC.H3,
    'li': PC.Li,
    'img': PC.Img,
    'label': PC.Label,
    'span': PC.Span,
    'a': PC.A,
    'dt': PC.Dt,
    'dd': PC.Dd,
    'div': PC.Div,
    'legend': PC.Legend,
    'option': PC.Option,
    'small': PC.Small,
    'th': PC.Th,
    'td': PC.Td,
    'br': PC.Br,
    'time': PC.Time,
    'address': PC.Address,
    'script': PC.ScriptDiv,
    'link': PC.A,
    'blockquote': PC.BlockquoteDiv,
    'footer': PC.Footer
    
    }
tag_to_passive_div = {

    'div': PC.Div,
    'span': PC.SpanDiv,
    'nav': PC.Nav,
    'ol': PC.Ol,
    'li': PC.Li,
    'dl': PC.Dl,
    'dt': PC.DtDiv,
    'dd': PC.DdDiv,
    'header': PC.Header,
    'p': PC.PDiv,
    'label': PC.LabelDiv,
    'section': PC.Section,
    'aside': PC.Aside,
    'main': PC.Main,
    'fieldset': PC.Fieldset,
    'optgroup': PC.Optgroup,
    'datalist': PC.Datalist,
    'ul': PC.Ul,
    'details': PC.Details,
    'summary': PC.Summary,
    'article': PC.Article,
    'table': PC.Table,
    'thead': PC.Thead,
    'tr': PC.Tr,
    'td': PC.Td,
    'th': PC.Th,
    'tbody': PC.Tbody,
    'h1': PC.H1Div,
    'h2': PC.H2Div,
    'h3': PC.H3Div,
    'time': PC.Time,
    'strong': PC.Strong,
    'footer': PC.Footer,
    'address': PC.Address,
    'script': PC.ScriptDiv,
    'blockquote': PC.BlockquoteDiv
    }

# has both text and childs
tag_to_passive_component_div = {
    'span': PC.SpanDiv,
    'p': PC.PDiv
    }

tag_to_active_component = {
    'input': AC.TextInput,
    'button': AC.Button,
    'textarea': AC.Textarea
    }

tag_to_active_div = {
    'button': AD.Button,
    'a': AD.A,
    'form': AD.Form,
    'select': AD.Select
    }

active_id_ctr = 0
oj.set_style('un')
def visit(element):
    global active_id_ctr
    twsty_tags = []
    if 'class' in element.attrib:
        print("=======================================")
        print ("encoding class = ", element.attrib['class'])

        twsty_tags = encode_twstr(element.attrib['class'])
        print("Encoded decode = ",  tstr(*twsty_tags))
        del element.attrib['class']
        print("===================EnD====================")

    component_generator= None
    f = None
    num_children = len(element.getchildren())
    if element.tag in svg_tags_use:
        tag = element.tag
        c_tag = tag[0].capitalize() + tag[1:]
        component_generator = getattr(SVGPassiveComponents, c_tag)
        f = lambda childs: component_generator(**element.attrib, childs=childs, twsty_tags=twsty_tags)

    else:
        if num_children == 0:
            if element.tag in tag_to_passive_component:
                component_generator = tag_to_passive_component[element.tag]
                text = element.text

                if text:
                    return component_generator(**element.attrib, text=text, twsty_tags=twsty_tags)
                else:
                    return component_generator(**element.attrib, twsty_tags=twsty_tags)

            elif element.tag in tag_to_active_component:
                component_generator = tag_to_active_component[element.tag]
                active_id_ctr += active_id_ctr
                if element.text:
                    return component_generator(key=str(active_id_ctr), **element.attrib, text=element.text, twsty_tags=twsty_tags)
                else:
                    return component_generator(key=str(active_id_ctr), **element.attrib)
            else:
                print(" not found ", element.tag, " num_children=", num_children)
                assert False

        else:

            if element.tag in tag_to_passive_component_div:
                kwargs = {}
                if element.text:
                    kwargs['text'] = element.text.strip()

                component_generator = tag_to_passive_div[element.tag]
                f = lambda childs, kwargs=kwargs: component_generator(**element.attrib, **kwargs, childs=childs, twsty_tags=twsty_tags)

            elif element.tag in tag_to_passive_div:
                kwargs = {}
                if element.text:
                    kwargs['text'] = element.text.strip()
                component_generator = tag_to_passive_div[element.tag]
                f = lambda childs, kwargs=kwargs: component_generator(**element.attrib, childs=childs, twsty_tags=twsty_tags, **kwargs)

            elif element.tag in tag_to_active_div:
                kwargs = {}
                if element.text.strip():
                    kwargs['text'] = element.text.strip()
                component_generator = tag_to_active_div[element.tag]
                f = lambda childs, key=str(active_id_ctr), kwargs=kwargs: component_generator(key=key, **element.attrib, childs = childs, twsty_tags=twsty_tags, **kwargs)
                active_id_ctr += active_id_ctr


            else:
                print(" not found ", element.tag, " num_children=", num_children)
                assert False

    childs = [visit(_) for _ in element]
    #print ("exit ", element.tag, " with attribute: ", element.attrib)
    return f(childs=childs)


    

def build_component(html_content):
    """
    from hyperui html+tailwind css description -- derive an ofjustpy component 
    """
    parser = etree.HTMLParser()
    root = etree.fromstring(html_content, parser)
    #root level tag
    rlt = None
    if root.find("./body"):
        rlt = "./body"
    if root.find("./head"):
        rlt = "./head"

    assert rlt is not None
    if root.find(f"{rlt}/link") and root.find(f"{rlt}/script"):
        content_root_elem = root.find(f"{rlt}/*[3]")
    elif root.find(f"{rlt}/script") or root.find(f"{rlt}/link"):
        content_root_elem = root.find(f"{rlt}/*[2]")
    else:
        content_root_elem = root.find(f"{rlt}/*[1]")

    # root_hcpo: html_component python object
    root_hcpo = visit(content_root_elem)
    return root_hcpo


# ======================= build all components =======================
hyper_ui_src_repo = '/home/kabiraatmonallabs/DrivingRange/hyperui'
path = Path(f'{hyper_ui_src_repo}/public/components')

def get_metadata(ui_category):
    """
    get metadata for a ui_category.
    returns title of the of the ui_category, and id, title for each component of
    the category
    """
    mdx_file_path = f"{hyper_ui_src_repo}/src/data/components/{ui_category}.mdx"
    with open(mdx_file_path, "r", encoding="utf-8") as file:
        # Parse frontmatter and content
        post = frontmatter.load(file)
        # Extract metadata
        title = post.get("title", "")
        emoji = post.get("emoji", "")
        category = post.get("category", "")
        container = post.get("container", "")
        seo_title = post.get("seo", {}).get("title", "")
        seo_description = post.get("seo", {}).get("description", "")

        # Extract components
        components = post.get("components", {})

        components_pyds = []
        for component_id, component_data in components.items():
            # print(f"{component_id}:")
            # print(f"  Title: {component_data.get('title', '')}")
            # print(f"  Dark: {component_data.get('dark', '')}")
            pyds = { 'id': component_id,
              'title': component_data.get('title', ''),
                     


                }
            if 'dark' in component_data:
                pyds['dark']  =  component_data.get('dark')
            components_pyds.append(pyds
                )

        # Extract main content
        main_content = post.content
        return title, components_pyds
    pass

def build_all_components():
    for child in path.iterdir():
        if child.is_dir():
            title, component_pyds = get_metadata(child.name)

            print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=> ", title)
            print (component_pyds)

            for html_file in child.rglob('*.html'):
                print('----------------------------------')
                if 'interactive' in html_file.name:
                    print("DEBUG : skip interactive")
                    continue
                print ("?????????????????????????????????????????????????now build component for ", html_file.name)

                content = html_file.read_text()
                yield build_component(content)



