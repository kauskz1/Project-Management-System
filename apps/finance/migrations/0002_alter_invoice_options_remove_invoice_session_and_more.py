# Generated by Django 4.2.11 on 2024-04-02 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ['student', 'class_for']},
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='session',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='term',
        ),
    ]
