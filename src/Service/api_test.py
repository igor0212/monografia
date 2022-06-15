from api import app

class TestApi:

    def test_api_district_all_should_return_status_code_200(self):        
        response = app.test_client().get('/api/district/all')    
        assert response.status_code == 200
            