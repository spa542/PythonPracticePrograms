# Password Checker
import requests # create and use requests
import hashlib # use sha1 hashing for API
import sys # command line arguments

def request_api_data(query_char):
    '''
    Takes a string which is the first 5 letters in the hash
    Creates a secure request for the API and tracks the status of connection
    '''
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
         raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    '''
    Takes a list of tuples containing the trailing hash and the amount of pings
    Also takes the hash that is being checked which is a string
    '''
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    '''
    Takes a string which is the password that should be checked and then completes
    the process of finding the pings on the specified password
    '''
    # Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... change it maybe?')
        else:
            print(f'{password} was NOT found. Safe and Secure!')
    return 'done!'

if __name__ == '__main__':
    main(sys.argv[1:])
