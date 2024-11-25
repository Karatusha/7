import psycopg2

# Функція для підключення до бази даних
def connect():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="shipping_db",
        user="user",
        password="password"
    )

# Функція для очищення таблиць
def delete_all_data():
    connection = connect()
    cursor = connection.cursor()

    # Очищення даних у таблицях
    cursor.execute("TRUNCATE TABLE shipping RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE shipments RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE goods RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE ports RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE ships RESTART IDENTITY CASCADE;")

    connection.commit()
    cursor.close()
    connection.close()
    print("Всі дані успішно видалено!")

# Виконуємо функцію
if __name__ == "__main__":
    delete_all_data()
