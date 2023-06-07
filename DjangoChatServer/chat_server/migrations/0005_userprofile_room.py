

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_server', '0004_alter_userprofile_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='room',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat_server.room'),
        ),
    ]