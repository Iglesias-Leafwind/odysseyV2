# Generated by Django 2.2.24 on 2022-09-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archaeology', '0015_auto_20220923_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithmexecution',
            name='purpose',
            field=models.CharField(choices=[('training', 'Training'), ('inference', 'Inference')], default='inference', max_length=15, verbose_name='Purpose'),
        ),
    ]
