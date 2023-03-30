class Palindromo:
    def __init__(self, texto):
        self.texto=texto
    
    def test(self):
        c= self.texto
        l=0
        for i in range(len(c)):
            if c[i]==c[len(c)-1-i]:
                pass
            else:
                l+=1
        if l==0:
            return True
        else:
            return False

    def __del__(self):
        print(self.texto.upper())
    
    
    @classmethod
    def esPalindromo(cls, texto):
        c=texto.upper()
        l=0
        for i in range(len(c)):
            if c[i]==c[len(c)-1-i]:
                pass
            else:
                l+=1
        if l==0:
            return True
        else:
            return False


#Se muestra RADAR, ya que el método destructor hace que se imprima en mayusculas el texto introducido. 
#Este método se activa cuando se destruye la instancia, en este caso, al declarar la nueva instancia, se destruye la se sonar, y es ahí cuando se activa el metodo destructor.
