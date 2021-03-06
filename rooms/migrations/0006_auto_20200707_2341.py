# Generated by Django 3.0.7 on 2020-07-07 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20200707_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='rooms.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='rooms.RoomType'),
        ),
    ]
