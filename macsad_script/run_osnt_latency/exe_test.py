import threading
import time
import re
import subprocess
import os
import argparse
import sys

#mac_directory= '/root/Juan/mac_16'  

osnt="python osnt-tool-cmd.py -ifp0 "
traces_l2= "../traces/ipv4_1_entries/ipv4_1_random." 
traces_nat_dl= "/home/sunnet/topicos_sistemas/nat_mac/PCAP/1entry_nat_dl/nfpa.trPR_nat_dl_1_random." 
traces_nat_ul= "/home/sunnet/topicos_sistemas/nat_mac/PCAP/1entry_nat_ul/nfpa.trPR_tcp_1_random." 

values=" -flt ../filter.cfg -rpn0 300 -lpn 300 -lty3 -rnm -ipg0 1000000 "


def exec_func(traces, size, args, num):

   if (size == 128):
     cmd= osnt + traces + str(size) + "bytes.cap "+values+"-txs0 7 -rxs3 8"+ " -llog " + args.pktio_env+"_"+ str(psize)+"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)

   elif (size == 256):
     cmd= osnt + traces + str(size) + "bytes.cap "+values+"-txs0 9 -rxs3 10"+ " -llog " +  args.pktio_env+"_"+ str(psize)+"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)
   
   elif (size == 512):
     cmd=osnt + traces + str(size) + "bytes.cap "+values+"-txs0 9 -rxs3 10"+ " -llog " + args.pktio_env+"_"+ str(psize) +"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)
   
   elif (size == 1024):
     cmd=osnt + traces + str(size) + "bytes.cap "+values+"-txs0 12 -rxs3 13"+ " -llog " + args.pktio_env+"_"+ str(psize)+"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)
   
   elif (size == 1280):
     cmd=osnt + traces + str(size) + "bytes.cap "+values+"-txs0 11 -rxs3 12"+ " -llog "+  args.pktio_env+"_"+ str(psize)+"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)
   
   elif (size == 1518):
     cmd=osnt + traces + str(size) + "bytes.cap "+values+"-txs0 12 -rxs3 13"+ " -llog "+ args.pktio_env+"_"+ str(psize)+"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)
   
   else: 
     print "put other value like: 128, 256, 512, 1024, 1280, 1518"


lst_psize= [128, 256, 512, 1024, 1280, 1518] 
#lst_psize= [256, 512]


#python osnt-tool-cmd.py -ifp0 ../traces/ipv4_1_entries/ipv4_1_random.256bytes.cap -flt ../filter.cfg -rpn0 300 -lpn 300 -lty3 -rnm -ipg0 10000 -ipg3 10000 -txs0 7 -rxs3 8   

#Main funcion
if __name__ == '__main__':


    parser = argparse.ArgumentParser(description = 'Um programa de exemplo.')
    parser.add_argument("-s", "--psize", action= "store", dest="psize",
                      default = "128", required = False,
                      help="Output file test name ")

    parser.add_argument("-e", "--env", action="store", dest="pktio_env",
                      default= '0', required = False,
                      help="Choose the pktio enviroment/s to compile with MACSAD core i.e 0=l2, 1=l3, 2=nat_ul, 3=nat_dl")


    parser.add_argument("-t", "--test", action="store", dest="set_test",
                      default= '0', required = False,
                      help="Choose the pktio enviroment/s to compile with MACSAD core i.e 0=l2, 1=l3, 2=nat_ul, 3=nat_dl")
    parser.add_argument("-r", "--rate", action="store", dest="rate",
                      default= '0', required = False,
                      help="Choose the rate to do a throughput test")
    arguments = parser.parse_args() 

