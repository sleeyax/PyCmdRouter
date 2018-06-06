# PyCmdRouter (Python Command Router)
With PyCmdRouter you can invent your own set of commands which can be used within your python application.
Routng syntax is based on [Simple-API-Framework (PHP)](https://github.com/sleeyax/Simple-API-Framework).

## Example
Possible interactions & output of example.py:
```
> python example.py

+--------------------------------------+
+ Example application                  +
+ v1.0                                 +
+--------------------------------------+

Welcome, guest!
guest>: get color
color: white
guest>: set color orange
Permission denied!
guest>: login admin
Enter your password: ***

 Welcome back, admin

guest>admin>: set color orange
Changed car color to orange
guest>admin>: get color
color: orange
guest>admin>:
```

## Getting started
### Create a command

```
user = new User() # Example callback
router = CommandRouter() # Create cmd router object
```

Method 1:
```
router.set_callback(user)
router.register('set username {:str}', 'set_username')
router.route()
```

Method 2:
```
router.register('set username {:str}', [user, 'set_username']) # Callback is specified inline
router.route()
```
