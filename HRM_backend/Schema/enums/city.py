from pydantic import BaseModel
from typing import Dict, List

class City(BaseModel):
    name: str

class CityResponse(BaseModel):
    city_name: str
    zip_codes: List[str]

cities_data = {
    "Prishtine": ["10000", "10020","10030", "10040","10050", "10060","10070", "10080","16000", "12060","16000", "12060","16000", "12060","16000", "12060","16000", "12060","16000", "12060","16000", "12060","16000", "12060"],
    "Peje": ["30000", "30010", "30030"],
    "Decan": ["51000"]

} 