# hahahhahahaha
import subprocess
# os (operation system) ili tuwez kuingia kwa own system
import os
#user walishatiag password...connected wifi
username = os.getlogin() 
wifi_data = subprocess.check_output("netsh wlan show profiles", shell=True).decode("utf-8") 
wifi_data_to_str = wifi_data.split("\n") 
# profile set for usernames
profiles = [] 
# dictionary ni njia simple ya kupata hizo password kwa urahis
passwords = {}
#loop for username
for profile in wifi_data_to_str: 
    if "All User Profile" in profile:
         profile = profile.split(":")[1].strip() 
         profiles.append(profile)
    for profile in profiles:
        # try na except inatumika kwa erroe handling instead ya kuleta error inaleta specific input
        try:
             wifi_data_profile = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear', shell=True).decode("utf-8")
             wifi_data_profile_to_str = wifi_data_profile.split("\n")
             # if password not found
             password = "No password found" 
             for line in wifi_data_profile_to_str:
                 if "Key Content" in line: password = line.split(":")[1].strip() 
                 break 
             passwords[profile] = password 
        except subprocess.CalledProcessError: 
            # kama password ikigoma kuchukulika 
            passwords[profile] = "imegoma kupata"
             # Display connected username and Wi-Fi passwords 
            print(f"Logged in as: {username}") 
            print("\nWi-Fi Profiles and Passwords:") 
            for profile, password in passwords.items(): 
                print(f"Profile: {profile} | Password: {password}")