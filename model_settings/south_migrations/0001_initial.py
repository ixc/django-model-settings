# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Setting'
        db.create_table(u'model_settings_setting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'polymorphic_model_settings.setting_set', null=True, to=orm['contenttypes.ContentType'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'model_settings', ['Setting'])

        # Adding model 'Boolean'
        db.create_table(u'model_settings_boolean', (
            (u'setting_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['model_settings.Setting'], unique=True, primary_key=True)),
            ('value', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'model_settings', ['Boolean'])

        # Adding model 'Date'
        db.create_table(u'model_settings_date', (
            (u'setting_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['model_settings.Setting'], unique=True, primary_key=True)),
            ('value', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'model_settings', ['Date'])

        # Adding model 'DateTime'
        db.create_table(u'model_settings_datetime', (
            (u'setting_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['model_settings.Setting'], unique=True, primary_key=True)),
            ('value', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'model_settings', ['DateTime'])

        # Adding model 'Decimal'
        db.create_table(u'model_settings_decimal', (
            (u'setting_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['model_settings.Setting'], unique=True, primary_key=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=10)),
        ))
        db.send_create_signal(u'model_settings', ['Decimal'])

        # Adding model 'File'
        db.create_table(u'model_settings_file', (
            (u'setting_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['model_settings.Setting'], unique=True, primary_key=True)),
            ('value', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'model_settings', ['File'])

        # Adding model 'Float'
        db.create_table(u'model_settings_float', (
            (u'setting_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['model_settings.Setting'], unique=True, primary_key=True)),
            ('value', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'model_settings', ['Float'])

        # Adding model 'Integer'
        db.create_table(u'model_settings_integer', (
            (u'setting_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['model_settings.Setting'], unique=True, primary_key=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'model_settings', ['Integer'])

        # Adding model 'Text'
        db.create_table(u'model_settings_text', (
            (u'setting_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['model_settings.Setting'], unique=True, primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'model_settings', ['Text'])

        # Adding model 'Time'
        db.create_table(u'model_settings_time', (
            (u'setting_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['model_settings.Setting'], unique=True, primary_key=True)),
            ('value', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'model_settings', ['Time'])


    def backwards(self, orm):
        # Deleting model 'Setting'
        db.delete_table(u'model_settings_setting')

        # Deleting model 'Boolean'
        db.delete_table(u'model_settings_boolean')

        # Deleting model 'Date'
        db.delete_table(u'model_settings_date')

        # Deleting model 'DateTime'
        db.delete_table(u'model_settings_datetime')

        # Deleting model 'Decimal'
        db.delete_table(u'model_settings_decimal')

        # Deleting model 'File'
        db.delete_table(u'model_settings_file')

        # Deleting model 'Float'
        db.delete_table(u'model_settings_float')

        # Deleting model 'Integer'
        db.delete_table(u'model_settings_integer')

        # Deleting model 'Text'
        db.delete_table(u'model_settings_text')

        # Deleting model 'Time'
        db.delete_table(u'model_settings_time')


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