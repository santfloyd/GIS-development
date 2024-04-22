# -*- coding: utf-8 -*-
"""
Created on Fri May 11 13:42:47 2018

@author: ASUS
"""

#importar los modulos para adjuntar, i entre carpetas, etc
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
#username y pass asignados a variables
gmail_user='santfloyd@gmail.com'
gmail_pwd='1018451218'
#crear una fucnión que acepte 4 parametros
def mail(to,subject,text,attach):
    #crear un MIMEMultipart object y asignar los parametros a las keys
    msg=MIMEMultipart()
    msg['From']=gmail_user
    msg['To']=to
    msg['Subject']=subject
    msg.attach(MIMEText(text))
    #adjuntar
    part=MIMEBase('application','octet_stream')
    part.set_payload(open(attach,'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment;filename="%s"' % os.path.basename(attach))
    msg.attach(part)
    #crear un objeto SMTP que referencia google mail service y pasa username y pass, envia mail, y cierra conexion
    mailServer=smtplib.SMTP("smtp.gmail.com",465)
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()
#llamar la funcion
mail("santfloyd@gmail.com", "Hello Santiago", "Este es un ejercicio del curso python GIS", "bc_pop1996.csv")