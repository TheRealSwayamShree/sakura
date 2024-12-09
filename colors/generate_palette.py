import os

# Updated function to save images in the same folder as the Python script
def create_palette_grid(theme, filename, is_light_theme=False, custom_dark_text_rows=None):
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties

    # Define fallback fonts within the function
    font = FontProperties(family="DejaVu Sans", size=9)
    bold_font = FontProperties(family="DejaVu Sans", size=9, weight="bold")

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.axis("off")
    
    # Grid configuration
    rows, cols = 4, 4
    cell_width = 1 / cols
    cell_height = 1 / rows
    
    for i, color_entry in enumerate(theme):
        row = i // cols
        col = i % cols
        
        rect_color = color_entry["color"]
        purpose = color_entry["purpose"]
        
        # Determine text color
        if is_light_theme and (row in [0, 2, 3] or (row == 1 and col in [0, 1])):
            text_color = "black"
        elif not is_light_theme and custom_dark_text_rows:
            # Custom rules for dark theme text colors
            if row in custom_dark_text_rows["black_rows"] or (row == 1 and col in custom_dark_text_rows["black_cols"]):
                text_color = "black"
            else:
                text_color = "white"
        else:
            text_color = "white"
        
        # Draw the color rectangle
        rect = plt.Rectangle((col * cell_width, (rows - 1 - row) * cell_height),
                             cell_width, cell_height, color=rect_color)
        ax.add_patch(rect)
        
        # Add the purpose text
        ax.text((col + 0.5) * cell_width, (rows - 0.35 - row) * cell_height,
                purpose,
                ha="center", va="center", fontproperties=font, color=text_color, wrap=True)
        
        # Add the bold hex code below the purpose
        ax.text((col + 0.5) * cell_width, (rows - 0.65 - row) * cell_height,
                rect_color,
                ha="center", va="center", fontproperties=bold_font, color=text_color, wrap=True)
    
    # Save the image in the same folder as the Python script
    output_path = os.path.join(os.getcwd(), filename)
    plt.savefig(output_path, bbox_inches="tight", dpi=300)
    plt.close(fig)

# Custom dark theme text color configuration
dark_text_rules = {
    "black_rows": [0, 2],       # 1st and 3rd rows
    "black_cols": [2, 3]        # 3rd and 4th elements of the 2nd row
}

# Define the color palettes
light_theme = [
    {"purpose": "Primary", "color": "#A7C7E7"},
    {"purpose": "Primary Variant", "color": "#89AFD7"},
    {"purpose": "Secondary", "color": "#FFD7BA"},
    {"purpose": "Secondary Variant", "color": "#FFC4A3"},
    {"purpose": "Background", "color": "#FAEFE6"},
    {"purpose": "Surface", "color": "#F5E8DE"},
    {"purpose": "Text Primary", "color": "#333333"},
    {"purpose": "Text Secondary", "color": "#666666"},
    {"purpose": "Accent", "color": "#98D4A8"},
    {"purpose": "Error", "color": "#F5A6A6"},
    {"purpose": "Warning", "color": "#F5D47F"},
    {"purpose": "Success", "color": "#98D4A8"},
    {"purpose": "Highlight", "color": "#D4B5E6"},
    {"purpose": "Disabled/Inactive", "color": "#E0E0E0"},
    {"purpose": "Border", "color": "#DADADA"},
    {"purpose": "Shadow", "color": "#FAEFE6"}
]

dark_theme = [
    {"purpose": "Primary", "color": "#80CBC4"},
    {"purpose": "Primary Variant", "color": "#4DB6AC"},
    {"purpose": "Secondary", "color": "#FF9100"},
    {"purpose": "Secondary Variant", "color": "#F48FB1"},
    {"purpose": "Background", "color": "#121212"},
    {"purpose": "Surface", "color": "#1E1E1E"},
    {"purpose": "Text Primary", "color": "#F1F1F1"},
    {"purpose": "Text Secondary", "color": "#B0B0B0"},
    {"purpose": "Accent", "color": "#A5D6A7"},
    {"purpose": "Error", "color": "#EF9A9A"},
    {"purpose": "Warning", "color": "#FFCC80"},
    {"purpose": "Success", "color": "#A5D6A7"},
    {"purpose": "Highlight", "color": "#7C4DFF"},
    {"purpose": "Disabled/Inactive", "color": "#424242"},
    {"purpose": "Border", "color": "#303030"},
    {"purpose": "Shadow", "color": "#0D0D0D"}
]

# Create and save the images in the same folder as the script
create_palette_grid(light_theme, "light_grid.png", is_light_theme=True)
create_palette_grid(dark_theme, "dark_grid.png", custom_dark_text_rows=dark_text_rules)
