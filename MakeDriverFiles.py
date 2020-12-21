import os

def MakeDriverFiles():
  names =[ '_interface.h','_config.h','_private.h','_program.c']
  header=['_INTERFACE_H_','_CONFIH_H_','_PRIVATE_H_','_PROGRAM_C_']
  DriverName=input('What is your driver name : ')
  #Make dir
  os.mkdir(DriverName)
  #Enter dir 
  os.chdir(DriverName)


#Store the contents of the file that has your headers comments
  f0=open('../HeaderComments.txt','r')
  contents=f0.read()		
  #print(contents)
  f0.close()
  
    #Start making .h files
  for i in range(4):
      f=open(DriverName+names[i],'w')
      f.write(contents+'\n')	#insert header commentes
      f.write("#ifndef "+DriverName+header[i]+'\n')	#write header guards
      f.write('#define '+DriverName+header[i]+'\n')
      f.write('\n'*10+'#endif ')		#leave some space
      f.close()
  
  #Make .c file
  f=open(DriverName+names[3],'w')
  f.write(contents+'\n')	#insert header commentes
  #open xxxx_program.c to include librares and other files
  f=open(DriverName+'_program.c','r+')
  f.write(contents+'\n')	#insert header commentes
  #write libraries
  f.write('#include "STD_TYPES.h"')
  f.write('\n')
  f.write('#include "BIT_MATH.h"')
  f.write('\n')
  for i in range (3):
      f.write('#include "'+DriverName+names[i]+"\"")
      f.write('\n')
  #close file 
  f.close()
  print('Done ... \n')


def main():
   MakeDriverFiles()

if __name__ == '__main__':
  main()
