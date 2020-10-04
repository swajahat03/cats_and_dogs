# Cats And Dogs

[![Build Status](https://travis-ci.org/sindresorhus/pageres.svg?branch=master)](https://travis-ci.org/sindresorhus/pageres)  [![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/CSC307Fall2019/Group-3)

<h1 align="center">
  <br>
  <img src="https://github.com/CSC307Fall2019/Group-3/blob/master/docs/screenshot.png" alt="Easy Quiz" width="960">
</h1>

Easy Quiz is a web application built to be used by an elementary school teacher where he/she can build quizzes, assign those quizzes to classes, and view the grades for the classes that they're teaching. This webapp also allows students to take quizzes and get graded. 

## Installation

1) Clone the source locally
```sh
$ git clone https://github.com/CSC307Fall2019/Group-3
```
Once you have cloned the git repository locally, you would want to open two terminal tabs and navigate to the cloned repo in both these windows. 

2) In the first window, navigate to the api folder.
```sh
$ cd api/
```
  For the second window, navigate to the webapp folder.
```sh
$ cd webapp/
```
3) Now that you've navigated to the desired folders. Run the following command in both the windows to complete the webapp setup.
```sh
$ npm install
```
4) Next you'll run the api and webapp by running the webapp and api by running the following command:
```sh
$ npm run serve
```
This should have Easy Quiz up and running. 

5) To run the tests
```sh
$ npm run test
```
6) Required existing data 
```sh
*** Teacher ***
For the website to be used there has to be an existing entry in the "user" table 
of a teacher (a user who's IS_STUDENT is 0)
```

## Testing 
For testing purposes, the following credentials are assumed:
```sh
*** Teacher ***
username: teacher@t.edu
password: teacher
*** Student ***
username: student@eazyquiz.edu
password: student
```
