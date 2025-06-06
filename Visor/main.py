import dearpygui.dearpygui as dpg
import Callbacks.callbacks as cb
# from state import img_original, img_current, img_fusion

# Iniciamos el entorno gráfico -----------------------------------------
dpg.create_context()
dpg.create_viewport(title='Image Viewer', width=600, height=400)

with dpg.file_dialog(directory_selector=False, callback=cb.callback, show=False, tag="file_dialog", width=700 ,height=400):
    '''
    Configura el seleccionador de archivos
    '''
    
    dpg.add_file_extension(".jpg", color=(0, 255, 0, 255))
    dpg.add_file_extension(".png", color=(0, 255, 0, 255))
    dpg.add_file_extension(".bmp", color=(0, 255, 0, 255))

with dpg.file_dialog(directory_selector=False, callback=cb.fusion_callback, show=False, tag="file_dialog_fusion", width=700 ,height=400):
    '''
    Configura el seleccionador de archivos
    '''
    
    dpg.add_file_extension(".jpg", color=(0, 255, 0, 255))
    dpg.add_file_extension(".png", color=(0, 255, 0, 255))
    dpg.add_file_extension(".bmp", color=(0, 255, 0, 255))

with dpg.file_dialog(directory_selector=False, show=False, callback=cb.save_image, tag="file_dialog_save", width=700, height=400, modal=True):
    dpg.add_file_extension(".jpg", color=(0, 255, 0, 255))
    dpg.add_file_extension(".png", color=(255, 0, 0, 255))
    dpg.add_file_extension(".bmp", color=(0, 0, 255, 255))

# Ventanas para fusionar imagenes
with dpg.window(label="Fusion de imagenes", width=700, height=400, tag="fusion_window", show=False):
    '''
    Configura el seleccionador de archivos para fusionar imagenes
    '''
    dpg.add_text("Selecciona la imagen a fusionar:")
    dpg.add_button(label="Cargar", width=200, callback=lambda: dpg.show_item("file_dialog_fusion"))
    dpg.add_text("Selecciona el factor de fusion:")
    dpg.add_slider_float(label="Factor de fusion", tag="slider_factor", min_value=0.0, max_value=1.0, default_value=0.5, width=450)
    dpg.add_button(label="Fusionar",width=200,callback=lambda: cb.fusion_image(dpg.get_value("slider_factor")))

    dpg.add_button(label="Cancelar", callback=lambda: dpg.hide_item("fusion_window"))

