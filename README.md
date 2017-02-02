Sistema de Subastas Públicas
========================================
Se realizó un sistema de subastas on-line, el cual consiste en: iniciar una sesión de subastas, anunciando el objeto a subastar, admitir pujas de los participantes y anunciar el resultado.  

Para la implementación de nuestro sistema de subastas, se usará el paradigma cliente-servidor y paso de mensajes. Cada participante, así como el programa de  subastas, asumen a la vez el papel de cliente  y servidor, de la siguiente forma:     

Para el control de la sesión: 
+ Como servidor, un participante espera escuchar el anuncio del subastador (1) cuando comience la sesión, (2) en el momento en el que se produzca un cambio en la puja máxima, y (3) cuando la sesión termine.
+ Como servidor, el subastador envía una petición que anuncia los tres tipos  de eventos antes comentados.  

Para la aceptación de pujas: 
+ Como servidor, un participante envía una nueva puja a un servidor. 
+ Como cliente, un subastador acepta nuevas pujas y actualiza la puja máxima. 

Metodología
-------------
Se utilizó el modelo de mensajes publicación/suscripción, la implementación de nuestro sistema de subastas se realizaría de la siguiente forma:  
Cada participante se suscribe a los mensajes del evento comienzo-subasta.
+ El subastador anuncia el comienzo de la sesión de subasta enviando un mensaje de evento comienzo-subasta. 
+ Tras recibir el evento de comienzo-subasta, cada participante se suscribe a los mensajes del evento fin-subasta. 
+ El subastador se suscribe a los mensajes del evento nueva-puja. 
+ Un participante que desee realizar una nueva puja lanzará el evento nueva-puja, que será reenviado al subastador. 
+ Al final de la sesión, el subastador lanzará en mensaje fin-subasta para informar a todos los participantes del resultado.Si se desea, se puedenañadirotrosmensajes adicionalesquepermitanalos participantes conocer el estado de la subasta.   

Files
-------------
+ **pub.py**, que permite iniciar el canal donde va los mensajes, con el método publish() nos permite seleccionar el canal y los mensajes transmitir, y quien sea que esté suscrito podrá acceder a todos los mensajes.
+ **sub.py** , con el método pubsub() crea una nueva instancia pubsub y es necesario acceder al método subscribe() para escuchar el canal.
+ **subastador.py**, que hace el papel de publicador y subscritor, incluye el menú para iniciar una subasta, es decir crea un canal para el envío de mensajes de un nuevo producto que se quiere subastar y luego actúa como subscritor para escuchar las posibles ofertas del producto.
+ **paticipante.py**, que hace el papel de publicador y subscritor, incluye el menú para escoger un canal activo creado y subscribirse para escuchar el canal y recibir las subastas activas, una vez elegido, el participante manda mensajes en el canal de su oferta y así es como se convierte en publicador también.


