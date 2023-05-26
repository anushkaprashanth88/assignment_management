# Generated by Django 3.0.5 on 2022-01-28 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assigment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AssignmentNumber', models.CharField(max_length=100, null=True)),
                ('AssignmentTitle', models.CharField(max_length=150, null=True)),
                ('AssignmentDescription', models.CharField(max_length=300, null=True)),
                ('SubmissionDate', models.DateField(null=True)),
                ('AssignmentMarks', models.CharField(max_length=150, null=True)),
                ('AssignmentFile', models.FileField(null=True, upload_to='')),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BranchName', models.CharField(max_length=150, null=True)),
                ('CourseName', models.CharField(max_length=200, null=True)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200, null=True)),
                ('Description', models.CharField(max_length=500, null=True)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MobileNumber', models.CharField(max_length=200, null=True)),
                ('RollNumber', models.CharField(max_length=200, null=True)),
                ('RegDate', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeAssignment.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Uploadass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Assdesc', models.CharField(max_length=300, null=True)),
                ('AnswerFile', models.FileField(null=True, upload_to='')),
                ('SubmitDate', models.DateField(null=True)),
                ('Marks', models.CharField(max_length=100, null=True)),
                ('Remarks', models.CharField(max_length=250, null=True)),
                ('UpdationDate', models.DateField(null=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeAssignment.Assigment')),
                ('userdetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeAssignment.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpID', models.CharField(max_length=50, null=True)),
                ('MobileNumber', models.CharField(max_length=15, null=True)),
                ('Gender', models.CharField(max_length=50, null=True)),
                ('Dob', models.DateField(null=True)),
                ('Religion', models.CharField(max_length=100, null=True)),
                ('Password', models.CharField(max_length=50, null=True)),
                ('ProfilePic', models.FileField(null=True, upload_to='')),
                ('JoiningDate', models.DateField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeAssignment.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubjectFullname', models.CharField(max_length=200, null=True)),
                ('SubjectShortname', models.CharField(max_length=50, null=True)),
                ('SubjectCode', models.CharField(max_length=50, null=True)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeAssignment.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Newsbyteacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200, null=True)),
                ('Description', models.CharField(max_length=500, null=True)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeAssignment.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='assigment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeAssignment.Course'),
        ),
        migrations.AddField(
            model_name='assigment',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeAssignment.Subject'),
        ),
        migrations.AddField(
            model_name='assigment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeAssignment.Teacher'),
        ),
    ]
