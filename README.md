# Twitter-API


**POST:** `http://127.0.0.1:8000/auth/users/`
```json
{
    "username": "gacakaj968",
    "email": "gacakaj968@fitwl.com",
    "password": "AYON#8sjJy@!",
    "re_password": "AYON#8sjJy@!"
}
```
![image](https://github.com/Ayon-SSP/Twitter/assets/80549753/8594ffbc-95b9-4a0e-abbb-3b0cc26d8de7)
![image](https://github.com/Ayon-SSP/Twitter/assets/80549753/a3025e8d-3e9a-4bc9-bb0b-456015ca14a5)


**POST:** `http://127.0.0.1:8000/auth/users/activation/`
```json
{
    "uid": "MTU",
    "token": "bqt85e-fb8aef65de05b5d3927471650014eaff"
}
```
![image](https://github.com/Ayon-SSP/Twitter/assets/80549753/81bf6bb3-1220-4f92-9b17-b2e132d525d9)
![image](https://github.com/Ayon-SSP/Twitter/assets/80549753/8196c729-abaa-4a80-81da-4ed5abf5ad3b)



**POST:** `http://127.0.0.1:8000/auth/jwt/create/`
```json
{
    "email": "gacakaj968@fitwl.com",
    "password": "AYON#8sjJy@!"
}
```
Response:
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4ODgxNTMyOCwianRpIjoiMGNhMWM1MWNiOWNlNGRmZDkxNmViNDc3ZWUxYzFhYWQiLCJ1c2VyX2lkIjoxNX0.aF87pNgThvso3on7wVzq79N_pEk5DSHK_5_YnPEnsiI",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4NjQyNTI4LCJqdGkiOiJmYjQ5MDQ0MjgyNzM0ZjFjOWFiMjJhYjE3OWIyNjY4OSIsInVzZXJfaWQiOjE1fQ.3I_dzIhD1v3cFiKMyLGSfDfI5i5vKB7pAijNr4eJ31c"
}
```
![image](https://github.com/Ayon-SSP/Twitter/assets/80549753/8f4e70ba-9698-4b7e-9898-b71e68dd983b)


![image](https://github.com/Ayon-SSP/Twitter/assets/80549753/7fecfe20-0619-40c9-aee7-152d545f60a3)

![image](https://github.com/Ayon-SSP/Twitter/assets/80549753/f3ca766f-b037-4ce2-9c47-50086878f4e8)









# Twitter-API


```css
Django Rest framework API for Twitter.
Frontend: reactjs.
Will try to add all most all the features of twitter.

construct the model
Folder structure
all the api endpoints connection with frontend
all the features of twitter
```
