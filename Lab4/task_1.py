# TODO: описать базовый класс
class SocialNetwork:
    """
    Базовый класс для социальных сетей.

    Атрибуты:
        name (str): Название социальной сети.
        users (int): Количество пользователей.
    """

    def __init__(self, name: str, users: int):
        self.name = name
        self.users = users

    def __str__(self) -> str:
        """Человекочитаемое представление социальной сети."""
        return f"Социальная сеть: {self.name}, Пользователи: {self.users} млн."

    def __repr__(self) -> str:
        """Официальное строковое представление объекта."""
        return f"SocialNetwork(name={self.name!r}, users={self.users!r})"

    def calculate_user_growth(self, new_users: int) -> int:
        """
        Рассчитывает общее количество пользователей после прироста.

        Аргументы:
            new_users (int): Количество новых пользователей.

        Возвращает:
            int: Общее количество пользователей.
        """
        return self.users + new_users


# TODO: описать дочерний класс
class VK(SocialNetwork):
    """
    Класс для социальной сети ВКонтакте, наследуемый от SocialNetwork.

    Атрибуты:
        has_music (bool): Наличие музыкальных сервисов.
    """

    def __init__(self, users: int, has_music: bool):
        super().__init__("ВКонтакте", users)
        self.has_music = has_music

    def __str__(self) -> str:
        """
        Перегрузка метода __str__ для описания социальной сети ВКонтакте.
        """
        music_status = "Да" if self.has_music else "Нет"
        return f"Соцсеть: {self.name}, Пользователи: {self.users} млн., Музыка: {music_status}"

    def calculate_user_growth(self, new_users: int) -> int:
        """
        Перегрузка метода для расчёта прироста пользователей.
        Обоснование: Если есть музыкальные сервисы, прирост пользователей увеличивается на 10%.

        Аргументы:
            new_users (int): Количество новых пользователей.

        Возвращает:
            int: Общее количество пользователей.
        """
        if self.has_music:
            new_users = int(new_users * 1.1)
        return super().calculate_user_growth(new_users)


if __name__ == "__main__":
    social = SocialNetwork("Общая соцсеть", 100)
    print(social)
    print(repr(social))
    print(social.calculate_user_growth(10))

    vk = VK(70, has_music=True)
    print(vk)
    print(repr(vk))
    print(vk.calculate_user_growth(20))
