Список тестов в проекте: 
1. test_add_new_book_not_add_book_name_with_len_more_40_simbols - проверяет, что в словарь books_genre нельзя добавить книгу с кол-вом символов в названии > 40
2. test_set_book_genre_set_genre_for_book_not_in_dict - проверяет, что нельзя установить жанр для книги, которой нет в словаре books_genre
3. test_set_book_genre_set_genre_for_book_in_dict - проверяет, что можно установить жанр для книги, которая есть в словарь books_genre
4. test_get_book_genre_for_book_not_in_dict - проверяет, что нельзя получить жанр книги6 которой нет в словаре books_genre
5. test_get_books_with_specific_genre_for_unavailable_genre - проверяет, что нельзя вывести список книг с определённым жанром, если жанра нет в списке genre
6. test_get_books_with_specific_genre_for_available_genre - проверяет, что можно вывести список книг с определённым жанром, если этот жанр есть в списке genre
7. test_get_books_genre_return_dict - проверяем, что метод возвращает словарь
8. test_get_books_for_children_return_right_books - проверяем, что метод возвращает книги, подходящие детям
9. test_get_books_for_children_not_return_wrong_books - проверяем, что метод не возвращает книги, подходящие детям
10. test_add_book_in_favorites_is_successful - проверяем, что метод позволяет добавить книги в список favorites
11. test_add_book_in_favorites_add_two_books - проверяем, что метод позволяет добавить две книги в список favorites
12. test_add_book_in_favorites_twice_is_unsuccessful - проверяем, что нельзя добавить в список favorites книгу с одним и тем же названием дважды
13. test_delete_book_from_favorites_is_successful - проверяем, что можно удалить книгу из списка favorites
14. test_delete_book_from_favorites_delete_two_books - проверяем, что можно удалить две книги из списка favorites
15. test_get_list_of_favorites_books_return_list - проверяем, что метод get_list_of_favorites_books возвращает список
