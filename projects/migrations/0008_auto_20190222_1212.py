# Generated by Django 2.1.7 on 2019-02-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20190222_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layer',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='map',
            name='layer_collections',
        ),
        migrations.AddField(
            model_name='map',
            name='layers',
            field=models.ManyToManyField(to='projects.Layer'),
        ),
        migrations.DeleteModel(
            name='LayerCollection',
        ),
    ]
