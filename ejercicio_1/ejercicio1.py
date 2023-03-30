class Palindromo:
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







