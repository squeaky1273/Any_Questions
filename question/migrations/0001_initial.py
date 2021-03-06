# Generated by Django 2.2.6 on 2020-01-09 00:27

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
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(help_text='Title of your question.', max_length=1000, unique=True)),
                ('slug', models.CharField(blank=True, editable=False, help_text='Unique URL path to access this question. Generated by the system.', max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time this question was created. Automatically generated when the model saves.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='The date and time this page was updated. Automatically generated when the model updates.')),
                ('author', models.ForeignKey(help_text='The user that posted this question.', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('commenter', models.ForeignKey(help_text='The user that posted this question.', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question')),
            ],
        ),
    ]
