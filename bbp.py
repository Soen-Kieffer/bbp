#bubble py V.1.0

import os
from pty import slave_open
import webbrowser
'''
import subprocesss
'''
import webbrowser
re="y"
print("Bubble py FR v.1.0")
print("type <info> and <help> for more information")
print("type <maj> for update's search")

opening = open("data/open.bbp", "r")
if opening.read() == "n":
    name = input("def user name>>>")
    fichier = open("data/name.bbp", "r+")
    fichier.write(name)
    fichier.close()
    mdp = input("def password>>>")
    fichier2 = open("data/password.bbp", "w")
    fichier2.write(mdp)
    fichier2.close()
else :
    print("veuiller vous idetifier:")
    fichier = open("data/name.bbp", "r+")
    namev = fichier.read()
    name = input("User name>>>")
    fichier.close()
    if name==namev:
        fichier = open("data/password.bbp", "r+")
        pwv = fichier.read()
        pw = input("Password>>>")
        fichier.close()
        if pw==pwv :
            print("identification reusie!")
        else:
            print("Password false")
            quit()
    else :
        print("User name false")
        quit()
    
    
opening.close()
fichier = open("data/open.bbp", "w")
fichier.write("y")
fichier.close()
namef = open("data/name.bbp", "r")
name = namef.read()
fichier.close()
#debut du programe
print("bubble py BÊTA")
print("bonjour "+name)
while re=="y":
    cmd = input(">>>")
    if cmd == "reset":
        print("attention vous aller suprimer tout les donné de ce programme")
        yn = input("[y/n/s>")
        if yn=="y" :
            fichier = open("data/open.bbp", "w")
            fichier.write("n")
            fichier.close()
            fichier = open("data/name.bbp", "w")
            fichier.write("")
            fichier.close()
            fichier = open("data/password.bbp", "w")
            fichier.write("")
            fichier.close()
            os.system("restart.py")
            quit()
        if yn=="s":
            fichier = open("data/open.bbp", "w")
            fichier.write("n")
            fichier.close()
            fichier = open("data/name.bbp", "w")
            fichier.write("")
            fichier.close()
            fichier = open("data/password.bbp", "w")
            fichier.write("")
            fichier.close()
            quit()
        else :
            print("annulation")
    if cmd == "quit":
        quit()
    elif cmd =="pycmd":
        pycmd = input("py>>>")
        pycmd
    elif cmd =="script":
        print("")
    elif cmd =="settings":
        print("""
       Bubble py settings v1.0
       -Enter "password" to modify the root password""")
        settings = input("settings>>")
        if settings =="password":
              oldpassword=open("data/password.bbp", "r")
              oldpasswordr=oldpassword.read()
              opw = input("old password>>")
              if opw==oldpasswordr:
                  print("ok")
                  newpassword = open("data/password.bbp", "w")
                  npw = input("new password>>")
                  newpassword.write(npw)
                  newpassword.close()
                  print("mdp modifié !")
    elif cmd=="info":
        print("Bubble py version beta 1.0")
        print("©Bubble py 2021")
        print("devlopé par Soen Kieffer en 2021")
        print("nous sommes très heureux que vous utilise bubble py")
        print("Thank you !")
        print("👍")
    elif cmd=="maj":
        print("Recherche de Mise A Jour")
        maj = open("data/maj/maj.bbp")
        if maj.read() == "y":
            print("une mise à jour est disponible")
            print("voulez vous l'installer (y/n)")
            yn=input("yn>>>")
            if yn=="y":
                from data.maj.maj import DoMaj
                DoMaj()
        else :
            print("occune mise à jour n'est dissponile.")
        print("")
    elif cmd=="restart":
        os.system("restart.py")
        quit()
    elif cmd=="python info":
        print("quelques infos sur python:")
    elif cmd=="help":
        import webbrowser
    else :
        '''if os.path.exists("newcmd/new.py") == True:
            os.'''
        print("commande inconue")
