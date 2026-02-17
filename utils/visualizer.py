import matplotlib.pyplot as plt


class Visualizer:

    @staticmethod
    def plot_history(history):

        cardiac_load = [h["cardiac_load"] for h in history]
        recovery_deficit = [h["recovery_deficit"] for h in history]

        plt.figure()
        plt.plot(cardiac_load)
        plt.title("Cardiac Load Trajectory")

        plt.figure()
        plt.plot(recovery_deficit)
        plt.title("Recovery Deficit Trajectory")

        plt.show()
