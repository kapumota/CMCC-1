from __future__ import annotations

from faker import Faker

from tools.providers._locations import load_supported_locations
from tools.providers.travel_provider import TravelProvider

supported_locations = load_supported_locations()

fake = Faker()
travel_provider = TravelProvider(fake)
