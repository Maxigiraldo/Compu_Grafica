from Librerias import image_processor as ip
from Librerias import Transformaciones as tf
import state as st
import dearpygui.dearpygui as dpg
import numpy as np
import matplotlib.pyplot as plt

def show_image(img, ventana):
    textura = None
    display = None
    if ventana == "group_img":
        textura = "image_texture"
        display = "image_display"
    elif ventana == "fusion_window":
        textura = "fusion_texture"
        display = "fusion_display"
    
    max_width, max_height = 600, 400
    height, width = img.shape[:2]
    scale = min(max_width / width, max_height / height, 1.0)
    scaled_width = int(width * scale)
    scaled_height = int(height * scale)
    flat_img = img.flatten()

    if dpg.does_item_exist(textura):
        current_width = dpg.get_item_configuration(textura)["width"]
        current_height = dpg.get_item_configuration(textura)["height"]
        if current_width != width or current_height != height:
            dpg.delete_item(textura)
            dpg.delete_item(display)

    if not dpg.does_item_exist(textura):
        with dpg.texture_registry(show=False):
            dpg.add_raw_texture(width=width, height=height, default_value=flat_img,
                                format=dpg.mvFormat_Float_rgb, tag=textura)
    else:
        dpg.set_value(textura, flat_img)

    if not dpg.does_item_exist(display):
        dpg.add_image(textura, tag=display, width=scaled_width, height=scaled_height, parent=ventana)
    else:
        dpg.configure_item(display, width=scaled_width, height=scaled_height)

def brightness():
    factor = dpg.get_value("slider_brillo")
    if st.img_current is not None:
        st.img_current = tf.brightness_adjust(st.img_original.copy(), factor)
        show_image(st.img_current, "group_img")

def binary():
    umbral = dpg.get_value("slider_bin")
    if st.img_current is not None:
        st.img_current = tf.binary(st.img_original.copy(), umbral)
        show_image(st.img_current, "group_img")

def contrast():
    if st.img_original is None:
        return

    contraste = dpg.get_value("slider_contraste") 
    zona = dpg.get_value("radio_zonas") 

    # Proteger la imagen
    if zona == "Zonas claras":
        st.img_current = tf.contrast_adjust_brightness(st.img_original.copy(), contraste)
    elif zona == "Zonas oscuras":
        st.img_current = tf.contrast_adjust_darkness(st.img_original.copy(), contraste)

    show_image(st.img_current, "group_img")

def color_settings():
    '''
    Verifica según las checkboxs los canales activos, desactivandolos o activandolos según el caso
    '''
    
    if st.img_original is None:
        return

    img = st.img_original.copy()
    modo = dpg.get_value("color_settings")

    if modo == "Modo RGB":
        if not dpg.get_value("checkbox_r"):
            img = ip.red_cape(img)
        if not dpg.get_value("checkbox_g"):
            img = ip.green_cape(img)
        if not dpg.get_value("checkbox_b"):
            img = ip.blue_cape(img)

    elif modo == "Modo CMY":
        if dpg.get_value("checkbox_c"):
            img = ip.red_cape(img)   # Cian: eliminar rojo
        if dpg.get_value("checkbox_m"):
            img = ip.green_cape(img) # Magenta: eliminar verde
        if dpg.get_value("checkbox_y"):
            img = ip.blue_cape(img)  # Amarillo: eliminar azul

    st.img_current = img
    show_image(img, "group_img")

def visibility_channels():
    '''
    Al momento de utilizar los canales RGB y CMYK, está función lo que hace es 
    desahibilitar los campos del canal que no esté activo y resetea los valores de
    la imágen para evitar inconvenientes    
    '''
    modo = dpg.get_value("color_settings")

    if modo == "Modo RGB":
        dpg.show_item("grupo_rgb")
        dpg.hide_item("grupo_cmy")
        # Opcional: resetear CMY
        dpg.set_value("checkbox_c", False)
        dpg.set_value("checkbox_m", False)
        dpg.set_value("checkbox_y", False)

    else:
        dpg.show_item("grupo_cmy")
        dpg.hide_item("grupo_rgb")
        # Opcional: resetear RGB
        dpg.set_value("checkbox_r", True)
        dpg.set_value("checkbox_g", True)
        dpg.set_value("checkbox_b", True)

    color_settings()

