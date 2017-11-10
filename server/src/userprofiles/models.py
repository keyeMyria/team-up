from django.db import models
from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID

from games.models import GameAccount
from userprofiles.tasks import process_photo_image


def image_processor(file_name, variations, storage):
    """
    Send a task message to process image asynchronously.
    The storage argument can't be passed 'to Celery's' task.delay() method, since:
    django.core.files.storage.DefaultStorage is not JSON serializable,
    but it needs to be passed to image_processor, because StdImageFieldFile.save
    method passes storage as a argument.
    """
    process_photo_image.delay(file_name, variations)
    return False  # prevent default rendering


class UserProfile(models.Model):
    user = models.OneToOneField('accounts.User')
    avatar = StdImageField(
        upload_to=UploadToUUID(path='avatars'),
        default='avatars/default_avatar.png',
        variations={
            # "width", "height", "crop"
            'large': (150, 150, False),
            'thumbnail': (80, 80, False)
        },
        render_variations=image_processor
    )

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'

    def __str__(self):
        return f'userprofile: {self.user.username}'

    @property
    def accounts(self):
        """
        :return: User's active games accounts
        """
        account_names = [cls.__name__ for cls in GameAccount.__subclasses__()]
        accounts = {acc_name: getattr(self, f'{acc_name.lower()}_set').all()
                    for acc_name in account_names}
        return accounts
