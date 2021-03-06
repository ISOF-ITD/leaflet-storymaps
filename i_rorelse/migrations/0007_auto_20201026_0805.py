# Generated by Django 2.2.10 on 2020-10-26 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('i_rorelse', '0006_auto_20201016_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='narrative_Link_color',
            new_name='narrative_link_color',
        ),
        migrations.AlterField(
            model_name='chapter',
            name='overlay_transparency',
            field=models.FloatField(blank=True, help_text='Optional. Value between 0 and 1. E.g. 0.5', null=True, verbose_name='Overlay Transparency'),
        ),
    ]
