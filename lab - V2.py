# In this lab, you found users using an old email domain in a big list using regular expressions. 
# You wrote a script that included replacing the old domain name (abc.edu) with a new domain name (xyz.edu), and you stored all domain names, including the updated ones, in a new file.

#!/usr/bin/env python3

import re
import csv
from pathlib import Path

data_dir = Path("/home/mkulbat/projects/data")

def contains_domain(address, domain):
    domain_pattern = r"[\w\.-]+@" + re.escape(domain) + r"$"
    return re.match(domain_pattern, address) is not None

def replace_domain(address, old_domain, new_domain):
    old_domain_pattern = re.escape(old_domain) + r"$"
    return re.sub(old_domain_pattern, new_domain, address)

def main():
    old_domain, new_domain = "abc.edu", "xyz.edu"

    csv_file_location = Path("/home/mkulbat/projects/Work with regex/user_emails.csv")
    report_file = data_dir / "updated_user_emails.csv"

    old_domain_email_list = []
    new_domain_email_list = []

    with open(csv_file_location, "r", newline="", encoding="utf-8") as file:
        user_data_list = list(csv.reader(file))

    # remove space in header
    headers = [header.strip() for header in user_data_list[0]]
    email_index = headers.index("Email Address")

    user_email_list = [data[email_index].strip() for data in user_data_list[1:]]

    for email_address in user_email_list:
        if contains_domain(email_address, old_domain):
            old_domain_email_list.append(email_address)
            replaced_email = replace_domain(email_address, old_domain, new_domain)
            new_domain_email_list.append(replaced_email)

    for user in user_data_list[1:]:
        current_email = user[email_index].strip()

        for old_email, new_email in zip(old_domain_email_list, new_domain_email_list):
            if current_email == old_email:
                user[email_index] = new_email

    with open(report_file, "w", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)

main()