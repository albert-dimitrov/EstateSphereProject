from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView


class ChatRoomDetailView(DetailView):
    pass


class ChatRoomDeleteView(DeleteView):
    pass


class ChatRoomEditView(UpdateView):
    pass


class AddMassageView(CreateView):
    pass


class MassageDeleteView(DeleteView):
    pass

