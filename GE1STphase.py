import argparse, random
def simulate(num_doors, switch, verbose):
    winning_door = random.randint(0, num_doors-1)
    
    if verbose:
        print('Prize is behind door {}'.format(winning_door+1))
        choice = random.randint(0, num_doors-1)
    if verbose:
        print('Contestant chooses door {}'.format(choice+1))
        closed_doors = list(range(num_doors))
        while len(closed_doors) > 2:
            door_to_remove = random.choice(closed_doors)
            if door_to_remove == winning_door or door_to_remove == choice:
                continue
    closed_doors.remove(door_to_remove)
    if verbose:
        print('Host opens door {}'.format(door_to_remove+1))
        assert len(closed_doors) == 2
        if switch:
        if verbose:
            print('Contestant switches from door {} '.format(choice+1), end='')
            available_doors = list(closed_doors) # Make a copy of the list.
            available_doors.remove(choice)
            choice = available_doors.pop()
        if verbose:
            print('to {}'.format(choice+1))
            won = (choice == winning_door)
            if verbose:
                if won:
                    print('Contestant WON', end='\n\n')
                else:
                print('Contestant LOST', end='\n\n')
        return won
def main():
parser = argparse.ArgumentParser(
description='simulate the Monty Hall problem')
parser.add_argument('--doors', default=3, type=int, metavar='int',
help='number of doors offered to the contestant')
parser.add_argument('--trials', default=10000, type=int, metavar='int',
help='number of trials to perform')
parser.add_argument('--verbose', default=False, action='store_true',
help='display the results of each trial')
args = parser.parse_args()
print('Simulating {} trials...'.format(args.trials))
winning_non_switchers = 0
winning_switchers = 0

    for i in range(args.trials):
    won = simulate(args.doors, switch=False, verbose=args.verbose)
        if won:
            winning_non_switchers += 1
            won = simulate(args.doors, switch=True, verbose=args.verbose)
            if won:
                winning_switchers += 1
                print(' Switching won {0:5} times out of {1} ({2}% of the time)'.format(
                winning_switchers, args.trials,
                print('Not switching won {0:5} times out of {1} ({2}% of the time)'.format(
                winning_non_switchers, args.trials,
                (winning_non_switchers / args.trials * 100 ) ))
        if __name__ == '__main__':
            main()
            (winning_switchers / args.trials * 100 ) ))
