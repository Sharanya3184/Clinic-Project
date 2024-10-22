# Generated by Django 5.0.6 on 2024-07-06 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_appointment_cancel'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=20)),
                ('emergency_type', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Appointment_Cancel',
        ),
    ]
