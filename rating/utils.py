import sqlite3


def get_rating(group):
    """
    Функция поиска по рейтингу.
    :param group: children, family, adult.
    :return: рейтинг.
    """
    if group.lower() == 'children':
        return 'G', 'G'
    elif group.lower() == 'family':
        return 'G', 'PG', 'PG-13'
    elif group.lower() == 'adult':
        return 'R', 'NC-17'
    else:
        return 'Dont know this group'


def get_rating_query(rating):
    """
    Функция, которая принимает список допустимых рейтингов и
    возвращала данные в формате списка словарей.
    :param rating: данные рейтинга (get_rating(group)).
    :return: данные в формате списка словарей.
    """
    # SQL запрос.
    with sqlite3.connect('./netflix.db') as connection:
        cursor = connection.cursor()
        # Фильтрация по результатам агрегации и группировки.
        try:
            query = f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating IN {rating} AND type = 'Movie' 
            """
            results = []
            cursor.execute(query)
            for data in cursor.fetchall():
                result = {
                    "title": data[0].strip("\n"),
                    "rating": data[1].strip("\n"),
                    "description": data[2].strip("\n"),
                }
                results.append(result)
        except IndexError:
            return []
        return results


# print(get_rating_query('children'))
