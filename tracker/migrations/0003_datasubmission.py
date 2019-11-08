# Generated by Django 2.2.6 on 2019-11-08 15:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_location_sensor'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSubmission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('upload', models.FileField(null=True, upload_to='data-files/%Y/%m/%d/')),
                ('museum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Museum')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Sensor')),
            ],
        ),
    ]
