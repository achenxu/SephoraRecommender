var path = require('path')

loaders: [
  {
    test: /\.js?/,
    exclude: [/node_modules/, /styles/],
    loaders: ['babel'],
    include: path.join(__dirname, 'src')
  },
  {
    test: /\.scss$/,
    loader: 'style!css!resolve-url!sass?sourceMap'
  },
  {
    test: /\.css$/,
    loader: 'style-loader!css-loader'
  },
  {
    test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
    loader: 'url-loader?limit=10000&mimetype=application/font-woff'
  },
  {
    test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
    loader: 'file-loader'
  }
]
