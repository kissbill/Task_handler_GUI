cls - clear terminal

cd Desktop

cd . .

git init 

Initialized empty Git repository in C:/Users/hanokri/Desktop/SFJ_GIT/.git/

git status 
	ha tobb git folder is van
	amelyikben benne vagy azt fogja reportalni

git add test.txt

git commit -m "hozzaadtam a file-t"

git add *.txt 

git log

commit fe1b48fbe19ba8c3b7f6f2d57975fb334b10a6e3 (HEAD -> master)
Author: kissbill <milerik@hotmail.com>
Date:   Sat Apr 13 17:05:13 2019 +0200

    onn the way


//origin itt alias , Tamas[oregharcos] es hozzaadjuk a serverhez a helyi repot
git remote add origin
// en itt rossz repot adtam neki, ezzel szedtem le a remote origin alias-t 
git remove origin

// -u jegyezd meg, ha pusholok akkor az origin mastert fogja jelenteni -> git push kell mar ezutan
git push -u origin master


$ git config --global user.email
milerik@hotmail.com

$ git config --global user.name
kissbill

$ git config --global user.email "milerik@hotmail.com"
$ git config --global user.name	"kissbill"

//feltolom a masterre a lokalis desktoprol az anyagot
git push origin master

//ha nem akar pullolni a serverrol
git pull origin master --allow-unrelated-histories
------------------------------------------------------------
//letre hozok egy helyi repot 
git ini 
//es a helyi repohoz hozza kapcsolom
git remote add origin http://

EHELYETT CLONE:
git clone https://github.com/kissbill/magyar_test.git
------------------------------------------------------------
//a legutolso kommit ota mi valtozott
//HEAD az az allapot ahol minden szepen fel volt kommitolva
git diff HEAD

// adott file-ban mi valtozott
//piros torolve
//zold hozzaadva
git diff test.txt

//azokat mutatja amik a szinpadon mar fent vannak, commitolva
git diff --staged

//leveszi a szinapadrol, de megmarad a valtoztatas
git reset test.txt

//teljesen el akarom vetni
git checkout -- test.txt

//felkuldesz egy mappat szinpadra de egyet nem akarsz, akkor ez arra jo RESET
------------------------------------------------------------
BRANCH
//uj branch letre hozasa
git branch clean up
//ki is csekkolja
git checkout -b [yourbranchname]
//milyen branch-en vagy
git branch
  clean_up
* master
//lokal es remote branch-ek
git branch -a
//atvaltani 
git checkout clean_up

//torolni a clean_up-rol , most a szinpadra felloktok h ezek a file-ok ne letezzenek
git rm '*.txt'
//most ez commitoljuk, fel a szinpadra
git commmit
//viszont most vissza a master branch-re
git checkout master
//most pedig hozzafesuljuk a clean_up branch-et
git merge clean_up
//a masterrol is letunt a file-ok

//branch torles
 git branch -d clean_up

//utana mindent amit csinaltam, fel push-olom
git push 