class MatheMatics:
    @staticmethod 
    def Count_Digits(number:int)->int: #3.5/10
        if number == 0:
            return 1
        number = abs(number)
        count = 0
        while number>0:            
            number //= 10
            count+=1
        return count
    @staticmethod
    def Palindrome_Numbers(number:int)->int:
        pass
        