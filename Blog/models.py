from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
import string
from MyBlog.utils import unique_slug_generator
# Create your models here.
class Homestay(models.Model):
    
    name=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    slug=models.SlugField(max_length=500, unique=True, blank=True)
    
    def __str__(self):
        return self.name

    def imageurl(self):
        self.image
        try:
            url=self.image.url
        except:
            url='static/images/dummy.png'    
        return url


def slug_generator(sender,instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)
              
    
pre_save.connect(slug_generator,sender=Homestay)








def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug