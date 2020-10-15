import numpy as np
import json


def trunc(values, decs=0):
    return np.trunc(values*10**decs)/(10**decs)


class Grader(object):
    """docstring"""

    def __init__(self, yourname):
        """Constructor"""
        self.name = yourname
        self.ans = [0 for i in range(6)]
        self.values = np.array([
            120,
            35,
            10.023,
            0.40,
            0.66,
            1291.55
        ], dtype=float)
  
    def send(self, number, answer_input):
        """
        Send your n-th answer
        """      
        test = {
            number == 1: lambda ai: ai(5),
            number == 2: lambda ai: ai(7, 3),
            number == 3: lambda a: trunc(a.std(), 3),
            number == 4: lambda a: trunc(a, 2),
            number == 5: lambda a: trunc(a, 2),
            number == 6: lambda a: trunc(a, 2)
        }[True]

        answer = test(answer_input)
        self.ans[number - 1] = answer
        if answer == self.values[number - 1]:
            print('Correct')
        else:
            print('Probably, there is a mistake')
        return

    def compile_answers(self):
        """
        """
        for i,v in enumerate(self.ans):
            if v == 0:
                print('[', i + 1, '] is not answered !')
            else:
                correct = self.ans[i] == self.values[i]
                if correct:
                    print('[',i + 1,'] Correct')
                else:
                    print('[', i + 1, '] Incorrect')

        nm_ar = np.array([ord(self.name[i]) for i in range(len(self.name))])
        ans_std = np.round(np.concatenate([self.ans, nm_ar]).std(), 5)

        res = {'ans': self.ans, 'nm': self.name, 'crc': ans_std}
        with open('answers.txt', 'w') as outfile:
            json.dump(res, outfile)
        print('File "answers.txt" was successfully generated. Don\'t forget to send it too.')