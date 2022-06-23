import json, os

def main():
    while True:
        os.system('cls')
        name  =  str(input('Ingresa un nombre: ')).lower().strip()
        words = name.split()
        if len(words) > 1 or name.isalpha() != True:
            print('El valor ingresado no parece un nombre, por favor escribe solo un nombre.')
            input("Presiona enter para volver a intentarlo...")
        else:
            gender = name_gender(name)
            print('¿Quieres intentarlo de nuevo? y/n')
            keep_going  =  str(input()).lower().strip()[0]
            if keep_going != 'y' :
                print('Finalizado.')
                break


    
class name_gender:
    
    def __init__(self, given_name):
        name_list = self.__load_data()
        found_name = False
        for name in name_list:
            if given_name == str(name).lower():
                print('EL nombre : '+ given_name + ' es: ' + name_list[name])
                found_name = True
        if found_name != True:
            while True:
                print('No conozco ese nombre, por favor escribe "F" si es femenino o "M" masculino y lo recordare en futuras ejecuciones')
                print('F: Femenino')
                print('M: Masculino')
                response = str(input()).lower().strip()[0]
                gender = ''

                if response == 'm':
                    gender = 'Masculino'
                    break
                elif response == 'f':
                    gender = 'Femenino'
                    break
                else:
                    print('Introduciste un valor incorrecto, intentalo de nuevo por favor')
                    input('Presiona enter para continuar....')
            name_list[given_name] = gender
            self.__save_data(name_list)


    def __save_data(self, data):
        dictionary = json.dumps(data)
        with open('./data/data.json', 'w') as file:
            file.write(dictionary)
            file.close
    
    def __load_data(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        dictionary = json.load(open(os.path.join(__location__,'./data/data.json')))
        return dictionary

                
        

if __name__ == '__main__':
    main()