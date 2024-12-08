from task_1 import Table, Book, SocialMediaAccount

if __name__ == "__main__":
    table = Table(1.5, 0.8, "дерево")  # Правильные данные для стола
    book = Book("1984", "Джордж Оруэлл", 328)  # Правильные данные для книги
    account = SocialMediaAccount("user123", "user123@example.com")

    try:
        table_invalid = Table(-1.5, 0.8, "дерево")
    except ValueError:
        print("Ошибка: неправильные данные")

    try:
        book_invalid = Book("1984", "Джордж Оруэлл", -10)
    except ValueError:
        print("Ошибка: неправильные данные")

    try:
        account_invalid = SocialMediaAccount("user123", "invalid-email")
    except ValueError:
        print("Ошибка: неправильные данные")
