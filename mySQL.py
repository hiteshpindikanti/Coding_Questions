import pandas as pd
import mysql.connector
from mysql.connector import Error


def create_connection(host_name: str, user_name: str, user_password: str):
    """
    Creating MySQL Connection
    :param host_name: host name of the mySQL server
    :param user_name: username for the Database
    :param user_password: password for the account
    :return:

    USAGE:
    create_connection("user","pwd")
    """
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return conn


def insert_df(dataframe: pd.DataFrame, cursor: mysql.connector.connection.MySQLCursor, table_name: str) -> bool:
    """
    Inserting the Dataframe in the MySQL table
    :param dataframe:
    :param cursor:
    :param table_name: Complete DB.Table_name
    :return:
    """
    try:
        for row1 in dataframe.itertuples():
            row = list(row1)
            row[-3] = "{2}-{0}-{1}".format(row[-3][:2], row[-3][3:5], row[-3][6:]) if row[-3] is not None else None
            row[-2] = "{2}-{0}-{1}".format(row[-2][:2], row[-2][3:5], row[-2][6:]) if row[-2] is not None else None

            cur.execute("REPLACE INTO {} \
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(table_name),
                        row[1:]
                        )
        return True
    except:
        return False




# Create Connection
connection = create_connection('localhost', 'root', 'password')
cur = connection.cursor()

# Drop the Table if it exists
dropTableStatement = "DROP TABLE IF EXISTS test_db.restaurants"
cur.execute(dropTableStatement)

# Create Table
createTableStatement = "CREATE TABLE IF NOT EXISTS test_db.restaurants \
                        (LOCATION_ACCOUNT VARCHAR(17) NOT NULL, \
                        BUSINESS_NAME TEXT, DBA_NAME TEXT, STREET_ADDRESS TEXT, \
                        CITY TEXT, ZIP_CODE TEXT, LOCATION_DESCRIPTION TEXT, MAILING_ADDRESS TEXT, \
                        MAILING_CITY TEXT, MAILING_ZIP_CODE TEXT, NAICS TEXT, \
                        PRIMARY_NAICS_DESCRIPTION TEXT, COUNCIL_DISTRICT TEXT, LOCATION_START_DATE DATE, \
                        LOCATION_END_DATE DATE, LOCATION TEXT, \
                        PRIMARY KEY(LOCATION_ACCOUNT))"
cur.execute(createTableStatement)

# Read and transform data
data = pd.read_csv('/Users/hiteshpindikanti/Downloads/restaurants.csv', header=0)
df = pd.DataFrame(data, columns=list(data.columns))
df = df.where((pd.notnull(df)), None)

# Insert Data
insert_df(df, cur, 'test_db.restaurants')

# Commit the Changes
connection.commit()

# Read and transform data
data = pd.read_csv('/Users/hiteshpindikanti/Downloads/restaurants-dataset-2.csv', header=0)
df = pd.DataFrame(data, columns=list(data.columns))
df = df.where((pd.notnull(df)), None)
insert_df(df, cur, 'test_db.restaurants')

# Commit the Changes
connection.commit()

# Close the connection
cur.close()

