from hyperui_plugin.component_builder import build_component
import frontmatter
import markdown2
from pathlib import Path

hyper_ui_src_repo = '/home/kabiraatmonallabs/DrivingRange/hyperui'
path = Path(f'{hyper_ui_src_repo}/public/components')

def get_metadata(ui_category):
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


input_box_path = {
    'alerts': ["./div/div/div"]
    }

# list widget directory
for child in path.iterdir():
    if child.is_dir():
        title, component_pyds = get_metadata(child.name)
        for html_file in child.rglob('*.html'):
            print(html_file.name)
            with open(html_file_path, "r", encoding="utf-8") as file:
                return file.read()
            # build component using content in html_file
            hui.dropdown(type_tags=[])
            

