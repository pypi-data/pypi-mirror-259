import json
import os
import sqlite3
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class JSONDatabase:
    def __init__(self, db_file):
        self.db_file = db_file
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as file:
                file.write('{}')

    def read_data(self):
        with open(self.db_file, 'r') as file:
            data = json.load(file)
            return data

    def write_data(self, data):
        with open(self.db_file, 'w') as file:
            json.dump(data, file, indent=4)

    def create_table(self, table_name, schema):
        data = self.read_data()
        if table_name not in data:
            data[table_name] = {"schema": schema, "data": []}
            self.write_data(data)
            return f"Table '{table_name}' created successfully."
        else:
            return f"Table '{table_name}' already exists."

    def insert(self, table_name, values):
        data = self.read_data()
        if table_name not in data:
            raise ValueError(f"Table '{table_name}' does not exist.")

        schema = data[table_name]["schema"]
        row = values

        if len(schema) != len(row):
            raise ValueError("Number of values does not match number of columns in schema.")

        # Create a list of tuples instead of a dictionary to represent the row
        row_data = {field["name"] : value for field, value in zip(schema, row)}

        data[table_name]["data"].append(row_data)
        self.write_data(data)
    def insert_multiple(self, table_name, rows):
        data = self.read_data()
        if table_name in data:
            schema = data[table_name]["schema"]
            for row in rows:
                if len(schema) == len(row):
                    data[table_name]["data"].append(dict(zip([field["name"] for field in schema], row)))
                else:
                    return f"Skipping row {row}: number of values does not match the schema."
            self.write_data(data)
            return "Multiple rows inserted successfully."
        else:
            return f"Table '{table_name}' does not exist."

    def select_all(self, table_name):
        data = self.read_data()
        if table_name in data:
            return data[table_name]["data"]
        else:
            return f"Table '{table_name}' does not exist."

    def delete_data(self, table_name, condition_func):
        data = self.read_data()
        if table_name in data:
            data[table_name]["data"] = [row for row in data[table_name]["data"] if not condition_func(row)]
            self.write_data(data)
            return "Data deleted successfully."
        else:
            return f"Table '{table_name}' does not exist."
    
    def update_data(self, table_name, condition_func, update_func):
        data = self.read_data()
        if table_name in data:
            for row in data[table_name]["data"]:
                if condition_func(row):
                    update_func(row)
            self.write_data(data)
            return "Data updated successfully."
        else:
            return f"Table '{table_name}' does not exist."
    
    def drop_table(self, table_name):
        data = self.read_data()
        if table_name in data:
            del data[table_name]
            self.write_data(data)
            return f"Table '{table_name}' dropped successfully."
        else:
            return f"Table '{table_name}' does not exist."
    
    def drop_all_tables(self):
        self.write_data({})
        return "All tables dropped successfully."
    
    def get_table_schema(self, table_name):
        data = self.read_data()
        if table_name in data:
            return data[table_name]["schema"]
        else:
            return f"Table '{table_name}' does not exist."
        
    def get_all_tables(self):
        data = self.read_data()
        return list(data.keys())
    
    def get_table_data(self, table_name):
        data = self.read_data()
        if table_name in data:
            return data[table_name]["data"]
        else:
            return f"Table '{table_name}' does not exist."
    
    # Encrypt the database
    def encrypt_database(self, key):
        # Read data from the database file
        with open(self.db_file, 'rb') as f:
            data = f.read()

        # Generate initialization vector (IV)
        iv = get_random_bytes(AES.block_size)

        # Pad the data to be a multiple of AES block size
        padded_data = self._pad_data(data)

        # Create AES cipher object
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Encrypt the padded data
        encrypted_data = cipher.encrypt(padded_data)

        # Combine IV and encrypted data
        encrypted_data_with_iv = iv + encrypted_data

        # Write the encrypted data to the database file
        with open(self.db_file, 'wb') as f:
            f.write(encrypted_data_with_iv)
            f.close()
        
        with open(self.db_file + ".key", 'wb') as f:
            f.write(base64.b64encode(key))
            f.close()
        
        return base64.b64encode(key).decode('utf-8')
    
    # Decrypt the database
    def decrypt_database(self, key):

        # Decode the base64 encoded key
        key = base64.b64decode(key)

        # Read encrypted data from the database file
        with open(self.db_file, 'rb') as f:
            encrypted_data_with_iv = f.read()

        # Extract IV from the encrypted data
        iv = encrypted_data_with_iv[:AES.block_size]

        # Extract encrypted data (excluding IV)
        encrypted_data = encrypted_data_with_iv[AES.block_size:]

        # Create AES cipher object
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Decrypt the encrypted data
        decrypted_data = cipher.decrypt(encrypted_data)

        # Unpad the decrypted data
        unpadded_data = self._unpad_data(decrypted_data)

        # Write the decrypted data back to the database file
        with open(self.db_file, 'wb') as f:
            f.write(unpadded_data)

    def _pad_data(self, data):
        block_size = AES.block_size
        padding = block_size - len(data) % block_size
        return data + bytes([padding] * padding)

    def _unpad_data(self, data):
        padding = data[-1]
        return data[:-padding]
class JDBStoSQLite:
    def __init__(self, json_file, sqlite_file):
        self.json_file = json_file
        self.sqlite_file = sqlite_file
        self.datatypes = {
            "int": "INTEGER",
            "string": "TEXT",
            "float": "REAL",
            "boolean": "INTEGER"
        }

    def convert(self):
        # Load JSON data
        with open(self.json_file, 'r') as f:
            data = json.load(f)

        # Connect to SQLite database
        conn = sqlite3.connect(self.sqlite_file)
        cursor = conn.cursor()

        # Create tables and insert data
        for table_name, table_data in data.items():
            fields = ', '.join([f"{field['name']} {self.datatypes[field['type']]}" for field in table_data['schema']])
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({fields})")
            for row in table_data['data']:
                placeholders = ', '.join(['?' for _ in row])
                cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", row)

        # Commit changes and close connection
        conn.commit()
        conn.close()
        return True

