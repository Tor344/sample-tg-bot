import sqlite3
import json
from typing import List, Dict, Optional

class JsonCartDatabase:
    def __init__(self, db_path: str = 'shopping_cart.db'):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Инициализация таблицы корзин"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
            CREATE TABLE IF NOT EXISTS carts (
                user_id INTEGER PRIMARY KEY,
                items_json TEXT NOT NULL DEFAULT '[]',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            ''')
            conn.commit()

    def _get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    async def add_to_cart(self, user_id: int, product_name: str) -> None:
        """Добавление товара в корзину"""
        with self._get_connection() as conn:
            # Получаем текущую корзину или создаём новую
            cursor = conn.execute(
                'SELECT items_json FROM carts WHERE user_id = ?',
                (user_id,)
            )
            cart = cursor.fetchone()

            if cart:
                items = json.loads(cart[0])
                items.append(product_name)
            else:
                items = [product_name]

            # Обновляем или создаём запись
            conn.execute(
                '''
                INSERT OR REPLACE INTO carts 
                (user_id, items_json, updated_at) 
                VALUES (?, ?, CURRENT_TIMESTAMP)
                ''',
                (user_id, json.dumps(items))
            )
            conn.commit()

    async def get_cart_items(self, user_id: int) -> List[str]:
        """Получение всех товаров в корзине"""
        with self._get_connection() as conn:
            cursor = conn.execute(
                'SELECT items_json FROM carts WHERE user_id = ?',
                (user_id,)
            )
            cart = cursor.fetchone()
            return json.loads(cart[0]) if cart else []

    async def remove_from_cart(self, user_id: int, product_name: str) -> bool:
        """Удаление товара из корзины"""
        with self._get_connection() as conn:
            cursor = conn.execute(
                'SELECT items_json FROM carts WHERE user_id = ?',
                (user_id,)
            )
            cart = cursor.fetchone()

            if not cart:
                return False

            items = json.loads(cart[0])
            if product_name not in items:
                return False

            items.remove(product_name)

            conn.execute(
                '''
                UPDATE carts 
                SET items_json = ?, updated_at = CURRENT_TIMESTAMP
                WHERE user_id = ?
                ''',
                (json.dumps(items), user_id)
            )
            conn.commit()
            return True

    async def clear_cart(self, user_id: int) -> None:
        """Очистка корзины"""
        with self._get_connection() as conn:
            conn.execute(
                'DELETE FROM carts WHERE user_id = ?',
                (user_id,)
            )
            conn.commit()


db = JsonCartDatabase()