def negative():
    if st.img_original is None:
        return

    st.img_current = ip.invert_color(st.img_original.copy())
    show_image(st.img_current, "group_img")

def rotate():
    if st.img_original is None:
        return

    angle = dpg.get_value("slider_rotar")
    st.img_current = tf.rotate(st.img_original.copy(), angle)
    show_image(st.img_current, "group_img")

def grayscale():
    if st.img_original is None:
        return

    st.img_current = ip.midgray(st.img_original.copy())
    
    show_image(st.img_current, "group_img")

def histogram():
    if st.img_original is None:
        return

    # Calcular el histograma
    tf.RGB_Histogram(st.img_original.copy())
    

def zoom():
    if st.img_original is None:
        return

    # Obtener el factor de zoom del slider
    zoom_factor = dpg.get_value("slider_zoom")
    
    # Aplicar el zoom a la imagen original
    st.img_current = tf.zoom(st.img_original.copy(), zoom_factor)
    
    show_image(st.img_current, "group_img")

def fusion_image(factor):
    if st.img_original is None:
        return
    # Fusionar las imágenes
    st.img_current = tf.fusion_images(st.img_original.copy(), st.img_fusion.copy(), factor)
    
    show_image(st.img_current, "group_img")

def reset():
    if st.img_original is None:
        return

    # Resetear la imagen actual a la original
    st.img_current = st.img_original.copy()
    # Resetear los sliders a sus valores por defecto
    dpg.set_value("slider_brillo", 0.0)
    dpg.set_value("slider_bin", 0.0)
    dpg.set_value("slider_contraste", 0.0)
    dpg.set_value("slider_rotar", 0)
    dpg.set_value("slider_zoom", 1.0)
    dpg.set_value("checkbox_r", True)
    dpg.set_value("checkbox_g", True)
    dpg.set_value("checkbox_b", True)
    dpg.set_value("checkbox_c", False)
    dpg.set_value("checkbox_m", False)
    dpg.set_value("checkbox_y", False)
    show_image(st.img_current, "group_img")

def save_image(sender, app_data, user_data):
    '''
    Guardar la imagen actual en el directorio especificado
    '''
    if st.img_current is None:
        print("No hay imagen para guardar.")
        return

    ruta = app_data['file_path_name']
    img_guardar = (np.clip(st.img_current, 0, 1) * 255).astype(np.uint8) # Convertir la imágen a un formato que se pueda guardar en matplotlib
    
    plt.imsave(ruta, img_guardar)
    print(f"Imagen guardada en: {ruta}")

def callback(sender, app_data, user_data):
    '''
    Callback que se ejecuta para seleccionar una imagen
    '''
    
    reset()
    file_path = app_data['file_path_name']
    if file_path:
        # Cargar la imagen
        img = tf.create_img(file_path)
        # Guardar la imagen original y la actual 
        st.img_original = img.copy()
        st.img_current = img.copy()
        show_image(img, "group_img")  

def fusion_callback(sender, app_data, user_data):
    '''
    Callback que se ejecuta para seleccionar la imágen a fusionar
    '''
    file_path = app_data['file_path_name']
    if file_path:
        # Cargar la imagen
        img = tf.create_img(file_path)
        # Guardar la imagen a fusionar
        st.img_fusion = img.copy()
        
        # Recortar la imagen a fusionar al tamaño de la imagen original
        width, height = st.img_original.shape[:2]
        st.img_fusion = tf.snip(st.img_fusion, 0, 0, width, height)
        
        # Mostrar la imagen a fusionar
        show_image(st.img_fusion, "fusion_window")