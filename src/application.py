import requests

def sendHTTPRequest(url: str):
    response = requests.get(url)
    return(response.status_code)

if __name__ == '__main__':
    print(sendHTTPRequest('https://simpledebit.gocardless.io/health_check'))
