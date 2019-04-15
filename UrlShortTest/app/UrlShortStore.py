import psycopg2
from configparser import ConfigParser
 
 
class UrlShortStore:
    tblShort='tblShort'
    def __init__(self):
        self.config()
        self.db = psycopg2.connect(**self.params)
 
        self.cursor = self.db.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS {} (id SERIAL PRIMARY KEY, tag VARCHAR(255), url VARCHAR(255) NOT NULL);'.format(UrlShortStore.tblShort))
        self.db.commit()
    def config(self,filename='database.ini', section='postgresql'):
        parser = ConfigParser()
        parser.read(filename)
 
        self.params = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                self.params[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    def len(self):
        self.cursor.execute('SELECT COUNT(*) FROM {}'.format(UrlShortStore.tblShort))

        result = self.cursor.fetchone()

        return result[0]
    def setShort(self, index, short):
        sql='UPDATE {} SET tag=\'{}\' WHERE id={};'.format(UrlShortStore.tblShort,short,index)
        self.cursor.execute(sql)
        self.db.commit()
    def addUrl(self, url):
        sql='INSERT INTO {} (url) VALUES (\'{}\') RETURNING id;'.format(UrlShortStore.tblShort,url,)
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]
    def getUrl(self, short):
        sql='SELECT url FROM {} WHERE tag=\'{}\';'.format(UrlShortStore.tblShort,short,)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if len(result)>0:
            return result[0][0]
        raise Exception('Invalid Link')