#pr int "leee " + str(len(dic[arguments.pktio_env]))


      



    if (arguments.pktio_env == '0') or (arguments.pktio_env == '1'): 
      print "l2" 
    
    
      if (arguments.set_test == "1"): 
         for i in range(5): 
            for psize in lst_psize:                                                      
                print "set of tests for diferents packet sizes"                           
                print "test  "+ str(lst_psize)     
                #cmd= osnt + traces_l2 + arguments.psize + "bytes.cap "+values+"-txs0 7 -rxs3 8 " + " -llog "+ arguments.psize+"_"+ str(psize)+"_num_"+str(i)   
                #print "command= "+ cmd 
                #os.system(cmd)
    
            
                #os.chdir(nfpa_directory)                                                
                if (psize == 128):
                  cmd= osnt + traces_l2 + str(psize) + "bytes.cap "+values+"-txs0 7 -rxs3 8" + " -llog "+ arguments.pktio_env+"_"+ str(psize)+"_num_"+str(i)  
                  print "command= "+ cmd 
                  os.system(cmd)
    
                elif (psize == 256):
                  cmd= osnt + traces_l2 + str(psize) + "bytes.cap "+values+"-txs0 7 -rxs3 8" + " -llog "+ arguments.pktio_env+"_"+ str(psize)+"_num_"+str(i)
                  print "command= "+ cmd 
                  os.system(cmd)
                
                elif (psize == 512):
                  cmd=osnt + traces_l2 + str(psize) + "bytes.cap "+values+"-txs0 7 -rxs3 8" + " -llog "+ arguments.pktio_env+"_"+ str(psize)+"_num_"+str(i)
                  print "command= "+ cmd 
                  os.system(cmd)
                
                elif (psize == 1024):
                  cmd=osnt + traces_l2 + str(psize) + "bytes.cap "+values+"-txs0 9 -rxs3 10" + " -llog "+ arguments.pktio_env+"_"+ str(psize)+"_num_"+str(i)
                  print "command= "+ cmd 
                  os.system(cmd)
                
                elif (psize == 1280):
                  cmd=osnt + traces_l2 + str(psize) + "bytes.cap "+values+"-txs0 10 -rxs3 11" + " -llog "+ arguments.pktio_env+"_"+ str(psize)+"_num_"+str(i)
                  print "command= "+ cmd 
                  os.system(cmd)
                
                elif (psize == 1518):
                  cmd=osnt + traces_l2 + str(psize) + "bytes.cap "+values+"-txs0 10 -rxs3 11" + " -llog "+ arguments.pktio_env+"_"+ str(psize)+"_num_"+str(i)
                  print "command= "+ cmd 
                  os.system(cmd)
                
                else: 
                  print "put other value like: 128, 256, 512, 1024, 1280, 1518"
                   
                                                                                        
                time.sleep(1)    
    
           
      elif (arguments.rate == "1"):
       
         cmd= "python osnt-tool-cmd.py -ifp0 ../traces/ipv4_l2_100_pcap/ipv4_100_random."+arguments.psize + "bytes.cap -rpn0 10000000000 -run -st -ds"
         print "command= "+ cmd 
         os.system(cmd)
    
    elif (arguments.pktio_env == '2'): 
      print "nat_ul"
      if (arguments.set_test == "1"): 
         for i in range(5): 
            for psize in lst_psize:                                                      
              exec_func(traces_nat_ul, psize, arguments, i)
         #md= "cat -n tcpdump_"+arguments.pktio_env+"1280_num_4 | grep -n ^ | grep ^302  
      elif (arguments.rate == "1"):
         cmd= "python osnt-tool-cmd.py -ifp0 /home/sunnet/topicos_sistemas/nat_mac/PCAP/1entry_nat_ul/nfpa.trPR_tcp_1_random."+ arguments.psize+ "bytes.cap -rpn0 100000000 -run -st -ds "
         print "command= "+ cmd 
         os.system(cmd)
      else:
         exec_func(traces_nat_ul, int(arguments.psize), arguments)
    
    elif (arguments.pktio_env == '3'): 
      print "nat_dl"
      if (arguments.set_test == "1"):  
         for i in range(5): 
            for psize in lst_psize:                                                      
              exec_func(traces_nat_dl, psize, arguments, i)


           
      elif (arguments.rate == "1"):
         cmd= "python osnt-tool-cmd.py -ifp0 /home/sunnet/topicos_sistemas/nat_mac/PCAP/1entry_nat_dl/nfpa.trPR_nat_dl_1_random."+ arguments.psize+ "bytes.cap -rpn0 100000000 -run -st -ds "
         print "command= "+ cmd 
         os.system(cmd)


      else:
         exec_func(traces_nat_ul, int(arguments.psize))
      #exec_func(arguments,traces_nat_dl)
     
    print "ENDING PROGRAM"







