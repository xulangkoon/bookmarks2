# -*- coding: utf-8 -*-  
# author: xulang time: 18-3-12
from django import forms
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreateForm(forms.ModelForm):
    """我们通过Image模型来动态创建的ModelForm(模型表单)"""
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')  # 虽然包含了URL字段，但用户不用手动填写，我们使用Javascript!
        """widgets是字段的默认控件，我们使用它来隐藏url字段，不让用户看见"""
        widgets = {
            'url': forms.HiddenInput,
        }
    """该方法在view对这个表单执行is_valid()时被执行"""
    def clean_url(self):
        url = self.cleaned_data['url'] # 从表单的实例(一个字典)中获取了url的值
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower() # 分离URL来获取文件的扩展名
        if extension not in valid_extensions: # 检查扩展名与我设定的格式是否一致
            raise forms.ValidationError('The given URL does not match valid image extensions')
        return url
    """这里我们不用写views.py中的操作表单的视图来保存表单里的图片，
        而是通过覆写ModelForm里的save()方法来完成保存的任务"""
    def save(self, force_insert=False, force_update=False, commit=True):
        """从表单中新建了一个image对象，commit=false使django返回一个模型实例但不会把它保存到数据库里"""
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        """通过slug，和扩展名生成图片的名字"""
        image_name = '{}.{}'.format(slugify(image.title),
                                    image_url.rsplit('.', 1)[1].lower())
        # 从给定的URL中下载图片
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save()
        return image