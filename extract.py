import re

with open('index.html', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'(<svg class="india-svg".*?</svg>)', content, re.DOTALL)
if m:
    with open('old_svg.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(1))
    print("Extracted")
else:
    print("Not found")
