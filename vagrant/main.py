from debian import stop_debian, start_debian
from ubuntu import stop_ubuntu, start_ubuntu
from fedora import stop_fedora, start_fedora

vm_functions = {
    "ubuntu": {
        "start": start_ubuntu,
        "stop": stop_ubuntu
    },
    "fedora": {
        "start": start_fedora,
        "stop": stop_fedora
    },
    "debian": {
        "start": start_debian,
        "stop": stop_debian
    }
}
def main():
    while True:
        vm = input("Choose a VM (ubuntu, fedora, debian, or exit): ").strip().lower()
        
        if vm == "exit":
            break
        
        if vm in vm_functions:
            action = input("Choose an action (start or stop): ").strip().lower()
            
            if action in vm_functions[vm]:
                vm_functions[vm][action]()
            else:
                print("Invalid action")
        else:
            print("Invalid VM")

if __name__ == "__main__":
    main()

