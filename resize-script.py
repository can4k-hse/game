from PIL import Image

def resize_image(input_path, output_path, size):
    """
    size: (width, height)
    """
    img = Image.open(input_path)
    # Сохраняем пропорции, подгоняя под заданный размер:
    img.thumbnail(size)
    img.save(output_path, optimize=True, quality=85)

# Пример:
resize_image("./images/photo/katusha.jpg", "./images/photo/katusha-resize.jpg", (1920, 1080))