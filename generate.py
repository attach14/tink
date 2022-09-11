import numpy
import pickle
import argparse

parser = argparse.ArgumentParser(description='Training')
parser.add_argument('--prefix', default=[], nargs='*', help='Beginning of the sentence')
parser.add_argument('--model', type=str, help='File with model')
parser.add_argument('--length', type=int, help='Length of the sentence')
args = parser.parse_args()

class rand(object):
    def choose(self, vas):
        a = []
        b = []
        for i in vas:
            a.append(i)
            b.append(vas[i])
        return numpy.random.choice(a, 1, b)

    def start(self, vas):
        a = []
        x = ""
        for i in vas:
            x = i[2:-2]
            a.append(x)
        return numpy.random.choice(a, 1)


pickle_in = open(args.model, "rb")
model = pickle.load(pickle_in)
sent = []
t = rand()
if len(args.prefix) == 0:
    g = t.start(model[1])
    sent.append(g[0])
else:
    sent = args.prefix
    for i in range(0, len(sent)):
        sent[i] = sent[i].lower()
ln = args.length
while len(sent) < ln:
    for k in range(min(len(sent), 4), 0, -1):
        f = str(sent[-k:])
        if f not in model[k]:
            continue
        g = t.choose(model[k][f])
        sent.append(g[0])
        break
for c in sent:
    print(c, end=" ")
