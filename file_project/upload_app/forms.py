from .models import Book
from django.forms import ModelForm


class BookForm(ModelForm):

    class Meta:
        # Название модели на основе
        # которой создается форма
        model = Book
        # Включаем все поля с модели в форму
        fields = '__all__'