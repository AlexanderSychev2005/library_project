from django.db import models


# Create your models here.
class StudentOrder(models.Model):
    STATUS_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned')
    ]

    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE)
    created_at = models.DateField()
    returned_at = models.DateField(null=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student} - {self.book}"
