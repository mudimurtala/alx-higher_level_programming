infile = open('values.txt', 'rt')
outfile = open('values-total.txt', 'wt')
print('Processing input')
sum = 0
for line in infile:
    sum += int(line)
    print(line.rstrip(), file=outfile)
print('\nTotal:' + str(sum), file=outfile)
outfile.close()
infile.close()
print('Output complete')