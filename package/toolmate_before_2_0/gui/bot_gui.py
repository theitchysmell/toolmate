import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox, QLineEdit, QLabel
from PySide6.QtCore import QThread, Signal
from toolmate.autocaptain import AutoCaptainAgent
from toolmate.autobuild import AutoGenBuilder

class WorkerThread(QThread):
    finished = Signal()

    def __init__(self, mode, task):
        super().__init__()
        self.mode = mode
        self.task = task

    def run(self):
        if self.mode == 0:
            bot = AutoCaptainAgent()
            bot.getResponse(self.task)
        elif self.mode == 1:
            bot = AutoGenBuilder()
            bot.getResponse(self.task, coding=True)
        self.finished.emit()

class BotGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Assistant Bot")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Choose the mode:")
        layout.addWidget(self.label)

        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["Agent Dispatcher (CaptainAgent)", "Agent Creator (AgentBuilder)"])
        layout.addWidget(self.mode_combo)

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter your task here...")
        layout.addWidget(self.task_input)

        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.run_bot)
        layout.addWidget(self.run_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_bot(self):
        mode = self.mode_combo.currentIndex()
        task = self.task_input.text()
        if not task:
            return

        self.run_button.setEnabled(False)
        self.worker = WorkerThread(mode, task)
        self.worker.finished.connect(self.on_finished)
        self.worker.start()

    def on_finished(self):
        self.run_button.setEnabled(True)

def main():
    app = QApplication(sys.argv)
    window = BotGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
