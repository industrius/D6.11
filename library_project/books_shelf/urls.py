from django.urls import path
from . import views

urlpatterns = [
    path("", views.BooksView.as_view(), name="books"),
    path("book/<int:id>/", views.BookDetails.as_view()),
    path("author/<int:id>/", views.AuthorDetails.as_view()),
    path("increment", views.book_increment, name="inc"),
    path("decrement", views.book_decrement, name="dec"),
    path("authors", views.AuthorsView.as_view(), name="authors"),
    path("publishers", views.PublishersView.as_view(), name="publishers"),
    path("publisher/<int:id>", views.PublisherDetail.as_view()),
    path("friends", views.FriendsView.as_view(), name="friends"),
    path("friend/<int:id>", views.FriendDetails.as_view(), name="friend"),
    path("give_to_friend", views.give_to_friend, name="give"),
    path("return_book", views.return_book, name="return"),
    path("book/new", views.CreateBook, name="create_book"),
    path("author/new", views.CreateAuthor, name="create_author"),
    path("publisher/new", views.CreatePublisher, name="create_publisher"),
    path("friend/new", views.CreateFriend, name="create_friend"),
    path("author/delete", views.DeleteAuthor, name="delete_author"),
    path("publisher/delete", views.DeletePublisher, name="delete_publisher"),
    path("friend/delete", views.DeleteFriend, name="delete_friend"),
    path("book/delete", views.DeleteBook, name="delete_book")
]