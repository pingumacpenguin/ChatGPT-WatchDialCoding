import svgwrite
import math

def generate_watch_dial():
    # Create SVG Drawing
    drawing = svgwrite.Drawing('numeric_dial.svg', size=(30, 30), profile='full')

    # Define styles
    dial_style = "stroke:#192A56;stroke-width:0.1mm;fill:none;"
    hour_marker_style = {"stroke": "#001F3F", "stroke-width": "0.2mm", "stroke-linecap": "round"}
    minute_marker_style = {"stroke": "#85C1E9", "stroke-width": "0.1mm", "stroke-linecap": "round"}
    center_circle_style = {"stroke": "#000000", "stroke-width": "0.1mm", "fill": "none"}
    hour_number_style = {"text-anchor": "middle", "dominant-baseline": "central", "font-size": "1mm", "fill": "#000000"}  # Black color for hour numbers

    # Draw watch dial
    drawing.add(svgwrite.shapes.Circle(center=(15, 15), r=15, style=dial_style))

    # Draw hour markers
    for hour in range(1, 13):
        if hour % 3 != 0:  # Skip drawing hour markers at 12, 3, 6, and 9
            angle = math.radians((hour - 3) * 30)  # Calculate angle
            x1 = 15 + 12 * math.cos(angle)  # Calculate x coordinate
            y1 = 15 + 12 * math.sin(angle)  # Calculate y coordinate
            x2 = 15 + 13 * math.cos(angle)  # Calculate x coordinate for line end
            y2 = 15 + 13 * math.sin(angle)  # Calculate y coordinate for line end
            drawing.add(drawing.line(start=(x1, y1), end=(x2, y2), **hour_marker_style))

    # Draw minute markers
    for minute in range(1, 61):
        if minute % 5 != 0:  # Skip drawing minute markers at 15, 30, 45, and 60
            angle = math.radians((minute - 15) * 6)  # Calculate angle
            x1 = 15 + 13.5 * math.cos(angle)  # Calculate x coordinate
            y1 = 15 + 13.5 * math.sin(angle)  # Calculate y coordinate
            x2 = 15 + 14 * math.cos(angle)  # Calculate x coordinate for line end
            y2 = 15 + 14 * math.sin(angle)  # Calculate y coordinate for line end
            drawing.add(drawing.line(start=(x1, y1), end=(x2, y2), **minute_marker_style))

    # Draw center circle
    drawing.add(svgwrite.shapes.Circle(center=(15, 15), r=1.5, **center_circle_style))

    # Draw hour numbers
    for hour, angle_offset in [(12, -90), (3, 0), (6, 90), (9, 180)]:
        angle = math.radians(angle_offset)  # Calculate angle
        radius = 11  # Radius of the circle passing through the midpoint of the hour marker lines
        x = 15 + radius * math.cos(angle)  # Calculate x coordinate
        y = 15 + radius * math.sin(angle)  # Calculate y coordinate
        drawing.add(svgwrite.text.Text(f'{hour}', insert=(x, y), **hour_number_style))

    # Save the SVG
    drawing.save()

generate_watch_dial()

