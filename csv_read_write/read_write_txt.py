

with open('read_file.txt','r') as rf:
    with open('write_file.txt','w') as wf:
        for line in rf:
            wf.write(line)

with open('details_copy.txt','r') as rf:
    with open('write_file.txt','w') as wf:
        for line in rf:
            wf.write(line)

