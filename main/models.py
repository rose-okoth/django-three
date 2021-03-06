from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from PIL import Image

# Create your models here.
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Project(models.Model):
    user = models.ForeignKey('Profile', default=1, on_delete=models.CASCADE, related_name='project')
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = CloudinaryField(
            null=True, 
            blank=True, 
            height_field='height_field', 
            width_field='width_field')    
    description = models.TextField()
    link = models.URLField()
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    publish = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

def create_slug(instance, new_slug=None):

    '''Create slug function'''

    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Project.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):

    '''Save slug function'''

    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Project)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

class Review(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name="review")
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="review")
    design_rating = models.FloatField(null=True, blank=True)
    usability_rating = models.FloatField(null=True, blank=True)
    content_rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.bio} Project'