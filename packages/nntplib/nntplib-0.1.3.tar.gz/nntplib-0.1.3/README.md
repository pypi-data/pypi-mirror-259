nntplib library from Python 3 standard library as an independent module.

Because `nntplib` is still a valid library in all relevant
versions of the standard library up to and including Python 3.12,
so when asking for it, the care should be made to avoid the
conflict. For example, use this line in your `pyproject.toml`
`project.dependencies` section:

```
    'nntplib; python_version>="3.12"'
```

All issues, questions, complaints, or (even better!) patches
should be send via email to
[~mcepl/devel@lists.sr.ht](mailto:~mcepl/devel@lists.sr.ht) email
list (for patches use [git
send-email](https://git-send-email.io/)).
