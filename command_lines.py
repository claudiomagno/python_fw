#http://wsloterias.azurewebsites.net/gettingstarted

import json
import requests

r = requests.get('http://wsloterias.azurewebsites.net/api/sorteio/getresultado/1')

r.text
r.json()

dados = r.json()
print json.dumps(dados,indent=1)
dados['ValorAcumuladoEspecial']

for x in dados['Sorteios']:
	print x['Numeros']
	
n =dados['NumeroConcurso']
numeros=[]
listMega=[]
n = n -1

################################################################

#r = requests.get('http://wsloterias.azurewebsites.net/api/sorteio/getresultado/1/'+ str(n))

def teste(n):
	while(n !=1076):
		r = requests.get('http://wsloterias.azurewebsites.net/api/sorteio/getresultado/1/'+ str(n))
		n = n -1
		dados = r.json()
		for x in dados['Sorteios']:
			numeros.append(x['Numeros'])
################################################################
			
def verificar(numero):
	return numero.sort() in numeros.sort()
################################################################	
def verificar2(numero):
	for x in numeros:
		for y in x:
			for z in numeros:
				if(y == z): return z
################################################################			
class mega:
	def __init__(self,concurso,numeros):
		self.concurso = concurso
		self.numeros = numeros

################################################################		
def teste(n):
	while(n !=1076):
		r = requests.get('http://wsloterias.azurewebsites.net/api/sorteio/getresultado/1/'+ str(n))
		n = n -1
		dados = r.json()
		for x in dados['Sorteios']:
			m=mega(n,x['Numeros'])
			listMega.append(m)
			
################################################################			
sortear=[6,45,18,55,40,10]
def verificar3(sortear):
	for x in listMega:
		for y in x.numeros:
			for z in sortear:
				if(y == z): print 'Concurso: '+ str(x.concurso) + ' já saiu: '+ str(z)
			
################################################################	
listSort=[]
def nMaisRepete():
	for x in listMega:
		sortear.sort()
		x.numeros.sort()
		for z in sortear:
			if(z in x.numeros):
				if(z not in listSort):
					listSort.append(z)
					
################################################################	
def repeteConcurso():
	for x in listMega:
		m = mega(x.concurso,set(sortear).intersection(x.numeros))
		listSort.append(m)
	for x in listSort:
		'Concurso: '+ str(x.concurso) , ' Números: ' + str(x.numeros)
					
####################################################################

import csv

def arqCabecalho():
	arq = 'E:/magno/magno/Project_Test/D3/teste2.csv'
	c = csv.writer(open(arq, "wb"))
	c.writerow(["Concurso","Números"])
	cr = csv.reader(open(arq,"rb"))
	for i in cr:
		print i
		


def arqCabecalho():
	arq = 'E:/magno/magno/Project_Test/D3/population2.csv'
	c = csv.writer(open(arq, "wb"))
	c.writerow(["year","age","sex","people"])
	cont=0
	cont2=0
	for x in range(1,17):

		for ano in range(19):
			ano = ano+1
			c.writerow([1850+cont,cont2,1,10*100*ano])
			c.writerow([1850+cont,cont2,2,10*2255*ano])
			cont2= cont2+5
		cont2=0
		cont = cont+10
#########################################################################

import cx_Oracle
uid = 'sisgaf3'
pwd = 'sisgaf3'
db = 'SISGAF3'
connection = cx_Oracle.connect(uid+"/"+pwd+"@"+db)
cursor = connection.cursor()
cursor.execute("SELECT * from AGENCIA")
result = cursor.fetchone()
if result == None: 
        print "Nenhum Resultado"
        exit
else:
        while result:   
                print result[0]
                result = cursor.fetchone()
cursor.close()
connection.close()

def con():
    uid = 'sisgaf3'
    pwd = 'sisgaf3'
    db = 'SISGAF3'
	con = None
	try:
		con = cx_Oracle.connect(uid+"/"+pwd+"@"+db)
	except Exception, e:
		print str(e)
	return con

