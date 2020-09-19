from collections import defaultdict, Counter
import itertools
import math
import random
from pprint import pprint
from data import data


class BayesNet(object):
    "Bayesian network: a graph of variables connected by parent links."

    def __init__(self):
        self.variables = []  # List of variables, in parent-first topological sort order
        self.lookup = {}  # Mapping of {variable_name: variable} pairs

    def add(self, name, parent_names, cpt):
        "Add a new Variable to the BayesNet. parent_names must have been added previously."
        parents = [self.lookup[name] for name in parent_names]
        var = Variable(name, cpt, parents)
        self.variables.append(var)
        self.lookup[name] = var
        return self


class Variable(object):
    "A discrete random variable; conditional on zero or more parent Variables."

    def __init__(self, name, cpt, parents=()):
        "A variable has a name, list of parent variables, and a Conditional Probability Table."
        self.__name__ = name
        self.parents = parents
        self.cpt = CPTable(cpt, parents)
        self.domain = set(itertools.chain(*self.cpt.values()))  # All the outcomes in the CPT

    def __repr__(self): return self.__name__


class Factor(dict): "An {outcome: frequency} mapping."


class ProbDist(Factor):
    """A Probability Distribution is an {outcome: probability} mapping.
    The values are normalized to sum to 1.
    ProbDist(0.75) is an abbreviation for ProbDist({T: 0.75, F: 0.25})."""

    def __init__(self, mapping=(), **kwargs):
        if isinstance(mapping, float):
            mapping = {T: mapping, F: 1 - mapping}
        self.update(mapping, **kwargs)
        normalize(self)


class Evidence(dict):
    "A {variable: value} mapping, describing what we know for sure."


class CPTable(dict):
    "A mapping of {row: ProbDist, ...} where each row is a tuple of values of the parent variables."

    def __init__(self, mapping, parents=()):
        """Provides two shortcuts for writing a Conditional Probability Table.
        With no parents, CPTable(dist) means CPTable({(): dist}).
        With one parent, CPTable({val: dist,...}) means CPTable({(val,): dist,...})."""
        if len(parents) == 0 and not (isinstance(mapping, dict) and set(mapping.keys()) == {()}):
            mapping = {(): mapping}
        for (row, dist) in mapping.items():
            if len(parents) == 1 and not isinstance(row, tuple):
                row = (row,)
            self[row] = ProbDist(dist)


class Bool(int):
    "Just like `bool`, except values display as 'T' and 'F' instead of 'True' and 'False'"
    __str__ = __repr__ = lambda self: 'T' if self else 'F'


T = Bool(True)
F = Bool(False)


def P(var, evidence={}):
    "The probability distribution for P(variable | evidence), when all parent variables are known (in evidence)."
    row = tuple(evidence[parent] for parent in var.parents)
    return var.cpt[row]


def normalize(dist):
    "Normalize a {key: value} distribution so values sum to 1.0. Mutates dist and returns it."
    total = sum(dist.values())
    for key in dist:
        dist[key] = dist[key] / total
        assert 0 <= dist[key] <= 1, "Probabilities must be between 0 and 1."
    return dist


def sample(probdist):
    "Randomly sample an outcome from a probability distribution."
    r = random.random()  # r is a random point in the probability distribution
    c = 0.0  # c is the cumulative probability of outcomes seen so far
    for outcome in probdist:
        c += probdist[outcome]
        if r <= c:
            return outcome


def globalize(mapping):
    "Given a {name: value} mapping, export all the names to the `globals()` namespace."
    globals().update(mapping)


def joint_distribution(net):
    "Given a Bayes net, create the joint distribution over all variables."
    return ProbDist({row: prod(P_xi_given_parents(var, row, net)
                               for var in net.variables)
                     for row in all_rows(net)})


def all_rows(net): return itertools.product(*[var.domain for var in net.variables])


def P_xi_given_parents(var, row, net):
    "The probability that var = xi, given the values in this row."
    dist = P(var, Evidence(zip(net.variables, row)))
    xi = row[net.variables.index(var)]
    return dist[xi]


