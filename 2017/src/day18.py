# Day 18: Duet (Musical Assembly)


def compile1(lines):
    reg = {}
    pos = 0
    snd = -1

    def radd(a):
        if a not in reg:
            reg[a] = 0

    def rval(a):
        if a in reg:
            return reg[a]
        else:
            return int(a)

    while 0 <= pos < len(lines):
        line = lines[pos]
        args = line.split()[1:]
        if 'snd' in line:
            snd = rval(args[0])
        elif 'set' in line:
            radd(args[0])
            reg[args[0]] = rval(args[1])
        elif 'add' in line:
            radd(args[0])
            reg[args[0]] += rval(args[1])
        elif 'mul' in line:
            radd(args[0])
            reg[args[0]] *= rval(args[1])
        elif 'mod' in line:
            radd(args[0])
            reg[args[0]] %= rval(args[1])
        elif 'jgz' in line:
            if rval(args[0]) != 0:
                pos += rval(args[1])
                continue
        elif 'rcv' in line:
            if rval(args[0]) > 0:
                rcv = snd
                print('Recovered: ', rcv)
                break
        pos += 1


def compile2(lines):
    duet = (DuetAssembly(lines), DuetAssembly(lines))
    for i in (0, 1):
        duet[i].reg['p'] = i
    state = [False, False]

    while sum(state) < 2:
        for i in (0, 1):
            try:
                duet[i].exe()
            except RuntimeError:
                state[i] = True

        for i in (0, 1):
            if duet[i].snd:
                duet[1 - i].rcv.append(duet[i].snd.pop(0))

    print('P1 Sent: ', duet[1].snd_counter)


class DuetAssembly:

    def __init__(self, lines):
        self.lines = lines
        self.reg = {}
        self.pos = 0
        self.snd_counter = 0
        self.snd = []
        self.rcv = []

    def exe(self):
        line = self.lines[self.pos]
        args = line.split()[1:]
        if 'set' in line:
            self.radd(args[0])
            self.reg[args[0]] = self.rval(args[1])
        elif 'add' in line:
            self.radd(args[0])
            self.reg[args[0]] += self.rval(args[1])
        elif 'mul' in line:
            self.radd(args[0])
            self.reg[args[0]] *= self.rval(args[1])
        elif 'mod' in line:
            self.radd(args[0])
            self.reg[args[0]] %= self.rval(args[1])
        elif 'jgz' in line:
            if self.rval(args[0]) > 0:
                self.pos += self.rval(args[1])
                return
        elif 'rcv' in line:
            if self.rcv:
                self.reg[args[0]] = self.rcv.pop(0)
            else:
                raise RuntimeError
        elif 'snd' in line:
            self.snd.append(self.rval(args[0]))
            self.snd_counter += 1
        self.pos += 1

    def exit(self):
        return not 0 <= self.pos < len(self.lines)

    def radd(self, a):
        if a not in self.reg:
            self.reg[a] = 0

    def rval(self, a):
        if a in self.reg:
            return self.reg[a]
        else:
            return int(a)


if __name__ == '__main__':
    file = open('../assets/day18_input.txt').readlines()
    compile1(file)
    compile2(file)
