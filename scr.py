import psycopg2

# Підключення до бази даних
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="shipping_db",
    user="user",
    password="password"
)
cursor = conn.cursor()

# Створення таблиць
cursor.execute("""
CREATE TABLE ships (
    ship_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    captain_name VARCHAR(100),
    ship_type VARCHAR(50),
    load_capacity INT,
    build_year INT
);
""")

cursor.execute("""
CREATE TABLE ports (
    port_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(100)
);
""")

cursor.execute("""
CREATE TABLE goods (
    good_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    type VARCHAR(50),
    unit VARCHAR(50),
    price_per_unit DECIMAL,
    requires_custom_declaration BOOLEAN
);
""")

cursor.execute("""
CREATE TABLE shipments (
    shipment_id SERIAL PRIMARY KEY,
    good_id INT,
    quantity INT,
    port_id INT,
    FOREIGN KEY (good_id) REFERENCES goods(good_id),
    FOREIGN KEY (port_id) REFERENCES ports(port_id)
);
""")

cursor.execute("""
CREATE TABLE shipping (
    shipping_id SERIAL PRIMARY KEY,
    shipment_id INT,
    ship_id INT,
    shipping_date DATE,
    delivery_days INT,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id),
    FOREIGN KEY (ship_id) REFERENCES ships(ship_id)
);
""")

conn.commit()
cursor.close()
conn.close()
