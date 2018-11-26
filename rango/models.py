from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField(blank=True)
    '''
     When we update the models via the migration tool, it will add the field,
    and provide the option of populating the field with a default value. Of course, we want a specific
    value in each field. In order to correctly populate the slug field we will need to first perform the
    migration and then re-run the population script - this is because in the population script we explicitly
    call the ‘save’ method for each entry. This will trigger the ‘save’ we have implemented and update
    the slug accordingly
    '''
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        #everytime when name will be updated this method will rerun
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __str__(self): # For Python 2, use __unicode__ too
        return self.title

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __srt__(self):
        return self.user.username
