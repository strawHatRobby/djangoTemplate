# Welcome
## Django Template for all the tutorials

*To download clone this repo by typing the following a terminal*


      git clone https://github.com/strawHatRobby/djangoTemplate


### Installing the packages

**use pip to install the packages**

  ```python
  pip install -r dev-requirements.txt
  ```

### Installing behave-parallel to run your tests in parallel


1.  ```
git clone https://github.com/hugeinc/behave-parallel
```
2. ```
mkdir ~/.custom_packages
```

  ```
 mv ./behave-parallel ~/.custom_packages
```
3. Open the file **~/.bashrc** in your fav text editor

4.  Add the following to your ~/.bashrc file at the end

```
################ Python package aliases ################

function behaveP() {
  command /usr/bin/time python2 ~/.custom_packages/behave-parallel/bin/behave-parallel --processes "$1" --parallel-element "$2"
}
########################################################
```

##### Sourcing the command to command line

1. run the command
```
source ~/.bashrc
```
2. Make sure you are in the project folder and then run the following

  ```
behaveP 2 feature

  ```

## Notes

- Make sure firefox is installed in your system as by default this template uses firefox to run the functional tests. Ignore if you've tested the features folder and are ready to write your own tests and features file.

- The feature for folder contains basic features to test against, these are just basic tests and do not cover anything significant, furthermore they are app specific tests.For more info look look into behave documentation, https://pythonhosted.org/behave/api.html.

- Not using headless browsers for implementing tests, this will cause problem when working with a CI system like travis CI, use headless browsing feature of selenium to solve it.

- Refer to the behave-parallel documentation for more info on running behave tests in parallel. Will be adding a man page support for it soon. Stay Tuned.

- Behave doesn't  support REST API testing out of the box, but the feature can be added by installing behave-web-api package using pip
