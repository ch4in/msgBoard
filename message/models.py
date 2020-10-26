from django.db import models


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField('时间')
    name = models.CharField('姓名', max_length=8, default='')
    grade = models.CharField('年级',max_length=3, default='一年级')
    classNum = models.CharField('班级',max_length=2, default='1班')
    title = models.CharField('留言标题',max_length=100)
    message_text = models.TextField('留言内容',max_length=5000)
    isShow = models.BooleanField('是否显示',default=False)

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name
