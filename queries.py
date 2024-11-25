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

# Виконання SQL-запиту
def execute_query(query, params=None):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query, params)  # Виконання запиту з параметрами, якщо вони є
    results = cursor.fetchall()   # Отримання результатів
    cursor.close()
    connection.close()
    return results

# Виведення всіх суден обраного типу
def get_ships_by_type(ship_type):
    query = "SELECT * FROM ships WHERE ship_type = %s;"
    return execute_query(query, (ship_type,))

# Підрахунок вартості товарів у партії
def calculate_goods_value():
    query = """
    SELECT g.name, s.quantity, (g.price_per_unit * s.quantity) AS total_value
    FROM goods g
    JOIN shipments s ON g.good_id = s.good_id;
    """
    return execute_query(query)

# Підрахунок кількості кожного типу товару
def count_goods_by_type():
    query = """
    SELECT g.type, SUM(s.quantity) AS total_quantity
    FROM goods g
    JOIN shipments s ON g.good_id = s.good_id
    GROUP BY g.type;
    """
    return execute_query(query)

if __name__ == "__main__":
    # Демонстрація виконання запитів
    print("Судна типу 'Passenger':")
    ships = get_ships_by_type("Passenger")
    for ship in ships:
        print(ship)

    print("\nВартість товарів у партіях:")
    goods_values = calculate_goods_value()
    for value in goods_values:
        print(value)

    print("\nКількість товарів за типом:")
    goods_count = count_goods_by_type()
    for count in goods_count:
        print(count)
