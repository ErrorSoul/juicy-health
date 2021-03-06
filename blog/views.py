# Create your views here.
#coding: utf-8
from django.views.generic import ListView, DetailView
from blog.models import Post, Category


class CommentTagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(CommentTagMixin,
                        self).get_context_data(**kwargs)
        context["comments"] = Comment.objects.\
          filter(post=self.object)
        return context


class CategoryMixin(object):
    def get_context_data(self, **kwargs):
        context = super(CategoryMixin,
                        self).get_context_data(**kwargs)
        context["categories"] = self.categories
        return context

class Posts(CategoryMixin, ListView):
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

    def get_queryset(self):
        queryset = self.model.objects.all().\
          prefetch_related('tags')
        self.categories = Category.objects.all()
        return queryset


class PostDetailView(CategoryMixin, DetailView):
    model = Post
    template_name = 'blog/post.html'
    queryset = Post.objects.all().\
      prefetch_related('tags')

    def get_object(self):
        self.categories = Category.objects.all()
        obj = super(PostDetailView,
                    self).get_object()
        return obj 
        
        
         
