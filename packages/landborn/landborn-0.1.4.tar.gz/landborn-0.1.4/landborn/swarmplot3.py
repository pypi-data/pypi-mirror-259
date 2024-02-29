import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb

def swarmplot(categorical_data, numerical_data, radius=0.05):

    categories = list(set(categorical_data))
    category_indices = {category: i for i, category in enumerate(categories)}
    plotted_points = {category: {} for category in categories}
    
    colors = plt.cm.tab10(np.linspace(0, 1, len(categories)))  # Using a colormap for unique colors
    category_color = dict(zip(categories, colors))
    
    plt.figure(figsize=(10, 6))
    
    for category in categorical_data:
        for value in numerical_data:
            if value in plotted_points[category]:
                plotted_points[category][value] += 1
            else: 
                plotted_points[category][value] = 1
    print(plotted_points)
    for category in categorical_data:
        for key,value in plotted_points[category].items():
            if value == 1:
                x_position = category_indices[category]
                plt.scatter(x_position, key, color=category_color[category])
            elif value > 1:
                start = -value//2
                stop = value//2
                step = 1
                range_with_skip = list(range(start, 0, step)) + list(range(0 + step, stop + step, step))
                for i in range_with_skip:
                    x_position = category_indices[category] + (i * radius)
                    print('i is: ', i)
                    plt.scatter(x_position, key, color=category_color[category])

    print(plotted_points)
    plt.xticks(range(len(categories)), categories)
    
    plt.xlabel('Category')
    plt.ylabel('Numerical Value')
    plt.title('Numerical Data by Category with Adjusted X for Duplicates')
    
    plt.grid(True)
    plt.show()

# Example usage
categorical_data = ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C']
numerical_data = [10, 10, 15, 20, 20, 15, 15, 15]
# plot_categorical_numerical_with_adjusted_x(categorical_data, numerical_data)

data = {
'Category': ['A']*50 + ['B']*50 + ['C']*50,
'Value': np.concatenate([np.random.randint(0, 51, size=50), np.random.randint(20, 71, size=50), np.random.randint(40, 91, size=50)])
}

swarmplot(['A', 'B', 'C'], data['Value'])