class Solution:
    def interpret(self, command: str) -> str:
        index = 0
        output =[]
        while index < len(command):
            if command[index] == "G":
                output.append("G")
                index +=1
            elif command[index] == "(" and command[index + 1] == ")":
                output.append("o")
                index +=2
            else:
                output.append("al")
                index += 4
        return "".join(output)