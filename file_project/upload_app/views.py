from django.views.generic import CreateView
from .forms import BookForm
from django.shortcuts import render
from .models import Book
from django.core.files.storage import FileSystemStorage

def home_page(request):
    # POST - обязательный метод
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        # сохраняем на файловой системе
        filename = fs.save(file.name, file)
        # получение адреса по которому лежит файл
        file_url = fs.url(filename)
        return render(request, 'home_page.html', {
            'file_url': file_url
        })
    return render(request, 'home_page.html')

#class BookCreate(CreateView):
    # Модель куда выполняется сохранение
 #   model = Book

    # Класс на основе которого будет валидация полей
  #  form_class = BookForm

    # Выведем все существующие записи на странице
   # extra_context = {'books': Book.objects.all()}
    # Шаблон с помощью которого

    # будут выводиться данные
    #template_name = 'book_create.html'

    # На какую страницу будет перенаправление
    # в случае успешного сохранения формы
    #success_url = '/book/'