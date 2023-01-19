from django.db import models


class Position(models.Model):
    position_name = models.CharField(max_length=99)
    department = models.CharField(max_length=99)

    def __str__(self):
        return f'{self.position_name}'


class Employee(models.Model):
    FIO = models.CharField(max_length=99)
    birth_date = models.DateField()
    zp = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.FIO} {self.position.position_name}'

