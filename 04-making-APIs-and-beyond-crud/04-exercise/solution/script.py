import requests

def main():
    requests.get('http://localhost:8000/serialize_todays_aholes')
    requests.get('http://localhost:8000/refresh_most_wholesome')
    requests.get('http://localhost:8000/update_wholesome_gist')


if __name__ == '__main__':
    main()

