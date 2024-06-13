
# Powershell CLI



## Century 2

`$PSVersion`
Build version:
10.0.14393.5582


## Century 3
`Invoke-WebRequest`
`ls`

invoke-Webrequest443


## Century 4

`(Get-ChildItem -File).Count`
123


## Century 5
`ls`
`cd "Can You Open Me"`

34182

## Century 6
`ls`

3347


` $Domain = Get-WmiObject Win32_ComputerSystem | Select-Object -ExpandProperty Domain `
` $Domain`

underthewire.tech

--> is the domain name, but not the short domain name, try again.

` Get-WmiObject -Class Win32_NTDomain`

so it'll be

 underthewire3347

 ## Century 7

ezzzzz
`(Get-ChildItem -Directory).Count`
197


## Century 8

`Get-ChildItem -Path C:\users\century7 *readme* -Recurse -ErrorAction SilentlyContinue `

Directory = C:\users\century7\Downloads

`cd C:\users\century7\Downloads`
`Get-Content Readme.txt`

7points


## Century 9

`ls`
--> unique.txt

`$password = (Get-Content -Path ".\unique.txt" | Select-Object -Unique | Measure-Object).Count`

` Write-Output "Bro you finally found the passw: $password" `

696

## Century 10

hay ma kanet 7elwe sara7a`
`ls`
-> Word_File.txt

`$word = (Get-Content -Path .\Word_File.txt -Raw | Select-String -Pattern '\b\w+\b' -AllMatches).Matches[160].Value`

`$word`

-> pierid


## Century 11

`ls`

-> 110


Get the description of the Windows Update service:
`$serviceDescription = (Get-WmiObject -Class Win32_Service -Filter "Name='wuauserv'").Description` 

Extract the words:
`$words = $serviceDescription -split '\s+'`

Get the 8th and 10th words:
`$eighthWord = $words[7]`
`$tenthWord = $words[9]`

Display the words:
`$eighthWord`
`$tenthWord`

= updates
= Windows

so:
windowsupdates110

## Century 12

`cd ../`
`cd Downloads`

`Get-ChildItem -Force`

hidden file: 
Secret_sauce

## Century 13

`ls`

file : _things

`Get-AdDomainController`
Name: UTW

`Get-ADComputer -Properties Description -Filter 'Name -like "UTW"'`

Description: i_authenticate

password: 
i_authenticate_things


## Century 14

Replace "filename.txt" with the name of your file:
`$fileContent = Get-Content -Path "filename.txt" -Raw`

Split the content into words:
`$words = $fileContent -split '\s+'`

Count the number of words:      
`$wordCount = $words.Count`

Display the word count:
`$wordCount`

= 755


## Century 15

Read the content of the file:
`$fileContent = Get-Content -Path .\countpolos -Raw`

Count the occurrences of the word "polo":
`$poloCount = ($fileContent -split '\W' | Where-Object { $_ -eq 'polo' }).Count`

Display the password:
`$poloCount`

=153


