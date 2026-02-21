import responses
from application import sendHTTPRequest

@responses.activate
def test_with_mock():
    responses.add(
        responses.GET, 
        "https://api.example.com/data",
        json={'error': 'not found'}, 
        status=404
    )
    print("test")
    status = sendHTTPRequest("https://api.example.com/data")
    assert type(status) == int, "Expecting status to be an integer"
    assert status == 404, "Expecting status to be 404"