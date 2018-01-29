from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
import os

def _add_thumb(s):
    """
    Modifies a string (filename, URL) containing an image filename, to insert
    '.thumb.jpg' at the end.
    """
    return s + ".thumb.jpg"

class ThumbnailImageFieldFile(ImageFieldFile):
    @property
    def thumb_path(self):
        return _add_thumb(self.path)

    @property
    def thumb_url(self):
        return _add_thumb(self.url)

    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile, self).save(name, content, save)
        img = Image.open(self.path)
        size = img.size
        watermark = Image.open('/var/django/silica/gel/SilicaGelWatermark.png')
        img.paste(watermark, (img.size[0]-watermark.size[0],img.size[1]-watermark.size[1]),watermark)
        img.save(self.path, 'JPEG', quality=94)
        img.thumbnail((self.field.thumb_width, self.field.thumb_height), Image.ANTIALIAS )
        img.save(self.thumb_path, 'JPEG', quality=92)

    def delete(self, save=True):
        if os.path.exists(self._add_thumb(self.path)):
            os.remove(self._add_thumb(self.path))
        super(ThumbnailImageFieldFile, self).delete(save)

class ThumbnailImageField(ImageField):
    """
    Behaves like a regular ImageField, but stores an extra (JPEG) thumbnail
    image, providing get_FIELD_thumb_url() and get_FIELD_thumb_filename().

    Accepts two additional, optional arguments:  thumb_width and thumb_height,
    both defaulting to 100 (pixels).  Resizing will preserve aspect ratio while
    staying inside the requested dimensions; see PIL's Image.thumbnail()
    method documentation for details.
    """
    attr_class = ThumbnailImageFieldFile
    
    def __init__(self, thumb_width=100, thumb_height=100, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)

