from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from picture.forms import PhotoForm
from picture.models import Photo


class PhotoDetailView(DetailView):
    template_name = 'photo.html'
    model = Photo
    context_object_name = 'photo'

    def get(self, request, *args, **kwargs):
        fav = request.GET.get('favorite')
        if fav:
            request.user.favorites.add(fav)
        not_fav = request.GET.get('not_favorite')
        if not_fav:
            request.user.favorites.remove(not_fav)
        return super().get(request, *args, **kwargs)


class PhotoListView(ListView):
    template_name = 'index.html'
    model = Photo
    context_object_name = 'photos'

    def get_queryset(self):
        return super(PhotoListView, self).get_queryset().order_by('-created_at')


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create_photo.html'
    model = Photo
    form_class = PhotoForm
    success_message = 'Публикация создана'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author = request.user
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class PhotoUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'update_photo.html'
    form_class = PhotoForm
    model = Photo
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse('index')


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_photo.html'
    model = Photo
    success_url = reverse_lazy('index')
    success_message = 'Публикация удалена'
