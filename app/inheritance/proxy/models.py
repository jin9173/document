from django.db import models

#
# class UserMixin(models.Model):
#     # nickname = models.CharField(max_length=30, blank=True)
#
#     class Meta:
#         abstract = True


class BaseUser(models.Model):
    is_superuser = models.BooleanField(default=False)

    def show_pk(self):
        print(self.pk)
    pass


class NormalUser(BaseUser):
    class Meta:
        proxy = True


# SuperUser모델에서 사용할 Manager
class SuperUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_superuser=True)


class SuperUser(BaseUser):
    # 프록시 모델에 Manager를 지정
    objects = SuperUserManager()

    class Meta:
        proxy = True

    def delete_user(self, pk):
        BaseUser.objects.get(pk=pk).delete()

#
# # Multiple inheritance
# class Book(models.Model):
#     pass
#
# #
# # class Article(models.Model):
# #     pass
#
#
# class BookReview(Book):
#     pass