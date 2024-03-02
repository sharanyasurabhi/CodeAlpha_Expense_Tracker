import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+919959108476")
phone_number2 = phonenumbers.parse("+919494198476")
phone_number3 = phonenumbers.parse("+919346918223")
phone_number4 = phonenumbers.parse("+918500144474")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4,"en"))
