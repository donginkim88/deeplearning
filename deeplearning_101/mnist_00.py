import sys, os
sys.path.append(os.pardir)  #allow python to look at the parents' dir for modules
# print(sys.path)

from dataset.mnist import load_mnist
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape, t_train.shape, x_test.shape, t_test.shape)