with dpg.window(label="Image Viewer", width=1500, height=700, tag="ImageViewer"):
    '''
    Crea la ventana principal
    '''
    dpg.add_text("Visor de Imagenes", tag="title")
    dpg.add_separator()
    with dpg.group(horizontal=True):  # <- imagen a la izq, controles a la der
        # Imagen a la izquierda
        with dpg.group(tag="group_img"):
            dpg.add_spacer(height=10, width=700) # Colocamos un espacio en blanco de pequeño tamaño para que despues se inice ahí la imágen

        # Controles a la derecha
        with dpg.group(tag="group_controls"):
            dpg.add_text("Selecciona una imagen para visualizarla:")
            
            # Botones principales ------------------------------------------------------------------
            with dpg.group(horizontal=True):
                dpg.add_button(label="Cargar", width=200, callback=lambda: dpg.show_item("file_dialog"))
                dpg.add_button(label="Guardar Imagen", tag="btn_save", width=200, callback=lambda: dpg.show_item("file_dialog_save"))
                dpg.add_button(label="Resetear cambios", tag="btn_reset", width=200, callback=cb.reset)
            dpg.add_separator()
            
            # Botones para editar la imagen ---------------------------------------------------
            dpg.add_text("Controles de imagen:")
            dpg.add_text("Brillo: ")
            dpg.add_slider_float(label="Brillo", tag="slider_brillo", min_value=-1.0, max_value=1.0, default_value=0.0, width=450, callback=cb.brightness)
            dpg.add_text("Binarizar: ")
            dpg.add_slider_float(label="Binarizar", tag="slider_bin", min_value=0.0, max_value=1.0, default_value=0.0, width=450, callback=cb.binary)
            dpg.add_text("Contraste: ")
            dpg.add_slider_float(label="Contraste", tag="slider_contraste", min_value=0.0, max_value=2.0, default_value=0.0, width=450, callback=cb.contrast)
            dpg.add_radio_button(label="Zonas", tag="radio_zonas", items=["Zonas claras", "Zonas oscuras"], horizontal=True, callback=cb.contrast)
            
            # Botones para transformar la imagen ---------------------------------------------------
            dpg.add_text("Rotar: ")
            dpg.add_slider_int(label="Rotar", tag="slider_rotar", min_value=0, max_value=360, default_value=0, width=450, callback=cb.rotate)
            dpg.add_text("Zoom: ")
            dpg.add_slider_float(label="Zoom", tag="slider_zoom", min_value=1.0, max_value=3.0, default_value=1.0, width=450, callback=cb.zoom)
            dpg.add_separator()
            
            # Botones de caneles de color ---------------------------------------------------
            dpg.add_text("Canales de color:")
            with dpg.group(horizontal=True):
                dpg.add_button(label="Negativo", tag="btn_negativo", width=200, callback=cb.negative)
                dpg.add_button(label="Escala de grises", tag="btn_grises", width=200, callback=cb.grayscale)
                dpg.add_button(label="Histograma", tag="btn_histograma", width=200, callback=cb.histogram) 
            dpg.add_radio_button(items=["Modo RGB", "Modo CMY"], tag="color_settings", default_value="Modo RGB", callback=cb.visibility_channels)
            
            with dpg.group(tag="grupo_rgb", horizontal=True):
                dpg.add_text("Canales RGB:")
                dpg.add_checkbox(label="Rojo", tag="checkbox_r", default_value=False, callback=cb.color_settings)
                dpg.add_checkbox(label="Verde", tag="checkbox_g", default_value=False, callback=cb.color_settings)
                dpg.add_checkbox(label="Azul", tag="checkbox_b", default_value=False, callback=cb.color_settings)

            with dpg.group(tag="grupo_cmy", horizontal=True, show=False):
                dpg.add_text("Canales CMY:")
                dpg.add_checkbox(label="Cian", tag="checkbox_c", default_value=False, callback=cb.color_settings)
                dpg.add_checkbox(label="Magenta", tag="checkbox_m", default_value=False, callback=cb.color_settings)
                dpg.add_checkbox(label="Amarillo", tag="checkbox_y", default_value=False, callback=cb.color_settings)
            
            # Botones para fusionar imagenes ---------------------------------------------------
            dpg.add_text("Fusionar imagenes:")
            dpg.add_button(label="Fusionar", tag="btn_fusion", width=200, callback=lambda: dpg.show_item("fusion_window"))


# Estilos -----------------------------------------------------------------------------
with dpg.theme(tag="custom_theme"):
    '''
    Estilo de la ventana principal
    '''
    with dpg.theme_component(dpg.mvAll):
        # Fondo ventana
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (215, 217, 206, 255))
        # Fondo botón
        dpg.add_theme_color(dpg.mvThemeCol_Button, (12, 116, 137, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (17, 157, 164, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (19, 80, 91, 255))
        # Color texto
        dpg.add_theme_color(dpg.mvThemeCol_Text, (4, 4, 4, 255))
        # Fondo slider
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (17, 157, 164, 255))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (19, 80, 91, 255))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (12, 116, 137, 255))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (17, 157, 164, 255))
        # Fondo checkbox
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (215, 217, 206, 255))

# Aplicar a la ventana principal
dpg.bind_theme("custom_theme")

# Aplicar a los botones
with dpg.theme() as texto_widget_theme:
    '''
    Estilo de los widgets de texto
    '''
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (215, 217, 206, 255))
    with dpg.theme_component(dpg.mvSliderFloat):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (215, 217, 206, 255))
    with dpg.theme_component(dpg.mvSliderInt):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (215, 217, 206, 255))
dpg.bind_item_theme("ImageViewer", texto_widget_theme)

# Añadir fuentes de texto
with dpg.font_registry():
    title_font = dpg.add_font("fonts/norwester.otf", 40, tag="title_font")
    body_font = dpg.add_font("fonts/Roboto-VariableFont_wdth,wght.ttf", 17, tag="body_font")

# Estilo titulo
with dpg.theme(tag="title_theme"):
    with dpg.theme_component(dpg.mvText):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (17, 157, 164, 255))  


dpg.bind_item_font("title", title_font)
dpg.bind_item_theme("title", "title_theme")

dpg.bind_item_font("group_controls", body_font)

# Inicializacón de la ventana ----------------------------------
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("ImageViewer", True)
dpg.start_dearpygui()
dpg.destroy_context()