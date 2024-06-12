# Generated by Django 4.1.2 on 2024-06-12 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('business_type', models.CharField(max_length=255)),
                ('years_in_business', models.CharField(max_length=255)),
                ('company_insured', models.BooleanField()),
                ('company_licensed', models.BooleanField()),
                ('gst_number', models.CharField(max_length=50)),
                ('products_services', models.TextField()),
                ('company_website', models.URLField(blank=True, max_length=255, null=True)),
                ('company_address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('company_year', models.CharField(max_length=4)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('country_code', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
    ]
