#!/Users/akshaybodla/.pyenv/shims/python3
import sys, sqlite3 as sql, os
import pandas as pd

def main():
    """
        Usage
            - arg 1: relative directory to csv
            - arg 2: relative direcotry to create db
    """

    
    argv = sys.argv[1:]
    if len(argv) <= 0:
        print('Usage: add relative path to file as csv')
        return

    try:
        df = pd.read_csv(argv[0], encoding = "ISO-8859-1")
        os.chdir(argv[1])
        conn = sql.connect('database.db')
        df.to_sql('Database', if_exists='replace', con=conn)
    except Exception as e:
        raise e

    # Create a cursor object
    print('Successfully created database, printing first few lines')
    cur = conn.cursor()
    # Fetch and display result
    x = 0
    for row in cur.execute('SELECT * FROM Database'):
        print(row, end='\n\n')
        if x >5:
            break
        x += 1


    

if __name__ == "__main__":
    main()
