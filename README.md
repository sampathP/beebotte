# beebotte
beebotteをRaspberry Piで受け取るソース

## 概要
Beebotteとラズパイで通信を行うためのPythonコード  
 - Beebotte => Publisher  
 - Raspberry Pi => Subscriber  
 
実装の役割は上記のイメージ  
※実際にはAmazon Echo => IFTTT => Beebotte => Raspberry Piで通信を行う
 
## 準備
1.必要なライブラリをインストール  
''' sudo pip3 install paho-mqtt '''

2.SSLで接続するためにCACERTを指定する  
pemは以下からダウンロードしてラズパイに配置しておく  
https://beebotte.com/certs/mqtt.beebotte.com.pem  
''' wget https://beebotte.com/certs/mqtt.beebotte.com.pem '''  




