from django.db import models

class Approvals(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    MARRIED_CHOICES = (
        ("Yes", "Yes"),
        ("No", "No")
    )
    GRADUATED_CHOICES = (
        ("Graduate", "Graduate"),
        ("Not_Graduate", "Not_Graduate")
    )
    SELF_EMPLOYED_CHOICES = (
        ("Yes", "Yes"),
        ("No", "No")
    )
    PROPERTY_CHOICES = (
        ("Rural", "Rural"),
        ("Semiurban", "Semiurban"),
        ("Urban", "Urban")
    )

    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    dependants = models.IntegerField(default=0)
    applicantincome = models.IntegerField(default=0)
    coapplicantincome=models.IntegerField(default=0)
    loanamt = models.IntegerField(default=0)
    loanterm = models.IntegerField(default=0)
    credicthistory = models.IntegerField(default=0)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
    graduateducation = models.CharField(max_length=15, choices=GRADUATED_CHOICES)
    selfemployed = models.CharField(max_length=15, choices=SELF_EMPLOYED_CHOICES)
    area = models.CharField(max_length=15, choices=PROPERTY_CHOICES)

    def __str__(self):
        return self.firstname