# Generated by Django 2.2.7 on 2019-11-12 20:37

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_location_sensor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='location',
        ),
        migrations.AddField(
            model_name='sensor',
            name='room',
            field=models.CharField(blank=True, help_text='Please describe the location of your sensor', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='museum',
            name='city',
            field=models.CharField(help_text='Please enter the city in which your insitution is located', max_length=100),
        ),
        migrations.AlterField(
            model_name='museum',
            name='institution',
            field=models.CharField(help_text='Please enter the name of your institution', max_length=150),
        ),
        migrations.AlterField(
            model_name='museum',
            name='state',
            field=localflavor.us.models.USStateField(help_text='Please choose the state in which your institution is located from the provided list', max_length=2),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(blank=True, help_text='Please give your sensor a unique name to distinguish it from other sensors you may have', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sensortype',
            name='model',
            field=models.CharField(help_text='Please describe the model of the sensor you have (ie 2.0)', max_length=150),
        ),
        migrations.AlterField(
            model_name='sensortype',
            name='type',
            field=models.CharField(help_text='Please describe the brand of the sensor you have (ie Raspberry Pi)', max_length=150),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
