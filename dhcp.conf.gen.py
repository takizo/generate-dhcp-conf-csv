#!/opt/local/bin/python

with open("machine.csv") as f:
    array = []

    for line in f:
        array.append(line)

    for etc in array:
        x =  etc.split(',')
        hosta = """host %s-ipmi {\n\thardware ethernet %s;\n\tfixed-address %s;\n}
host %s-1GA {\n\thardware ethernet %s;\n\tfixed-address %s;\n}
host %s-1GB {\n\thardware ethernet %s;\n\tfixed-address %s;\n}
host %s-10GA {\n\thardware ethernet %s;\n\tfixed-address %s;\n}
host %s-10GB {\n\thardware ethernet %s;\n\tfixed-address %s;\n}"""

        print hosta % (x[0], x[2], x[1], x[0], x[4], x[3], x[0], x[6], x[5], x[0], x[8], x[7], x[0], x[10], x[9])
