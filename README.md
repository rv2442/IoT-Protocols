## This repository is to demonstrate IoT protocols for beginners. It provides basic demonstration of 5 IoT protocols.  
>1. AMQP  
>2. SOAP  
>3. HTTP  
>4. MQTT

## References
* [COAP](https://aiocoap.readthedocs.io/en/latest/examples.html)    
* [AMQP](https://pypi.org/project/amqp/)      
* [SOAP](https://docs.python-zeep.org/en/master/)    
* [HTTP](https://docs.python.org/3/library/http.html)    
* [MQTT](https://pypi.org/project/paho-mqtt/)  

## AMQP
> Run it using below command, it will install rabbitmq locally and only then will any code under AMQP will work.    
> Note: Docker Client must be installed and running before running below command  
> After execution of this command the container will automatically be deleted  
`docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management`

### Requirements.txt
> Install all dependencies with the command below  
`pip install -r .\requirements.txt`
