# Otoparktaki Bos Yerleri Sayan Dedektor

# 1. Giriş

## 1.1. Projenin Altyapısı

Proje Python dilini kullanarak OpenCV, numpy ve Pickle kütüphaneleri ile Spyder IDE kullanılarak oluşturulmuştur.

## 1.2 Projenin Amacı

Otoparktaki park yeri bulma sorunlarından dolayı geliştirmekte olduğumuz bu proje ile bunun önüne geçilmesi planlanmaktadır. Araç sürücüleri boş alan bulamadıklarından dolayı otopark içerisinde
yoğunluk olmaktadır. Bu proje sayesinde araç sahiplerine boş alanları bildirerek bu yoğunluğu azaltmak amaçlanmıştır.

## 1.3 Projenin Kullanım Alanları

Projenin ana kullanım amacı otoparklar ve park alanları olmasına rağmen herhangi bir nesnenin varlığının tespit edilmesi istenilen sistemlerde de kullanılabilir. Sistem farklı otoparklardaki kameralara kolaylıkla entegre edilip kullanılabilir.


# 2. Projenin Genel Tanıtımı

Projede iki farklı python dosyamız bulunmaktadır. İlk python
dosyamızı kullanarak otoparkta seçilmek istenen alanlar belirtilir.
Belirtilen alanların koordinatlarını bir dosyaya kaydeder. İkinci python
dosyamız çalıştırıldığında koordinatların kaydedilmiş olduğu dosyayı
okur. İkinci programda bulunan videoya bazı filtreleme işlemleri
uygulanarak daha işlenebilir bir görüntü sağlanır. Seçilmiş
koordinatlardaki bölgelerde işlemler yapılarak, eğer boşsa yeşil
değilse kırmızı çerçeveyle gösterilir. Ekranın sol üst tarafında boş ve
dolu olan park alanı sayısını gösterir.


## 2.1. Projenin Ekran Görüntüleri ile Detaylı Tanıtılması

**2.1.1. Boş Alan Seçim Ekranı**

Alan seçim ekranındaki tıklanan iki noktanın koordinatları
listeye’a kaydedilerek ardışık bir koordinat listesi oluşturulur ve bu
koordinatlar pickle kütüphanesi aracılığıyla binary bir dosya olarak
kaydedilir. AlanSecici.py dosyamızı çalıştırdığımızda binary dosyasında
koordinat varsa resimde gösterilir. Mouse’un sol tuşu ile iki nokta
işaretlenerek yeni alanlar belirlenebilir. Seçilen iki koordinat arasında
rectangle fonksiyonu ile mavi, dikdörtgen bir çerçeve çizilir.
İstediğimiz çerçevenin içerisine Mouse ile sağ tıklayarak silinebilir. q
tuşuna basılarak programdan çıkılabilir. n tuşuna basılarak diğer
uygulama çalıştırılır.
<br/><br/>
![carparkPhoto0](https://user-images.githubusercontent.com/77435563/170721718-fb491ce0-f263-49c9-b0f0-24903ce3c23a.jpg)
<br/><br/>


**2.1.2. Ana Ekran (Canlı Görüntü Ekranı)**

Kameradan gelen görüntü belli bir sıralama ile filtreleme
işlemlerinden geçirilir. İlk filtreleme aşamasında görüntü gri ye
dönüştürülür. İkinci filtreleme aşamasında griye dönüştürülmüş olan
görüntüye gaussian blur işlemi uygulanır. Üçüncü filtreleme
aşamasında görüntüye Threshold uygulanarak belirlenen pikselin
altındaki pikseller siyaha üstündeki pikseller beyaza boyanır.
Dördüncü filtreleme aşamasında siyah beyaz görüntüye median blur
uygulanır. Beşinci ve son aşama olarak da görüntüye dilation
yapılarak beyaz alanlar genişletilir. Daha sonra boş alan seçim
ekranında seçilen koordinatlar binary dosyadan okunarak kamera
ekranına aktarılır. Aktarılan her bölgenin videodaki koordinatı kırpılır.
Kırpılmış bölgenin toplam piksel sayısı alınıp bu sayı 5 e bölünerek
eşik değeri oluşturulur. Kırpılan alandaki beyaz piksellerin sayısı eşik
değerinden büyük ise seçilmiş alanda bir araç var demektir ve bu alan
kırmızı renkli çerçeve ile gösterilir. Beyaz piksellerin sayısı eşik
değerinden küçük ise alan boş demektir ve yeşil renkli çerçeve ile
gösterilir.
<br/><br/>
![carparkPhoto1](https://user-images.githubusercontent.com/77435563/170721798-dbb33bd0-c382-46bb-8a0b-2fdc61455160.jpg)
<br/><br/>



# 3. Sonuç

Her geçen gün trafiğe çıkan araç sayısı artmakta ve bununla
birlikte otopark, park yerleri gibi alanlarda yoğunluk olmaktadır.
Bununla birlikte sürücülerin otoparklarda boş yer bulmak için çok
zaman sarf etmektedirler. Bu proje ile araçların park edebileceği boş
alanları sürücülere bildirerek zamandan tasarruf yapmayı ve
otoparklarda bulunan yoğunluğu azaltmak planlanmaktadır. Güvenlik
önlemleri için kullanılan kameralara proje entegre edilerek
minimum maliyetle proje uygulanabilir.


