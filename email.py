import sys
import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.message
expmail = input("votre adresse mail ")
mdp=input("nvotre mot de passe")
destmail = input("mail du destinataire")
objet = input("objet du mail")
contenu = input("contenu du mail(deux espace pour sauter une ligne)").replace('  ','<br>')
message=contenu.replace('<br>','n')

print(message)


if input("envoyer ? (O/N)")=="O"or"o":
    msg = email.message.Message()

    msg.add_header('Content-Type','text/html')
    msg.set_payload('{}'.format(contenu,))

    s = smtplib.SMTP('smtp.gmail.com',587)

    s.starttls()

    try:
        s.login(destmail,
            mdp)

        s.sendmail(expmail, destmail, msg.as_string())

        s.quit()
        print('nnnnmessage envoyer avec succés')
    except:
        print("nnnnERREUR: mauvais mail ou mot de passe nsinon allez sur [https://myaccount.google.com/lesssecureapps] et activer l'option" )
else:
    sys.exit()
