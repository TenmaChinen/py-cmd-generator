const HtmlWebPackPlugin = require('html-webpack-plugin');
const path = require('path');

module.exports = {
  mode: 'development',
  output: {
    path: path.resolve(__dirname, 'build'),
    filename: 'bundle.js',
    // publicPath: '/', // U K N O WN
  },
  // U K N O WN
  // resolve: {
  //   modules: [path.join(__dirname, 'src'), 'node_modules'],
  //   alias: {
  //     react: path.join(__dirname, 'node_modules', 'react'),
  //   },
  // },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: 'babel-loader',
      },
      {
        test: /\.s?css$/i,
        use: ["style-loader", "css-loader"]
      },
      {
        test: /\.(png|svg|jpg|gif|svg)$/i,
        loader: 'file-loader',
      },
    ],
  },
  // Needed to use JSX file extension
  resolve : {
    extensions : ['.js', '.jsx']
  },
  plugins: [
    new HtmlWebPackPlugin({
      template: './src/index.html',
      filename: './index.html'
    }),
  ],
};