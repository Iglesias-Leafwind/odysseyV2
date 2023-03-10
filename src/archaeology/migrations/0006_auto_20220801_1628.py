# Generated by Django 2.2.24 on 2022-08-01 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archaeology', '0005_auto_20220731_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='attribute',
            field=models.ManyToManyField(blank=True, to='archaeology.AttributeChoice'),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='document',
            field=models.ManyToManyField(blank=True, to='documents.Document'),
        ),
        migrations.AlterField(
            model_name='site',
            name='attribute',
            field=models.ManyToManyField(blank=True, to='archaeology.AttributeChoice'),
        ),
        migrations.AlterField(
            model_name='site',
            name='document',
            field=models.ManyToManyField(blank=True, to='documents.Document'),
        ),
    ]
