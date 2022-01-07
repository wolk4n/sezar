# Sezar Şifrelemesi
Sezar şifrelemesi, ilk kez Romalı lider Jül Sezar tarafından kullanılmış olan şifreleme tekniğidir. Bu şifreleme en basit ve en bilinen şifreleme tekniklerinden biridir. Düz metindeki her harfin, alfabeden belirli bir sayı ileride konumlu olan bir harfle değiştirildiği bir şifreleme türüdür. Sezar şifresi kolayca kırılabilir ve modern uygulamada hiçbir iletişim güvenliği sağlamaz. Sezar şifrelemesinin matematiksel formulü <strong>E(x,K) = (x+K) mod 26</strong> ve çözmek için tam tersi <strong>E(x,K) = (x-K) mod 26</strong> formulü kullanılır. K değeri alfabenin kaydırma sayısıdır. Genellikle kaydırma sayısı 3'dür ve programda buna göre yazılmıştır.

Kaba kuvvet (brute-force) saldırısıyla çok kolay çözülür. Çünkü Şifreleme/Şifre çözme yöntemi gizli değildir.
Sadece 25 farklı deneme yeterlidir. (Anahtar uzayı 25 elemanlıdır.)
Düz metin (plaintext) ve formatı gizli değildir.

## Program İndirilmesi & Çalıştırılması
`git clone https://github.com/wolkann/sezar/`<br>
`python3 sezar.py`

## Program Arayüz
Programı çalıştırdıktan sonra karşınıza gelen seçeneklerden ilerleyebilirsiniz.<br>
<img src="/img/arauz.png"/>

## Sezar Şifresi Oluşturma
Sezar şifresi oluşturmak istediğiniz herhangi bir kelime yazmalısınız ve tüm harfleri küçük olmak zorundadır.
<img src="/img/1.png"/>

## Sezar Şifresi Kırma
Kırmak istediğiniz sezar şifresini küçük harfler ile yazıyorsunuz ve şifre kolay bir şekilde kırılmış oluyor.
<img src="/img/2.png"/>
