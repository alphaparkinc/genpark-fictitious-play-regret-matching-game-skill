"""Example evaluating regret matching learning dynamics."""
from client import RegretMatchingLearner

def main():
    learner = RegretMatchingLearner(num_actions=3)
    # Simulate Rock-Paper-Scissors rounds
    for _ in range(50):
        # Action 0 against opponent playing uniform
        learner.update(action_taken=0, payoffs=[0.0, -1.0, 1.0])
    print("Average Strategy after 50 rounds:", learner.get_average_strategy())

if __name__ == "__main__":
    main()
