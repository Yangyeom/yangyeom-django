# Generated by Django 2.2.7 on 2019-11-28 08:06

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
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.CharField(max_length=100)),
                ('tid', models.CharField(max_length=100)),
                ('payment_method_type', models.CharField(max_length=100)),
                ('item_name', models.CharField(max_length=100)),
                ('item_code', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('approved_at', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
