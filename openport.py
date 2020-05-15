#-*-coding: utf-8-*-
import socket
import sys
print """
#################################################
# OpenPort v1.0 by: Renegado                    #
# email: thebinaryman@protonmail.com            #
#################################################
"""
def help():
  print """
  Ajuda do OpenPort:
  o openport tem 2 modos de funcionamento
  automatico e manual, exemplo de uso:
  openport --manual --tcp 127.0.0.1 22
  no exemplo acima, o scan será feito na porta 22 ssh no modo manual (apenas
  uma porta) no protocolo tcp
  vc pode usar de modo manual, exemplo:
  openport --tcp --auto 127.0.0.1 21 22
  no exemplo acima, o scan sera feito entre as portas 21 e 22 (ftp e ssh)
  no modo tcp.
  vc pode usar --udp no lugar do --tcp para um scan em portas udp.
  openport possue 2 estados on e off
  onde on significa aberto e off fechado.
  """
if sys.argv[1] == "--tcp":
  if sys.argv[2] == "--manual":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scan = sock.connect_ex((sys.argv[3], int(sys.argv[4])))
    if scan == 0:
      print "Porta %d on" %int(sys.argv[4])
    else:
      print "Porta %d off" %int(sys.argv[4])
  elif sys.argv[2] == "--auto":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    inp = int(sys.argv[5]) + 1
    for out in range(int(sys.argv[4]), inp):
      scan = sock.connect_ex((sys.argv[3], int(out)))
      if  scan == 0:
        print "Porta %d on" %int(out)
      else:
        print "Porta %d off" %int(out)
elif sys.argv[1] == "--udp":
  if sys.argv[2] == "--manual":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    scan = sock.connect_ex((sys.argv[3], int(sys.argv[4])))
    if scan == 0:
      print "Porta %d on" %int(sys.argv[4])
    else:
      print "Porta %d off" %int(sys.argv[4])
  elif sys.argv[2] == "--auto":
    inp = sys.argv[5] + 1
    for out in range(int(sys.argv[4]), int(inp)):
      scan = sock.connect_ex((sys.argv[3], int(out)))
      if  scan == 0:
        print "Porta %d on" %int(out)
      else:
        print "Porta %d off" %int(out)
elif sys.argv[1] == "-h":
  help()
else:
  print "-h para ajuda"
