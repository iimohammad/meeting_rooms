# Generated by Django 4.2 on 2024-03-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='CompanyManager',
            field=models.CharField(choices=[('Company CEO', 'Company CEO'), ('Member', 'member')], default='Member', max_length=15),
        ),
    ]