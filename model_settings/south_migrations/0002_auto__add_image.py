# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'model_settings_image', (
            (u'setting_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['model_settings.Setting'], unique=True, primary_key=True)),
            ('value', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'model_settings', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'model_settings_image')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'model_settings.boolean': {
            'Meta': {'ordering': "['name']", 'object_name': 'Boolean', '_ormbases': [u'model_settings.Setting']},
            u'setting_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['model_settings.Setting']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.BooleanField', [], {})
        },
        u'model_settings.date': {
            'Meta': {'ordering': "['name']", 'object_name': 'Date', '_ormbases': [u'model_settings.Setting']},
            u'setting_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['model_settings.Setting']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.DateField', [], {})
        },
        u'model_settings.datetime': {
            'Meta': {'ordering': "['name']", 'object_name': 'DateTime', '_ormbases': [u'model_settings.Setting']},
            u'setting_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['model_settings.Setting']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'model_settings.decimal': {
            'Meta': {'ordering': "['name']", 'object_name': 'Decimal', '_ormbases': [u'model_settings.Setting']},
            u'setting_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['model_settings.Setting']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '10'})
        },
        u'model_settings.file': {
            'Meta': {'ordering': "['name']", 'object_name': 'File', '_ormbases': [u'model_settings.Setting']},
            u'setting_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['model_settings.Setting']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'model_settings.float': {
            'Meta': {'ordering': "['name']", 'object_name': 'Float', '_ormbases': [u'model_settings.Setting']},
            u'setting_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['model_settings.Setting']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'model_settings.image': {
            'Meta': {'ordering': "['name']", 'object_name': 'Image', '_ormbases': [u'model_settings.Setting']},
            u'setting_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['model_settings.Setting']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'model_settings.integer': {
            'Meta': {'ordering': "['name']", 'object_name': 'Integer', '_ormbases': [u'model_settings.Setting']},
            u'setting_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['model_settings.Setting']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'model_settings.setting': {
            'Meta': {'ordering': "['name']", 'object_name': 'Setting'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_model_settings.setting_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"})
        },
        u'model_settings.text': {
            'Meta': {'ordering': "['name']", 'object_name': 'Text', '_ormbases': [u'model_settings.Setting']},
            u'setting_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['model_settings.Setting']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'model_settings.time': {
            'Meta': {'ordering': "['name']", 'object_name': 'Time', '_ormbases': [u'model_settings.Setting']},
            u'setting_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['model_settings.Setting']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['model_settings']