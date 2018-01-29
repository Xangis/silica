from django.db import models
from gel.fields import ThumbnailImageField
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify
from tagging.fields import TagField, Tag
import tagging

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class Color(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Color,self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Language,self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    brands = models.CharField(max_length=120, null=True, blank=True)
    slug = models.CharField(max_length=30, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Manufacturer,self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class SilicaPacket(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True) # Title
    additional_info = models.CharField(max_length=500, blank=True, null=True)
    found_in = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_id = models.ForeignKey('Manufacturer', null=True, blank=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    text_language = models.ManyToManyField('language', blank=True)
    print_color = models.ManyToManyField('color', blank=True)
    width = models.IntegerField(null=True, blank=True, help_text='in mm')
    height = models.IntegerField(null=True, blank=True, help_text='in mm')
    thickness = models.IntegerField(null=True, blank=True, help_text='in mm')
    weight = models.IntegerField(null=True, blank=True, help_text='in grams')
    date_added = models.DateField(auto_now_add=True)
    image = ThumbnailImageField(max_length=140, upload_to='images', null=True, blank=True)
    rear_image = ThumbnailImageField(max_length=140, upload_to='images', null=True, blank=True)

    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ('id',)

