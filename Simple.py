def generate_svg_watch_dial_with_markers(diameter, num_minutes_markers, num_hours_markers, hole_radius):
    svg_content = f'<svg width="{diameter}mm" height="{diameter}mm" xmlns="http://www.w3.org/2000/svg">\n'

    # Draw white circle for watch dial
    svg_content += f'<circle cx="{diameter/2}mm" cy="{diameter/2}mm" r="{diameter/2}mm" fill="white" stroke="black" stroke-width="1"/>\n'

    # Draw markers for minutes
    for i in range(num_minutes_markers):
        angle = i * (360 / num_minutes_markers)
        x1 = diameter / 2 + (diameter / 2 - 2) * math.cos(math.radians(angle))
        y1 = diameter / 2 + (diameter / 2 - 2) * math.sin(math.radians(angle))
        x2 = diameter / 2 + (diameter / 2 - 6) * math.cos(math.radians(angle))
        y2 = diameter / 2 + (diameter / 2 - 6) * math.sin(math.radians(angle))
        svg_content += f'<line x1="{x1}mm" y1="{y1}mm" x2="{x2}mm" y2="{y2}mm" style="stroke:darkblue;stroke-width:1"/>\n'

    # Draw markers for hours
    for i in range(num_hours_markers):
        angle = i * (360 / num_hours_markers)
        x1 = diameter / 2 + (diameter / 2 - 2) * math.cos(math.radians(angle))
        y1 = diameter / 2 + (diameter / 2 - 2) * math.sin(math.radians(angle))
        x2 = diameter / 2 + (diameter / 2 - 8) * math.cos(math.radians(angle))
        y2 = diameter / 2 + (diameter / 2 - 8) * math.sin(math.radians(angle))
        svg_content += f'<line x1="{x1}mm" y1="{y1}mm" x2="{x2}mm" y2="{y2}mm" style="stroke:darkblue;stroke-width:2"/>\n'

    # Draw solid black circle in the center
    svg_content += f'<circle cx="{diameter/2}mm" cy="{diameter/2}mm" r="{hole_radius}mm" fill="black"/>\n'

    svg_content += '</svg>'
    return svg_content

import math

# Diameter of watch dial in mm
DIAMETER_MM = 30

# Number of minute and hour markers
NUM_MINUTES_MARKERS = 60
NUM_HOURS_MARKERS = 12

# Radius of hole in the center in mm
HOLE_RADIUS_MM = 1.5

svg_code = generate_svg_watch_dial_with_markers(DIAMETER_MM, NUM_MINUTES_MARKERS, NUM_HOURS_MARKERS, HOLE_RADIUS_MM)
print(svg_code)
