import requests

def sendHTTPRequest(url: str):
    response = requests.get(url)
    
    return(
        response.status_code, 
        response.json() if response.headers['content-type'].__contains__("json") else response.content
    )

if __name__ == '__main__':
    print(sendHTTPRequest('https://simpledebit.gocardless.io/health_check'))
