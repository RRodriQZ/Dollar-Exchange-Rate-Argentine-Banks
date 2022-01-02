# Dollar-Values-of-Banks #

Web Scraping dollar values of Argentine Banks

* **Banco Nacion**
* **Banco Ciudad**
* **Banco Provincia**
* **Banco Santander Rio**
* **Banco Galicia**
* **BBVA Banco Frances**
* **Banco Comafi**
* **Banco Patagonia**
* **Banco ICBC**
* **Banco Supervielle**
* **Banco Hipotecario**

# Pre Requirements 📋

* **Docker-compose**

# Running Docker 🐳
```
docker-compose build .
docker-compose up
```
# Testing 🧪

The tests in **LOCAL** were done with postman from the url: http://localhost:5001

**Endpoints:**

1) GET → ***/status***
2) GET → ***/banks***

**[RESPONSE]**
```
1) GET → http://localhost:5001/status
```
```yaml
{
    "message": "'Dollar-exchange-rate-argentine-banks' API works!",
    "status_code": 200,
    "version": "0.1"
}
```

**[RESPONSE]**
```
2) GET → http://localhost:5001/banks
```
```yaml
[
    {
        "0.Banco": "BANCO-NACION",
        "1.Fecha": "Fri, 31 Dec 2021 16:12:41 GMT",
        "2.Compra ($)": 101.75,
        "3.Venta ($)": 107.75,
        "4.Valor de compra parcial ($)": 140.08,
        "5.Valor de compra final ($)": 177.79
    },
    {
        "0.Banco": "BANCO-CIUDAD",
        "1.Fecha": "Fri, 31 Dec 2021 16:12:41 GMT",
        "2.Compra ($)": 101.75,
        "3.Venta ($)": 107.75,
        "4.Valor de compra parcial ($)": 140.08,
        "5.Valor de compra final ($)": 177.79
    },
    {
        "0.Banco": "BANCO-PROVINCIA",
        "1.Fecha": "Fri, 31 Dec 2021 16:12:42 GMT",
        "2.Compra ($)": 101.75,
        "3.Venta ($)": 107.75,
        "4.Valor de compra parcial ($)": 140.08,
        "5.Valor de compra final ($)": 177.79
    },
    ...
]
```

# Author 🖋

* Rodrigo Quispe - Developer - [RRodriQZ]
 
[RRodriQZ]: https://github.com/RRodriQZ