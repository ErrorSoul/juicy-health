# Create your views here.
#coding: utf-8
from django.views.generic import ListView
from blog.models import Post

class Posts(ListView):
    """
    Список всех доступных статей
    """

    # Нижеуказанные параметры можно также передать данному отображению через метод as_view()
    # url(r'^$', Posts.as_view(context_object_name='posts', template_name='posts.html))
    model = Post
    # Под данным именем наш список статей будет доступен в шаблоне
    context_object_name = 'post_list'
    # Название шаблона
    template_name = 'blog/index.html'
    # Количество объектов на 1 страницу
    paginate_by = 5

