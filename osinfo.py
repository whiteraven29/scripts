import os
import platform

def get_os_info():
    # Get the current operating system
    current_os = platform.system()
    
    # Get the current logged in user
    if current_os == "Windows":
        logged_in_user = os.getlogin()
    else:
        logged_in_user = os.environ.get('USER') or os.environ.get('LOGNAME')

    return current_os, logged_in_user

if __name__ == "__main__":
    os_info = get_os_info()
    print(f"Operating System: {os_info[0]}")
    print(f"Logged-in User: {os_info[1]}")
