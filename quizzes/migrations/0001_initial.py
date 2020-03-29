# Generated by Django 3.0.3 on 2020-03-29 22:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('view_count', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='quizzes.Category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_vote', models.IntegerField(default=0)),
                ('quiz', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='quizzes.Quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, max_length=250, validators=[django.core.validators.MinLengthValidator(1)])),
                ('answer', models.TextField(blank=True, max_length=250, validators=[django.core.validators.MinLengthValidator(1)])),
                ('quiz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='quizzes.Quiz')),
            ],
        ),
    ]
