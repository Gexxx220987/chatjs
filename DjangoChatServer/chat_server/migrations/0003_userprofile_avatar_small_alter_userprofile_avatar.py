
from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chat_server', '0002_rename_room_name_room_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar_small',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='images_small/default.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='images/default.jpg', upload_to='images'),
        ),
    ]
