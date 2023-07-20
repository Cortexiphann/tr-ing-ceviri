# Türkçe-İngilizce Çeviri Uygulaması

Bu Python programı, kullanıcının girdiği Türkçe metni İngilizce'ye çeviren basit bir Tkinter uygulamasını içermektedir.

## Kütüphaneler

Bu proje, `tkinter` ve `translate` kütüphanelerini kullanmaktadır. Eğer bu kütüphaneler daha önceden yüklü değilse, aşağıdaki adımları takip ederek kurulumunu gerçekleştirebilirsiniz:

1. `tkinter` kütüphanesi, Python'ın standart kütüphanelerinden biridir ve genellikle Python kurulumuyla birlikte gelir. Bu nedenle, ayrıca kurulum yapmanıza gerek yoktur.

2. `translate` kütüphanesini ise pip paket yöneticisi ile kurabilirsiniz. Aşağıdaki komutu kullanarak `translate` kütüphanesini kurabilirsiniz:

pip install translate

## Nasıl Çalışır?

1. `translate_text()` fonksiyonu, kullanıcının girdiği Türkçe metni İngilizce'ye çevirir.
2. Çeviri işlemi için `translate` kütüphanesinden `Translator` sınıfı kullanılır.
3. Kullanıcıdan alınan metin, `Translator` sınıfı ile Türkçe'den İngilizce'ye çevrilir.
4. Çevrilen metin, ekrana yazdırılır.

## Kullanım

Program çalıştırıldığında, kullanıcıdan bir Türkçe metin girmesi istenir. Ardından, metin İngilizce'ye çevrilir ve çevrilen metin ekrana yazdırılır.


