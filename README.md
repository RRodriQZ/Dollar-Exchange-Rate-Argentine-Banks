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

* **Docker**
* **Docker-compose**

# Running Application 🐳
```bash
sudo make up-d
```
# Testing 🧪

The tests in **LOCAL** were done with postman from the url: http://localhost:5000

**Endpoints:**

1) GET → ***/status***
2) GET → ***/api/v1/banks***

# 1) GET → /status

**[ REQUEST ]**
```yaml
url: http://localhost:5000/status
```

**[ RESPONSE ]**
```yaml
{
    "message": "'Dollar-exchange-rate-argentine-banks' API works!",
    "status_code": 200,
    "version": "2.0"
}
```

# 2) GET → /api/v1/banks

**[ REQUEST ]**
```yaml
url: http://localhost:5000/api/v1/banks
```

**[ RESPONSE ]**
```yaml
{
    "datetime": "2023-03-19 21:17:22",
    "banks": [
        {
            "1.Banco": "Banco-nacion",
            "2.Compra ($)": 202.0,
            "3.Venta ($)": 210.0,
            "4.Valor de compra parcial ($)": 273.0,
            "5.Valor de compra final ($)": 346.5,
            "6.Ultima actualizacion": "viernes, 17 de marzo de 2023 17:59 Argentina"
        },
        {
            "1.Banco": "Banco-ciudad",
            "2.Compra ($)": 202.0,
            "3.Venta ($)": 210.0,
            "4.Valor de compra parcial ($)": 273.0,
            "5.Valor de compra final ($)": 346.5,
            "6.Ultima actualizacion": "viernes, 17 de marzo de 2023 17:59 Argentina"
        },
        {
            "1.Banco": "Banco-provincia",
            "2.Compra ($)": 202.0,
            "3.Venta ($)": 210.0,
            "4.Valor de compra parcial ($)": 273.0,
            "5.Valor de compra final ($)": 346.5,
            "6.Ultima actualizacion": "viernes, 17 de marzo de 2023 17:59 Argentina"
        },
        ...
    ]

}
```

# Author 🖋

* Rodrigo Quispe - Developer - [RRodriQZ]
 
[RRodriQZ]: https://github.com/RRodriQZ