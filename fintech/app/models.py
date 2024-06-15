from django.db import models

class Contact(models.Model):
    company_name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=255)
    years_in_business = models.CharField(max_length=255)
    company_insured = models.BooleanField()
    company_licensed = models.BooleanField()
    gst_number = models.CharField(max_length=50)
    products_services = models.TextField()
    company_website = models.URLField(max_length=255, blank=True, null=True)
    company_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    company_year = models.CharField(max_length=4)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.company_name}"


class ContactSubmission(models.Model):
    full_name = models.CharField(max_length=255)
    email_address = models.EmailField()
    phone_no = models.CharField(max_length=15)
    message = models.TextField(max_length=650)

    def __str__(self):
        return f"{self.full_name} - {self.email_address}"