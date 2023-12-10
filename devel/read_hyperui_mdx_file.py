import frontmatter
import markdown2

# Path to your .mdx file
mdx_file_path = "/home/kabiraatmonallabs/DrivingRange/hyperui/src/data/components/application-ui-alerts.mdx"


# Read the content of the .mdx file
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

    # Extract main content
    main_content = post.content

# Print the extracted information
print("Title:", title)
print("Emoji:", emoji)
print("Category:", category)
print("Container:", container)
print("SEO Title:", seo_title)
print("SEO Description:", seo_description)

print("\nComponents:")
for component_id, component_data in components.items():
    print(f"{component_id}:")
    print(f"  Title: {component_data.get('title', '')}")
    print(f"  Dark: {component_data.get('dark', '')}")

print("\nMain Content:")
print(main_content)