#########################################################################
				
arq = 'E:/magno/magno/Project_Test/D3/banco.csv'
import os
import csv
file=open(arq,'w')
output=csv.writer(file,dialect='excel')
cursor.execute("SELECT * from BETO_LOG")
for row in cursor:
        output.writerow(row)

        
file.close()
cursor.close()
connection.close()


def gerarCSV(lista,arquivo):
	file=open(arquivo,'w')
	output=csv.writer(file,dialect='excel')
	for linha in lista:
		tup =(linha.codigo,linha.descricao,linha.cdPeriodo,linha.periodo)
		output.writerow(tup)
	file.close()

#########################################################

class Carencia(object):
	def __init__(self,codigo=None,descricao=None,periodo=None,cdPeriodo=None):
		self.codigo = codigo
		self.descricao = descricao
		self.periodo = periodo
		self.cdPeriodo = cdPeriodo
	def getCodigo(self):
		return self.codigo
	def setCodigo(self,codigo):
		self.codigo = codigo
	def getDescricao(self):
		return self.descricao
	def setDescricao(self,descricao):
		self.descricao = descricao
	def getPeriodo(self):
		return self.periodo
	def setPeriodo(self,periodo):
		self.periodo = periodo
	def getCdPeriodo(self):
		return self.cdPeriodo
	def setCdPeriodo(self,cdPeriodo):
		self.cdPeriodo = cdPeriodo
	def toString(self):
		return 'Codigo: ' + str(self.codigo) + ' Descricao: ' + self.descricao + ' Periodo: ' + str(self.periodo) + ' Cod.Unidade: ' + self.cdPeriodo
	def atributos(self):
		atribu=['setCodigo','setDescricao','setPeriodo','setCdPeriodo']
		return atribu
	def classe(self):
		return type(self).__name__
#################################################################

def con():
	con = None
	try:
		con = cx_Oracle.connect(uid+"/"+pwd+"@"+db)
	except Exception, e:
		print str(e)
	return con
	
######################################################
listCarencia=[]

def getCarencias(con):
	cursor2 = con.cursor()
	cursor2.execute("SELECT * from CARENCIA")
	result = cursor2.fetchone()
	carencias = []
	if result == None:
		print "Nenhum Resultado"
		exit
	else:
		while result:
						
			carencias.append(Carencia(result[0],result[1],result[2],result[3]))
			result = cursor2.fetchone()
	cursor2.close()
	con.close()
	return carencias
	
#######################################

import sys
def str_to_class(str):
	return getattr(sys.modules[__name__], str)
	

#################################################

def teste(obj):
	c='classe'
	cod='3434'
	classe = getattr(sys.modules[__name__], obj)()
	r = c+".setCodigo('"+cod+"')"
	ex=eval(r)
	ex
	lista.append(classe)

#################################################
	
def teste2(obj):
	classe = getattr(sys.modules[__name__], obj)()
	for i in classe.atributos():
		r = "classe."+ i + "('"+i+"')"
		ex=eval(r)
		ex
		lista.append(classe)

#######################################################

def getObjetos(con,obj):
	cursor2 = con.cursor()
	cursor2.execute("SELECT * from "+obj)
	result = cursor2.fetchone()
	objetos = []

	if result == None:
		print "Nenhum Resultado"
		exit
	else:
		while result:
			i =0
			classe = getattr(sys.modules[__name__], obj)()
			ex1=eval("classe.atributos()")
			for x in ex1:
				r2 = "classe."+ x +"('"+str(result[i])+"')"
				ex2=eval(r2)
				ex2
				if(classe not in objetos):
					objetos.append(classe)
				i=i+1
			result = cursor2.fetchone()
	cursor2.close()
	con.close()
	return objetos
		
#######################################################

