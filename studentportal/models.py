from django.db import models
from django.core import validators

class Student(models.Model):
    name = models.CharField(max_length=120, unique=True)
    rollNo = models.BigIntegerField(unique=True)
    physics = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)])
    chemistry = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)])
    maths = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)])
    total = models.BigIntegerField(editable=False, default=0)
    percentage = models.FloatField(editable=False, default=0)

    class Meta:
        unique_together = ['name', 'rollNo']
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.total = (self.physics + self.chemistry + self.maths)
        self.percentage = round(self.total/3, 2)
        super(Student, self).save(*args, **kwargs)
