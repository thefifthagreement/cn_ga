import gymnasium as gym
import time
import pickle

MAX_STEPS = 200
FLAG_LOCATION = 0.5

class MountainCar:

    def __init__(self, randomSeed, render_mode=None):

        self.env = gym.make('MountainCar-v0',  render_mode=render_mode)
        self.env.action_space.seed(randomSeed)

    def __len__(self):
        return MAX_STEPS


    # TODO
    def getScore(self, actions):
        """
        calculates the score of a given solution, represented by the list of actions, for the Moutain-Car environment,
        by initiating an episode of the Mountain-Car environment and running it with the provided actions.
        
        :param actions: a list of actions to be fed into the mountain cart environment
        :return: the calculated score value
        """

        # start a new episode:
        self.env.reset()

        actionCounter = 0

        # feed the actions to the environment:
        for action in actions:
            actionCounter += 1

            # provide an action and get feedback:
            observation, reward, terminated, truncated, info = self.env.step(action)

            # episode over - either the car hit the flag, or 200 actions processed:
            if terminated or truncated:
                break

        # evaluate the results to produce the score:
        if actionCounter < MAX_STEPS:
            # the car hit the flag:
            # TODO define the score using the action count
            score = -1
        else:
            # the car did not hit the flag:
            # TODO reward according to distance from flag
            score = 1

        return score

    def saveActions(self, actions):
        """
        serializes and saves a list of actions using pickle
        :param actions: a list of actions (values 0, 1, or 2) to be fed into the mountain cart environment
        """
        savedActions = []
        for action in actions:
            savedActions.append(action)

        pickle.dump(savedActions, open("mountain-car-data.pickle", "wb"))

    def replaySavedActions(self):
        """
        deserializes a saved list of actions and replays it
        """
        savedActions = pickle.load(open("mountain-car-data.pickle", "rb"))
        self.replay(savedActions)

    def replay(self, actions):
        """
        renders the environment and replays list of actions into it, to visualize a given solution
        :param actions: a list of actions (values 0, 1, or 2) to be fed into the mountain cart environment
        """
        # start a new episode:
        observation = self.env.reset()

        # start rendering:
        self.env.render()

        actionCounter = 0

        # replay the given actions by feeding them into the environment:
        for action in actions:

            actionCounter += 1
            self.env.render()
            observation, reward, terminated, truncated, info = self.env.step(action)
            print(actionCounter, ": --------------------------")
            print("action = ", action)
            print("observation = ", observation)
            print("distance from flag = ", abs(observation[0] - 0.5))
            print()

            if terminated or truncated:
                break
            else:
                time.sleep(0.02)

        self.env.close()


def main():

    RANDOM_SEED = 42
    car = MountainCar(RANDOM_SEED, render_mode="human")
    car.replaySavedActions()

if __name__ == '__main__':
    main()