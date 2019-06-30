from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=35,null=False,verbose_name='用户名')
    password=models.CharField(max_length=30,null=False,verbose_name='密码')
    uphone=models.IntegerField(max_length=11,null=True,verbose_name='手机号')

    class Meta:
        db_table='UserInfo'
        verbose_name='用户信息表'
        verbose_name_plural=verbose_name