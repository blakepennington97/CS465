import BayesNet


def example1():
    earthquake = BayesNet.Variable('Earthquake', 0.5)
    output = BayesNet.P(earthquake)
    print(output)


if __name__ == '__main__':
    example1()