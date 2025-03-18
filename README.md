# Classor

IP sınıfı tarayıcı - Belirtilen IP aralığındaki aktif cihazları bulan basit bir araç.

## Özellikler

- Belirtilen IP aralığındaki tüm adresleri tarar
- Çoklu iş parçacığı ile hızlı tarama
- Basit ve kullanımı kolay

## Kurulum

```bash
pip install git+https://github.com/2xafa/classor.git
```

## Kullanım

```bash
classor 192.168.1.0/24
```

## Örnek Çıktı

```
192.168.1.0/24 ağı taranıyor...

192.168.1.1 hayatta
192.168.1.5 hayatta
192.168.1.10 hayatta
```