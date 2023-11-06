const path = require('path');

module.exports = {
  entry: './assets/index.js',  // path to our input file
  module: {
    rules: [
      // ... other rules ...

      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
    ],
  },
  output: {
    filename: 'index-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, './static/js'),  // path to our Django static directory
  },
};