def prod(numbers):
    "The product of numbers: prod([2, 3, 5]) == 30. Analogous to `sum([2, 3, 5]) == 10`."
    result = 1
    for x in numbers:
        result *= x
    return result


def enumeration_ask(X, evidence, net):
    "The probability distribution for query variable X in a belief net, given evidence."
    i = net.variables.index(X)  # The index of the query variable X in the row
    dist = defaultdict(float)  # The resulting probability distribution over X
    for (row, p) in joint_distribution(net).items():
        if matches_evidence(row, evidence, net):
            pprint(matches_evidence(row, evidence, net))
            dist[row[i]] += p
    return ProbDist(dist)


def matches_evidence(row, evidence, net):
    "Does the tuple of values for this row agree with the evidence?"
    return all(evidence[v] == row[net.variables.index(v)]
               for v in evidence)

def calculate(X, evidence, true_false, net):
    "The probability distribution for query variable X in a belief net, given evidence."
    i = net.variables.index(X)  # The index of the query variable X in the row
    dist = defaultdict(float)  # The resulting probability distribution over X
    for (row, p) in joint_distribution(net).items():
        if matches_evidence(row, evidence, net):
            #pprint(matches_evidence(row, evidence, net))
            dist[row[i]] += p
    if (true_false):
        return dist[1]
    else:
        return dist[0]


def entropy(probdist):
    "The entropy of a probability distribution."
    return - sum(p * math.log(p, 2)
                 for p in probdist.values())


def create_test_net():
    test_net = (BayesNet()
                 .add('Burglary', [], 0.001)
                 .add('Earthquake', [], 0.002)
                 .add('Alarm', ['Burglary', 'Earthquake'], {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001})
                 .add('JohnCalls', ['Alarm'], {T: 0.90, F: 0.05})
                 .add('MaryCalls', ['Alarm'], {T: 0.70, F: 0.01}))
    return test_net


def create_bayes_net():
    bayes_net = (BayesNet()
                 .add('IW', [], data.get('IW'))
                 .add('B', ['IW'], data.get('B'))
                 .add('SM', ['IW'], data.get('SM'))
                 .add('R', ['B'], data.get('R'))
                 .add('I', ['B'], data.get('I'))
                 .add('G', [], data.get('G'))
                 .add('S', ['I', 'SM', 'G'], data.get('S'))
                 .add('M', ['S'], data.get('M')))

    return bayes_net


def format_input(user_input):
    if (len(user_input) <= 1):
        exit('Please enter a valid input.')
    evidence_dict = {}
    x = []
    show_true = ''
    show_true = user_input.split(',')[0].split('=')[1]
    x.append(user_input.split(',')[0].split('=')[0])
    if x[0] == 'IW':
        x[0] = IW
    if x[0] == 'B':
        x[0] = B
    if x[0] == 'R':
        x[0] = R
    if x[0] == 'I':
        x[0] = I
    if x[0] == 'SM':
        x[0] = SM
    if x[0] == 'G':
        x[0] = G
    if x[0] == 'S':
        x[0] = S
    if x[0] == 'M':
        x[0] = M
    evidence = user_input.split(',')
    iterevidence = iter(evidence)
    next(iterevidence)
    for i in iterevidence:
        i = i.split('=')
        if i[0] == 'IW':
            i[0] = IW
        if i[0] == 'B':
            i[0] = B
        if i[0] == 'R':
            i[0] = R
        if i[0] == 'I':
            i[0] = I
        if i[0] == 'SM':
            i[0] = SM
        if i[0] == 'G':
            i[0] = G
        if i[0] == 'S':
            i[0] = S
        if i[0] == 'M':
            i[0] = M
        if i[1] == 'true':
            i[1] = T
        if i[1] == 'false':
            i[1] = F
        evidence_dict[i[0]] = i[1]

    if show_true == 'true':
        show_true = 1
    if show_true == 'false':
        show_true = 0

    return(x[0], evidence_dict, show_true)


if __name__ == '__main__':
    bayes_net = create_bayes_net()
    globalize(bayes_net.lookup)
    user_query = '';

    while (user_query != 'exit'):
        user_query = input('Enter query: ')
        command = format_input(user_query)
        print("Result: ", calculate(command[0], command[1], command[2], bayes_net))
