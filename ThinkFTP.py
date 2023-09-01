#!/usr/bin/env python3

"""
Descriere:
Acest script se conectează la un server FTP și încarcă fișierele specificate într-un director specific pe server.

Instrucțiuni de utilizare:
1. Asigură-te că ai Python 3 instalat pe sistemul tău. Dacă nu, poți instala Python 3 cu comanda:
sudo pacman -S python
2. Salvează acest script cu un nume relevant, cum ar fi `ThinkFTP.py`.
3. Deschide un terminal și navighează către directorul în care ai salvat scriptul.
4. Rulează scriptul folosind Python 3. Dacă ai numit scriptul `ThinkFTP.py`, rulează comanda:
python3 ThinkFTP.py -v
5. Scriptul se va conecta la serverul FTP și va încărca fișierele specificate în directorul specificat pe server. Opțiunea `-v` va afișa mesaje detaliate pe parcurs.
6. Asigură-te că ai permisiunile adecvate pentru fișierele pe care dorești să le încarci și că ai introdus corect detaliile serverului FTP (adresă, nume utilizator, parolă) în script.

Pentru întrebări sau ajutor suplimentar, consultă documentația Python sau secțiunea de ajutor a scriptului.

Autor: ThinkRoot99
"""

from ftplib import FTP

def upload_files(hostname, username, password, remote_directory, files):
 try:
     with FTP(hostname) as ftp:
         print(f"Conectare la {hostname}...")
         ftp.login(username, password)
         
         ftp.cwd(remote_directory)
         
         for file_path in files:
             with open(file_path, 'rb') as file:
                 remote_filename = file_path.split("/")[-1]
                 print(f"Se încarcă '{remote_filename}'...")
                 ftp.storbinary('STOR ' + remote_filename, file)
                 print(f"File '{remote_filename}' încărcat cu succes.")
         
         print("Încărcare finalizată.")
                 
 except Exception as e:
     print(f"O eroare a apărut: {str(e)}")

if __name__ == "__main__":
 parser = argparse.ArgumentParser(description="Script pentru încărcare FTP")
 parser.add_argument("-v", "--verbose", action="store_true", help="Afișează mesaje detaliate")
 args = parser.parse_args()

 ftp_hostname = "adresa_ftp_server"
 ftp_username = "nume_utilizator"
 ftp_password = "parola_utilizator"
 remote_dir = "/cale/catre/director/pe/ftp"
 files_to_upload = ["fisier1.txt", "fisier2.txt"]
 
 upload_files(ftp_hostname, ftp_username, ftp_password, remote_dir, files_to_upload)
