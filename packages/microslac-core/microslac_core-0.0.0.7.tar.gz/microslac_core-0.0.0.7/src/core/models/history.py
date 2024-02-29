from django.db import models
from django.utils import timezone

from core.models.manager import BaseManager, BaseQuerySet


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DeletedQuerySet(BaseQuerySet):
    def delete(self, deleter: str = ""):
        for obj in self:
            obj.delete(deleter, save=False)
        return self.bulk_update(self, ["deleted", "deleter"])

    def destroy(self):
        for obj in self:
            obj.destroy()


class DeletedManager(BaseManager):
    def get_queryset(self):
        return DeletedQuerySet(self.model, using=self._db).filter(deleted__isnull=True)

    def include_deleted(self):
        return DeletedQuerySet(self.model, using=self._db)


class DeletedModel(models.Model):
    deleted = models.DateTimeField(null=True)
    deleter = models.CharField(max_length=20, default="")

    class Meta:
        abstract = True

    objects = DeletedManager()

    def delete(self, deleter: int = 0, save: bool = True):
        if not self.deleted:
            self.deleted = timezone.now()
            self.deleter = deleter or self.deleter
            save and self.save()

    def restore(self, save: bool = True):
        if self.deleted:
            self.deleted = None
            self.deleter = ""
            save and self.save()

    def destroy(self, using=None, keep_parents=False):
        super().delete(using=using, keep_parents=keep_parents)


class HistoryModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creator = models.CharField(max_length=20, default="")
    updater = models.CharField(max_length=20, default="")

    class Meta:
        abstract = True
