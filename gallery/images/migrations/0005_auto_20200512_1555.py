# Generated by Django 3.0.3 on 2020-05-12 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20200512_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='uuid',
            field=models.CharField(blank=True, max_length=36, null=True, unique=True, verbose_name='image uuid'),
        ),
        migrations.AlterField(
            model_name='like',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Image', to_field='uuid'),
        ),
    ]
