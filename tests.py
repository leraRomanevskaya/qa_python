import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('book_name', ['', 'Преступление и наказание в бандитском Пет', 'Преступление и наказание в бандитском Пете'])
    def test_add_new_book_books_with_len_0_41_42_simbols_have_not_been_added_to_the_dictionary(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    @pytest.mark.parametrize('book_name', ['П', 'Пр',
                                           'Преступление и наказание в бандитском П', 'Преступление и наказание в бандитском Пе'])
    def test_add_new_book_books_with_len_1_2_39_40_simbols_have_been_added_to_the_dictionary(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_set_book_genre_set_genre_for_book_not_in_dict(self):
        collector = BooksCollector()
        collector.set_book_genre('Форест Гамп', 'Фантастика')
        assert collector.get_book_genre('Форест Гамп') is None

    def test_set_book_genre_set_genre_for_book_in_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Форест Гамп')
        collector.set_book_genre('Форест Гамп', 'Фантастика')
        assert collector.get_book_genre('Форест Гамп') == 'Фантастика'

    def test_get_books_with_specific_genre_for_unavailable_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Форест Гамп')
        collector.set_book_genre('Форест Гамп', 'Мистика')
        assert len(collector.get_books_with_specific_genre('Мистика')) == 0

    def test_get_books_with_specific_genre_for_available_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Форест Гамп')
        collector.set_book_genre('Форест Гамп', 'Фантастика')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 1

    def test_get_books_genre_return_dict(self):
        collector = BooksCollector()
        collector.get_books_genre()
        assert collector.get_books_genre() == dict()

    @pytest.mark.parametrize('book_genre', ['Фантастика', 'Мультфильмы', 'Комедии'])
    def test_get_books_for_children_return_right_books(self, book_genre):
        collector = BooksCollector()
        collector.add_new_book('Форест Гамп')
        collector.set_book_genre('Форест Гамп', book_genre)
        assert 'Форест Гамп' in collector.get_books_for_children()

    @pytest.mark.parametrize('book_genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_not_return_wrong_books(self, book_genre):
        collector = BooksCollector()
        collector.add_new_book('Форест Гамп')
        collector.set_book_genre('Форест Гамп', book_genre)
        assert 'Форест Гамп' not in collector.get_books_for_children()

    def test_add_book_in_favorites_is_successful(self):
        collector = BooksCollector()
        collector.add_new_book('Форест Гамп')
        collector.add_book_in_favorites('Форест Гамп')
        assert 'Форест Гамп' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice_is_unsuccessful(self):
        collector = BooksCollector()
        collector.add_new_book('Форест Гамп')
        collector.add_book_in_favorites('Форест Гамп')
        collector.add_book_in_favorites('Форест Гамп')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_is_successful(self):
        collector = BooksCollector()
        collector.add_new_book('Форест Гамп')
        collector.delete_book_from_favorites('Форест Гамп')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_return_list(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == list()
