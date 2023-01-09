from ubuntu import start_ubuntu, stop_ubuntu
from fedora import start_fedora, stop_fedora

while True:
    print("FEDORA")
    print("UBUNTU")
    print("EXIT")
    user_in = input("CHOOSE VM: ")
    user_in = user_in.strip().lower()
    
    if user_in == "ubuntu":
        
        print("START")
        print("STOP")
        print("EXIT")
        ubuntu_user_in = input("CHOOSE OPTION:")
        ubuntu_user_in = ubuntu_user_in.strip().lower()
        
        if ubuntu_user_in == "start":
            start_ubuntu()
            break
        if ubuntu_user_in == "stop":
            stop_ubuntu()
            break
        if ubuntu_user_in == "exit":
            break
    
    if user_in == "fedora":
        
        print("START")
        print("STOP")
        print("EXIT")
        fedora_user_in = input("CHOOSE OPTION:")
        fedora_user_in = fedora_user_in.strip().lower()
        
        
        if fedora_user_in == "start":
            stop_fedora()
            break
        if fedora_user_in == "stop":
            stop_fedora()
            break
        if fedora_user_in == "exit":
            break
    if user_in == "exit":
        break
    
    else:
        print("Invalid action")