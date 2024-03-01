from ddaptools.dda_constants import *
from ddaptools.dda_models import *
import json, random, string
import datetime

import json
from dateutil import parser


       
class Utils:
    def NoneSafe(dictItem:dict, key:string, default=None):
        """Safely gets the value from the dictionary, if it does not exist, it returns the default

        Args:
            dictItem (dict): dictionary to get the value from
            key (string): key to get the value from
            default (string): default value to return if the key does not exist | 

        Returns:
            str: Value that is returned safely
        """
        # return dictItem.get(key, default)
        if key in dictItem:
            try:
                return dictItem[key]
            except Exception as e:
                # print("Exception at NoneSafe:", e
                #       , "dictItem:", type(dictItem) ,dictItem, 
                #       "key:",  type(key),key)
                pass
        return default
    
    def getNow():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    

    def parseDate(dateString) -> datetime.datetime:
        """
        Returns a datetime object from a string or a datetime object (In both cases returns a datetime object).
        Useful to operate with dates that are either strings or datetime objects.
        """
        if dateString == None:
            return None
        
        if type(dateString) == datetime.datetime:
            return dateString
        
        return parser.parse(dateString)

    def datetimeToYearMonthDayMinute(dateString) -> str:
        """
        Converts a datetime to a string in the format of "%Y-%m-%dT%H:%M"
        """
        if dateString == None:
            return None
        
        if type(dateString) == datetime.datetime:
            dateString = dateString.strftime("%Y-%m-%dT%H:%M")
        
        return parser.parse(dateString).strftime("%Y-%m-%dT%H:%M")
    