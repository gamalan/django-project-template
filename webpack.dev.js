const merge = require('webpack-merge');
const common = require('./webpack.common.js');

common.output.publicPath = 'http://localhost:8081/assets/bundle/';
module.exports = merge(common, {
    mode: 'development',
    devtool: 'source-map'
});