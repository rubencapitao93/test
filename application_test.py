from application import sendHTTPRequest

def test_send_correct_url():
    # Testing the correct link
    status = sendHTTPRequest("https://simpledebit.gocardless.io/health_check")
    assert type(status) == int, "Expecting status to be an int"
    assert status == 200, "Expecting a status code 200"

def test_send_incorrect_url():
    status = sendHTTPRequest("https://simpledebit.gocardless.io/health_checkz")
    assert status == 404