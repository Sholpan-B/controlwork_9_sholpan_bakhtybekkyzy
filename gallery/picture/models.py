from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    picture = models.ImageField(upload_to='photos', blank=False, null=False, verbose_name='Фото')
    description = models.CharField(null=False, blank=False, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(to=get_user_model(), related_name='photos', null=False, blank=False,
                               on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return f"Фото пользователя: {self.author} (Id {self.id})"

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'


class AuthorPhotoRelation(models.Model):
    author = models.ForeignKey(to='accounts.Account', on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    in_bookmarks = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author}"


class Comment(models.Model):
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='comments', null=False,
                               blank=False, on_delete=models.CASCADE)
    photo = models.ForeignKey(verbose_name='Фотография', to='picture.Photo', related_name='comments', null=False,
                              blank=False, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Комментарий', null=False, blank=False, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата комментирования')
