# Generated by Django 3.0.5 on 2022-02-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeAssignment', '0006_auto_20220201_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigment',
            name='AssignmentFile',
            field=models.FileField(max_length=200, null=True, upload_to=''),
        ),
    ]
