import csv
import matplotlib.pyplot as plt
import numpy as np
import os


class DataPlotter:
    def __init__(self, data_dir):
        self.data_dir = data_dir
    def read_csv_data(self, file_path):
        data = []
        
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if not row:
                    continue
                parsed = []
                for value in row:
                    try:
                        parsed.append(float(value))
                    except Exception:
                        
                        continue
                if parsed:
                    data.append(parsed)

        if not data:
            return np.array([])

        
        max_cols = max(len(r) for r in data)
        arr = np.full((len(data), max_cols), np.nan, dtype=float)
        for i, row in enumerate(data):
            arr[i, : len(row)] = row
        return arr

    def plot_data(self, file_name, title, x_label, y_label, save_as=None):
        file_path = os.path.join(self.data_dir, file_name)
        data = self.read_csv_data(file_path)
        plt.figure()
        
        if data.size == 0:
            print(f"No numeric data found in {file_path}")
            return

        
        if data.ndim == 1 or data.shape[1] == 1:
            y = data[:, 0] if data.ndim > 1 else data
            x = np.arange(len(y))
            plt.plot(x, y, label='Series 1')
        else:
            
            x = data[:, 0]
            for i in range(1, data.shape[1]):
                plt.plot(x, data[:, i], label=f'Series {i}')
        
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend()
        
    
        plt.savefig(os.path.join(self.data_dir, save_as))
    
        plt.show()

if __name__ == "__main__":
    data_dir = 'data'  
    plotter = DataPlotter(data_dir)
      
    
    plotter.plot_data('Ticks.csv', 'timings', 'frame', 'time(ms)', save_as='example_plot.png'   )
    