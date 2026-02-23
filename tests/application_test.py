from src.application import sendHTTPRequest
import responses

@responses.activate
def test_with_mock():
    responses.add(
        responses.GET, 
        "https://api.example.com/data",
        json={'error': 'not found'}, 
        status=404
    )
    print("test")
    status, content = sendHTTPRequest("https://api.example.com/data")
    assert type(status) == int, "Expecting status to be an integer"
    assert status == 404, "Expecting status to be 404"
    assert 'error' in content and content['error'] == 'not found' 

    
def test_send_correct_url():
    # Testing the correct link
    status, content = sendHTTPRequest("https://simpledebit.gocardless.io/health_check")
    assert type(status) == int, "Expecting status to be an int"
    assert status == 200, "Expecting a status code 200"

def test_send_incorrect_url():
    status, content = sendHTTPRequest("https://simpledebit.gocardless.io/health_checkz")
    assert status == 404
    