from django.db import models

class PredictionHistory(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    trestbps = models.FloatField()
    chol = models.FloatField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.FloatField()
    exang = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()
    prediction = models.IntegerField()
    probability = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
