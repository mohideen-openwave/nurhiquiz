# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomUser'
        db.create_table(u'profile_customuser', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('phoneno', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('professional', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('town', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('country', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('worktype', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('currentlyworking', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('stafftype', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('familyplaning', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('providedit', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('nurhitraining', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('education', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('religion', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('sex', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('age', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
        ))
        db.send_create_signal(u'profile', ['CustomUser'])


    def backwards(self, orm):
        # Deleting model 'CustomUser'
        db.delete_table(u'profile_customuser')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profile.customuser': {
            'Meta': {'object_name': 'CustomUser', '_ormbases': [u'auth.User']},
            'age': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'currentlyworking': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'education': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'familyplaning': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'nurhitraining': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'phoneno': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'professional': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'providedit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'religion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'stafftype': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'town': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'worktype': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        }
    }

    complete_apps = ['profile']