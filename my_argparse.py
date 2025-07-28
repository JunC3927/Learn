import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--epochs',type=int,default=20,help='训练轮数')
parser.add_argument('--lr',type=float,default=1e-3,help='学习率')
parser.add_argument('--batch_size',type=int,default=64,help='批大小')
parser.add_argument('--cuda',action='store_true',help='训练设备')

args = parser.parse_args()
print(args.epochs)
print(args.lr)
print(args.cuda)