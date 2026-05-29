#!/usr/bin/env python3

import re

# FIND WEBSITE
def find_gov_urls(website):
 pattern = r"https://www\.[\w\-]+\.gov" #enter the regex pattern here
 result = re.findall(pattern, website) #enter the re method here
 return result

print(find_gov_urls("https://www.data.gov is a great place to find open source datasets!")) # Should return ['https://www.data.gov']
print(find_gov_urls("Learn more about US National Parks at https://www.nps.gov, https://www.nationalparks.org, or https://www.recreation.gov.")) # Should return ['https://www.nps.gov', 'https://www.recreation.gov']
print(find_gov_urls("The Library of Congress (https://www.loc.gov) is an incredible resource!")) # Should return ['https://www.loc.gov']
print(find_gov_urls("The Library of Congress (www.loc.gov) is an incredible resource!")) # Should return []

# FIND CITIES
def parse_city_country(text):
  pattern = r"[,.]\s" #enter the regex pattern here
  result = re.split(pattern, text) #enter the re method  here

  if len(result) != 2:
    return ""
  return result[0] #return the correct capturing group

print(parse_city_country("Paris, France")) # should return Paris
print(parse_city_country("Mumbai, India")) # should return Mumbai
print(parse_city_country("Rio de Janeiro. Brazil")) # should return Rio de Janeiro
print(parse_city_country("Tokyo! Japan"))  # result should be blank

# FIND ISBN

def find_isbn(list):
  pattern = r"^\d{3}-\d-\d{2}-(\d{6})-\d$" #enter the regex pattern here
  result = re.search(pattern, list) #enter the re method  here
  if result is None:
    return ""
  return result.group(1) #return the correct capturing group

print(find_isbn("123-4-12-098754-0")) # Should return 098754
print(find_isbn("223094-AB-30")) # result should be blank
print(find_isbn("1123-4-12-098754-0")) # result should be blank
