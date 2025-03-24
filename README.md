# upnqr

Python knjižnica za generiranje QR kod za Univerzalni Plačilni Nalog (UPN).

Specifikacije:

https://www.zbs-giz.si/standardi-in-prirocniki/

(direktna povezava: https://www.zbs-giz.si/wp-content/uploads/2021/07/objava_dokumentacije_UPN_QR-2016-12-15.zip)

Prvotne povezave, nedostopne:

~~https://upn-qr.si/uploads/files/Tehnicni%20standard%20UPN%20QR.pdf~~

~~https://www.upn-qr.si/uploads/files/NavodilaZaProgramerjeUPNQR.pdf~~


~

Python library for QR code generation for UPN payment forms.

Specifications:

https://www.zbs-giz.si/en/standards/

(direct link: https://www.zbs-giz.si/wp-content/uploads/2021/10/EN_Tehnicni_standard_UPN_QR.pdf)

Original links, now dead:

~~https://upn-qr.si/uploads/files/EN_Tehnicni%20standard%20UPN%20QR.pdf~~

~~https://upn-qr.si/uploads/files/EN_NavodilaZaProgramerjeUPNQR.pdf~~

## Installation
To install the required dependencies, you can use the following command:

```
pip install -r requirements.txt
```

## Usage
To use the `upnqr` module, you can import the necessary classes and functions from the module. Here is a simple example:

```python
from upnqr.upnqr import Data, Placnik, Prejemnik

# Create instances of Placnik and Prejemnik
placnik = Placnik(ime="Janez Novak", ulica="Glavna 1", kraj="Ljubljana")
prejemnik = Prejemnik(ime="Marta Kovač", ulica="Strma 2", kraj="Maribor", iban="SI56012345678901234")

# Create a Data object
data = Data(
    placnik=placnik,
    prejemnik=prejemnik,
    znesek=100.50,
    koda_namena="TEST",
    namen_placila="Plačilo za storitve",
    rok_placila=datetime.date(2023, 12, 31),
    referenca="REF123456"
)

# Generate QR code
qr_code = make_from_data(data)
```

## License
This project is licensed under the GNU General Public License Version 3. See the LICENSE file for more details.
