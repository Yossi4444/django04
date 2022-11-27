from django.db import models

# Create your models here.
class Admin(models.Model):
    """管理岗表"""
    objects = models.Manager()
    name = models.CharField(verbose_name='姓名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)

class Department(models.Model):
    """部门表"""
    objects = models.Manager()
    title = models.CharField(verbose_name='标题',max_length=32)
    def __str__(self):
        return self.title
class UserInfo(models.Model):
    """员工表"""
    objects = models.Manager()
    name=models.CharField(verbose_name='姓名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=32)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2,default=0)
    # create_time = models.DateTimeField(verbose_name='入职时间')
    create_time = models.DateField(verbose_name='入职时间')
    # to=与某一个表关联，to_fields:与那个表的某一列关联
    # 会自动将depart转换成depart_id
    # 级联删除
    depart = models.ForeignKey(to='Department',to_field='id',on_delete=models.CASCADE)
    # 置空（若删除数据表一项，则关联的会置为空）
    # depart = models.ForeignKey(to='Department', to_fields='id',null=True,blank=True,on_delete=models.SET_NULL)
    gender_choices=(
        (1,'男'),
        (2,'女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)
class PrettyNum(models.Model):
    """靓号表"""
    objects= models.Manager()
    mobile = models.CharField(verbose_name='号码',max_length=11)
    price = models.IntegerField(verbose_name="价格")
    level_choices = {
        (1,'vip'),
        (2,'normal')
    }
    status_choices = {
        (1,'已占用'),
        (2,'未占用')
    }
    level = models.SmallIntegerField(verbose_name="等级",choices=level_choices,default=2)
    status = models.SmallIntegerField(verbose_name='状态',choices=status_choices,default=2)
