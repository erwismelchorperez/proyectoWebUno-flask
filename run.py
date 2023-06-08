from aplication import create_app
app = create_app()#aqui lo pegue pera mandarlo a un entorno de producción
if __name__ == '__main__':
    #app = create_app()#se movio para mas arriba ya que lo mandare a un entorno de producción
    app.run() 