class Agente(object):
	def __init__(self,codigo=None,descricao=None,tipo=None):
		self.codigo = codigo
		self.descricao = descricao
		self.tipo = tipo
	def getCodigo(self):
		return self.codigo
	def setCodigo(self,codigo):
		self.codigo = codigo
	def getDescricao(self):
		return self.descricao
	def setDescricao(self,descricao):
		self.descricao = descricao
	def getTipo(self):
		return self.tipo
	def setTipo(self,tipo):
		self.tipo = tipo
	def toString(self):
		return 'Codigo: ' + str(self.codigo) + ' Descricao: ' + self.descricao + ' Tipo: ' + str(self.tipo) 
	def atributos(self):
		atribu=['setCodigo','setDescricao','setTipo']
		return atribu

#######################################################

def obterColunas(con,obj):
	cursor = con.cursor()
	cursor.execute("SELECT * from "+obj)
	colunas = []
	for i in range(0, len(cursor.description)):
		colunas.append(cursor.description[i][0])
	cursor.close()
	con.close()
	return colunas

colunas=['codigo','nome']

def criarClasse(classe):
	teste = ("class "+classe+"(object):\n"
		 " def __init__(self,"+colunas[0]+"=None,"+colunas[1]+"=None):\n"
		  "  self."+colunas[0]+" = "+colunas[0]+"\n"
		  "  self."+colunas[1]+" = "+colunas[1]+"")
	exec(teste)
	return teste

def criarAtributos(colunas):
	for i in colunas:
		atributo = "  self."+str(i)+" = "+str(i)+"\n"
		atributo


init=" def __init__(self,"

def construtor_Init_(colunas):
	for i in colunas:
		atributo = "  self."+str(i)+" = "+str(i)+"\n"
		if(colunas[-1] == i):
			init = init + str(i) + "=None):\n"
		else: init = init + str(i) + "=None,"


def construtor_Init_(colunas):
	atributo=''
	init=" def __init__(self,"
	for i in colunas:
		atributo = atributo + "  self."+str(i)+" = "+str(i)+"\n"
		if(colunas[-1] ==i):
			init = init + str(i)+ "=None):\n"
			init = init + atributo
		else: init = init + str(i) + "=None,"
	return init


def get(colunas):
	get=''
	for i in colunas:
		if(colunas[-1]== i):
			get = get + " \ndef get"+ str(i)+"(self):\n"
		else:
			get = get + " def get"+ str(i)+"(self):\n"
		get = get + "  return self."+ str(i)
	return get


def sett(colunas):
	sett=''
	for i in colunas:
		if(colunas[-1]== i):
			sett = sett + " \ndef set"+ str(i)+"(self,"+str(i)+"):\n"
		else:
			sett = sett + " def set"+ str(i)+"(self,"+str(i)+"):\n"
		sett = sett + "  self."+ str(i) + " = " + str(i)
	return sett


def criarClasse(con,obj):
	cursor = con.cursor()
	cursor.execute("SELECT * from "+obj)
	coluna = []
	for i in range(0, len(cursor.description)):
		coluna.append(cursor.description[i][0])
	cursor.close()
	con.close()
	teste = "class "+obj+"(object):\n"
	atributo=' '
	init=" def __init__(self,"
	get=' '
	sett=' '
	for i in coluna:
		atributo = atributo + "	self."+str(i)+" = "+str(i)+"\n"
		if(coluna[-1] ==i):
			init = init + str(i)+ "=None):\n"
			init = init + atributo
			get = get + "def get"+ str(i)+"(self):\n  return self."+ str(i) + "\n"
			sett = sett + "def set"+ str(i)+"(self,"+str(i)+"):\n  self."+ str(i) + " = " + str(i) + "\n"
		else:
			init = init + str(i) + "=None,"
			get = get + "def get"+ str(i)+"(self):\n  return self."+ str(i) + "\n "
			sett = sett + "def set"+ str(i)+"(self,"+str(i)+"):\n   self."+ str(i) + " = " + str(i) + "\n "
	teste = teste + init + get + sett
	return teste
	
