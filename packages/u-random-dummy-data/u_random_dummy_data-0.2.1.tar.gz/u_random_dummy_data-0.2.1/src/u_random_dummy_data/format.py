from enum import Enum
from typing import List
import json
import yaml

from u_random_dummy_data.generate_dummy_data import DummyData
from dataclasses import asdict


class FormatStyle(Enum):
    csv = 1
    tsv = 2
    json = 3
    yaml = 4
    scala = 5


def format_data(data_list: List[DummyData], style: FormatStyle) -> str:
    if style == FormatStyle.csv:
        return format_csv(data_list)
    elif style == FormatStyle.tsv:
        return format_tsv(data_list)
    elif style == FormatStyle.json:
        return json.dumps([asdict(data) for data in data_list], ensure_ascii=False, indent=True)
    elif style == FormatStyle.yaml:
        return yaml.dump([asdict(data) for data in data_list], allow_unicode=True)
    elif style == FormatStyle.scala:
        return format_scala(data_list)
    else:
        return format_csv(data_list)


def format_csv(data_list: List[DummyData]) -> str:
    return format_separated_value(data_list, ',')


def format_tsv(data_list: List[DummyData]) -> str:
    return format_separated_value(data_list, '\t')


def format_separated_value(data_list: List[DummyData], separator: str) -> str:
    values_list = [asdict(item).values() for item in data_list]
    return '\n'.join([separator.join(row) for row in values_list])


def format_scala(data_list: List[DummyData]) -> str:
    lines = [format_scala_case_class(data) for data in data_list]
    return "List(\n" + "\n".join(lines) + "\n)"


def format_scala_case_class(data: DummyData) -> str:
    return ("  DummyData(FamilyNameKanji(\"{}\"), FirstNameKanji(\"{}\"), FamilyNameKana(\"{}\"), FirstNameKana(\"{"
            "}\"), PostalCode1({}), PostalCode2(\"{}\"), Address1(\"{}\"), Address2(\"{}\"), Address3(\"{}\"), "
            "Address4(\"{}\"), Phone1(\"{}\"), Phone2(\"{}\"),Phone3(\"{}\"), BirthDate(\"{}\"))").format(
        data.family_name_kanji,
        data.first_name_kanji,
        data.family_name_kana,
        data.first_name_kana,
        data.postal_code_1,
        data.postal_code_2,
        data.address_1,
        data.address_2,
        data.address_3,
        data.address_4,
        data.phone_1,
        data.phone_2,
        data.phone_3,
        data.birth_date
    )
