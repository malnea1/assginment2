import sys
import os.path
import crypt


def getArguments():
   return sys.argv[1], sys.argv[2]

def openFile(filename):
   if os.path.isfile(filename):
      if os.access(filename, os.R_OK):
         return open(filename, 'r')
      else:
         sys.exit("File not found.")

def crack(hash, dictPath, ctype, salt):
   insalt = '${}${}$'.format(ctype, salt)

   dict = openFile(dictPath)

   for password in dict:
      if crypt.crypt(password.strip(), insalt) == hash:
         sys.exit("Found password:" + password)
   sys.exit("Password not found in dictionary.")

def getPassword(user, shadow):
   for line in shadow:
      line = line.split(":")

      if line[0] == user:
         if line[1] == "*":
            sys.exit("user does not have a password.")
         else:
            return line[1]
   sys.exit("no user found.")


if len(sys.argv) < 3:
   sys.exit("Error")
else:
   user, shadowfile = getArguments()

   dictPath = "./dictionary.txt"

   if len(sys.argv) > 3:
      if sys.argv[3] == "-d" and len(sys.argv) > 4:
         dictPath = sys.argv[4]
      else:
         sys.exit("Invalid Arguments.")

   shadow = openFile(shadowfile)
   hash = getPassword(user, shadow)
   enc = hash.split("$")
   ctype = enc[1]
   salt = enc[2]
   insalt = '${}${}$'.format(ctype, salt)
   crack(hash, dictPath, ctype, salt)
