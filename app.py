# -*- coding: utf-8 -*
from flask import Flask, render_template, request, abort
from car import Car
from config import WEB_PORT

app = Flask(__name__)

car = Car()

handle_map = {
    'steer_up': car.steering_up,
    'steer_down': car.steering_down,
    'steer_left': car.steering_left,
    'steer_right': car.steering_right,
    'steer_center': car.steering_center,
    'forward': car.forward,
    'left': car.left,
    'right': car.right,
    'pause': car.stop,
    'backward': car.backward, 
}


@app.route('/', methods=['GET'])
def main_page():
    return render_template("index.html")


@app.route('/handle', methods=['GET'])
def handle():
    try:
        # 获取GET参数
        operation = request.args.get('type', '')
    except ValueError:
        abort(404)  # 返回 404
    else:
        if operation in handle_map.iterkeys():
            handle_map[operation]()
        else:
            abort(404)
    return 'ok'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=WEB_PORT, debug=True)
