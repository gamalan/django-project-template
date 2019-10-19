const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

const scriptFolder = './src/js/';
const fs = require('fs');
let scriptFiles = {};


function walkSync(currentDirPath, callback) {
    fs.readdirSync(currentDirPath).forEach(function (name) {
        var filePath = path.join(currentDirPath, name);
        var stat = fs.statSync(filePath);
        var basename = path.basename(filePath,'.js');
        if (stat.isFile()) {
            callback(filePath, basename);
        } else if (stat.isDirectory()) {
            walkSync(filePath, callback);
        }
    });
}

walkSync(scriptFolder,function(filePath, basename) {
    scriptFiles[basename]='./'+filePath;
});

module.exports = {
    entry: scriptFiles,
    output: {
        path: path.resolve(__dirname, 'assets/bundle'),
        filename: 'scripts/[name].bundle.js',
        chunkFilename: 'scripts/chunk.[name].[chunkhash].bundle.js',
    },
    module: {
        rules: [
            {
                test: /\.(le|c|sc)ss$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader
                    },
                    {
                        loader: 'css-loader',
                        options: {
                            sourceMap: true
                        }
                    },
                    {
                        loader: 'sass-loader',
                        options: {
                            sourceMap: true
                        }
                    }
                ]
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf|svg)$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: '[name].[ext]',
                            outputPath: 'font/'
                        }
                    }
                ]
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'style/style.bundle.css'
        }),
        new webpack.optimize.SplitChunksPlugin({
            name: "vendor",
            minChunks: function (module) {
                return module.context &&
                    module.context.includes("node_modules");
            }
        }),
        new webpack.optimize.SplitChunksPlugin({
            name: "manifest",
            minChunks: Infinity
        }),
        new BundleTracker({filename: './webpack-stats.json'})
    ]
};