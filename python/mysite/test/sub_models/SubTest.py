from django.db import models

# Create your models here.

class SubTest(models.Model):
    """
    测试 model
    """

    id = models.AutoField(primary_key=True)  # 不写则，django默认创建ID列，自增，主键

    # CharFields must define a 'max_length' attribute
    # db_column 自定义字段
    name = models.CharField(max_length=30, db_column='testname', unique=True)
    description = models.CharField(max_length=30, blank=True)

    price = models.IntegerField(default=0)
    # price1 = models.IntegerField(default=0)

    # create_date = models.DateField(auto_now_add=True)
    # time = models.TimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # 自定义表名
    # class Meta:
    #     db_table = 'test'