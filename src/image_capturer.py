from io import BytesIO
from PIL import Image


def get_image_from_browser(browser):
    script = "return document.getElementsByTagName('canvas')[0].toDataURL()"

    raw_image = browser.execute_script(script)
    raw_image = raw_image[raw_image.find(',')+1:]
    image = Image.open(BytesIO(raw_image.decode('base64')))
    return image

