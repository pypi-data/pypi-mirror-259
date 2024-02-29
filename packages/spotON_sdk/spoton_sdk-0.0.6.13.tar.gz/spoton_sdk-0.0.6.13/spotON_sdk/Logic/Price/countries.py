from dataclasses import dataclass


from typing import Optional,List


from .customBaseModel import CustomBaseModel


import pandas as pd
import pytz

from pydantic import Field
import pandas as pd
import pytz

class Country(CustomBaseModel):
    capital: str
    country_code: str
    country_name: str
    emoji: str = ""
    UTC_time_difference: int = 0

    def __init__(self, **data):
        super().__init__(**data)
        self.validate_timezone()
        self.calculate_utc_time_difference()
        self.country_code_to_emoji()

    def validate_timezone(self):
        try:
            timezone = f"Europe/{self.capital}"
            pytz.timezone(timezone)
        except Exception:
            raise ValueError(f"{self.capital} not found in European capitals.")

    def calculate_utc_time_difference(self):
        timezone = f"Europe/{self.capital}"
        local_tz = pytz.timezone(timezone)
        utc_dt = pd.Timestamp.utcnow().to_pydatetime()
        local_dt = utc_dt.astimezone(local_tz)
        offest = local_dt.utcoffset()
        # convert timedelta to Timedelta
        if offest is None:
            raise ValueError(f"Could not calculate UTC time difference for {self.capital}.")

        self.UTC_time_difference = offest.seconds // 3600

    def country_code_to_emoji(self):
        cleaned_code = self.country_code.split("_")[0] if "_" in self.country_code else self.country_code
        OFFSET = 127397
        self.emoji = ''.join(chr(ord(c) + OFFSET) for c in cleaned_code.upper())




def get_country_by_code(countries: List[Country], country_code: str) -> Optional[Country]:
    """
    Returns the country object that matches the given country code.
    If no such object is found, returns None.
    """
    for country in countries:
        if country.country_code == country_code:
            return country
    return None



@dataclass
class all_Countries():
    Austria = Country(capital="Vienna", country_code="AT", country_name="Austria")
    Belgium = Country(capital="Brussels", country_code="BE", country_name="Belgium")
    Bulgaria = Country(capital="Sofia", country_code="BG", country_name="Bulgaria")
    Croatia = Country(capital="Zagreb", country_code="HR", country_name="Croatia")
    Cyprus = Country(capital="Nicosia", country_code="CY", country_name="Cyprus")
    Czech_republic = Country(capital="Prague", country_code="CZ", country_name="Czech republic")
    Denmark = Country(capital="Copenhagen", country_code="DK", country_name="Denmark")
    Estonia = Country(capital="Tallinn", country_code="EE", country_name="Estonia")
    Finland = Country(capital="Helsinki", country_code="FI", country_name="Finland")
    France = Country(capital="Paris", country_code="FR", country_name="France")
    Germany = Country(capital="Berlin", country_code="DE", country_name="Germany")
    Greece = Country(capital="Athens", country_code="GR", country_name="Greece")
    Hungary = Country(capital="Budapest", country_code="HU", country_name="Hungary")
    Ireland = Country(capital="Dublin", country_code="IE", country_name="Ireland")
    Italy = Country(capital="Rome", country_code="IT", country_name="Italy")
    Latvia = Country(capital="Riga", country_code="LV", country_name="Latvia")
    Lithuania = Country(capital="Vilnius", country_code="LT", country_name="Lithuania")
    Luxembourg = Country(capital="Luxembourg", country_code="LU", country_name="Luxembourg")
    Netherlands = Country(capital="Amsterdam", country_code="NL", country_name="Netherlands")
    Poland = Country(capital="Warsaw", country_code="PL", country_name="Poland")
    Portugal = Country(capital="Lisbon", country_code="PT", country_name="Portugal")
    Romania = Country(capital="Bucharest", country_code="RO", country_name="Romania")
    Slovakia = Country(capital="Bratislava", country_code="SK", country_name="Slovakia")
    Slovenia = Country(capital="Ljubljana", country_code="SI", country_name="Slovenia")
    Spain = Country(capital="Madrid", country_code="ES", country_name="Spain")
    Sweden = Country(capital="Stockholm", country_code="SE_1", country_name="Sweden")

    return_List= [Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech_republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Netherlands, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden]

    @classmethod
    def get_country_by_name(cls,country_name: str) -> Optional[Country]:
        """
        Returns the country object that matches the given country name.
        If no such object is found, returns None.
        """
        for country in cls.return_List:
            if country.country_name == country_name:
                return country
        return None


