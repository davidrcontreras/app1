from main import app 
# On the top the first app reference to app name, and second app reference to the drectory name 
def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Boquita" in response.data
