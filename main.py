from BayesNet import BayesNet, T, F, P, globalize, enumeration_ask


def create_bayes_net():
    bayes_net = (BayesNet()
                 .add('IcyWeather', [], 0.5)
                 .add('Battery', ['IcyWeather'], {T: 0.8, F: 0.2})
                 .add('StarterMotor', ['IcyWeather'], {T: 0.7, F: 0.3})
                 .add('Radio', ['Battery'], {T: 0.9, F: 0.1})
                 .add('Ignition', ['Battery'], {T: 0.6, F: 0.4})
                 .add('Gas', [], 0.9)
                 .add('Starts', ['Ignition', 'StarterMotor', 'Gas'], {(T, T, T): 0.378, (T, T, F): 0.988,
                                                                      (T, F, F): 0.154, (F, F, F): 0.012,
                                                                      (T, F, T): 0.988, (F, T, F): 0.154,
                                                                      (F, T, T): 0.988, (F, F, T): 0.154})
                 .add('Moves', ['Starts'], {T: 0.378, F: 0.622}))


    alarm_net = (BayesNet()
                 .add('Burglary', [], 0.001)
                 .add('Earthquake', [], 0.002)
                 .add('Alarm', ['Burglary', 'Earthquake'], {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001})
                 .add('JohnCalls', ['Alarm'], {T: 0.90, F: 0.05})
                 .add('MaryCalls', ['Alarm'], {T: 0.70, F: 0.01}))

    return bayes_net


if __name__ == '__main__':
    bayes_net = create_bayes_net()
    globalize(bayes_net.lookup)
    print(bayes_net.variables)
    print(P(Battery))
