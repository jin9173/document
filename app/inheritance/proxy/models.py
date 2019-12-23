from django.db import models


class BaseUser(models.Model):
    def show_pk(self):
        print(self.pk)
    pass


class NormalUser(BaseUser):
    class Meta:
        proxy = True


class SuperUser(BaseUser):
    class Meta:
        proxy = True

    def delete_user(self, pk):
        BaseUser.objects.get(pk=pk).delete()
