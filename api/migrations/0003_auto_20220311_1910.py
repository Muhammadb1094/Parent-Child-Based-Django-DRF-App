# Generated by Django 3.2.12 on 2022-03-11 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220311_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.topic'),
        ),
        migrations.DeleteModel(
            name='Child',
        ),
    ]
