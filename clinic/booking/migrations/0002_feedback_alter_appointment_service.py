# Generated by Django 5.0.6 on 2024-07-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(choices=[('Doctor care', 'Doctor care'), ('Nursing care', 'Nursing care'), ('Medical social services', 'Medical social services'), ('Homemaker or basic assistance care', 'Homemaker or basic assistance care')], default='Doctor care', max_length=50),
        ),
    ]