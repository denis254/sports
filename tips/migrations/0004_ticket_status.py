# Generated by Django 2.0.3 on 2018-07-27 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0003_auto_20180725_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
