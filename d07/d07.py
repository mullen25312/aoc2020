class DailyPuzzle07:
    def __init__(self):
        self.data = {}

    def read_data(self):
        with open("./d07/input.txt") as f:
            for line in f:
                line = line[:-1]
                container = line.split('contain')[0][:-5]
                content = line.split('contain')[1].split(',')
                content[-1] = content[-1][:-1]
                content_list = []
                for bag in content:
                    bag = bag[1:]
                    if bag == 'no other bags':
                        content_list.append('no other bags')
                    else:
                        amount = bag[0]
                        if int(amount) == 1:
                            content_list.append([int(amount), bag[2:-4]])
                        else:
                            content_list.append([int(amount), bag[2:-5]])

                self.data[container] = content_list


    def solve_part_one(self):
        for rule in self.data:
            tmp = rule
            
            # while tmp in dict.keys():
        return ''

    def solve_part_two(self):
        return ''
