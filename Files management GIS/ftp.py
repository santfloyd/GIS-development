# -*- coding: utf-8 -*-
"""
Created on Fri May 11 15:21:42 2018

@author: ASUS
"""

#import modulos
import ftplib
import os
import socket
#crear variables pora el host, directorio, y fichero
#hay que conocerlos de antemano
HOST = 'ftp.geodesia.ign.es'
DIRN = '/Red_Geodesica/Hoja0964/'

FILE = '096497.pdf'
#○abrir conexion al servidor ftp para descarga
try:
    f=ftplib.FTP(HOST)
except (socket.error, socket.gaierror),e:
    print 'error: "%s"' % HOST
print '*** connected to host "%s"' % HOST

#login al server que acepta acceso anonimo pero de no hacerlo usar username y pass como argumentos
try:
    f=ftplib.FTP(HOST)
    f.login()
except ftplib.error_perm:
    print 'error cannot login anonymously'
print '*** logged in as "anonymous"'
#cambiar el directorio a la ubicacion
try:
    f.cwd(DIRN)
except ftplib.error_perm:
    print 'error: "%s"' % DIRN
    f.quit()
print '*** change to "%s"'  % DIRN

#recuperar archivo
try:
    f.retrbinary('RETR %s' % FILE, open(FILE,'wb').write)
except ftplib.error_perm:
    print 'error: "%s"' % FILE
    os.unlink(FILE)
else:
    print '*** downloaded "%s" to cwd' % FILE
#DESCONECTARSE
f.quit()