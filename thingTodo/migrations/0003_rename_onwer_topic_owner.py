# Generated by Django 4.1.3 on 2022-12-04 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("thingTodo", "0002_topic_onwer"),
    ]

    operations = [
        migrations.RenameField(model_name="topic", old_name="onwer", new_name="owner",),
    ]
