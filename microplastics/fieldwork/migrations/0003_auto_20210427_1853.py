# Generated by Django 3.1.7 on 2021-04-27 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fieldwork', '0002_auto_20210426_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='feeder',
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('field_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fieldwork.fielduser')),
                ('site_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fieldwork.site')),
            ],
        ),
    ]
