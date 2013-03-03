## Using Gitlab Continous Integration

![Alt text](http://ci.zenobi.us/projects/1/status?ref=develop)

use following script to automate testing

```
    mkvirtualenv `basename $PWD`
    pip install .
    pip install django-lettuce
    python ./test.py
```