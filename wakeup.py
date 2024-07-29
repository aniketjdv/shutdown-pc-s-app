# import socket
# import struct
# def wake_on_lan(mac_address, broadcast_address):
#     # Create a magic packet
#     magic_packet = b'\xff' * 6 + bytes.fromhex(mac_address.replace(':', '')) * 16
    
#     # Send the magic packet
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#         sock.sendto(magic_packet, (broadcast_address, 9))
#         print(f"Magic packet sent to {mac_address} ({broadcast_address})")
#     except socket.error as e:
#         print(f"Failed to send magic packet: {e}")


# if __name__=="__main__":
#     wake_on_lan("30:E1:71:7D:6D:35","192.168.1.255")


import socket
import struct

def wake_on_lan(mac_address, broadcast_address):
    try:
        # Create a magic packet
        magic_packet = b'\xff' * 6 + bytes.fromhex(mac_address.replace(':', '')) * 16
        
        # Send the magic packet
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, (broadcast_address, 9))
        print(f"Magic packet sent to {mac_address} ({broadcast_address})")
        
    except OSError as e:
        print(f"OS error: {e}")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        wake_on_lan("30:E1:71:7D:6D:35", "192.168.1.255")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"Error: {e}")