from Repository.District import District as RepositoryDistrict

class District:
    def get_all():
        data = RepositoryDistrict.get_all()    
        if(data):
            return data

    def get_by_id(id):                
        data = RepositoryDistrict.get_by_id(id)    
        if(data):
            return data[0]
        return {}