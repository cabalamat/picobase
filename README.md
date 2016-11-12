# Picobase

**Picobase** is a small NoSQL database written in Python.

It is inspired by MongoDB.

Usage. e.g.:

```py
import pico

db = pico.Database("mydatabase")
doc = pico.Doc(name="George Orwell")
db.author.add(doc) # add the document to the author table
```
