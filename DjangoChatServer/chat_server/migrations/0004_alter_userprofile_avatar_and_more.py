

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chat_server', '0003_userprofile_avatar_small_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='djangochatserver/default.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar_small',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='djangochatserver/default_small.jpg', upload_to='images'),
        ),
    ]
