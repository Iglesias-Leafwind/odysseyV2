# Generated by Django 2.2.24 on 2022-08-03 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archaeology', '0007_auto_20220802_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='metric',
            name='unit_measurement',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
