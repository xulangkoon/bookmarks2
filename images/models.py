from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse


class Image(models.Model):
    """foreignkey一对多字段，即一个用户可以上传多张图片，但每张图片只属于一个用户
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now=True, db_index=True) # 这里的db_index=True,django将为这个字段创建引索
    """该字段用于保存点击喜欢这张图片的用户，是多对多的关系
        manytomany字段提供了多对多管理器，方便我们可以回溯相关联的对象,可以通过照片追查到user,也可以追查user喜欢的所有照片
    """
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # 定义save()l函数来自动生成slug字段
        if not self.slug:
            self.slug = slugify(self.title)  # slugify()可以根据title自动生成slug,而不需要用户输入slug字段。
            super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])