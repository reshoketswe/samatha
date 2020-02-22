from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image




class Post(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length=100, blank = True)
	date = models.DateTimeField(default = timezone.now)
	content = models.TextField()

	image = models.ImageField(required=False , upload_to='mobile_uploads')


	def get_absolute_url(self):
		return reverse('home')

	def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)