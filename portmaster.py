import sys
import socket
import subprocess
from datetime import datetime

# Banner Display 

print('''
\x1b[32m#**********************************************************************************************************************
# 8888888b.   .d88888b.  8888888b. 88888888888 888b     d888        d8888  .d8888b. 88888888888 8888888888 8888888b.  #
# 888   Y88b d88P" "Y88b 888   Y88b    888     8888b   d8888       d88888 d88P  Y88b    888     888        888   Y88b #
# 888    888 888     888 888    888    888     88888b.d88888      d88P888 Y88b.         888     888        888    888 #
# 888   d88P 888     888 888   d88P    888     888Y88888P888     d88P 888  "Y888b.      888     8888888    888   d88P #
# 8888888P"  888     888 8888888P"     888     888 Y888P 888    d88P  888     "Y88b.    888     888        8888888P"  #
# 888        888     888 888 T88b      888     888  Y8P  888   d88P   888       "888    888     888        888 T88b   #
# 888        Y88b. .d88P 888  T88b     888     888   "   888  d8888888888 Y88b  d88P    888     888        888  T88b  #
# 888         "Y88888P"  888   T88b    888     888       888 d88P     888  "Y8888P"     888     8888888888 888   T88b #
# 														      #
#  														      #
# PortMaster - All-in-one solution for lightning-fast port scanning and network reconnaissance.			      #														
# Coded by Anujaya Bhattarai 	 										      #
# ceo@trexif.com 							  					      #					# 
# TREXIF INCORPORATIONS  										              #
#**********************************************************************************************************************\x1b[0m
''')                                                                                                                    
                                                                                                                    
print("Please be patient and do not panic if the program seems stuck. It is still working.\n")                                                                                                       							    																



# Function Definitions 

def print_help():
    #Print usage instructions or help menu 
  
    print("Usage: python3 scanner.py -u/--host <ip1>,<ip2>,... [-p/--port <num_ports>] [-hl/--host-list <file_path>] [-oN/--output <filename>]")
    print("Options:")
    print("  -u, --host    Specify target host(s) (comma-separated list of IPs)")
    print("  -p, --port    Specify the number of ports to scan (default: 65535)")
    print("  -hl, --host-list Specify a file containing target hosts (one per line)")
    print("  -oN, --output Write output to a file named <filename>")
    sys.exit()

def is_host_up(host):
    #Check if the host is up.
    result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def scan_ports(targets, ports, output_file=None):

    # Scan ports on the specified targets.
  
    try:
        for target in targets:
            if is_host_up(target):
                # If the host is up, start scanning ports
                output = []  # List to store output lines
                output.append("=" * 74)
                output.append(f"Scanning targets: {target}")
                output.append(f"Time started: {datetime.now().strftime('%H:%M:%S')}")
                output.append("=" * 74)
                output.append(f"Host {target} is up. Starting TCP port scan...")
                output.append("{:<10} {:<6} {:<8}".format("PORT", "STATE", "SERVICE"))  # Header for port information
                closed_ports = 0  # Initialize count for closed ports
                for port in ports:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = s.connect_ex((target, port))
                    if result == 0:
                        try:
                            service = socket.getservbyport(port)
                        except OSError:
                            service = "unknown"
                        output.append("{:<10} {:<6} {}".format(port, "open", service))  # Append port, state, and service info
                    else:
                        closed_ports += 1  # Increment count for closed ports
                    s.close()
                output.append(f"Not shown: {closed_ports} closed tcp ports (reset)")  # Display count of closed ports
                
                # Print output to console
                for line in output:
                    print(line)
                
                # Write output to file if specified
                if output_file:
                    with open(output_file, 'a') as f:
                        for line in output:
                            f.write(line + "\n")
                        f.write("\n")

            else:
                print(f"Host {target} is not reachable. Skipping...")
    except KeyboardInterrupt:
        print("\nExiting the port scanner.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Could not connect to server.")
        sys.exit()

def main():
    """
    Main function to parse command line arguments and start scanning ports.
    """
    if len(sys.argv) < 2 or sys.argv[1] not in ["-u", "--host", "-hl", "--host-list"]:
        if len(sys.argv) == 2 and sys.argv[1] in ["-h", "--help"]:
            print_help()
        else:
            print("Invalid usage. Use -h or --help for usage instructions.")
            sys.exit()

    hosts = []
    ports = range(1, 65536)
    output_file = None

    # Error Handling If empty Syntax Is Entered 
    try:
    	# Parse command line arguments
        i = 1
        while i < len(sys.argv):
            if sys.argv[i] == "-u" or sys.argv[i] == "--host":
                hosts = sys.argv[i+1].split(",")
                i += 1
            elif sys.argv[i] == "-p" or sys.argv[i] == "--port":
                ports = range(1, int(sys.argv[i+1]) + 1)
                i += 1
            elif sys.argv[i] == "-oN" or sys.argv[i] == "--output":
                output_file = sys.argv[i+1]
                i += 1
            elif sys.argv[i] == "-hl" or sys.argv[i] == "--host-list":
                try:
                    with open(sys.argv[i+1], 'r') as file:
                        hosts = [line.strip() for line in file.readlines()]
                except FileNotFoundError:
                    print("Host list file not found.")
                    sys.exit()
                i += 1
            i += 1

        scan_ports(hosts, ports, output_file)
    except Exception:
    	print("Invalid usage. Use -h or --help for usage instructions." )

if __name__ == "__main__":
    main()

