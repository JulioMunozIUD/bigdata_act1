import sqlite3
import pandas as pd

def export_db_to_excel():
    db_path = "src/static/db/ingestion.db"
    output_path = "output.xlsx"
    
    # Connect to the database
    conn = sqlite3.connect(db_path)
    
    # Read the entire table into a DataFrame
    df = pd.read_sql_query("SELECT * FROM characters", conn)
    
    # Save DataFrame to an Excel file
    df.to_excel(output_path, index=False, engine='openpyxl')
    
    # Close connection
    conn.close()
    
    print("Archivo Excel 'output.xlsx' generado exitosamente.")

if __name__ == "__main__":
    export_db_to_excel()
