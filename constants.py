"""
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

import json

from api_model import apis_model_from_dict

with open('apis.json') as f:
    constants = json.dumps(json.load(f))
    result = apis_model_from_dict(json.loads(constants))


class KhaltiApis:
    khaltiApi = result["Khalti"].api


class ImeApi:
    imeiApi = result["ImePay"].api
    imeiApi2 = result["ImePay"].api2


class SajiloAPI:
    SajiloPayAPI = result["SajiloPay"].api
    SajiloHost = result["SajiloPay"].host
    SajiloUA = result["SajiloPay"].ua


class IcashApi:
    IcashApi = result["Icash"].api
    IcashHost = result["Icash"].host
    IcashOrigin = result["Icash"].origin
    IcashReferer = result["Icash"].referer
    IcashUA = result["Icash"].ua


class Moco:
    MocoApi = result["Moco"].api
    MocoHost = result["Moco"].host
    MocoOrigin = result["Moco"].origin
    MocoReferer = result["Moco"].referer
    MocoUA = result["Moco"].ua


class Ncell:
    NcellApi = result["Ncell"].api
    NcellHost = result["Ncell"].host
    NcellOrigin = result["Ncell"].origin
    NcellReferer = result["Ncell"].referer
    NcellUA = result["Ncell"].ua


class Nagrik:
    NagrikApi = result["Nagrik"].api
    NagrikHost = result["Nagrik"].host
    NagrikOrigin = result["Nagrik"].origin
    NagrikReferer = result["Nagrik"].referer
    NagrikUA = result["Nagrik"].ua


class NID:
    NIDApi = result["NID"].api
    NIDAPi2 = result["NID"].api2
    NIDHost = result["NID"].host
    NIDOrigin = result["NID"].origin
    NIDReferer = result["NID"].referer
    NIDUA = result["NID"].ua


class Pathao:
    PathaoApi = result["Pathao"].api
    PathaoHost = result["Pathao"].host
    PathaoOrigin = result["Pathao"].origin
    PathaoReferer = result["Pathao"].referer
    PathaoUA = result["Pathao"].ua


class Moru:
    MoruApi = result["Moru"].api
    MoruHost = result["Moru"].host
    MoruOrigin = result["Moru"].origin
    MoruReferer = result["Moru"].referer
    MoruUA = result["Moru"].ua


class PrabhuPay:
    PrabhuPayApi = result["PrabhuPay"].api
    PrabhuPayApi2 = result["PrabhuPay"].api2
    PrabhuPayHost = result["PrabhuPay"].host
    PrabhuPayOrigin = result["PrabhuPay"].origin
    PrabhuPayReferer = result["PrabhuPay"].referer
    PrabhuPayUA = result["PrabhuPay"].ua


class PrabhuTv:
    PrabhuTvApi = result["PrabhuTv"].api
    PrabhuTvHost = result["PrabhuTv"].host
    PrabhuTvOrigin = result["PrabhuTv"].origin
    PrabhuTvReferer = result["PrabhuTv"].referer
    PrabhuTvUA = result["PrabhuTv"].ua


class OnlineSathi:
    OnlineSathiApi = result["OnlineSathi"].api
    OnlineSathiApi2 = result["OnlineSathi"].api2
    OnlineSathiHost = result["OnlineSathi"].host
    OnlineSathiOrigin = result["OnlineSathi"].origin
    OnlineSathiReferer = result["OnlineSathi"].referer
    OnlineSathiUA = result["OnlineSathi"].ua


class Upaya:
    UpayaApi = result["Upaya"].api
    UpayaApi2 = result["Upaya"].api2
    UpayaHost = result["Upaya"].host
    UpayaOrigin = result["Upaya"].origin
    UpayaReferer = result["Upaya"].referer
    UpayaUA = result["Upaya"].ua
