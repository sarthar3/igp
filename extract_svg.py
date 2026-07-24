import re

# Read existing file to extract SVG content
with open('index.html', encoding='utf-8') as f:
    content = f.read()

# Extract the india SVG with all state paths (between <svg class="india-svg" ... </svg>)
svg_match = re.search(r'(<svg class="india-svg".*?</svg>)', content, re.DOTALL)
india_svg_raw = svg_match.group(1) if svg_match else ''

# Replace the styling attributes on the group element to match new design
india_svg = india_svg_raw.replace(
    'fill="rgba(255,255,255,0.03)" stroke="rgba(0,212,255,0.4)" stroke-width="2"',
    'fill="rgba(0,82,255,0.05)" stroke="rgba(0,82,255,0.35)" stroke-width="1.2"'
)

# Update hotspot coordinates and styling for new map (viewBox 0 0 612 696)
india_svg = re.sub(
    r'<!-- Hotspots -->.*?</svg>',
    '''<!-- Hotspots -->
            <g class="map-hotspot" onclick="selectCity('Delhi NCR', '450+ Installations', '24x7 Regional Command Center')">
              <circle cx="185" cy="185" r="14" fill="rgba(0,82,255,0.2)" class="hotspot-pulse"/>
              <circle cx="185" cy="185" r="6" fill="#0052FF"/>
              <text x="198" y="190" fill="#F8FAFC" font-size="11" font-family="Plus Jakarta Sans, sans-serif" font-weight="700">Delhi NCR</text>
            </g>
            <g class="map-hotspot" onclick="selectCity('Mumbai', '380+ Installations', 'Western Fleet Operations Hub')">
              <circle cx="125" cy="415" r="14" fill="rgba(0,82,255,0.2)" class="hotspot-pulse"/>
              <circle cx="125" cy="415" r="6" fill="#0052FF"/>
              <text x="55" y="420" fill="#F8FAFC" font-size="11" font-family="Plus Jakarta Sans, sans-serif" font-weight="700">Mumbai</text>
            </g>
            <g class="map-hotspot" onclick="selectCity('Bengaluru', '410+ Installations', 'Tech Park Grid Hub')">
              <circle cx="195" cy="548" r="14" fill="rgba(16,185,129,0.25)" class="hotspot-pulse"/>
              <circle cx="195" cy="548" r="6" fill="#10B981"/>
              <text x="208" y="553" fill="#F8FAFC" font-size="11" font-family="Plus Jakarta Sans, sans-serif" font-weight="700">Bengaluru</text>
            </g>
            <g class="map-hotspot" onclick="selectCity('Hyderabad', '260+ Installations', 'High-Power DC Plaza')">
              <circle cx="220" cy="450" r="14" fill="rgba(0,82,255,0.2)" class="hotspot-pulse"/>
              <circle cx="220" cy="450" r="6" fill="#0052FF"/>
              <text x="233" y="455" fill="#F8FAFC" font-size="11" font-family="Plus Jakarta Sans, sans-serif" font-weight="700">Hyderabad</text>
            </g>
          </svg>''',
    india_svg,
    flags=re.DOTALL
)

print(f"SVG extracted: {len(india_svg)} chars")
print(india_svg[:200])

# Write to a temp file for reference
with open('india_svg_extracted.txt', 'w', encoding='utf-8') as f:
    f.write(india_svg)
print("SVG saved to india_svg_extracted.txt")
