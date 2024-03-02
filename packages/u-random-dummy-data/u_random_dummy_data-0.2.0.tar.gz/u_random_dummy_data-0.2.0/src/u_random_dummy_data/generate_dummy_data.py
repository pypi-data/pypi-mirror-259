import re
from typing import Optional, Tuple
from faker import Faker
import pykakasi
from dataclasses import dataclass


@dataclass
class DummyData:
    family_name_kanji: str
    first_name_kanji: str
    family_name_kana: str
    first_name_kana: str
    postal_code_1: int
    postal_code_2: int
    address_1: str
    address_2: str
    address_3: str
    address_4: str
    phone_1: str
    phone_2: str
    phone_3: str
    birth_date: str


def generate() -> DummyData:
    fake = Faker("ja_JP")
    kakashi = pykakasi.kakasi()

    name_kanji = fake.name()
    [family_name_kanji, first_name_kanji] = name_kanji.split(' ')

    converted = kakashi.convert(name_kanji)
    name_katakana = ''.join(map(lambda x: x['kana'], converted))
    [family_name_kana, first_name_kana] = name_katakana.split(' ')

    postal_code = fake.zipcode()
    [postal_code_1, postal_code_2] = postal_code.split('-')

    address = fake.address()

    split_address = parse_address(address)

    address1 = split_address[0] if split_address[0] is not None else ''
    address2 = split_address[1] if split_address[1] is not None else ''
    address3 = split_address[2] if split_address[2] is not None else ''
    address4 = split_address[3] if split_address[3] is not None else ''

    phone = fake.phone_number()
    [phone_1, phone_2, phone_3] = phone.split('-')

    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=100).strftime('%Y-%m-%d')

    return DummyData(
        family_name_kanji,
        first_name_kanji,
        family_name_kana,
        first_name_kana,
        postal_code_1,
        postal_code_2,
        address1,
        address2,
        address3,
        address4,
        phone_1,
        phone_2,
        phone_3,
        birth_date
    )


def parse_address(address: str) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
    match = re.match(r'([^都道府県]+[都道府県])([^市区町村]+[市区町村])(.*)', address)
    if match:
        [address1, address2, address3] = match.groups()
        splited = address3.split(' ')
        if len(splited) > 1:
            address3_1 = splited[0]
            address3_2 = splited[1]
        else:
            address3_1 = splited[0]
            address3_2 = None

        return address1, address2, address3_1, address3_2
    else:
        return None, None, None, None
