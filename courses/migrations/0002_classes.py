# Generated by Django 3.2.8 on 2021-10-09 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('content', models.FileField(upload_to='classes')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.courses')),
            ],
        ),
    ]
