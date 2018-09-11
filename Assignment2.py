#!/usr/bin*//env python
# -*- coding: utf-8 -
"""Users enter ID number to print out user's info and logges errors"""


import urllib2
import datetime
import logging
import argparse

#I WASN'T ABLE TO MAKE THE argparse TO WORK.  THIS IS WHAT I TRIED:
#parser = argparse.ArgumentParser(description='url where the file is located')
#parser.add_argument('url', type=str)
#arg = parser.parse_args()


def downloadData(url):
    """download contents located at the url and return it to the caller
   
    Arg:
        url(str): url containing the data
    """
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return processData(response)
 
 
def displayPerson(id, personData):
    """ prints name and DOB of a given user identified by the id
   
    Args:
        id(int):  Person's id number.
        personData(dict):  person's name and DOB.
       
    return:
        name and DOB of a given user identified by the id
       
    Example:
        Person #41 is Diana Nolan whith a birthday of 1973-04-09
    """
    print "Person #" + str(id) +  " is " + personData[str(id)][0] + " whith a birthday of "  + str(personData[str(id)][1])
      
      
def processData(my_file):
    """Takes the content of the file, processes the file, returns a dict with
    person's ID, name and DOB. 
    Arg:
        my_file:  file containing the data.
       
    Returns: 
        A dictionary that maps a person’s ID to a tuple (name, birth)
       
    Examples:
        70: (Zoe Bailey (2007-09-25))
        79: (Donna Burgess (1964-08-4))
    """
    LOG_FILENAME ='mylogs.log'
    logging.basicConfig(filename= LOG_FILENAME, level=logging.ERROR)
    logger=logging.getLogger(__name__)
    logging.error('This is an error message')

    my_dict={}
    dob_list=[]
    for line in my_file:
        person_id = line.split(',')[0]
        person_name = line.split(',')[1]
        person_dob = line.split(',')[2]
        dob_list= person_dob.split('/')
        try:
#            if len(dob_list)>2:
#                if len(dob_list[1])==2:
            dob_month=int(dob_list[1])
#                    if dob_month<=12:
            dob_year=int(dob_list[2])
#                        if dob_year<=9999:
            dob_day=int(dob_list[0])
#                            if dob_day<=31  and dob_day>0:
            dob_date=datetime.date(dob_year, dob_month, dob_day)
            my_dict[person_id]=(person_name,dob_date)
        except IndexError as err:
            logger.error(err)
            print "Incorrect set of values = "
            print dob_list
        except ValueError as err:
            logger.error(err)
            print "Incorrect value for a date = "
            print dob_list
           
#I WAS ABLE TO IDENTIFY THE ERRORS AND PRINT THEM WITH THE RESPECTIVE
#            ERROR.  bUT I WASN'T ABLE TO CREATE THE FILE TO RECORD THEM.
#            I TRIED THE SAME WAY THAT THE MODULE DOCUMENTATION SUGGESTED
#            AND THE OTHER WAY THAT I FOUND ON THE INTERNET
#    logging.error('This message should go to the log file')
#   
#    f = open(LOG_FILENAME, 'rt')
#    try:
#        body = f.read()
#    finally:
#        f.close()       
          
    return my_dict
   
if __name__ == '__main__':
     displayPerson(id,downloadData('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'))
     #displayPerson(id,downloadData(arg.url))
#def main():
#    csvData=downloadData(url)
