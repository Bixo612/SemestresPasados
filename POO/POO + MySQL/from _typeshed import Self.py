    def agregarPelicula(pelicula):

        sql= "INSERT INTO `pelicula` (`idPelicula`, `titulo`, `año_estreno`, `duracion`, `censura`, `estudio`,`tipoPelicula`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        valor= (pelicula.get_idPelicula(),pelicula.get_titulo(), pelicula.get_año_estreno(), pelicula.get_duracion(), pelicula.get_censura(),pelicula.get_estudio(),pelicula.get_TipoPelicula())
        
        mycursor.execute(sql,valor)
        con.commit()