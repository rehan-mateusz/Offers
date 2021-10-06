from django.db import models
from django.db.models import F
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

def get_max_categories_amount():
    return Category.objects.all().count() + 1

def adjust_ordering(new_ordering, old_ordering):
    if new_ordering < old_ordering:
        Category.objects.filter(ordering__gte=new_ordering,
            ordering__lt=old_ordering).update(ordering=F('ordering') + 1)
    elif new_ordering > old_ordering:
        Category.objects.filter(ordering__gt=old_ordering,
            ordering__lte=new_ordering).update(ordering=F('ordering') - 1)


class Category(models.Model):
    name = models.CharField(max_length=100)
    ordering = models.PositiveIntegerField(
        default=get_max_categories_amount,
        validators=[
            MaxValueValidator(get_max_categories_amount),
            MinValueValidator(1)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id and Category.objects.filter(id=self.id).exists():
            old_ordering = Category.objects.get(id=self.id).ordering
        else:
            old_ordering = Category.objects.all().count()
        adjust_ordering(self.ordering, old_ordering)
        super().save(*args, **kwargs)

    def delete(self):
        adjust_ordering(get_max_categories_amount()-1, self.ordering)
        super().delete()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(ordering__gte=1),
                name='ordering_gte_1'),
        ]


class Offer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
