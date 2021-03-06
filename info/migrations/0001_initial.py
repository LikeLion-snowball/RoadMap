# Generated by Django 3.2.5 on 2021-07-29 15:38

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
            name='Recruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corp', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('end_date_str', models.CharField(blank=True, max_length=20, null=True)),
                ('career', models.CharField(max_length=20)),
                ('academic', models.CharField(max_length=20)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('area', models.CharField(max_length=20)),
                ('scrap_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scraps', to='info.recruit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='recruit',
            name='scrap',
            field=models.ManyToManyField(related_name='recruits', through='info.Scrap', to=settings.AUTH_USER_MODEL),
        ),
    ]
