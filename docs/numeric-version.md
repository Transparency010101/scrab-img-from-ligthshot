# About "my" numeric version using in project

I use standard numeric version like major.minor.patch.mimi-patch(1.2.2.5), but I need something for showing 
developing stage. There is described "my" extended standard numeric version:

In public(releases) I use major.minor.patch-mini-patch. But in developing I need something for developing stages.
So I think out this:

major.minor.patch-mini-patch + stage + substage

Stage: 
- alpha: letter a
- beta: letter b
- release condition: rc
- release: r

Substage: it's number for updating stage like 3.2.8.1-a4
3 is major
2 is minor 
8 is patch
1 is mini-patch
a4 is stage of developing program version 3.2.8.1
In the end(in release) it will seem: 3.2.8.2, it depends on from weight of this update.
3.3.0.0(in short 3.3), 3.2.9.0(in short 3.2.9)

Don't write substage in releases, only in developing.