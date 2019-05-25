from django.db import models


class Result(models.Model):
    app_name = models.CharField(max_length=256, null=True, blank=True)
    class_name = models.CharField(max_length=256)
    file_name = models.CharField(max_length=256)
    test_name = models.CharField(max_length=256)
    time = models.FloatField()

    def __str__(self):
        return f'{self.id}: {self.class_name}.{self.test_name}: {self.time}'
