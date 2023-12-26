import numpy as np
import neurolab as nl

target = [[1, 0, 0, 1, 0,
           1, 0, 1, 0, 0,
           1, 1, 0, 0, 0,
           1, 0, 1, 0, 0,
           1, 0, 0, 1, 0],
          [1, 1, 1, 1, 1,
           1, 0, 0, 0, 1,
           1, 0, 0, 0, 1,
           1, 0, 0, 0, 1,
           1, 1, 1, 1, 1],
          [0, 0, 1, 0, 0,
           0, 0, 1, 0, 0,
           0, 0, 1, 0, 0,
           0, 0, 1, 0, 0,
           0, 0, 1, 0, 0]]

chars = ['K', 'O', 'I']
target = np.asfarray(target)
target[target == 0] = -1

# Create and train network
net = nl.net.newhop(target)

output = net.sim(target)
print("Test on train samples:")
for i in range(len(target)):
    print(chars[i], (output[i] == target[i]).all())

print("\nTest on defaced I:")
test = np.asfarray([0, 0, 1, 0, 0,
                    0, 0, 1, 0, 0,
                    0, 0, 1, 0, 0,
                    0, 0, 1, 0, 0,
                    0, 1, 0, 0, 0])
test[test == 0] = -1
out = net.sim([test])
print((out[0] == target[0]).all(), 'Sim. steps', len(net.layers[0].outs))
