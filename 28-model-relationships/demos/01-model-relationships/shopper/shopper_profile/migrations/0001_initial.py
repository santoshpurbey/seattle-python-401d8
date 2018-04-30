# Generated by Django 2.0.4 on 2018-04-24 16:48

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
            name='ShopperProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=1024, null=True)),
                ('city', models.CharField(blank=True, max_length=1024, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=12, null=True)),
                ('cell', models.CharField(blank=True, max_length=20, null=True)),
                ('home', models.CharField(blank=True, max_length=20, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]