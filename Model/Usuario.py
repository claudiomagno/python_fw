class Usuario(object):
 def __init__(self,CD_USUARIO=None,NR_IDENTIFICADOR=None,NM_USUARIO=None,NM_APELIDO=None,CD_LOGIN=None,DC_SENHA=None,FL_STATUS=None,DC_EMAIL=None,DT_EXPIRA_SENHA=None):
 	self.CD_USUARIO = CD_USUARIO
	self.NR_IDENTIFICADOR = NR_IDENTIFICADOR
	self.NM_USUARIO = NM_USUARIO
	self.NM_APELIDO = NM_APELIDO
	self.CD_LOGIN = CD_LOGIN
	self.DC_SENHA = DC_SENHA
	self.FL_STATUS = FL_STATUS
	self.DC_EMAIL = DC_EMAIL
	self.DT_EXPIRA_SENHA = DT_EXPIRA_SENHA
 def getCD_USUARIO(self):
  return self.CD_USUARIO
 def getNR_IDENTIFICADOR(self):
  return self.NR_IDENTIFICADOR
 def getNM_USUARIO(self):
  return self.NM_USUARIO
 def getNM_APELIDO(self):
  return self.NM_APELIDO
 def getCD_LOGIN(self):
  return self.CD_LOGIN
 def getDC_SENHA(self):
  return self.DC_SENHA
 def getFL_STATUS(self):
  return self.FL_STATUS
 def getDC_EMAIL(self):
  return self.DC_EMAIL
 def getDT_EXPIRA_SENHA(self):
  return self.DT_EXPIRA_SENHA
 def setCD_USUARIO(self,CD_USUARIO):
   self.CD_USUARIO = CD_USUARIO
 def setNR_IDENTIFICADOR(self,NR_IDENTIFICADOR):
   self.NR_IDENTIFICADOR = NR_IDENTIFICADOR
 def setNM_USUARIO(self,NM_USUARIO):
   self.NM_USUARIO = NM_USUARIO
 def setNM_APELIDO(self,NM_APELIDO):
   self.NM_APELIDO = NM_APELIDO
 def setCD_LOGIN(self,CD_LOGIN):
   self.CD_LOGIN = CD_LOGIN
 def setDC_SENHA(self,DC_SENHA):
   self.DC_SENHA = DC_SENHA
 def setFL_STATUS(self,FL_STATUS):
   self.FL_STATUS = FL_STATUS
 def setDC_EMAIL(self,DC_EMAIL):
   self.DC_EMAIL = DC_EMAIL
 def setDT_EXPIRA_SENHA(self,DT_EXPIRA_SENHA):
  self.DT_EXPIRA_SENHA = DT_EXPIRA_SENHA
 def atributos(self):
  return ['setCD_USUARIO', 'setNR_IDENTIFICADOR', 'setNM_USUARIO', 'setNM_APELIDO', 'setCD_LOGIN', 'setDC_SENHA', 'setFL_STATUS', 'setDC_EMAIL', 'setDT_EXPIRA_SENHA']