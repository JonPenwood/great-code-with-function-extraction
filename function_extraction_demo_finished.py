import json
import urllib2


def display_values(unique_company_names):
    print('')
    for unique_company_name in unique_company_names:
        print(unique_company_name)
    print('')


def get_unique_values(users_company_names):
    return list(set(users_company_names))


def get_users_company_names(users):
    users_company_names = []
    for user in users:
        user_company_name = user['company']['name']
        users_company_names.append(user_company_name)
        
    return users_company_names


def get_users_from_jsonplaceholder():
    # Go get Data from Web API
    users_jsonplaceholder_url = 'https://jsonplaceholder.typicode.com/users'
    users_get_request = urllib2.urlopen(users_jsonplaceholder_url)
    unformatted_users = users_get_request.read()

    # Format Users from stringified json to Dictionary
    users = json.loads(unformatted_users)

    return users


def get_all_users_unique_company_names():
    users = get_users_from_jsonplaceholder()

    users_company_names = get_users_company_names(users)

    unique_company_names = get_unique_values(users_company_names)
    
    display_values(unique_company_names)


if __name__ == "__main__":
    get_all_users_unique_company_names()
