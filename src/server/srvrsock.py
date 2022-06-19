import socket
from dotenv import dotenv_values
import tictactoe.tictactoeServer as tttS

# HOST = socket.gethostbyname(socket.gethostname()) <- returns loopback ip, not sure why
# HOST = dotenv_values("../.env")['PRIVATE_IP_ADDRESS'] <- TODO: script private ip via hostname -I 

tttGames = tttS.TicTacToeSrvr()


tttSwitcher = {"1": tttGames.initiate_game_data, "2": tttGames.initiate_game_start, 
    "3": tttGames.deny_game_start, "4": tttGames.move_player, "5": tttGames.end_game,
    "6": tttGames.autoplay}


#internet, tcp
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((dotenv_values("../../.env")['HOST'], int(dotenv_values("../../.env")['PORT'])))

server.listen()
print(f"Server listening")

while True:
    # accept all connections to obtain return values of connection socket to use for comm and client's address
    conn_socket, address = server.accept()
    msg = conn_socket.recv(1024).decode("utf-8")
    func = msg[0]
    msg_data = msg[2:]
    ret_msg = "Error: "

    try:
        ret_msg=tttSwitcher[func](msg_data)
        
    except:
        ret_msg += "server unable to find request function"
    
    # ret_msg += "server unable to find request function"
    conn_socket.send(ret_msg.encode('utf-8'))
    conn_socket.close()

# TODO: capture ctrl+c, to exit gracefully