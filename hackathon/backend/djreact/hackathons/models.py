from django.db import models
from django.contrib.auth.models import User


class Hackathon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hackathon/background/')
    hackathon_image = models.ImageField(upload_to='hackathon/image/')
    submission_type = models.CharField(max_length=10, choices=(
        ('image', 'Image'), ('file', 'File'), ('link', 'Link')))
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.DecimalField(max_digits=8, decimal_places=2)


class HackathonSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    submission_text = models.TextField(blank=True)
    submission_file = models.FileField(
        upload_to='submissions/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s submission for {self.hackathon.title}"
