from Repository.city import City as RepositoryCity

class City:
    def get_all():        
        data = RepositoryCity.get_all()    
        if(data):
            return data
        return []

    def get_by_id(id):                
        data = RepositoryCity.get_by_id(id)    
        if(data):
            return data[0]
        return {}