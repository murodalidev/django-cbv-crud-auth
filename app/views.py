from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, RedirectView
from app.forms import *
from django.db.models import F
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# #########################################################################
class UserRegisterView(View):

    def get(self, request):
        return render(request, 'app/auth.html', {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))

        return render(request, 'app/auth.html', {'form': form})


class UserLoginView(View):
    def get(self, request):
        return render(request, 'app/auth.html', {'form':  AuthenticationForm})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is None:
                return render(
                    request,
                    'app/auth.html',
                    {'form': form, 'invalid_creds': True}
                )

            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'app/auth.html',
                    {'form': form, 'invalid_creds': True}
                )
            login(request, user)

            return redirect(reverse('authors'))


class UserLogoutView(RedirectView):
    url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(UserLogoutView, self).get(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    # form_class = UserCreationForm
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'app/auth.html'
    success_url = '/'
    slug_field = 'username'

    def get(self, request, **kwargs):
        self.object = User.objects.get(pk=self.request.user.pk)
        # self.object = User.objects.get(username=self.request.user.username)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.success_url)


# #########################################################################
class PublisherListView(ListView):
    model = Publisher
    template_name = 'app/publishers.html'
    context_object_name = 'publishers'
    paginate_by = 5


class PublisherDetailView(DetailView):
    template_name = 'app/publisher-detail.html'
    model = Publisher
    context_object_name = 'detail'


class PublisherCreateView(CreateView):
    template_name = 'app/create.html'
    form_class = CreatePublisherForm
    model = Publisher
    success_url = '/publishers/'
    # pk_url_kwarg = 'pk'


class PublisherUpdateView(UpdateView):
    model = Publisher
    form_class = CreatePublisherForm
    template_name = 'app/create.html'
    success_url = '/publishers/'


class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'app/delete.html'
    success_url = '/publishers/'


# #########################################################################
class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'app/authors.html'
    paginate_by = 5


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'detail'
    template_name = 'app/author-detail.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = CreateAuthorForm
    template_name = 'app/create.html'
    success_url = '/authors/'
    # fields = ['salutation', 'name', 'email', 'headshot']


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = CreateAuthorForm
    template_name = 'app/create.html'
    success_url = '/authors/'


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'app/delete.html'
    success_url = '/authors/'


# #########################################################################
class BookListView(ListView):
    model = Book
    template_name = 'app/books.html'
    context_object_name = 'books'
    paginate_by = 5


class BookDetailView(DetailView):
    model = Book
    template_name = 'app/book-detail.html'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Book.objects.filter(pk=self.kwargs.get('pk'))
        post.update(views=F('views') + 1)
        return context


class BookCreateView(CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'app/create.html'
    success_url = '/books/'


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'app/create.html'
    success_url = '/books/'


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'app/delete.html'
    success_url = '/books/'
