# Generated by Django 2.1.7 on 2019-02-22 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20190222_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maplayer',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='layers', to='projects.Map'),
        ),
    ]
