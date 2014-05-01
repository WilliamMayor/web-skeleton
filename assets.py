from flask.ext.assets import Environment, Bundle

assets = Environment()

js = Bundle(
    'js/libs/**/*.js',
    Bundle(
        'js/main.js',
        filters='rjsmin'),
    output='main.min.js')
assets.register('js', js)

css = Bundle(
    'css/main.scss',
    filters='scss,cssmin',
    output='main.min.css',
    depends='scss/**/_*.scss')
assets.register('css', css)