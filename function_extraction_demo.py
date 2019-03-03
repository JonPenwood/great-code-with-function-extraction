import urllib2
import json


def main():
    # Go get Data from Web API
    users_jsonplaceholder_url = 'https://jsonplaceholder.typicode.com/users'
    users_get_request = urllib2.urlopen(users_jsonplaceholder_url)
    unformatted_users = users_get_request.read()

    # Format Users from stringified json to Dictionary
    users = json.loads(unformatted_users)

    # Get User company names
    users_company_names = []
    for user in users:
        user_company_name = user['company']['name']
        users_company_names.append(
            user_company_name
        )

    # Get Unique Company Names
    unique_company_names = list(set(users_company_names))

    # Display All Unique Company Names
    print('')
    for unique_company_name in unique_company_names:
        print(unique_company_name)
    print('')



if __name__ == "__main__":
    main()