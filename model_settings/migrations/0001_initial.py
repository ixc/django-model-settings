# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Boolean',
            fields=[
                ('setting_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='model_settings.Setting')),
                ('value', models.BooleanField()),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('model_settings.setting', models.Model),
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('setting_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='model_settings.Setting')),
                ('value', models.DateField()),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('model_settings.setting', models.Model),
        ),
        migrations.CreateModel(
            name='DateTime',
            fields=[
                ('setting_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='model_settings.Setting')),
                ('value', models.DateTimeField()),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('model_settings.setting', models.Model),
        ),
        migrations.CreateModel(
            name='Decimal',
            fields=[
                ('setting_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='model_settings.Setting')),
                ('value', models.DecimalField(max_digits=20, decimal_places=10)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('model_settings.setting', models.Model),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('setting_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='model_settings.Setting')),
                ('value', models.FileField(upload_to=b'model-settings/files')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('model_settings.setting', models.Model),
        ),
        migrations.CreateModel(
            name='Float',
            fields=[
                ('setting_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='model_settings.Setting')),
                ('value', models.FloatField()),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('model_settings.setting', models.Model),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('setting_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='model_settings.Setting')),
                ('value', models.ImageField(upload_to=b'model-settings/images')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('model_settings.setting', models.Model),
        ),
        migrations.CreateModel(
            name='Integer',
            fields=[
                ('setting_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='model_settings.Setting')),
                ('value', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('model_settings.setting', models.Model),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('setting_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='model_settings.Setting')),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('model_settings.setting', models.Model),
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('setting_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='model_settings.Setting')),
                ('value', models.TimeField()),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('model_settings.setting', models.Model),
        ),
        migrations.AddField(
            model_name='setting',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_model_settings.setting_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
    ]
