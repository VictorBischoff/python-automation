from ubuntu import start_ubuntu, stop_ubuntu
from fedora import start_fedora, stop_fedora
from debian import start_debian, stop_debian

while True:
    print("FEDORA")
    print("UBUNTU")
    print("DEBIAN")
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
            start_fedora()
            break
        if fedora_user_in == "stop":
            stop_fedora()
            break
        if fedora_user_in == "exit":
            break
        
    if user_in == "debian":
        
        print("START")
        print("STOP")
        print("EXIT")
        debian_user_in = input("CHOOSE OPTION:")
        debian_user_in = debian_user_in.strip().lower()
        
        
        if debian_user_in == "start":
            start_debian()
            break
        if debian_user_in == "stop":
            stop_debian()
            break
        if debian_user_in == "exit":
            break
        
    if user_in == "exit":
        break
    
    else:
        print("Invalid action")