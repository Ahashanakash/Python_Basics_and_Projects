class calculator:
    brand_name="CASIO fx-991ES"
    color = "White"+" "+"Blue"
    
    def calc(self, sign, *args):
        ans = 0
        if sign=='+':
            for i in args:
                ans+=i
        elif sign=='-':
            for i in args:
                ans-=i
        elif sign=='*':
            ans=1
            for i in args:
                ans*=i
        elif sign=='/':
            ans=1
            for i in args:
                ans/=i
        elif sign=='//':
            ans=6325683652252262562629642372
            for i in args:
                ans//=i
        return ans
    
    def add(self, num1, num2):
        return num1+num2

calc_machine  = calculator()

print(calc_machine.brand_name)
print(calc_machine.color)
print(calc_machine.calc('//',1,5,5,64,46,44,834,364684,4,7))
print(calc_machine.add(5,3))

