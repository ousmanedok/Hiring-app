# Generated by Django 4.0.3 on 2022-05-04 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_teammember_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publication_publisher', models.CharField(max_length=100, null=True)),
                ('publication_url', models.URLField()),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=1000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_publications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
