# 导入标准组件
import sys
_top = sys.modules['__main__']
from PySide6.QtWidgets import QDialog, QVBoxLayout

# 导入UI组件
from view.pops.chart._view import Ui_Form

# 导入定制内容
import math,random
from PySide6.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Dialog(QDialog):
    def __init__(self, parent=None, dialog_args=None, input=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("实时曲线")

        self.count = dialog_args["count"] # 绘图点数

        # Initialize matplotlib figure and canvas
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        # Create layout for the chart widget
        layout = QVBoxLayout(self.ui.wgt_chart)
        layout.addWidget(self.canvas)

        # Initialize data for the chart
        self.x_data = list(range(self.count))
        self.y_data = [0] * self.count

        # Initialize the plot
        self.init_plot()

        # Set up timer for real-time updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)

        # Counter for stopping after 10 seconds
        self.counter = 0

        # Start the timer when the dialog is shown
        self.showEvent = self.on_show

    def on_show(self, _):
        # Start the timer when the dialog is shown
        self.timer.start(1000)  # Update every 1 second

    def init_plot(self):
        # Create the initial plot
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('Real-time Line Chart')
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Value')
        self.line, = self.ax.plot(self.x_data, self.y_data, 'b-')
        self.ax.set_ylim(-10, 10)

        # Add text for time display
        self.time_text = self.ax.text(0.02, 0.95, 'Time: 0s', transform=self.ax.transAxes)

        self.canvas.draw()

    def update_plot(self):
        # Update counter
        self.counter += 1

        # Stop after 10 seconds
        if self.counter > self.count:
            self.timer.stop()
            return

        # Generate a more interesting pattern (sine wave with noise)
        new_value = 5 * math.sin(self.counter * 0.5) + random.uniform(-2, 2)

        # Shift data to the left
        self.y_data = self.y_data[1:] + [new_value]

        # Update the plot
        self.line.set_ydata(self.y_data)

        # Update time text
        self.time_text.set_text(f'Time: {self.counter}s')

        self.canvas.draw()

    def get_result(self):
        return {
            "name": "绘图结果",
            "value": self.y_data
        }