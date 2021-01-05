# Add Jekyll Frontmatter to a markdown files

from pathlib import Path
import re

paths = Path('.').glob('*.md')
for path in paths:
    # because path is object not string
    path_in_str = str(path)
    # Do thing with the path
    print(path_in_str)
    with open(path_in_str,'r') as f:
        content = f.read()

    if content.startswith("---"):
        print(" - found frontmatter")
        continue

    match = re.search(r'^# ([^\n]*)', content)
    if not match:
        print(" - no title found")
        continue


    frontmatter = [
        "---",
        "layout: page",
        "title: %s" % match.group(1),
        "permalink: /%s" % path_in_str.replace(".md", ".html"),
        "---",
        ""
    ]
    with open(path_in_str,'w') as f:
        f.write("\n".join(frontmatter))
        f.write(content)
