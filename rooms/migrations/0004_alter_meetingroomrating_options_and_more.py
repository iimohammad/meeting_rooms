# Generated by Django 4.2 on 2024-03-12 16:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0003_sessions_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meetingroomrating',
            options={'verbose_name': 'Meeting Room Rating', 'verbose_name_plural': 'Meeting Room Ratings'},
        ),
        migrations.AlterField(
            model_name='meetingroomrating',
            name='score',
            field=models.PositiveSmallIntegerField(help_text='Enter a rating between 1 and 5.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.CreateModel(
            name='SessionRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(help_text='Enter a rating between 1 and 5.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.sessions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Session Rating',
                'verbose_name_plural': 'Session Ratings',
            },
        ),
    ]
