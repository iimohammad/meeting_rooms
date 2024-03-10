# Generated by Django 4.2 on 2024-03-10 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='start_datetime',
            new_name='start_date_time',
        ),
        migrations.AlterField(
            model_name='manager',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team'),
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='duration',
            field=models.DurationField(),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
