import os
import shutil
class Backup:
    def __init__(self,rutaOrigen,rutaDestino):
        self.rutaOrigen = rutaOrigen
        self.rutaDestino = rutaDestino
        self.cuantosNiveles = rutaOrigen.count('\\')
    
    def dameRuta(self):
        return (self.rutaOrigen)
        
    def dameArchivos(self,ruta):
        todosLosArchivos = []
        for nombreCarpeta, subCarpetas, nombreArchivos in os.walk(ruta):
            for subCarpeta in subCarpetas:
                todosLosArchivos.append(nombreCarpeta+'\\'+subCarpeta)
            for archivo in nombreArchivos:
                todosLosArchivos.append(nombreCarpeta+'\\'+archivo)
        return todosLosArchivos

    def enseniaArchivos(self):
        for nombreCarpeta, subCarpetas, nombreArchivos in os.walk(self.rutaOrigen):
            print('The current folder is ' + nombreCarpeta)
            for subCarpeta in subCarpetas:
                print('SUBFOLDER OF ' + nombreCarpeta + ': ' + subCarpeta)
            for archivo in nombreArchivos:
                print('FILE INSIDE ' + nombreCarpeta + ': '+ archivo)
            print('')

    def copiaTodo(self):
        origen = self.dameArchivos(self.rutaOrigen)
        destino = self.dameArchivos(self.rutaDestino)
        print(self.cuantosNiveles)
        if destino!=origen:
            for num, i in enumerate(origen):
                rutaNueva = self.rutaDestino + origen[num][len(self.rutaOrigen):]
                texto = str(origen[num])
                if os.path.isfile(i):
                    print(origen[num][len(self.rutaOrigen):])
                    print('Esto es Origen:  '+origen[num][origen[num].index(self.rutaOrigen):])
                    print('Esto es Destino: '+rutaNueva)
                    if not os.path.exists(rutaNueva):
                        shutil.copyfile(i, rutaNueva)
                else:
                    print(origen[num][len(self.rutaOrigen):])
                    print('Esto es Origen:  '+origen[num][origen[num].index(self.rutaOrigen):])
                    print('Esto es Destino: '+rutaNueva)
                    if not os.path.exists(rutaNueva):
                        os.makedirs(rutaNueva)


def main():
    mimimi = Backup("C:\\Users\\lotis\\Desktop\\backup",'C:\\Users\\lotis\\Documents\\pruebaBack')
    mimimi.copiaTodo()

    
if __name__ =='__main__':
    main()