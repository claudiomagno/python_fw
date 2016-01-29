class Banco(object):
 def __init__(self,CD_BANCO=None,CD_PAIS=None,DC_BANCO=None,ID_BANCO_ERP=None):
 	self.CD_BANCO = CD_BANCO # <type 'cx_Oracle.STRING'>
	self.CD_PAIS = CD_PAIS # <type 'cx_Oracle.STRING'>
	self.DC_BANCO = DC_BANCO # <type 'cx_Oracle.STRING'>
	self.ID_BANCO_ERP = ID_BANCO_ERP # <type 'cx_Oracle.STRING'>
 def getCD_BANCO(self):
  return self.CD_BANCO
 def getCD_PAIS(self):
  return self.CD_PAIS
 def getDC_BANCO(self):
  return self.DC_BANCO
 def getID_BANCO_ERP(self):
  return self.ID_BANCO_ERP
 def setCD_BANCO(self,CD_BANCO):
   self.CD_BANCO = CD_BANCO
 def setCD_PAIS(self,CD_PAIS):
   self.CD_PAIS = CD_PAIS
 def setDC_BANCO(self,DC_BANCO):
   self.DC_BANCO = DC_BANCO
 def setID_BANCO_ERP(self,ID_BANCO_ERP):
  self.ID_BANCO_ERP = ID_BANCO_ERP
 def atributos(self):
  return ['setCD_BANCO', 'setCD_PAIS', 'setDC_BANCO', 'setID_BANCO_ERP']

