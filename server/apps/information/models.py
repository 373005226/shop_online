from django.db import models
import datetime


class PCVisitNumber(models.Model):
    count=models.IntegerField(verbose_name='网站访问总次数',default=0,help_text="网站访问总次数")
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='访问时间',help_text="访问时间")

    class Meta:
        verbose_name = 'PC网站访问总次数'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.count)


class MobileVisitNumber(models.Model):
    count=models.IntegerField(verbose_name='网站访问总次数',default=0,help_text="网站访问总次数")
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='访问时间',help_text="访问时间")

    class Meta:
        verbose_name = '移动端访问总次数'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.count)