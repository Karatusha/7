import psycopg2

# Параметри підключення
def connect():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="shipping_db",
        user="user",
        password="password"
    )
def create_tables():
    connection = connect()
    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE ships (
        ship_id SERIAL PRIMARY KEY,       -- Унікальний ідентифікатор (автоінкремент)
        name VARCHAR(100),               -- Назва судна
        captain_name VARCHAR(100),       -- Ім'я капітана
        ship_type VARCHAR(50),           -- Тип судна (наприклад, "танкер", "суховантажний")
        load_capacity INT,               -- Вантажопідйомність
        build_year INT                   -- Рік побудови
    );
    """)

    cursor.execute("""
    CREATE TABLE ports (
        port_id SERIAL PRIMARY KEY,
        name VARCHAR(100),               -- Назва порту
        country VARCHAR(100)             -- Країна, де розташований порт
    );
    """)

    cursor.execute("""
    CREATE TABLE goods (
        good_id SERIAL PRIMARY KEY,
        name VARCHAR(100),               -- Назва товару
        type VARCHAR(50),                -- Тип товару
        unit VARCHAR(50),                -- Одиниця вимірювання (наприклад, "шт", "тонни")
        price_per_unit DECIMAL,          -- Ціна за одиницю
        requires_custom_declaration BOOLEAN -- Потрібна митна декларація (True/False)
    );
    """)

    cursor.execute("""
    CREATE TABLE shipments (
        shipment_id SERIAL PRIMARY KEY,
        good_id INT REFERENCES goods(good_id), -- Зв'язок із таблицею товарів
        quantity INT,                          -- Кількість товару
        port_id INT REFERENCES ports(port_id)  -- Зв'язок із таблицею портів
    );
    """)

    cursor.execute("""
    CREATE TABLE shipping (
        shipping_id SERIAL PRIMARY KEY,
        shipment_id INT REFERENCES shipments(shipment_id), -- Зв'язок із таблицею партій
        ship_id INT REFERENCES ships(ship_id),             -- Зв'язок із таблицею суден
        shipping_date DATE,                                -- Дата відправки
        delivery_days INT                                  -- Кількість днів доставки
    );
    """)

    connection.commit()
    cursor.close()
    connection.close()

    print("Таблиці успішно створені!")

if __name__ == "__main__":
    create_tables()
