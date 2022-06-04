samples =[]

with open('ml-100k/new_udataset', 'w') as f:
    file_object = open('ml-100k/u.data', 'r')
    try:
        for line in file_object:
            parameters = line.split("\t")
            if len(parameters) == 4:
                parameters.pop()
            sample = " ".join(str(i) for i in parameters)
            sample = sample + '\n'
            samples.append(sample)
    finally:
        file_object.close()
    f.writelines(samples)
