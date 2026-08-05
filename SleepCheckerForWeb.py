import csv
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for


class SleepCheckerForWeb:
    def __init__(self, log_path='sleep_log.csv'):
        self.log_path = log_path

    def record_event(self, event):
        ts = datetime.now().isoformat()
        with open(self.log_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([ts, event])


def create_app(log_path='sleep_log.csv'):
    app = Flask(__name__, template_folder='templates')
    checker = SleepCheckerForWeb(log_path=log_path)

    @app.route('/', methods=['GET'])
    def index():
        return render_template('sleep_checker_web.html')

    @app.route('/sleep', methods=['POST'])
    def sleep_event():
        checker.record_event('入眠')
        return redirect(url_for('index'))

    @app.route('/wake', methods=['POST'])
    def wake_event():
        checker.record_event('起床')
        return redirect(url_for('index'))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=5000, debug=True)
