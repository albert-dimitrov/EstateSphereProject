from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from estatesphere.contacts.forms import MassageAddForm
from estatesphere.contacts.models import ChatRoom, Massages


class ChatRoomDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ChatRoom
    template_name = 'contacts/chat-room.html'

    def test_func(self):
        chat_room = get_object_or_404(ChatRoom, pk=self.kwargs['pk'])
        return self.request.user == chat_room.user or self.request.user.groups.filter(name='Moderation Group').exists() or self.request.user.is_superuser


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['massage_form'] = MassageAddForm

        return context


class ChatRoomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ChatRoom
    template_name = 'contacts/chatroom-delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Moderation Group').exists()



class AddMassageView(LoginRequiredMixin, CreateView):
    model = Massages
    form_class = MassageAddForm

    def form_valid(self, form):
        chat_room_id = self.kwargs.get('chat_room_id')
        chat_room = get_object_or_404(ChatRoom, pk=chat_room_id)
        form.instance.sender = self.request.user
        form.instance.chatroom = chat_room

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('chatroom-detail', kwargs={'pk': self.kwargs.get('chat_room_id')})

