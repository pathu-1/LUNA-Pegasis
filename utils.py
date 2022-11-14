import os
from werkzeug.utils import secure_filename

basepath = os.path.dirname(__file__)
def save_image(image_, dir_name_ = "uploads"):
    image_path_ = os.path.join(
        basepath,
        dir_name_,
        secure_filename(image_.filename)
    )
    image_.save(image_path_)
    return image_path_