import random,time

combinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
positions = [i for i in range(1,10)]
occupied =[]
def gameBoard():
    print(f"""

        {positions[0]} | {positions[1]} | {positions[2]}
       -----------
        {positions[3]} | {positions[4]} | {positions[5]}
       -----------
        {positions[6]} | {positions[7]} | {positions[8]}
            """)

def userMove(ch):
    pos = int(input("Enter Position :"))
    positions[pos-1] = ch
    occupied.append(pos)
    gameBoard()
    msg=checkWinner(pos,ch)
    return msg


def cpuMove(cpu_ch):
    cpu_pos = random.randint(1,9)
    print(f"cpu picked {cpu_pos}")
    if cpu_pos in occupied:
        cpuMove(cpu_ch)
        msg=checkWinner(cpu_pos,cpu_ch)
        return msg
    else:
        positions[cpu_pos-1] = cpu_ch
        gameBoard()
        occupied.append(cpu_pos)
        msg=checkWinner(cpu_pos,cpu_ch)
        return msg
        
def checkWinner(pos,ch):
    for i in range(len(combinations)):
        if pos in combinations[i]:
            index = combinations[i].index(pos)
            combinations[i][index] = ch

    for i in range(len(combinations)):
        if combinations[i][0]==ch and combinations[i][1]==ch and combinations[i][2]==ch:
            return "Wins"
            
    

def main():
    print("Welcome to Tic tac Toe".center(60,"*"))
    gameBoard()
    ch = input("enter your choice : X | 0 : ")
    print(f"you have picked : {ch}")
    if ch == 'X' or ch== 'x':
        cpu_ch = 0
    elif ch == '0':
        cpu_ch = 'X'
        
    while True:
        msg=userMove(ch)
        if msg=="Wins":
            print("User Wins")
            break
        time.sleep(5)
        msg=cpuMove(cpu_ch)
        if msg=="Wins":
            print("CPU Wins")
            break

main()
        
