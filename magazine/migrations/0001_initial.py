# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Chapter'
        db.create_table(u'magazine_chapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('cover_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'magazine', ['Chapter'])

        # Adding model 'Section'
        db.create_table(u'magazine_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'magazine', ['Section'])

        # Adding model 'Contributor'
        db.create_table(u'magazine_contributor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'magazine', ['Contributor'])

        # Adding model 'Tag'
        db.create_table(u'magazine_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
        ))
        db.send_create_signal(u'magazine', ['Tag'])

        # Adding model 'Content'
        db.create_table(u'magazine_content', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('publishDate', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('teaser', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('body', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('chapter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magazine.Chapter'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(related_name='section', to=orm['magazine.Section'])),
        ))
        db.send_create_signal(u'magazine', ['Content'])

        # Adding M2M table for field contributors on 'Content'
        m2m_table_name = db.shorten_name(u'magazine_content_contributors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('content', models.ForeignKey(orm[u'magazine.content'], null=False)),
            ('contributor', models.ForeignKey(orm[u'magazine.contributor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['content_id', 'contributor_id'])

        # Adding M2M table for field tags on 'Content'
        m2m_table_name = db.shorten_name(u'magazine_content_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('content', models.ForeignKey(orm[u'magazine.content'], null=False)),
            ('tag', models.ForeignKey(orm[u'magazine.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['content_id', 'tag_id'])

        # Adding model 'Article'
        db.create_table(u'magazine_article', (
            (u'content_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['magazine.Content'], unique=True, primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'magazine', ['Article'])

        # Adding model 'Image'
        db.create_table(u'magazine_image', (
            (u'content_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['magazine.Content'], unique=True, primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'magazine', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Chapter'
        db.delete_table(u'magazine_chapter')

        # Deleting model 'Section'
        db.delete_table(u'magazine_section')

        # Deleting model 'Contributor'
        db.delete_table(u'magazine_contributor')

        # Deleting model 'Tag'
        db.delete_table(u'magazine_tag')

        # Deleting model 'Content'
        db.delete_table(u'magazine_content')

        # Removing M2M table for field contributors on 'Content'
        db.delete_table(db.shorten_name(u'magazine_content_contributors'))

        # Removing M2M table for field tags on 'Content'
        db.delete_table(db.shorten_name(u'magazine_content_tags'))

        # Deleting model 'Article'
        db.delete_table(u'magazine_article')

        # Deleting model 'Image'
        db.delete_table(u'magazine_image')


    models = {
        u'magazine.article': {
            'Meta': {'object_name': 'Article', '_ormbases': [u'magazine.Content']},
            u'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['magazine.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'magazine.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'magazine.content': {
            'Meta': {'object_name': 'Content'},
            'body': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'chapter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magazine.Chapter']"}),
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['magazine.Contributor']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publishDate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'section'", 'to': u"orm['magazine.Section']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['magazine.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'teaser': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'magazine.contributor': {
            'Meta': {'object_name': 'Contributor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'magazine.image': {
            'Meta': {'object_name': 'Image', '_ormbases': [u'magazine.Content']},
            u'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['magazine.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'magazine.section': {
            'Meta': {'object_name': 'Section'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'magazine.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['magazine']