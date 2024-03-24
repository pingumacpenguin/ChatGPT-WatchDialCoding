import svgwrite
import math

def generate_watch_dial():
    # Create SVG Drawing with width and height in millimeters
    drawing = svgwrite.Drawing('watch_dial.svg', size=('30mm', '30mm'), profile='full')

    # Define styles
    dial_style = "fill:none;stroke:#2C3E50;stroke-width:0.1mm"  # Dark blue color for outer circle
    hour_marker_style = {"stroke": "#1F618D", "stroke-width": "0.4mm"}  # Dark blue color for hour markers
    minute_marker_style = {"stroke": "#34495E", "stroke-width": "0.2mm"}  # Slightly lighter shade of blue for minute markers
    center_circle_style = "fill:none;stroke:#1F618D;stroke-width:0.1mm"  # Dark blue color for center circle

    # Draw watch dial centered at (15mm, 15mm) with a radius of 15mm
    dial = drawing.circle(center=('15mm', '15mm'), r='15mm', style=dial_style)
    drawing.add(dial)

    # Draw center circle
    center_circle = drawing.circle(center=('15mm', '15mm'), r='1.5mm', style=center_circle_style)
    drawing.add(center_circle)

    # Define center coordinates in millimeters
    center_x, center_y = 15, 15

    # Define radius for markers in millimeters
    marker_radius = 12

    # Draw minute markers
    for minute in range(0, 60):
        minute_angle = math.radians(90 - minute * 6)  # Convert minute to radians
        minute_x_outer = center_x + marker_radius * math.cos(minute_angle)
        minute_y_outer = center_y - marker_radius * math.sin(minute_angle)
        minute_x_inner = center_x + (marker_radius - 1) * math.cos(minute_angle)  # Adjusted inner point
        minute_y_inner = center_y - (marker_radius - 1) * math.sin(minute_angle)  # Adjusted inner point
        marker = drawing.line(start=(f'{minute_x_outer}mm', f'{minute_y_outer}mm'),
                              end=(f'{minute_x_inner}mm', f'{minute_y_inner}mm'),
                              **minute_marker_style, stroke_linecap='round')
        drawing.add(marker)

    # Re-define marker radius for the hour markers
    marker_radius = 14.5

    # Draw hour markers
    for hour in range(0, 12):
        hour_angle = math.radians(90 - hour * 30)  # Convert hour to radians
        hour_x_outer = center_x + marker_radius * math.cos(hour_angle)
        hour_y_outer = center_y - marker_radius * math.sin(hour_angle)
        hour_x_inner = center_x + (marker_radius - 2) * math.cos(hour_angle)  # Adjusted inner point
        hour_y_inner = center_y - (marker_radius - 2) * math.sin(hour_angle)  # Adjusted inner point
        marker = drawing.line(start=(f'{hour_x_outer}mm', f'{hour_y_outer}mm'),
                              end=(f'{hour_x_inner}mm', f'{hour_y_inner}mm'),
                              **hour_marker_style, stroke_linecap='round')
        drawing.add(marker)

    # Save SVG
    drawing.save()


if __name__ == "__main__":
    generate_watch_dial()

