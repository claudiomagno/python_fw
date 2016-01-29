import cx_Oracle


class DAConexaoFactory():
 
    # Define atributos privados
	# http://desenvolvimentoaberto.org/2014/12/13/dao-data-access-object-pattern-crud-oracle-ibm-db2-mssql-server-python/
 
    def __init__(self):
        self.__ORACLE = 1
        self.__DB2 = 2
        self.__MSSQL = 3
        self.__erroCon = None
        self.__factory = None
        self.__IBMDriver = None # IBM DB2 driver (ibm_db)
 
    # Cria Factory para objetos
    def getConexao(self, banco):
 
        # Define conexão e fonte de dados
        con = None
        self.__factory = banco
 
        # Cria string de conexão Oracle
        if (banco == self.__ORACLE):
			sconexao = "user/pass@localhost/XE"
			uid = 'sisgaf3'
			pwd = 'sisgaf3'
			db = 'SISGAF3'
            try:				
                con = cx_Oracle.connect(uid+"/"+pwd+"@"+db)
            except Exception, e:
                self.__erroCon = str(e)
 
        # Cria string de conexão IBM DB2
        if (banco == self.__DB2):
            sconexao = "DATABASE=DEVA" + \
                       ";HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;" + \
                       "UID=user;" + \
                       "PWD=pass"
            try:
                self.__IBMDriver = ibm_db
                con = ibm_db.connect(sconexao, "", "")
            except Exception, e:
                self.__erroCon = str(e)
 
        # Cria string de conexão MSSQL
        if (banco == self.__MSSQL):
            sconexao = "MSSQLSERVER/user/pass"
            try:
                con = odbc.odbc(sconexao)
            except Exception, e:
                self.__erroCon = str(e)
 
        return con
 
    # Retorna Erros
    def getErros(self):
        return self.__erroCon
 
    # Retorna Factory da conexão
    def getFactory(self):
        return self.__factory
 
    # Retorna Driver da IBM (Oracle e MSSQL possui outro padrão)
    def getIbmDriver(self):
        return self.__IBMDriver