# yoklama

This is a mini OSINT tool that checks for usernames in Turkish social media
websites. Currently, these websites are tracked:

* DergiPark
* DonanımHaber Forum
* Ekşi Sözlük
* Evrim Ağacı
* İnci Sözlük
* İnstela
* Kızlar Soruyor
* Memurlar.net (sozluk.memurlar.net)
* Onedio
* Shiftdelete.Net Forum
* Techopat
* Teknoseyir
* Uludağ Sözlük

**If you want some other site to added, please [create a new issue](https://github.com/realsuayip/yoklama/issues/new).**

## Usage

This repo requires Python (at least 3.11). Optinally use a virtual environment
to isolate dependencies of this script.

Clone the repo:

```shell
git clone https://github.com/realsuayip/yoklama
```

In project root, run this command to install dependencies:

```shell
pip install .
```

Run the script:

```shell
python run.py 'username'
```

Example usages:

```shell
$ python run.py 'Cem Yılmaz'
Received: 'Cem Yılmaz'
donanimhaber.com — https://forum.donanimhaber.com/profil/79036
sozluk.memurlar.net — https://sozluk.memurlar.net/yazar/cem-yilmaz/
technopat.net — https://www.technopat.net/sosyal/uye/cem-yilmaz.88699/
```

```shell
$ python run.py 'cemyilmaz'
Received: 'cemyilmaz'
donanimhaber.com — https://forum.donanimhaber.com/profil/1108050
incisozluk.com.tr — http://www.incisozluk.com.tr/u/cemyilmaz/
kizlarsoruyor.com — https://www.kizlarsoruyor.com/uye/cemyilmaz
sozluk.memurlar.net — https://sozluk.memurlar.net/yazar/cemyilmaz/
eksisozluk.com — https://eksisozluk111.com/biri/cemyilmaz
onedio.com — https://onedio.com/profil/cemyilmaz
dergipark.com — https://dergipark.org.tr/tr/pub/@cemyilmaz
technopat.net — https://www.technopat.net/sosyal/uye/cemyilmaz.438517/
shiftdelete.net — https://forum.shiftdelete.net/members/cemyilmaz.31972/
```
