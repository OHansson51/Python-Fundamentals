'''
Name: Corin Chepko
Date: 10/23/23
Program Description: https://open.kattis.com/problems/imagedecoding
'''
def test():
    pass

def image_decode(scan_lines):
    pix_sym = ('#','.')
    pixels = 0
    image = []
    error_cond = False
    last_num_pix = 0
    if(scan_lines == []):
        return ''
    for i in range(len(scan_lines)):
        num_pix_in_line = 0
        
        line = scan_lines[i].split() 
        out_line = ""
        if(line[0] == '#'):
            sym = 0
        else:
            sym = 1
        
        for index in range(1,len(line)):
            added = pix_sym[sym]
            added = added*int(line[index])
            num_pix_in_line += int(line[index])
            out_line += added
            sym = (sym+1)%2
        #print(out_line)
        image.append(out_line)
        if((i!=0) and (num_pix_in_line != last_num_pix)):
            error_cond = True
        last_num_pix = num_pix_in_line
    ans = '\n'.join(image)
    if(error_cond == True):
        #print("Error decoding image")
        ans += "\nError decoding image"

    return ans

def main():
    
    num_lines = int(input())
    while(num_lines != 0):
        if(num_lines != 0):
            scan_lines = []
            for i in range(num_lines):
                scan_lines.append(input())

            out_lines = image_decode(scan_lines)
            print(out_lines)
        else:
            return
        num_lines = int(input())
        if(num_lines != 0): # Stupid Kattis! Need extra logic to make sure 
            print()

    
        
   #    scan_lines = int(input())

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()