####################################################################################

def criarClasse(con,obj):
	try:
		cursor = con.cursor()
		cursor.execute("SELECT * from "+obj)
	except Exception, e:
		print str(e)
	teste = "class "+obj+"(object):\n"
	atributo=' '
	init=" def __init__(self,"
	get=' '
	sett=' '
	try:
		for i in range(0, len(cursor.description)):
			value = cursor.description[i][0]
			atributo = atributo + "	self."+str(value)+" = "+str(value)+"\n"
			ult = cursor.description[-1][0]
			if(ult == value):
				init = init + str(value)+ "=None):\n"
				init = init + atributo
				get = get + "def get"+ str(value)+"(self):\n  return self."+ str(value) + "\n"
				sett = sett + "def set"+ str(value)+"(self,"+str(value)+"):\n  self."+ str(value) + " = " + str(value) + "\n"
			else:
				init = init + str(value) + "=None,"
				get = get + "def get"+ str(value)+"(self):\n  return self."+ str(value) + "\n "
				sett = sett + "def set"+ str(value)+"(self,"+str(value)+"):\n   self."+ str(value) + " = " + str(value) + "\n "
		teste = teste + init + get + sett
	except Exception, e:
		print str(e)
	cursor.close()
	con.close()
	return teste
	
---------------------------------------------------------------------------------
exec(criarClasse(con(),"Contrato_Cap"))
for i in getObjetos(con(),"Contrato_Cap"):
	i.atributos()

	
def criarClasse(con,obj):
	try:
		cursor = con.cursor()
		cursor.execute("SELECT * from "+obj)
	except Exception, e:
		print str(e)
	teste = "class "+obj+"(object):\n"
	atributo=' '
	init=" def __init__(self,"
	atrib =" def atributos(self):\n  "
	atrib2=[]
	get=' '
	sett=' '
	try:
		for i in range(0, len(cursor.description)):
			value = cursor.description[i][0]
			tipo = str(cursor.description[i][1])
			atributo = atributo + "	self."+str(value)+" = "+str(value)+" # "+tipo+"\n"
			atrib2.append('set'+value)
			ult = cursor.description[-1][0]
			if(ult == value):
				init = init + str(value)+ "=None):\n"
				init = init + atributo
				get = get + "def get"+ str(value)+"(self):\n  return self."+ str(value) + "\n"
				sett = sett + "def set"+ str(value)+"(self,"+str(value)+"):\n  self."+ str(value) + " = " + str(value) + "\n"
			else:
				init = init + str(value) + "=None,"
				get = get + "def get"+ str(value)+"(self):\n  return self."+ str(value) + "\n "
				sett = sett + "def set"+ str(value)+"(self,"+str(value)+"):\n   self."+ str(value) + " = " + str(value) + "\n "
		atrib = atrib + 'return ' + str(atrib2)
		teste = teste + init + get + sett + atrib
	except Exception, e:
		print str(e)
	cursor.close()
	con.close()
	modulo = 'E:/magno/magno/Project_Test/D3/Model/'+obj+'.py'
	try:
		arquivo = open(modulo, 'w')
		arquivo.writelines(teste)
		arquivo.close
	except Exception, e:
		print str(e)
	return teste
	
-------------------------------------------------------------------------------------------

def _unicode(coluna):
	retorno = "  return u'{0}'.format(self."
	_unicode="def __unicode__(self):\n"
	_unicode= _unicode + retorno + coluna +")"
	return _unicode


------------------------------------------------------------------------------


def criarModel(obj):
	from django.db import models
	classe = "class "+obj+"("+str(models.Model) +"):\n"
	atributo=' '
	_unicode=" def __unicode__(self):\n"
	retorno = "  return u'{0}'.format(self."+atributos[1]+"):\n"
	for i in atributos:
		atributo = atributo + i + " = CharField(max_length=30)\n "
	classe = classe + atributo + _unicode + retorno
	return classe



