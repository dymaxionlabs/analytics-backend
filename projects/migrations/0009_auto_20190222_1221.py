# Generated by Django 2.1.7 on 2019-02-22 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20190222_1212'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='layer',
            unique_together={('project', 'slug', 'date')},
        ),
    ]
