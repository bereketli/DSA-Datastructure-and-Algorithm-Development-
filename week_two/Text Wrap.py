import textwrap

def wrap(string, max_width):
    soln = ""
    for i in range(len(string)): 
        soln += string[i]
        if (i+1) % max_width == 0:
            soln += "\n"
         
         
            
    return soln

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)