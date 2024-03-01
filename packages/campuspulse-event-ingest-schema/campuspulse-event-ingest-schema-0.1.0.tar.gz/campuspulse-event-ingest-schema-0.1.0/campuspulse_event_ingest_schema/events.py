# Events rough Schema
# https://docs.pydantic.dev/latest/concepts/models/

import datetime
from pydantic import Field, datetime_parse
from .common import BaseModel
from typing import List, Optional

class StringDatetime(datetime.datetime):

    @classmethod
    def from_iso(cls, iso: str):
        """Parse ISO string to datetime"""
        dt = datetime_parse.parse_datetime(iso) 
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

# test it 
# dt = StringDatetime.from_iso("2024-01-01T07:15:00.000")
# print(dt)
    
class StringDate(datetime.datetime):
    @classmethod
    def from_iso(cls, iso: str):
        """Parse ISO string to date"""
        dt = datetime_parse.parse_datetime(iso) 
        return dt.date()
        
# test it 
# dt = StringDate.from_iso("2024-01-01T07:15:00.000")
# print(dt)

class StringTime(datetime.datetime):
    @classmethod
    def from_iso(cls, iso: str):
        """Parse ISO string to time"""
        dt = datetime_parse.parse_datetime(iso) 
        return dt.time()
        
# test it 
# dt = StringTime.from_iso("2024-01-01T07:15:00.000")
# print(dt)


class Accessibility(BaseModel):
    #Interpreter Requested, yes, not yet, none available
    #wheelchair accessible?
    pass


class Contact(BaseModel):
    name: Optional[str]
    email: Optional[str]
    organization: Optional[str]

class Location(BaseModel):
    """
    {
        "street": str,
        "city": str,
        "state": str,
        "zip": str,
        "building": str,
        "room-number": int
    
    }
    """
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zipcode: Optional[str]
    building: Optional[str]
    room_number: Optional[int]

       

class EventSource(BaseModel):
    source_id:  Optional[str]
    source_link: Optional[str]
    submitter: Optional[str]
    processed_at: str

class Freebies(BaseModel):
    
    has_food: bool
    merchendise: bool
    other: Optional[str]

class NormalizedEvent(BaseModel):
    """ name: str,
        event_id: int,   
        location: Location, 
        date: int,
        isAllDay: bool,
        time_start: int, 
        time_end: int, 
        duration: int, 
        description: str, 
        host: str
    """
    identifier: str
    title: Optional[str]
    location: Optional[Location]
    date: Optional[StringDate]
    # contact
    isAllDay: Optional[bool]
    time_start: Optional[StringTime]
    time_end: Optional[StringTime]
    start: datetime.datetime
    end: Optional[datetime.datetime]
    duration: Optional[StringTime]
    description: Optional[str]
    # internal notes
    host: Optional[str]
    is_public: bool
    source: EventSource

 