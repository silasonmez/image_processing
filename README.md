Proje Adı: Görüntü İşleme ile K-Means Segmentasyonu

Proje Amacı

Bu projede, temel görüntü işleme teknikleri ve K-Means algoritması kullanılarak bir görsel üzerinde segmentasyon işlemleri gerçekleştirilmiştir. Amaç, görseldeki benzer piksel değerlerini gruplayarak anlamlı bölgeler oluşturmak ve bu bölgeleri analiz etmektir.

Kullanılan Teknolojiler

Python

OpenCV

NumPy

Matplotlib

Adım Adım Proje Açıklaması

Veri Yükleme ve Hazırlık

Görsel OpenCV ile yüklenir ve RGB formatına dönüştürülür.

Gaussian ve Median blur filtreleri uygulanarak görselin yumuşatılması sağlanır.

Gri Tonlama ve K-Means Segmentasyonu

Görsel gri tona dönüştürülür.

Gri değerlere K-Means algoritması uygulanarak görsel k adet segmente ayrılır.

En Parlak Kümenin Maskeleme İşlemi

Segmentasyon sonucu elde edilen küme merkezlerinin parlaklık değerleri hesaplanır.

En parlak küme belirlenerek bu bölge maskelenir.

RGB Renk Uzayında K-Means Segmentasyonu

Orijinal RGB değerlerine de ayrıca K-Means uygulanarak 6 küme elde edilir.

Bu merkez renkler gri tona dönüştürülerek renk çubuğu oluşturulur.

Renk Küme Çubuğu Gösterimi

K-means ile elde edilen RGB küme merkezlerinden gri tonlu bir çubuk oluşturularak hangi tonların öne çıktığı gösterilir.

Küme Piksel Dağılımı Analizi

RGB renk kümelemesinden sonra her bir kümede kaç piksel bulunduğu hesaplanır.

Bu sayede görseldeki en baskın renklerin oransal olarak dağılımı gözlemlenir.

Görsel Çıktılar

Projede elde edilen çıktılar Matplotlib yardımıyla görsel olarak sunulmuştur:

Orijinal görsel

Bulanıklaştırılmış görsel (Gaussian ve Median Blur)

K-means segmentasyon sonucu

Maskeleme sonucu (en parlak bölge)

Gri tonlu renk küme merkezi çubuğu

