import sqlite3


def get_genre(genre):
    """
    Функция, которая получает название жанра
    в качестве аргумента и возвращает 10 самых свежих фильмов в формате json.
    :param genre: жанр фильма.
    :return: возвращает 10 самых свежих фильмов в формате json.
    """
    with sqlite3.connect('./netflix.db') as connection:
        cursor = connection.cursor()
        # Фильтрация по результатам агрегации и группировки.
        try:
            query = f"""
                SELECT title, description
                FROM netflix
                WHERE listed_in LIKE '%{genre}%'
                AND type LIKE '%Movie%' 
                ORDER BY release_year DESC
                LIMIT 10
            """
            results = []
            for data in cursor.execute(query).fetchall():
                result = {
                    "title": data[0].strip("\n"),
                    "description": data[1].strip("\n"),
                }
                results.append(result)
        except IndexError:
            results = []
        return results
