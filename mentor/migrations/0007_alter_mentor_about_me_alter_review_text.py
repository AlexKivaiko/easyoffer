# Generated by Django 4.2.5 on 2023-09-13 04:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0006_alter_mentor_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='about_me',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
