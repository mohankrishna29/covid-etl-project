import psycopg2

def load_data(df):
    conn = psycopg2.connect(
        dbname="covid_db",
        user="postgres",
        password="",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""INSERT INTO covid_stats (COUNTRY, CASES, DEATHS, RECOVERED,
                       CASESPERONEMILLION, DEATHSPERONEMILLION, TESTS, TESTSPERONEMILLION, 
                       POPULATION, CONTINENT)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", tuple(row))

    conn.commit()
    cursor.close()
    conn.close()