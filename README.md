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
* Technopat
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
# License

Copyright (c) 2023, Şuayip Üzülmez, and contributors

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
