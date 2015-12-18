var gulp = require('gulp')
var sass = require('gulp-sass')
var autoprefix = require('gulp-autoprefixer')
var flatten = require('gulp-flatten')

var config = {
  staticDir: './static',
  bootstrapDir: './bower_components/bootstrap-sass'
}
config.sass = {
  includePaths: [config.bootstrapDir + '/assets/stylesheets'],
  precision: 8,
  errLogToConsole: true
}
config.autoprefix = {
  browsers: [
    'Android 2.3',
    'Android >= 4',
    'Chrome >= 20',
    'Firefox >= 24',
    'Explorer >= 8',
    'iOS >= 6',
    'Opera >= 12',
    'Safari >= 6'
  ]
}

gulp.task('sass', function () {
  return gulp.src('./css/app.scss')
    .pipe(sass(config.sass))
    .pipe(autoprefix(config.autoprefix))
    .pipe(gulp.dest(config.staticDir + '/css'))
})

gulp.task('js', function () {
  return gulp.src('./bower_components/**/*.min.js')
    .pipe(flatten())
    .pipe(gulp.dest(config.staticDir + '/js'))
})

gulp.task('fonts', function () {
  return gulp.src(config.bootstrapDir + '/assets/fonts/**/*.*')
    // .pipe(flatten())
    .pipe(gulp.dest(config.staticDir + '/fonts'))
})

gulp.task('default', ['sass', 'js', 'fonts'])
