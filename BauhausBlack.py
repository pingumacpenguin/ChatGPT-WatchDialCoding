import svgwrite
import math

def generate_watch_dial():
    # Create SVG Drawing
    drawing = svgwrite.Drawing('bauhaus_black_dial.svg', size=(30, 30), profile='full')

    # Define dial parameters
    center = (15, 15)
    radius = 12
    hour_marker_length = 1  # Length of hour markers
    minute_marker_length = 1  # Length of minute markers

    # Define styles
    background_style = {"stroke": "none", "fill": "#000000"}  # Black background
    marker_style = {"stroke": "#000000", "stroke-width": "0.2mm"}  # Black marker color

    # Draw background circle
    drawing.add(drawing.circle(center=center, r=radius, **background_style))

    # Draw hour markers
    for hour in range(1, 13):
        angle = math.radians((hour / 12) * 360 - 90)
        x1 = center[0] + math.cos(angle) * radius
        y1 = center[1] + math.sin(angle) * radius
        x2 = center[0] + math.cos(angle) * (radius + hour_marker_length)
        y2 = center[1] + math.sin(angle) * (radius + hour_marker_length)
        drawing.add(drawing.line(start=(x1, y1), end=(x2, y2), **marker_style))

    # Draw minute markers (only where there are no hour markers)
    for minute in range(1, 61):
        if minute % 5 != 0:  # Draw minute marker only if not at an hour position
            angle = math.radians((minute / 60) * 360 - 90)
            x1 = center[0] + math.cos(angle) * radius
            y1 = center[1] + math.sin(angle) * radius
            x2 = center[0] + math.cos(angle) * (radius + minute_marker_length)
            y2 = center[1] + math.sin(angle) * (radius + minute_marker_length)
            drawing.add(drawing.line(start=(x1, y1), end=(x2, y2), **marker_style))

    # Save the SVG file
    drawing.save()


if __name__ == "__main__":
    generate_watch_dial()

