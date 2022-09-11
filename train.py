import argparse
import pathlib
import pickle

parser = argparse.ArgumentParser(description='Training')
parser.add_argument('--input-dir', type=str, help='Directory of input data')
parser.add_argument('--model', type=str, help='File with model')
args = parser.parse_args()


class word(object):
    badch = [',', '.', ':', '!', '?', ';', '”', '"', '“', '-', '—', ' ', '«', '»', '(', ')', '{', '}', '[', ']']

    def clean(self, s):
        s = s.strip()
        for i in self.badch:
            s = s.replace(i, '')
        s = s.lower()
        return s


class machine(object):
    data = []

    def collectdata(self):
        hlp = word()
        if args.input_dir is None:
            s = input().strip()
            while s:
                res = s.split()
                for i in res:
                    i = hlp.clean(i)
                    if len(i) > 0:
                        self.data += [i]
                s = input().strip()
        else:
            lib = pathlib.Path(args.input_dir)
            for currentFile in lib.iterdir():
                with open(currentFile,  'r', encoding="utf-8") as inp:
                    res = []
                    for ch in inp:
                        res = ch.split()
                        for i in res:
                            i = hlp.clean(i)
                            if len(i) > 0:
                                self.data += [i]



now = machine()
now.collectdata()
model = {1: {}, 2: {}, 3: {}, 4: {}}
pref = []
sm = 0.0
for i in range(1, 5):
    for y in range(0, len(now.data) - i):
        pref.clear()
        pref = now.data[y:y+i]
        gd = str(pref)
        if gd not in model[i]:
            model[i][gd] = {}
        if now.data[y+i] in model[i][gd]:
            model[i][gd][now.data[y+i]] += 1
        else:
            model[i][gd][now.data[y+i]] = 1
    for y in model[i]:
        sm = 0.0
        for j in model[i][y]:
            sm += model[i][y][j]
        for j in model[i][y]:
            model[i][y][j] /= sm
pickle_out = open(args.model, "wb")
pickle.dump(model, pickle_out)
pickle_out.close()







