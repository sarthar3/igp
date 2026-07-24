import re
import xml.etree.ElementTree as ET

# Read old HTML
with open('index.html', encoding='utf-8') as f:
    html_content = f.read()

# Read new SVG paths
with open('node_modules/@svg-maps/india/india.svg', encoding='utf-8') as f:
    new_svg_content = f.read()

# Extract paths from new SVG
paths = re.findall(r'<path.*?/>', new_svg_content, re.DOTALL)
paths_str = '\n'.join(paths)
paths_group = f'<g fill="rgba(255,255,255,0.03)" stroke="rgba(0,212,255,0.4)" stroke-width="2">\n{paths_str}\n</g>'

# Approximate coordinates for new viewBox (612 696)
# India map: Top ~50, Bottom ~685, Left ~60, Right ~585
# Delhi: North India
# Mumbai: West coast middle
# Bengaluru: South inland
# Hyderabad: Central South

hotspots = """
            <!-- Hotspots -->
            <g class="map-hotspot" onclick="selectCity('Delhi NCR', '450+ Stations', 'Hub 1')">
              <circle cx="185" cy="190" r="10" fill="rgba(0, 212, 255, 0.3)" class="hotspot-pulse"/>
              <circle cx="185" cy="190" r="5" fill="#00D4FF"/>
              <text x="195" y="195" fill="#FFF" font-size="12" font-weight="700">Delhi NCR</text>
            </g>

            <g class="map-hotspot" onclick="selectCity('Mumbai', '380+ Stations', 'Hub 2')">
              <circle cx="130" cy="420" r="10" fill="rgba(0, 212, 255, 0.3)" class="hotspot-pulse"/>
              <circle cx="130" cy="420" r="5" fill="#00D4FF"/>
              <text x="60" y="425" fill="#FFF" font-size="12" font-weight="700">Mumbai</text>
            </g>

            <g class="map-hotspot" onclick="selectCity('Bengaluru', '410+ Stations', 'Hub 3')">
              <circle cx="195" cy="550" r="10" fill="rgba(0, 212, 255, 0.3)" class="hotspot-pulse"/>
              <circle cx="195" cy="550" r="5" fill="#00D4FF"/>
              <text x="207" y="555" fill="#FFF" font-size="12" font-weight="700">Bengaluru</text>
            </g>

            <g class="map-hotspot" onclick="selectCity('Hyderabad', '260+ Stations', 'Hub 4')">
              <circle cx="215" cy="450" r="10" fill="rgba(0, 212, 255, 0.3)" class="hotspot-pulse"/>
              <circle cx="215" cy="450" r="5" fill="#00D4FF"/>
              <text x="227" y="455" fill="#FFF" font-size="12" font-weight="700">Hyderabad</text>
            </g>
"""

new_svg = f'<svg class="india-svg" viewBox="0 0 612 696" fill="none">\n{paths_group}\n{hotspots}\n</svg>'

new_html = re.sub(r'<svg class="india-svg".*?</svg>', new_svg, html_content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Done replacing.")
