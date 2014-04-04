import libvirt
import sys

def usage():
  print "Usage : python start.py <domian_name>"
  sys.exit(-1)

if __name__ == "__main__":

  try:
    domain_name =  sys.argv[1]
  except:
    usage()

  #connect to hypervisor running on localhost
  conn = libvirt.open('xen:///')
  # domain name : 'ubuntu-12.04'
  dom0 = conn.lookupByName(domain_name)
  dom0.shutdown()
