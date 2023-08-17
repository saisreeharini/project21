from django.db import models

# Create your models here.


class dept(models.model):
        dno=models.integerfield(primary_key=True)
        dname=models.charfield(max_length=100)
        dloc=models.charfield(max_length=100)
        def__str__(self):
            return self.Dname


class emp(models.model):
    eno=models.integerfield(primary_key=True)
    ename=models.charfield(max_length=100)
    job=models.charfield(max_length=100)
    hiredate=models.datefield()
    sal=models.integerfield()
    com=models.integerfield(default=None,null=True,blank=True)
    deptno=models.foreignkey(dept,on_delete=models.CASCADE)
    def__str__(self):
        return self.job



    