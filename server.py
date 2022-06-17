import socket
from dotenv import dotenv_values
import server_funcs.tictactoeServer

# HOST = socket.gethostbyname(socket.gethostname()) <- returns loopback ip, not sure why
# HOST = dotenv_values(".env")['PRIVATE_IP_ADDRESS'] <- private ip via hostname -I

i_g_d = getattr(server_funcs.tictactoeServer, 'initiate_game_data')
i_g_s = getattr(server_funcs.tictactoeServer, 'initiate_game_start')
d_g_s = getattr(server_funcs.tictactoeServer, 'deny_game_start')
m_p = getattr(server_funcs.tictactoeServer, 'move_player')
e_g = getattr(server_funcs.tictactoeServer, 'end_game')

tttSwitcher = {"1": i_g_d, "2": i_g_s, "3": d_g_s, "4": m_p, "5": e_g}

#internet, tcp
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((dotenv_values(".env")['HOST'], int(dotenv_values(".env")['PORT'])))

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
        print(func, tttSwitcher[func], msg_data)
        ret_msg=tttSwitcher[func](msg_data)
        
    except:
        ret_msg += "server unable to find request function"
    
    # ret_msg += "server unable to find request function"
    conn_socket.send(ret_msg.encode('utf-8'))
    conn_socket.close()

# TODO: capture ctrl+c, to exit gracefully