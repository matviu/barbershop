var gulp = require('gulp');
var less = require('gulp-less');
//var browserSync = require('browser-sync').create();
var ghPages = require('gulp-gh-pages');
var plumber = require("gulp-plumber");
var postcss = require("gulp-postcss");
var autoprefixer = require("autoprefixer");
var mqpacker = require("css-mqpacker");
var minify = require("gulp-csso");
var rename = require("gulp-rename");
var svgstore = require("gulp-svgstore");
var svgmin = require("gulp-svgmin");
var imagemin = require("gulp-imagemin");
var server = require("browser-sync").create();
var run = require("run-sequence");
var del = require("del");




gulp.task('watch', ['style'], function() {
  gulp.watch('./static/**/*.less', ['style']);
})

gulp.task('deploy', function() {
  return gulp.src('./**/*')
  .pipe(ghPages());
})

gulp.task("style", function() {
  return gulp.src("static/less/style.less")
    .pipe(plumber())
    .pipe(less(
//    {
//      includePaths: require('node-normalize-scss').includePaths
//    }
    ))
    .pipe(postcss([
      autoprefixer({browsers: [
        "last 2 version"
      ]}),
      mqpacker({
        sort: true
      })
    ]))
    .pipe(gulp.dest("static/css"))
    .pipe(minify())
    .pipe(rename("style.min.css"))
    .pipe(gulp.dest("static/css"))
});

//gulp.task('browserSync', function() {
//  browserSync.init({
//    server: {
//      baseDir: '.',
//      index: 'index.html'
//    },
//  })
//})


