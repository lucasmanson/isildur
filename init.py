import argparse
import csv
import sqlite3
from pathlib import Path


def load_csv_to_db(csv_path: Path, db_path: Path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with csv_path.open('r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        columns = ', '.join(f'{h} TEXT' for h in headers)
        cursor.execute(f'CREATE TABLE IF NOT EXISTS usuarios ({columns})')

        placeholders = ', '.join('?' for _ in headers)
        insert_query = f'INSERT INTO usuarios VALUES ({placeholders})'
        for row in reader:
            cursor.execute(insert_query, row)

    conn.commit()
    conn.close()


def main():
    parser = argparse.ArgumentParser(description="Cargar CSV en SQLite")
    parser.add_argument('csv', type=Path, help='Ruta al archivo CSV')
    parser.add_argument('--db', type=Path, default=Path('datos.db'), help='Ruta a la base de datos SQLite')
    args = parser.parse_args()

    load_csv_to_db(args.csv, args.db)
    print('Datos cargados en la base de datos')


if __name__ == '__main__':
    main()
