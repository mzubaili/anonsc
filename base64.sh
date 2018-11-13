#!/bin/bash
## tools base64
## author: AnonyMass aka Zhu Bai Lee
## nama author jangan di ganti ya palgiaters
## ingat bro/sis plagiat itu cuma orang2 yg gk punya kreativitas :v
## quotes gue juga jangan lu plagiatin juga -_-

#configuration tools
again='y'
while  [ $again == 'y' ] || [ $again == 'Y' ];
do

trap ctrl_c INT
ctrl_c() {
clear
toilet -f slant --metal THANK YOU
exit
}

clear
echo -n -e """\033[31;2m
000000000   000000000   0000000000  00000000000
00    0000  00     00   00      00  00       00
00    0000  00     00   00     0000 00      0000
000000000   000000000   00          00  0
00000000    00     00   0000000000  00000
00    0000  00     00           00  00  0
00    0000  00     00  0000     00  00      0000
00    0000  00     00   00      00  00       00
000000000  0000   0000  0000000000  00000000000 \033[37;3m

           6666666666       44
           66      66      44   44
           66     6666    44    44
           66            44     44
           6666666666   4444444444
           66      66           44
           66      66           44
           66      66           44
           6666666666          4444
"""

echo -n -e "\n\033[32;1mAuthor : ""\033[33;2mAnonyMass aka Zhu Bai Lee"
echo -n -e "\n\033[32;1mGithub : ""\033[33;2mhttps://github.com/mzubaili"
echo -n -e "\n\033[32;1mContact: ""\033[33;2m082215885532""\033[0m""\033[0m"
echo -n -e "\n\033[31;1m+++++++++++++++++++++++++++++++++++++++++++++++++++""\033[0m"

echo -n -e """
[1]               UPDATE TOOLS                  [1]
[2]          UBAH ISI FILE JADI BASE64          [2]
[3]          TRANSLATE ISI FILE BASE64          [3]
[4]            UBAH TEXT JADI BASE64            [4]
[5]            TRANSLATE TEXT BASE64            [5]
[6]             BUAT FILE BASE64                [6]
[7]        BUAT FILE TRANSLATE BASE64           [7]
[8]                  CREDITS                    [8]
[0]                   EXIT                      [0]
""" | lolcat -d 4 -8 
echo -n -e "\033[31;1m+++++++++++++++++++++++++++++++++++++++++++++++++++""\033[0m"
echo -n -e "\n\033[31;1m╭─""\033[37;1mAnonyMass""\033[0m"
echo -n -e "\n\033[31;1m╰─▶""\033[37;1m "
read a

if test $a == '1'
then
clear
pkg update && pkg upgrade
pkg install git
pkg install figlet
pkg install toilet
pkg install python2
pip install --upgrade pip
pip2 install lolcat
git clone https://github.com/mzubaili/base64
cd base64
chmod +x base64.sh
bash base64

elif test $a == '2' 
then 
clear 
read -p "masukkan nama file(ex:/storage/sdcard0/index.html)>> " sc;
echo -e "\033[31;1m"
cat $sc | base64
echo -e "\033[0m"

elif test $a == '3'
then
clear
read -p "masukkan nama file(ex:/storage/sdcard0/index.html)>> " sc;
echo -e "\033[31;1m"
cat $sc | base64 -d
echo -e "\033[0m"

elif test $a == '4'
then
clear
read -p "masukkan teks>> " tx;
echo -e "\033[31;1m"
echo $tx | base64
echo -e "\033[0m"

elif test $a == '5'
then
clear
read -p "masukkan teks>> " tx;
echo -e "\033[31;1m"
echo $tx | base64 -d
echo -e "\033[0m"

elif test $a == '8'
then
clear
toilet -f slant --metal spesial thank
echo -n -e """
ALLAH SUBHANAHUWATA'ALA
+++++++++++++++++++++++++++++++++++++++++
[APRILI][KITTKAT][LAKS KAPT][MICRO CLONE]
[WHITE SYSTEM][X3nx3][YUAN SANDRA]
+++++++++++++++++++++++++++++++++++++++++
""" | lolcat -d 3 -8 -a
sleep 4

elif test $a == '6'
then
clear
read -p "masukkan nama file(ex: /storage/sdcard/contoh.html>> " sc;
cat $sc | base64 >> $sc.txt
echo "keluar dari tools ini"
echo "lalu ketik cat nama file yg kalian ubah ke base64 tadi"
echo "contoh cat contoh.html.txt"

elif test $a == '7'
then
clear
read -p "masukkan nama file(ex: /storage/sdcard0/contoh.html>> " sc;
cat $sc | base64 -d >> $sc.txt
echo "keluar dari tools ini"
echo "lalu ketik cat nama file yg kalian translate tadi"
echo "contoh cat contoh.html.txt"

elif test $a == '0'
then
clear
toilet -f slant --metal THANK YOU
exit
fi

echo
echo -e -n $white "Apakah anda ingin kembali ke menu utama? (y/n): ";
read again;

    while  [ $again != 'y' ] && [ $again != 'Y' ] && [ $again != 'n' ] && [ $again != 'N'];
    do
   echo -n "Apakah anda ingin kembali ke menu utama? (y/n): ";
       read again;
    done

done