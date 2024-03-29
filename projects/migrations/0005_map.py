# Generated by Django 2.1.7 on 2019-02-21 14:02

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20190221_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('center', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('zoom', models.IntegerField(default=13, validators=[django.core.validators.MaxValueValidator(22), django.core.validators.MinValueValidator(1)])),
                ('is_private', models.BooleanField(default=True)),
                ('extra_fields', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('layer_collections', models.ManyToManyField(to='projects.LayerCollection')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Project')),
            ],
        ),
    ]
