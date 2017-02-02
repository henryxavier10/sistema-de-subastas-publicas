Sistema de Subastas Públicas
========================================
Se realizó un sistema de subastas on-line, el cual consiste en: iniciar una sesión de subastas, anunciando el objeto a subastar, admitir pujas de los participantes y anunciar el resultado.  

Para la implementación de nuestro sistema de subastas, se usará el paradigma cliente-servidor y paso de mensajes. Cada participante, así como el programa de  subastas, asumen a la vez el papel de cliente  y servidor, de la siguiente forma:     

Para el control de la sesión: 
+Como servidor, un participante espera escuchar el anuncio del subastador (1) cuando comience la sesión, (2) en el momento en el que se produzca un cambio en la puja máxima, y (3) cuando la sesión termine.
+Como servidor, el subastador envía una petición que anuncia los tres tipos  de eventos antes comentados.  

Para la aceptación de pujas: 
+Como servidor, un participante envía una nueva puja a un servidor. 
+Como cliente, un subastador acepta nuevas pujas y actualiza la puja máxima. 
