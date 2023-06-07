

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_server', '0006_alter_userprofile_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat_server.userprofile')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat_server.room')),
            ],
        ),
    ]
