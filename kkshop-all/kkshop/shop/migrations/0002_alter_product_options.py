# Generated by Django 4.2 on 2023-07-10 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('denotation',)},
        ),
    ]
