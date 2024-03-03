import numpy as np
import matplotlib.pyplot as plt

class NewtonRaphson:
    def __init__(self, function, derivative):
        self.function = function
        self.derivative = derivative

    def find_root(self, start, tol=1e-6, max_iter=100):
        x = start
        path = [x]  # Store the starting point
        for i in range(max_iter):
            x_new = x - self.function(x) / self.derivative(x)
            path.append(x_new)  # Store each new estimate
            if abs(x_new - x) < tol:
                return x_new, i + 1, path  # Return root, iteration count, and path
            x = x_new
        return None, None, path

    @staticmethod
    def unique_roots(roots, tol=1e-4):
        unique = []
        for root in roots:
            if not any(abs(root - uroot) < tol for uroot in unique):
                unique.append(root)
        return unique

    def visualize_convergence(self, start_points, tol=1e-4):
        roots = []
        iterations = []

        for start in start_points:
            root, iter_count, _ = self.find_root(start)
            if root is not None:
                roots.append(root)
                iterations.append(iter_count)

        # Assign a unique color to each root found
        unique_roots = np.unique(np.round(roots, 4))  # Round roots for grouping
        colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black']  # Define specific colors
        
        # Ensure we have enough colors for each root
        if len(unique_roots) > len(colors):
            raise ValueError("Not enough predefined colors for unique roots.")

        # Map each root to a specific color
        color_map = {ur: colors[i] for i, ur in enumerate(unique_roots)}

        # Plotting
        plt.figure(figsize=(10, 6))
        for i, start in enumerate(start_points):
            if roots[i] is not None:
                plt.scatter(start, iterations[i], color=color_map[np.round(roots[i], 4)], alpha=0.6)

        # Add vertical lines for each unique root
        for ur in unique_roots:
            plt.axvline(x=ur, color=color_map[ur], linestyle='--', linewidth=1)

        # Create custom legend
        legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=f'Root: {ur}', markersize=10, markerfacecolor=color_map[ur]) for ur in unique_roots]
        plt.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.xlabel('Starting Point')
        plt.ylabel('Iterations to Converge')
        plt.title('Basins of Attraction and Convergence using Newton-Raphson Method')
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.tight_layout()
        plt.show()
        
    def example(self):
        return """
        def f(x):
            return x**5 - 9

        def df(x):
            return 5*x**4

        q1 = NewtonRaphson(f, df)
        root, iteration, iteration_path = q1.find_root(1,max_iter=50)
        print(f"the root is {root} after {iteration} iteration\nhere is the converging path \n{iteration_path}\n")
        print("here is the visualization graph")
        print("if we change start point to 2, it only takes 6 steps")
        q1.visualize_convergence(np.linspace(-10,10,400))
        """
        