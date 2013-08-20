# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bestseller'
        db.create_table(u'bestsellers_app_bestseller', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Title', self.gf('django.db.models.fields.TextField')()),
            ('Author', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Isbn', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('ImageUrl', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('BestsellerDate', self.gf('django.db.models.fields.DateField')()),
            ('Rank', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('BookList', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bestsellers_app.BookList'])),
        ))
        db.send_create_signal(u'bestsellers_app', ['Bestseller'])

        # Adding model 'BookList'
        db.create_table(u'bestsellers_app_booklist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ListKey', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('DisplayName', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'bestsellers_app', ['BookList'])


    def backwards(self, orm):
        # Deleting model 'Bestseller'
        db.delete_table(u'bestsellers_app_bestseller')

        # Deleting model 'BookList'
        db.delete_table(u'bestsellers_app_booklist')


    models = {
        u'bestsellers_app.bestseller': {
            'Author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'BestsellerDate': ('django.db.models.fields.DateField', [], {}),
            'BookList': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bestsellers_app.BookList']"}),
            'ImageUrl': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'Isbn': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'Meta': {'object_name': 'Bestseller'},
            'Rank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'Title': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'bestsellers_app.booklist': {
            'DisplayName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ListKey': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'BookList'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['bestsellers_app']