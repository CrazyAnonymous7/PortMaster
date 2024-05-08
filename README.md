# PortMaster 
PortMaster is your go-to tool for lightning-fast port scanning and network reconnaissance. Developed in Python, PortMaster empowers security professionals, system administrators, and enthusiasts to quickly identify open ports, detect potential vulnerabilities, and assess network security posture with ease.

## Features
* **Host Discovery**: PortMaster offers flexible options for specifying target hosts, including single IP addresses, comma-separated lists of IPs, and host lists from files.
* **Port Scanning:**: Users can specify the number of ports to scan, enabling customized scans tailored to their specific requirements.
* **Service Detection:**: PortMaster detects open ports and identifies the associated services, providing detailed information about the services running on the target hosts..
* **Ping Functionality**: PortMaster includes ping functionality to check the availability of target hosts before initiating port scans, ensuring efficient resource utilization.
* **Output Options**: PortMaster supports both console output and file output, allowing users to save scan results for further analysis or documentation.

## Installation
### To use PortMaster, follow these steps:

##### 1. Clone the repository

      git clone https://github.com/CrazyAnonymous7/PortMaster 

##### 2. Navigate to the PortMaster directory:

       cd PortMaster


##### 3. Install the required dependencies

        pip3 install -r requirements.txt

## Usage

       python3 portmaster.py -u <ip1>,<ip2>,... [-p <num_ports>] [-oN <output_file>] [-hl <host_list_file>]

* **-u <ip1> ,<ip2>,... , --host <ip1> ,<ip2>,...**: Specify target host(s) (comma-separated list of IPs)
* **-p <num_ports> ,  --port <num_ports>** : Specify the number of ports to scan (default is 65535)
* **-oN <output_file>, --output <output_file>** :  Specify the output file to save scan results
* **-hl <host_list_file>, --help <host_file>**:  Specify a file containing a list of target hosts (one per line)

## Examples

### Scan All ports on a single host:

     python3 portmaster.py -u 192.168.1.1
### Scan All ports on multiple hosts
        python3 portmaster.py -u 192.168.1.1,192.168.1.2,192.168.1.3
        
### Scan All ports of multiple hosts with a host list file
          python3 portmaster.py -hl host_list.txt

### Scan All ports of multiple hosts with a host list file and save it to a file 
          python3 portmaster.py -hl host_list.txt -oN hosts_scan.txt

### Scan only Up to Some Ports 
          python3 portmaster.py -u 192.168.1.1 -p 1000


## License

#### PortMaster is licensed under the MIT License. See the LICENSE file for details.

## Author 
### PortMaster is created by :
#### Anujaya Bhattarai(CrazyAnonymous7)
#### ceo@trexif.com
#### TREXIF INCORPORATIONS

## Contributions
#### Contributions to PortMaster are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request on GitHub.

## Get Started:
#### Ready to take control of your network security? Clone the repository and start scanning with PortMaster today!
