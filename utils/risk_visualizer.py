import matplotlib.pyplot as plt


class RiskVisualizer:

    @staticmethod
    def plot_curve(scores):

        probabilities = scores

        plt.figure()
        plt.plot(probabilities)
        plt.title("Risk Probability Trajectory")
        plt.xlabel("Time")
        plt.ylabel("Risk Probability")

        plt.show()
