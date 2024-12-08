import doctest


class Table:
    def __init__(self, length: float, width: float, material: str):
        """
        Инициализация стола с заданными длиной, шириной и материалом.

        :param length: Длина стола в метрах
        :param width: Ширина стола в метрах
        :param material: Материал стола (дерево, металл, пластик)

        Пример:
        >>> table = Table(1.5, 0.8, "дерево")
        >>> table.length
        1.5
        >>> table.material
        'дерево'
        """
        if length <= 0 or width <= 0:
            raise ValueError("Длина и ширина стола должны быть положительными числами.")
        if material.lower() not in ["дерево", "металл", "пластик"]:
            raise ValueError("Материал должен быть одним из: дерево, металл, пластик.")

        self.length = length
        self.width = width
        self.material = material.lower()

    def area(self) -> float:
        """Метод для вычисления площади стола."""
        return self.length * self.width

    def change_material(self, new_material: str) -> None:
        """
        Метод для изменения материала стола.

        :param new_material: Новый материал стола

        Пример:
        >>> table = Table(1.5, 0.8, "дерево")
        >>> table.change_material("металл")
        >>> table.material
        'металл'
        """
        if new_material.lower() not in ["дерево", "металл", "пластик"]:
            raise ValueError("Материал должен быть одним из: дерево, металл, пластик.")
        self.material = new_material.lower()


if __name__ == "__main__":
    doctest.testmod()


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги с названием, автором и количеством страниц.

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Пример:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.title
        '1984'
        >>> book.pages
        328
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_to_read: int = 10) -> str:
        """
        Метод для чтения книги, уменьшает количество оставшихся страниц.

        :param pages_to_read: Количество страниц для чтения
        :return: Строка с количеством прочитанных страниц

        Пример:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.read(50)
        'Прочитано 50 страниц. Осталось 278 страниц.'
        """
        if pages_to_read <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным числом.")
        if pages_to_read > self.pages:
            raise ValueError("Вы не можете прочитать больше страниц, чем в книге.")
        self.pages -= pages_to_read
        return f"Прочитано {pages_to_read} страниц. Осталось {self.pages} страниц."

    def get_info(self) -> str:
        """
        Метод для получения информации о книге.

        Пример:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.get_info()
        'Книга: 1984, Автор: Джордж Оруэлл, Страниц: 328'
        """
        return f"Книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}"


if __name__ == "__main__":
    doctest.testmod()


class SocialMediaAccount:
    def __init__(self, username: str, email: str, followers: int = 0):
        """
        Инициализация аккаунта в социальной сети.

        :param username: Имя пользователя
        :param email: Электронная почта пользователя
        :param followers: Количество подписчиков

        Пример:
        >>> account = SocialMediaAccount("user123", "user123@example.com")
        >>> account.username
        'user123'
        >>> account.followers
        0
        """
        if "@" not in email or "." not in email:
            raise ValueError("Некорректный email.")

        self.username = username
        self.email = email
        self.followers = followers

    def follow(self, count: int) -> str:
        """
        Метод для увеличения количества подписчиков.

        :param count: Количество подписчиков для добавления

        Пример:
        >>> account = SocialMediaAccount("user123", "user123@example.com")
        >>> account.follow(100)
        'Теперь у пользователя user123 100 подписчиков.'
        """
        if count <= 0:
            raise ValueError("Количество подписчиков для добавления должно быть положительным числом.")
        self.followers += count
        return f"Теперь у пользователя {self.username} {self.followers} подписчиков."

    def unfollow(self, count: int) -> str:
        """
        Метод для уменьшения количества подписчиков.

        :param count: Количество подписчиков для удаления

        Пример:
        >>> account = SocialMediaAccount("user123", "user123@example.com", 100)
        >>> account.unfollow(30)
        'Теперь у пользователя user123 70 подписчиков.'
        """
        if count <= 0:
            raise ValueError("Количество подписчиков для удаления должно быть положительным числом.")
        if count > self.followers:
            raise ValueError("Невозможно удалить больше подписчиков, чем есть.")
        self.followers -= count
        return f"Теперь у пользователя {self.username} {self.followers} подписчиков."

    def get_account_info(self) -> str:
        """
        Метод для получения информации о аккаунте.

        Пример:
        >>> account = SocialMediaAccount("user123", "user123@example.com")
        >>> account.get_account_info()
        'Аккаунт: user123, Email: user123@example.com, Подписчики: 0'
        """
        return f"Аккаунт: {self.username}, Email: {self.email}, Подписчики: {self.followers}"


if __name__ == "__main__":
    doctest.testmod()
