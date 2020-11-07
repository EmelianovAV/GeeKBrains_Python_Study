"""Спортсмен занимается ежедневными пробежками. В первый день 
его результат составил a километров. Каждый день спортсмен увеличивал 
результат на 10 % относительно предыдущего. Требуется определить номер дня, 
на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня."""

real_result = int(input("Enter the result of your run in km: "))
wish_result = int(input("Enter your desired running result in km: "))
days = 1
while real_result < wish_result:
    real_result = real_result + 0.1 * real_result
    days += 1
print(f"On {days} day you achieve the desired result.")


