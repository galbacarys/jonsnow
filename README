# jonsnow

`jonsnow` is a tool to help improve development workflows for people with lots 
of unit tests and too little patience to run them. I developed it for my own use
case (namely, testing Ansible playbooks), but it should be useful to others as
well.

It works by checking to see if the contents of a directory have changed, and
runs an arbitrary shell command if they have. This is similar behavior to, for
example, development mode in Django or certain Node.JS deployment systems, but
simplified and generalized for use in any development environment.

My workflow usually looks like this (I use tmux):

```
+----------------------------+---------+
|                            |         |
|                            |         |
|             Vim            | jonsnow |
|                            |         |
|                            |         |
|                            |         |
+----------------------------+---------+
```

This way, any time I save a file in Vim, the results are immediately reflected
on my secondary terminal window, which allows me to continue working without
needing to run my deployment process manually.

To learn how to use `jonsnow`, just run `jonsnow --help`. It should be pretty
self explanatory. note that anything after the flag arguments is considered your
command, so you should always order as `jonsnow <flags> <command>`.

# Installing

Available on pip! Just run `pip install jonsnow` the way you would install any
other python-based executable.

# Name

There was a lame pun about being a "watcher" in here at some point, but that's
all I've got.
