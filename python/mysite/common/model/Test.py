from django.db import models

class Test(models.Model):

    id = models.AutoField(primary_key=True) # 不写则，django默认创建ID列，自增，主键

    name = models.CharField(max_length=30, db_column='testname', unique=True) # db_column 自定义字段
    price = models.IntegerField()
    description = models.CharField(blank=True)

    def __str__(self):
        return self.name

    # 自定义表名
    class Meta:
        db_table = 'test'
