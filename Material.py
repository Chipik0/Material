import cv2
import ctypes
import numpy as np
from sklearn.cluster import KMeans


RGB = 'rgb'
HEX = 'hex'

def get_wallpaper_path():
    '''
    # Wallpaper path
    Returns the full path of the installed Windows wallpaper.
    '''
    SPI_GETDESKWALLPAPER = 0x73
    buf_size = 260  # MAX_PATH
    wallpaper_path = ctypes.create_unicode_buffer(buf_size)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, buf_size, wallpaper_path, 0)
    return wallpaper_path.value

def get_popular_color(image_path, output=RGB):
    '''
    # Popular color
    Returns the most popular color of image.

    image_path - Path to image
    output - RGB / HEX color output
    '''

    try:
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except:
        stream = open(image_path, 'rb')
        bytes = bytearray(stream.read())
        array = np.asarray(bytes, dtype=np.uint8)
        image = cv2.imdecode(array, cv2.IMREAD_UNCHANGED)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pixels = image.reshape(-1, 3)
    color_counts = np.bincount(pixels[:, 0] * 65536 + pixels[:, 1] * 256 + pixels[:, 2])
    popular_color_index = np.argmax(color_counts)

    r = popular_color_index // 65536
    g = (popular_color_index % 65536) // 256
    b = popular_color_index % 256

    if output == RGB:
        return (int(r), int(g), int(b))
    elif output == HEX:
        return '#%02x%02x%02x' % (int(r), int(g), int(b))

def get_popular_colors(image_path, amount = 3, output=RGB):
    '''
    # Popular colors
    ##### ! - The colors are given in random order
    Returns the most popular colors of image.

    image_path - Path to image
    amount - amount of popular colors
    output - RGB / HEX color output
    '''

    try:
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except:
        stream = open(image_path, 'rb')
        bytes = bytearray(stream.read())
        array = np.asarray(bytes, dtype=np.uint8)
        image = cv2.imdecode(array, cv2.IMREAD_UNCHANGED)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pixels = image.reshape((-1, 3))
    kmeans = KMeans(n_clusters=amount)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_
    colors = colors.round().astype(int)

    if output == RGB:
        return colors
    
    elif output == HEX:
        list_of_colors = ["#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2]) for color in colors]
        list_of_colors.sort()
        return list_of_colors
    
def check_new_wallpapers():
    '''
    # Checking wallpapers
    Returns True if the wallpaper was changed to a new one after the program was launched
    '''

    new_wallpapers = get_wallpaper_path()
    if current_wallpapers != new_wallpapers:
        return True
    else:
        return False

current_wallpapers = get_wallpaper_path()