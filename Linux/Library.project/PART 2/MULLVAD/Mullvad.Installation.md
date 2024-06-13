
# Mullvad

This one actually gave me a headache 


mullvad: 
$ sudo apt-cache search mullvad

$ sudo apt install mullvad-vpn

to start mullvad: 
$ mullvad

if you're not usre where the executable is located, use which command: 
$ which mullvad

go to that directory and use same command to start mullvad



THIS DID NOT WORK....





wasn't able to download mullvad, After going in circles , did this: 

went to their website and ran the commands: 
https://mullvad.net/en/download/vpn/linux

$sudo curl -fsSLo /usr/share/keyrings/mullvad-keyring.asc https://repository.mullvad.net/deb/mullvad-keyring.asc


$echo "deb [signed-by=/usr/share/keyrings/mullvad-keyring.asc arch=$( dpkg --print-architecture )] https://repository.mullvad.net/deb/stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/mullvad.list


$sudo apt update
$sudo apt install mullvad-vpn




and it worked... :)