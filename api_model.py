

from dataclasses import dataclass
from typing import Any, Dict, TypeVar, Callable, Type, cast

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

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ApisModelValue:
    api: str
    api2: str
    host: str
    origin: str
    referer: str
    ua: str

    @staticmethod
    def from_dict(obj: Any) -> 'ApisModelValue':
        assert isinstance(obj, dict)
        api = from_str(obj.get("api"))
        api2 = from_str(obj.get("api2"))
        host = from_str(obj.get("host"))
        origin = from_str(obj.get("origin"))
        referer = from_str(obj.get("referer"))
        ua = from_str(obj.get("ua"))
        return ApisModelValue(api, api2, host, origin, referer, ua)

    def to_dict(self) -> dict:
        result: dict = {"api": from_str(self.api), "api2": from_str(self.api2), "host": from_str(self.host),
                        "origin": from_str(self.origin), "referer": from_str(self.referer), "ua": from_str(self.ua)}
        return result


def apis_model_from_dict(s: Any) -> Dict[str, ApisModelValue]:
    return from_dict(ApisModelValue.from_dict, s)


def apis_model_to_dict(x: Dict[str, ApisModelValue]) -> Any:
    return from_dict(lambda x: to_class(ApisModelValue, x), x)
