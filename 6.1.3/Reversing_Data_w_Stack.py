# reversing data using a stack
def reverse_file(filename):
    '''Overite given file with its conent line-by-line reserved'''
    
    S = Arraystack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()
    
    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()
    
file = open("initial.txt", 'w')
file.write("I am going home.\n")
file.write("Today is a holiday.")
file.close()

!cat initial.txt
print(`\n\n`)
reverse_file("initial.txt")
!cat initial.txt