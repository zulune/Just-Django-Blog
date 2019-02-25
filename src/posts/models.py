from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from tinymce import HTMLField
# Create your models here.


User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, verbose_name=_(
        "Author"), on_delete=models.CASCADE)
    profile_picture = models.ImageField(_("Profile picture"))

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    overview = models.TextField(_("Overview"))
    timestamp = models.DateTimeField(
        _("Timestamp"), auto_now=False, auto_now_add=True)
    content = HTMLField()
    comment_count = models.IntegerField(_("Comment count"), default=0)
    view_count = models.IntegerField(_("View count"), default=0)
    author = models.ForeignKey(Author, verbose_name=_(
        "Author"), on_delete=models.CASCADE)
    thumbnail = models.ImageField(_("Thumbnail"))
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))
    featured = models.BooleanField(_("Featured"), default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    