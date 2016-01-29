class Dominio(object):
 def __init__(self,CD_REFERENCIA=None,CD_DOMINIO=None,DC_DOMINIO=None):
 	self.CD_REFERENCIA = CD_REFERENCIA
	self.CD_DOMINIO = CD_DOMINIO
	self.DC_DOMINIO = DC_DOMINIO
 def getCD_REFERENCIA(self):
  return self.CD_REFERENCIA
 def getCD_DOMINIO(self):
  return self.CD_DOMINIO
 def getDC_DOMINIO(self):
  return self.DC_DOMINIO
 def setCD_REFERENCIA(self,CD_REFERENCIA):
   self.CD_REFERENCIA = CD_REFERENCIA
 def setCD_DOMINIO(self,CD_DOMINIO):
   self.CD_DOMINIO = CD_DOMINIO
 def setDC_DOMINIO(self,DC_DOMINIO):
  self.DC_DOMINIO = DC_DOMINIO
 def atributos(self):
  return ['setCD_REFERENCIA', 'setCD_DOMINIO', 'setDC_DOMINIO']