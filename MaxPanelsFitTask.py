def max_panels_fit(panel_dimension_1, panel_dimension_2, roof_width, roof_height):

    if panel_dimension_1 <= 0 or panel_dimension_2 <= 0 or roof_width <= 0 or roof_height <= 0:
        raise ValueError("Las dimensiones deben ser positivas.\n" +
                         f"Dimensiones recibidas: panel_dimension_1={panel_dimension_1}," + 
                         f"panel_dimension_2={panel_dimension_2}, roof_width={roof_width}, roof_height={roof_height}")
    
    def calculate_panels(panel_width, panel_height):
        panels_wide = roof_width // panel_width
        panels_tall = roof_height // panel_height
        total_full_panels = panels_wide * panels_tall
        
        residual_width = roof_width % panel_width
        residual_height = roof_height % panel_height
        
        extra_width = (residual_width // panel_height) * (roof_height // panel_width)
        extra_height = (residual_height // panel_width) * (roof_width // panel_height)
        
        return total_full_panels + max(extra_width, extra_height)

    panels_orientation_1 = calculate_panels(panel_dimension_1, panel_dimension_2)
    panels_orientation_2 = calculate_panels(panel_dimension_2, panel_dimension_1)
    
    return int(max(panels_orientation_1, panels_orientation_2))


try:
    print(max_panels_fit(1, 2, 2, 4))
except ValueError as e:
    print(e)
