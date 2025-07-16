import math
def simple_calculator():
    print("=" * 40)
    print("welcome to simple calculator!")
    print("=" * 40)
    print("supported operations:")
    print(" +    : addition")
    print(" -    : subtraction")
    print(" *    : multiplication")
    print(" /    : division")
    print(" %    : modulus ")
    print(" ^    : power operations")
    print(" sqrt : square root  ")
    print(" sin  : sine  ")
    print(" cos  : cosine  ")
    print(" tan  : tangent  ")
    print(" lg  : logarithmic ")
    print(" ln   : natural logarithm ")
    print(" ex   : exit  ")
    print("=" * 40)
    while True:
        try:
            expression = input("\nyou could enter expression(like 2 + 3,3 * 3 or sqrt 19) or enter 'ex' to exit'").strip()

            if expression.lower() == 'ex':
                print("goodbye")
                break
            if expression.startswith(('sin', 'cos', 'tan', 'log', 'ln', 'sqrt')):
                parts = expression.split()
                if len(parts) != 2:
                    print("invalid expression")
                    continue


                func = parts[0].lower()
                num  = float(parts[1])


                if func == 'sqrt':
                    if num < 0:
                        print("wrong input")
                    else:
                        result = math.sqrt(num)
                        print(f"sqrt{num} = {result}")



                elif func == 'sin':
                     result = math.sin(math.radians(num))
                     print(f"sin{num} = {result}")


                elif func == 'cos':
                    result = math.cos(math.radians(num))
                    print(f"cos{num} = {result}")


                elif func == 'tan':
                    if num % 180 == 90:
                        print("wrong input")
                    else:
                        result = math.tan(math.radians(num))
                        print(f"tan{num} = {result}")


                elif func == 'lg':
                    if num < 0:
                        print("wrong input")
                    else:
                        result = math.log(num,10)
                        print(f"lg{num} = {result}")


                elif func == 'ln':
                    if num <= 0:
                        print("wrong input")
                    else:
                        result = math.log(num)
                        print(f"ln{num} = {result}")
            else:
                parts = expression.split()
                if len(parts) != 3:
                    print("wrong expression")
                    continue

                num1 = float(parts[0])
                num2 = float(parts[2])
                operator =parts[1]


                if operator == '+':
                    result = num1+num2
                    print(f"{num1} + {num2} = {result}")


                elif operator == '-':
                    result = num1-num2
                    print(f"{num1} - {num2} = {result}")

                elif operator == '*':
                    result = num1*num2
                    print(f"{num1} * {num2} = {result}")


                elif operator == '/':
                    if num2 == 0:
                        print("wrong input!")
                    else:
                        result = num1/num2
                        print(f"{num1} / {num2} = {result}")
                elif operator == '^':
                    result = num1**num2
                    print(f"{num1}^{num2} = {result}")


                elif operator == '%':
                    result = num1%num2
                    print(f"{num1} % {num2} = {result}")




                else:
                    print(f"{operator} is not be supported")
        except ValueError:
            print("invalid expression")
        except Exception as e:
            print(f"wrong expression: {e}")


if __name__ == "__main__":
    simple_calculator()


