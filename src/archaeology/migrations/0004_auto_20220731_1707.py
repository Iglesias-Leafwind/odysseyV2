# Generated by Django 2.2.24 on 2022-07-31 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archaeology', '0003_auto_20220731_1704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attributeoccurrence',
            options={'ordering': ['value__category', 'value'], 'verbose_name': 'Occurrence Attribute', 'verbose_name_plural': 'Occurrence Attributes'},
        ),
        migrations.AlterModelOptions(
            name='attributesite',
            options={'ordering': ['value__category', 'value'], 'verbose_name': 'Site Attribute', 'verbose_name_plural': 'Site Attributes'},
        ),
        migrations.AlterModelOptions(
            name='documentoccurrence',
            options={'verbose_name': 'Occurrence Document', 'verbose_name_plural': 'Occurrence Documents'},
        ),
        migrations.AlterModelOptions(
            name='documentsite',
            options={'verbose_name': 'Site Document', 'verbose_name_plural': 'Site Documents'},
        ),
    ]