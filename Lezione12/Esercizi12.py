class MovieCatalog:
    def __init__(self,catalog = {}):
        self.catalog: dict[str:list] = catalog

    def __str__(self):
        return str(self.catalog)
    
    def directors_list(self):
        list = [n for n in self.catalog.keys()]
        return list

    def add_movie(self,director_name: str, movies: str):
        if director_name not in self.catalog:
            self.catalog[director_name] = [movies]
        else:
            self.catalog[director_name].append(movies)

    def remove_movie(self,director_name: str, movies: str):
        if director_name in self.catalog:
            if movies in self.catalog[director_name]:
                self.catalog[director_name].remove(movies)
                if len(self.catalog[director_name]) == 0:
                    del self.catalog[director_name]
                    
    def get_movies_by_director(self,director_name):
        lista = [n for n in self.catalog[director_name]]
        return lista
    
    def search_movies_by_title(self,movie):
        diz = {}
        for k,v in self.catalog.items():
            if movie in v:
                diz[k] = movie
        return diz

    

    
catalogo1 = MovieCatalog()

catalogo1.add_movie("Leonardo Di Caprio","Shutter Island")
catalogo1.add_movie("Giovanni","Le Meduse")
catalogo1.add_movie("Gab","Le Meduse")
catalogo1.add_movie("Giovanni","Le Palle")
catalogo1.add_movie("Mario","Le giraffe blu")
print(catalogo1)
print(catalogo1.directors_list())
print(catalogo1.get_movies_by_director("Giovanni"))
print(catalogo1.search_movies_by_title("Le Meduse"))